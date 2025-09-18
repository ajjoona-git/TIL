## Web Application

### 클라이언트와 서버

- 클라이언트(Client): 서비스를 요청하는 주체
    - 사용자의 웹 브라우저, 모바일 앱
- 서버(Server): 클라이언트의 요청에 응답하는 주체
    - 웹 서버, 데이터베이스 서버

**우리가 웹 페이지를 보게 되는 과정 [요청 & 응답]**

1. 웹 브라우저(클라이언트)에서 `google.com`을 입력 후 Enter
2. 웹 브라우저는 인터넷에 연결된 전세계 어딘가에 있는 구글 컴퓨터(서버)에게 `메인 페이지.html`파일을 달라고 요청
3. 요청을 받은 구글 컴퓨터는 데이터베이스에서 `메인 페이지.html`파일을 찾아 응답
4. 웹 브라우저는 전달받은 `메인 페이지.html`파일을 사람이 볼 수 있도록 해석해주고 사용자는 구글의 메인 페이지를 보게 됨 

### Frontend와 Backend

- Frontend (프론트엔드)
    - 사용자 인터페이스 (UI)를 구성하고 사용자가 애플리케이션과 상호작용할 수 있도록 함
    - HTML, CSS, JavaScript, 프론트엔드 프레임워크(예: Vue.js) 등

- Backend (백엔드)
    - 서버 측에서 동작하며 클라이언트의 요청에 대한 처리와 데이터베이스와의 상호작용을 담당
    - 서버 언어 (Python, Java 등), 백엔드 프레임워크(예: Django), 데이터베이스, API, 보안 등

## Framework

### Web Framework

웹 애플리케이션을 빠르게 개발할 수 있도록 도와주는 도구

- 개발에 필요한 기본 구조, 규칙, 라이브러리 등을 제공
- 로그인/로그아웃, 회원관리, 데이터베이스, 보안 등

### Django Framework

Python 기반의 대표적인 웹 프레임워크

- 검증된 웹 프레임워크: 대규모 트래픽 서비스에서도 안정적인 서비스를 제공한다.
    - Spotify, Instagram, Dropbox, Delivery Hero
- 웹 개발 시장을 주도
    - Django (Python) > Spring Boot (Java) > [ASP.NET](http://ASP.NET) Core (C#)