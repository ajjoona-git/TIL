import os
import re
import requests
from pathlib import Path
from urllib.parse import urlparse

# --- 이전과 동일한 헬퍼 함수 ---
def get_file_extension(url, response_headers):
    """URL이나 HTTP 응답 헤더에서 파일 확장자를 추측합니다."""
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
    return '.png' # 기본값

def process_single_markdown_file(md_file_path):
    """하나의 마크다운 파일을 처리하는 함수"""
    print(f"\n📄 '{md_file_path}' 파일 처리 시작...")

    # 1. 'images' 폴더 생성 (해당 마크다운 파일과 같은 위치에)
    image_dir = md_file_path.parent / "images"
    image_dir.mkdir(exist_ok=True)

    # 2. 파일명 기반으로 이미지 이름 생성 준비
    base_file_name = md_file_path.stem

    # 3. 마크다운 파일 읽기
    try:
        with open(md_file_path, 'r', encoding='utf-8') as f:
            content = f.read()
    except Exception as e:
        print(f"  ❌ 파일 읽기 오류: {e}")
        return

    # 4. 외부 이미지 URL 찾기 (http 또는 https로 시작)
    image_pattern = re.compile(r'!\[(.*?)\]\((https?://.*?)\)')
    matches = list(image_pattern.finditer(content))

    if not matches:
        print("  - 외부 이미지를 찾지 못했습니다. 건너뜁니다.")
        return

    print(f"  - 총 {len(matches)}개의 외부 이미지를 발견했습니다.")
    image_counter = 1
    new_content = content

    # 5. 각 이미지를 순회하며 처리
    for match in matches:
        alt_text = match.group(1)
        original_url = match.group(2).strip()

        try:
            # 6. 이미지 다운로드
            headers = {'User-Agent': 'Mozilla/5.0'}
            response = requests.get(original_url, headers=headers, stream=True, timeout=15)
            response.raise_for_status()

            # 7. 새 이미지 파일명 및 경로 설정
            file_ext = get_file_extension(original_url, response.headers)
            new_image_name = f"{base_file_name}_{image_counter}{file_ext}"
            
            # [수정됨] 마크다운 파일 기준의 상대 경로를 올바르게 계산
            # 예: md파일이 'AI/ml-intro.md'라면 -> 'images/ml-intro_1.png'
            relative_image_path = Path("images") / new_image_name
            absolute_image_path = md_file_path.parent / relative_image_path

            # 8. 이미지 파일 저장
            with open(absolute_image_path, 'wb') as f:
                for chunk in response.iter_content(chunk_size=8192):
                    f.write(chunk)

            # 9. 마크다운 본문의 URL 교체
            original_markdown_tag = match.group(0)
            new_markdown_tag = f"![{alt_text}]({relative_image_path.as_posix()})" # Posix-style 경로로 변경
            
            new_content = new_content.replace(original_markdown_tag, new_markdown_tag, 1)

            print(f"    ✅ '{new_image_name}' 저장 및 교체 완료.")
            image_counter += 1

        except requests.exceptions.RequestException as e:
            print(f"    ❌ URL 다운로드 실패: {original_url[:50]}... ({e})")
        except Exception as e:
            print(f"    ❌ 알 수 없는 오류 발생: {e}")
    
    # 10. 변경된 내용으로 원본 마크다운 파일 덮어쓰기
    try:
        with open(md_file_path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"  ✨ '{md_file_path.name}' 파일 업데이트 완료!")
    except Exception as e:
        print(f"  ❌ 파일 쓰기 오류: {e}")


# --- 메인 실행 로직 ---
if __name__ == "__main__":
    # 현재 스크립트가 실행되는 위치를 기준으로 모든 .md 파일을 찾습니다.
    # 이 스크립트를 'til' 폴더 최상단에 두면 됩니다.
    root_directory = Path(".")
    
    print(f"'{root_directory.resolve()}' 폴더 및 모든 하위 폴더에서 마크다운 파일을 찾습니다.")
    
    # pathlib의 rglob를 사용해 모든 하위 폴더를 포함하여 .md 파일을 찾음
    markdown_files = list(root_directory.glob("**/*.md"))

    if not markdown_files:
        print("처리할 마크다운 파일이 없습니다.")
    else:
        print(f"총 {len(markdown_files)}개의 마크다운 파일을 발견했습니다.")
        for md_file in markdown_files:
            # README.md 같은 최상위 설명 파일은 건너뛸 수 있습니다 (선택사항).
            if md_file.name.lower() == 'readme.md':
                print(f"\n📄 '{md_file}' 파일은 건너뜁니다.")
                continue
            process_single_markdown_file(md_file)
        
        print("\n🎉 모든 작업이 완료되었습니다!")