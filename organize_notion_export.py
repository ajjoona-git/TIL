import os
import re
import sys
import subprocess
import shutil
from pathlib import Path
from urllib.parse import unquote

# --- [새 기능] 다음 이미지 번호 찾기 ---
def get_next_image_index(image_dir, base_name):
    """
    'til/images/' 폴더를 스캔하여 'base_name_NUMBER.ext' 형식의
    파일을 찾아 가장 큰 NUMBER를 찾고, 그 다음 숫자를 반환합니다.
    (예: 'llm_1.png', 'llm_2.png'가 있으면 3을 반환)
    """
    max_index = 0
    # 정규식: '베이스이름_숫자.확장자'
    pattern = re.compile(rf"^{re.escape(base_name)}_(\d+)\..*$")

    if not image_dir.exists():
        return 1 # 'images' 폴더가 없으면 1부터 시작

    for f in image_dir.glob(f"{base_name}_*.*"):
        match = pattern.match(f.name)
        if match:
            num = int(match.group(1))
            if num > max_index:
                max_index = num

    # 다음 번호 반환
    return max_index + 1

# --- Git에서 변경된 .md 파일 목록 가져오기 ---
def get_changed_files(root_dir):
    """ 'git status'로 '수정'되거나 '추가'된 .md 파일 목록을 절대 경로로 반환 """
    print("Git 상태를 확인하여 변경된 .md 파일을 찾습니다...")
    changed_files = []
    try:
        result = subprocess.run(
            ['git', 'status', '--porcelain'],
            capture_output=True, text=True, encoding='utf-8', check=True,
            cwd=root_dir
        )

        for line in result.stdout.strip().split('\n'):
            if not line: continue
            status = line[:2].strip()
            file_path_str = line[3:]

            if (status in ('M', 'A', '??')) and file_path_str.endswith('.md'):
                if Path(file_path_str).name == Path(sys.argv[0]).name:
                    continue
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

    # 1. 최종 목적지 'images' 폴더 (루트)
    final_image_dir = root_dir / "images"
    final_image_dir.mkdir(exist_ok=True)
    base_file_name = md_file_path.stem # 예: 'llm-training'

    try:
        with open(md_file_path, 'r', encoding='utf-8') as f:
            content = f.read()
    except Exception as e:
        print(f"  ❌ 파일 읽기 오류: {e}")
        return

    # 2. 정규식: Notion에서 내보낸 '로컬' 이미지 링크만 찾기
    # (http://, https://, images/, ../images/ 로 시작하는 경로는 제외)
    image_pattern = re.compile(r'!\[([^\]]*)\]\((?!(?:https?://|images/|../images/))([^)]+)\)')
    matches = list(image_pattern.finditer(content))

    if not matches:
        print("  - 처리할 *새로운* Notion 로컬 이미지가 없습니다. 건너뜁니다.")
        return

    print(f"  - 총 {len(matches)}개의 새로운 Notion 로컬 이미지를 발견했습니다.")

    # --- [수정된 핵심 로직] ---
    # 3. 'til/images' 폴더를 스캔하여 다음 번호(예: 6)를 가져옴
    image_counter = get_next_image_index(final_image_dir, base_file_name)
    print(f"  - '{base_file_name}'의 기존 이미지를 확인. 새 이미지는 {image_counter}번부터 시작합니다.")

    new_content = content
    processed_count = 0
    notion_export_dirs = set()

    # 4. 처리할 작업을 순서대로(forward) 만듦 (번호 매기기: 6, 7, 8...)
    tasks = []
    for match in matches:
        alt_text = match.group(1)
        original_local_path_encoded = match.group(2).strip() # 예: 'image 1.png'

        try:
            original_local_path = Path(unquote(original_local_path_encoded))
            src_image_path = md_file_path.parent / original_local_path # 예: til/AI/image 1.png

            if not src_image_path.exists():
                print(f"    ⚠️ 원본 로컬 파일을 찾을 수 없습니다: {src_image_path}")
                continue

            file_ext = src_image_path.suffix
            # 새 이름 생성 (예: llm-training_6.png)
            new_image_name = f"{base_file_name}_{image_counter}{file_ext}"

            # 최종 저장 위치 (예: til/images/llm-training_6.png)
            absolute_dest_path = final_image_dir / new_image_name

            # md파일에 기록될 상대 경로 (예: ../images/llm-training_6.png)
            relative_path_for_md = Path(os.path.relpath(absolute_dest_path, md_file_path.parent)).as_posix()

            tasks.append({
                "match": match,
                "alt_text": alt_text,
                "src_image_path": src_image_path,
                "absolute_dest_path": absolute_dest_path,
                "new_markdown_tag": f"![{alt_text}]({relative_path_for_md})",
                "original_local_path_str": original_local_path.as_posix(),
                "relative_path_for_md": relative_path_for_md,
            })

            notion_export_dirs.add(src_image_path.parent)
            image_counter += 1 # 다음 번호 준비 (예: 7)

        except Exception as e:
            print(f"    ❌ [준비 단계] 오류 발생: {e}")

    # 5. 실제 파일 이동 및 .md 수정 (뒤에서부터)
    for task in reversed(tasks):
        try:
            shutil.move(task["src_image_path"], task["absolute_dest_path"])

            start, end = task["match"].span()
            new_content = new_content[:start] + task["new_markdown_tag"] + new_content[end:]

            print(f"    ✅ '{task['original_local_path_str']}' -> '{task['relative_path_for_md']}'로 이동 및 교체 완료.")
            processed_count += 1

        except Exception as e:
            print(f"    ❌ [처리 단계] 파일 이동/교체 오류: {e}")

    # --- (이하 동일) ---

    if processed_count > 0:
        try:
            with open(md_file_path, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f"  ✨ '{md_file_path.name}' 파일 업데이트 완료! (총 {processed_count}개 이미지 처리)")
        except Exception as e:
            print(f"  ❌ 파일 쓰기 오류: {e}")

    for export_dir in notion_export_dirs:
        try:
            # md파일과 같은 폴더에 이미지가 있었던 경우 (Notion 내보내기 기본)
            # 폴더가 아니므로 rmdir() 대신 continue
            if not export_dir.is_dir():
                continue
            if export_dir.exists() and not any(export_dir.iterdir()):
                export_dir.rmdir()
                print(f"  🗑️ 빈 폴더 삭제 완료: {export_dir.name}")
        except OSError as e:
            print(f"  ⚠️ 폴더 삭제 실패: {export_dir.name} ({e})")

# --- 메인 실행 로직 ---
if __name__ == "__main__":
    root_directory = Path.cwd()

    if not (root_directory / ".git").is_dir():
        print(f"❌ 이 스크립트는 Git 저장소의 루트 폴더(til)에서 실행해야 합니다.")
        sys.exit(1)

    markdown_files = get_changed_files(root_directory)

    if not markdown_files:
        print("\n처리할 마크다운 파일이 없습니다. (모든 파일이 최신 상태입니다)")
    else:
        for md_file_abs_path in markdown_files:
            if md_file_abs_path.name.lower() == 'readme.md':
                print(f"\n📄 '{md_file_abs_path.relative_to(root_directory)}' 파일은 건너뜁니다 (README).")
                continue
            process_single_markdown_file(md_file_abs_path, root_directory)

        print("\n🎉 모든 작업이 완료되었습니다!")