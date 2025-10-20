import os
import re
import requests
import sys
import subprocess  # Git 명령어를 실행하기 위해 추가
from pathlib import Path
from urllib.parse import urlparse

# --- [새 기능 1] 제외할 도메인 목록 ---
# 여기에 포함된 도메인의 URL은 이미지라도 다운로드하지 않습니다.
IGNORE_DOMAINS = [
    'img.shields.io',
    'github.com',
    # 필요시 다른 도메인도 추가 (예: 'velog.io')
]

# --- [새 기능 2] Git에서 변경된 .md 파일 목록 가져오기 ---
def get_changed_files():
    """
    'git status --porcelain' 명령을 실행하여
    '수정(Modified)'되거나 '추가(Untracked)'된 .md 파일 목록을 반환합니다.
    """
    print("Git 상태를 확인하여 변경된 .md 파일을 찾습니다...")
    changed_files = []
    try:
        # Git 상태를 기계가 읽기 쉬운 형태로 출력
        result = subprocess.run(
            ['git', 'status', '--porcelain'],
            capture_output=True,
            text=True,
            encoding='utf-8',
            check=True
        )

        for line in result.stdout.strip().split('\n'):
            if not line:
                continue

            # M, A, ?? (Modified, Added, Untracked) 상태 확인
            status = line[:2].strip()
            file_path = line[3:]

            if (status in ('M', 'A', '??')) and file_path.endswith('.md'):
                # 스크립트 파일 자체는 제외
                if Path(file_path).name == Path(sys.argv[0]).name:
                    continue
                changed_files.append(Path(file_path))

        if changed_files:
            print(f"✅ {len(changed_files)}개의 변경된 .md 파일을 찾았습니다.")
            for f in changed_files:
                print(f"   - {f}")
        else:
            print("✅ 변경된 .md 파일이 없습니다.")

        return changed_files

    except FileNotFoundError:
        print("  ❌ 'git' 명령을 찾을 수 없습니다. Git이 설치되어 있나요?")
        return []
    except subprocess.CalledProcessError as e:
        print(f"  ❌ Git 상태 확인 중 오류 발생: {e.stderr}")
        print("  ℹ️ 이 스크립트는 Git 저장소 루트 폴더에서 실행해야 합니다.")
        return []

# --- 헬퍼 함수 (이전과 거의 동일) ---
def get_file_extension(url, response_headers):
    parsed_url = urlparse(url)
    ext = Path(parsed_url.path).suffix
    if ext:
        return ext.split('?')[0]
    content_type = response_headers.get('content-type')
    if content_type:
        mime_to_ext = {'image/jpeg': '.jpg', 'image/png': '.png', 'image/gif': '.gif', 'image/webp': '.webp'}
        for mime, extension in mime_to_ext.items():
            if mime in content_type:
                return extension
    return '.png'

# --- [수정됨] 파일 처리 함수 ---
def process_single_markdown_file(md_file_path):
    print(f"\n📄 '{md_file_path}' 파일 처리 시작...")

    # 1. 파일이 실제로 존재하는지 확인 (git add만 하고 삭제한 경우)
    if not md_file_path.exists():
        print(f"  ❌ 파일이 존재하지 않습니다. 건너뜁니다: {md_file_path}")
        return

    image_dir = md_file_path.parent / "images"
    image_dir.mkdir(exist_ok=True)
    base_file_name = md_file_path.stem

    try:
        with open(md_file_path, 'r', encoding='utf-8') as f:
            content = f.read()
    except Exception as e:
        print(f"  ❌ 파일 읽기 오류: {e}")
        return

    # 2. 이미지 태그 정규식 (이전과 동일: ![]() 형태만)
    image_pattern = re.compile(r'!\[([^\]]*)\]\((https?://[^\)]*)\)')
    matches = list(image_pattern.finditer(content))

    if not matches:
        print("  - 외부 이미지를 찾지 못했습니다. 건너뜁니다.")
        return

    print(f"  - 총 {len(matches)}개의 외부 이미지를 발견했습니다.")
    image_counter = 1
    new_content = content
    processed_count = 0

    for match in reversed(matches):
        alt_text = match.group(1)
        original_url = match.group(2).strip()

        try:
            # --- [새 기능 1] 도메인 제외 로직 ---
            domain = urlparse(original_url).netloc
            if domain in IGNORE_DOMAINS:
                print(f"    ⚠️ 제외 목록 도메인입니다. 건너뜁니다: {domain}")
                continue

            # ------------------------------------

            if original_url.startswith("images/"):
                print(f"    ⚠️ 이미 로컬 경로입니다. 건너뜁니다: {original_url}")
                continue

            headers = {'User-Agent': 'Mozilla/5.0'}
            response = requests.get(original_url, headers=headers, stream=True, timeout=15)
            response.raise_for_status()

            file_ext = get_file_extension(original_url, response.headers)

            # 파일명 순서가 뒤섞이지 않도록 수정
            current_image_index = (len(matches) - image_counter) + 1
            new_image_name = f"{base_file_name}_{current_image_index}{file_ext}"

            relative_image_path = Path("images") / new_image_name
            absolute_image_path = md_file_path.parent / relative_image_path

            with open(absolute_image_path, 'wb') as f:
                for chunk in response.iter_content(chunk_size=8192):
                    f.write(chunk)

            original_markdown_tag = match.group(0)
            new_markdown_tag = f"![{alt_text}]({relative_image_path.as_posix()})"

            start, end = match.span()
            new_content = new_content[:start] + new_markdown_tag + new_content[end:]

            print(f"    ✅ '{new_image_name}' 저장 및 교체 완료.")
            processed_count += 1
            image_counter += 1

        except requests.exceptions.RequestException as e:
            print(f"    ❌ URL 다운로드 실패: {original_url[:50]}... ({e})")
        except Exception as e:
            print(f"    ❌ 알 수 없는 오류 발생: {e}")

    if processed_count > 0:
        try:
            with open(md_file_path, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f"  ✨ '{md_file_path.name}' 파일 업데이트 완료! (총 {processed_count}개 이미지 처리)")
        except Exception as e:
            print(f"  ❌ 파일 쓰기 오류: {e}")
    else:
        print("  - 실제로 처리된 이미지가 없습니다.")


# --- [수정됨] 메인 실행 로직 ---
if __name__ == "__main__":
    # 0. Git 저장소의 루트 폴더인지 확인
    if not Path(".git").is_dir():
        print("❌ 이 스크립트는 Git 저장소의 루트 폴더에서 실행해야 합니다.")
        print("   (예: 'ajjoona-git/til/' 폴더)")
        sys.exit(1)

    # 1. Git에서 변경된 .md 파일 목록을 가져옴
    markdown_files = get_changed_files()

    if not markdown_files:
        print("\n처리할 마크다운 파일이 없습니다. (모든 파일이 최신 상태입니다)")
    else:
        for md_file in markdown_files:
            # README.md는 건너뛰기
            if md_file.name.lower() == 'readme.md':
                print(f"\n📄 '{md_file}' 파일은 건너뜁니다 (README).")
                continue
            process_single_markdown_file(md_file)

        print("\n🎉 모든 작업이 완료되었습니다!")