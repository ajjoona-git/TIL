
## Django의 static tag


`{% load static %}`

- 정적 파일에 접근할 수 있는 URL을 만들어주는 태그
- static 태그를 쓰기 전이면 어디 쓰든 문법적으론 문제 없지만, 관례상 html 최상단에 선언
- 이미지 경로 하드코딩해서 작성해도 당연히 작동하는데, 굳이 static tag를 사용하는 이유는?
    - STATIC_URL 설정만 바꾸면 모든 static tag에 일괄 적용
    - 캐시 관리 기능인 `ManifestStaticFilesStorage` 등 고급 기능 활용에 유리함

### 활용

- 프론트엔드 프레임워크를 따로 사용하지 않고도 CSS, JavaScript를 static file로 로드하여 풀스택 개발 가능
- 이미지, 영상, 기타 모든 종류의 데이터를 쉽게 웹 서버에 저장하고 불러올 수 있음

### django template(html)에 css, js 붙이기

1. settings.py 수정
    - STATICFILES_DIRS : 개발 중 django가 정적 파일을 찾을 경로
    - STATIC_ROOT : 배포시 모든 정적 파일을 모을 경로

    ```python
    STATICFILES_DIRS = [
        BASE_DIR / 'static',
    ]

    STATIC_ROOT = BASE_DIR / 'staticfiles'
    ```

2. 참조할 경로 및 static 파일 생성
    - 당연히 이름 달라도 작동하지만 이게 표준
        - /static/css/style.css
        - /static/js/script.js

3. static 파일을 사용할 모든 템플릿(html파일) 최상단에 static 태그 사용 선언

    ```html
    {% load static %}
    ```

4. static 태그의 사용
    - bootstrap 쓰기 전에 \<link\>, \<script\> 작성하는 것과 같은 방식
    - html파일의 head 태그 안에 link 태그로 style.css 파일 로드
    
    ```html
    <link rel="stylesheet" href="{% static 'css/style.css' %}">
    ```
        
    - html파일의 body 태그 안(보통 맨 아래)에 script 태그로 script.js 파일 로드
    
    ```html
    <script src="{% static 'js/script.js' %}"></script>
    ```

