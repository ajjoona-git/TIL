import os
import re
import sys
import subprocess
import shutil
from pathlib import Path
from urllib.parse import unquote

# --- Git에서 변경된 .md 파일 목록 가져오기 ---
def get_changed_files(root_dir):
    """ 'git status'로 '수정'되거나 '추가'된 .md 파일 목록을 절대 경로로 반환 """
    print("Git 상태를 확인하여 변경된 .md 파일을 찾습니다...")
    changed_files = []
    try:
        # Git 명령어를 루트 디렉토리에서 실행
        result = subprocess.run(
            ['git', 'status', '--porcelain'],
            capture_output=True, text=True, encoding='utf-8', check=True,
            cwd=root_dir # 실행 위치를 스크립트가 있는 곳으로 고정
        )

        for line in result.stdout.strip().split('\n'):
            if not line: continue
            status = line[:2].strip()
            file_path_str = line[3:]

            if (status in ('M', 'A', '??')) and file_path_str.endswith('.md'):
                # 스크립트 파일 자체는 제외
                if Path(file_path_str).name == Path(sys.argv[0]).name:
                    continue

                # Git이 반환하는 상대 경로를 절대 경로로 변환
                abs_path = root_dir / file_path_str
                changed_files.append(abs_path)

        if changed_files:
            print(f"✅ {len(changed_files)}개의 변경된 .md 파일을 찾았습니다.")
            for f in changed_files:
                print(f"   - {f.relative_to(root_dir)}")
        else:
            print("✅ 변경된 .md 파일이 없습니다.")
        return changed_files

    except Exception as e:
        print(f"  ❌ Git 상태 확인 중 오류: {e}")
        print("  ℹ️ 이 스크립트는 Git 저장소 루트 폴더(til)에서 실행해야 합니다.")
        return []

# --- 파일 처리 함수 ---
def process_single_markdown_file(md_file_path, root_dir):
    print(f"\n📄 '{md_file_path.relative_to(root_dir)}' 파일 처리 시작...")

    if not md_file_path.exists():
        print(f"  ❌ 파일이 존재하지 않습니다. 건너뜁니다.")
        return

    # [수정] 1. 최종 목적지 'images' 폴더를 'til/images' (루트)로 설정
    final_image_dir = root_dir / "images"
    final_image_dir.mkdir(exist_ok=True)
    base_file_name = md_file_path.stem # 예: 'llm-training'

    try:
        with open(md_file_path, 'r', encoding='utf-8') as f:
            content = f.read()
    except Exception as e:
        print(f"  ❌ 파일 읽기 오류: {e}")
        return

    # 2. 로컬 파일 링크 정규식 (http, https, images/로 시작하지 않는 링크)
    image_pattern = re.compile(r'!\[([^\]]*)\]\((?!(?:https?://|images/|../images/))([^)]+)\)')
    matches = list(image_pattern.finditer(content))

    if not matches:
        print("  - 처리할 Notion 로컬 이미지가 없습니다. 건너뜁니다.")
        return

    print(f"  - 총 {len(matches)}개의 Notion 로컬 이미지를 발견했습니다.")
    image_counter = 1
    new_content = content
    processed_count = 0
    notion_export_dirs = set() # 삭제할 Notion 폴더 목록

    for match in reversed(matches):
        alt_text = match.group(1)
        original_local_path_encoded = match.group(2).strip() # 예: 'My%20Note/image.png'

        try:
            # 3. 원본 이미지 경로 확인 (md파일 기준)
            original_local_path = Path(unquote(original_local_path_encoded)) # 'My Note/image.png'
            src_image_path = md_file_path.parent / original_local_path

            if not src_image_path.exists():
                print(f"    ⚠️ 원본 로컬 파일을 찾을 수 없습니다: {src_image_path}")
                continue

            # 4. [수정] 새 이미지 파일명 및 *절대* 경로 설정
            file_ext = src_image_path.suffix
            new_image_name = f"{base_file_name}_{image_counter}{file_ext}" # 'llm-training_1.png'

            # [수정] 4-1. 최종 저장 위치 (절대 경로)
            # 예: /.../til/images/llm-training_1.png
            absolute_dest_path = final_image_dir / new_image_name

            # [수정] 4-2. 마크다운에 들어갈 *상대* 경로 계산
            # (md파일 위치 -> 최종 이미지 위치)
            # 예: ../images/llm-training_1.png (AI/llm-training.md 기준)
            # 예: images/llm-training_1.png (README.md 기준)
            relative_path_for_md = Path(os.path.relpath(absolute_dest_path, md_file_path.parent)).as_posix()

            # 5. 파일 이동
            shutil.move(src_image_path, absolute_dest_path)

            # 6. 마크다운 본문 교체
            new_markdown_tag = f"![{alt_text}]({relative_path_for_md})"
            start, end = match.span()
            new_content = new_content[:start] + new_markdown_tag + new_content[end:]

            print(f"    ✅ '{original_local_path.as_posix()}' -> '{relative_path_for_md}'로 이동 및 교체 완료.")

            notion_export_dirs.add(src_image_path.parent)
            processed_count += 1
            image_counter += 1

        except Exception as e:
            print(f"    ❌ 파일 처리 중 알 수 없는 오류 발생: {e} (URL: {original_local_path_encoded})")

    if processed_count > 0:
        # 8. .md 파일 저장
        try:
            with open(md_file_path, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f"  ✨ '{md_file_path.name}' 파일 업데이트 완료! (총 {processed_count}개 이미지 처리)")
        except Exception as e:
            print(f"  ❌ 파일 쓰기 오류: {e}")

        # 9. 빈 Notion 폴더 삭제
        for export_dir in notion_export_dirs:
            try:
                if export_dir.exists() and not any(export_dir.iterdir()):
                    export_dir.rmdir()
                    print(f"  🗑️ 빈 폴더 삭제 완료: {export_dir.name}")
            except OSError as e:
                print(f"  ⚠️ 폴더 삭제 실패 (아직 파일이 남음): {export_dir.name} ({e})")
    else:
        print("  - 실제로 처리된 이미지가 없습니다.")

# --- 메인 실행 로직 ---
if __name__ == "__main__":
    # 스크립트가 실행되는 위치 = Git 저장소 루트
    root_directory = Path.cwd()

    if not (root_directory / ".git").is_dir():
        print(f"❌ 이 스크립트는 Git 저장소의 루트 폴더(til)에서 실행해야 합니다.")
        print(f"   (현재 위치: {root_directory})")
        sys.exit(1)

    markdown_files = get_changed_files(root_directory)

    if not markdown_files:
        print("\n처리할 마크다운 파일이 없습니다. (모든 파일이 최신 상태입니다)")
    else:
        for md_file_abs_path in markdown_files:
            # README.md는 건너뛰기
            if md_file_abs_path.name.lower() == 'readme.md':
                print(f"\n📄 '{md_file_abs_path.relative_to(root_directory)}' 파일은 건너뜁니다 (README).")
                continue
            process_single_markdown_file(md_file_abs_path, root_directory)

        print("\n🎉 모든 작업이 완료되었습니다!")