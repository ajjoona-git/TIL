## RESTful API

### RESTful API

- REST (Representational State Transfer) 아키텍처 원칙을 따른 API를 의미합니다.
- 자원(Resource)을 URI(예: /users/1)로 표현하고, HTTP 메서드(GET, POST, PUT, DELETE 등)를 활용해 자원에 대한 행위를 정의합니다.
- 특징:
    - Stateless(무상태성): 서버는 클라이언트 상태를 보관하지 않고, 각 요청이 독립적으로 처리됨.
    - Uniform Interface(일관성): 동일한 구조로 요청/응답을 정의.
    - Client-Server 분리: 프론트엔드와 백엔드가 독립적으로 개발/운영 가능.
    - Cacheable: HTTP 캐싱을 활용해 성능 최적화 가능.

### 활용

- 웹/모바일 앱 백엔드와 통신할 때: 예를 들어, 모바일 앱에서 서버로 사용자 데이터 요청.
- 외부 서비스 연동: Google Maps API, Twitter API처럼 제3자 서비스를 사용할 때.
- 마이크로서비스 아키텍처: 여러 서비스 간 통신에 활용.
- CRUD 중심 시스템: 게시판, 쇼핑몰, 데이터 관리 시스템 등에서 자원 중심의 데이터 조작.

### 기능

CRUD(Create, Read, Update, Delete) 기능을 제공합니다.

- GET /users → 사용자 목록 조회
- POST /users → 사용자 생성
- PUT /users/1 → 특정 사용자 정보 수정
- DELETE /users/1 → 특정 사용자 삭제
- 확장적으로, 필터링, 페이징, 인증(OAuth2, JWT), 캐싱, 응답 포맷(JSON/XML) 등을 제공합니다.

### **RESTful API vs WebSocket**

REST는 하나의 요청, 하나의 응답으로 이루어지고

Socket은 세션이 열려있는 동안 계속해서 요청과 응답이 반복된다는 것이 가장 큰 차이점

- RESTful API는 데이터 중심의 요청-응답 모델에 적합합니다.
- WebSocket은 실시간성이 중요한 경우(채팅, 주식 시세, 게임) 적합합니다.
- 실제 시스템에서는 RESTful API + WebSocket을 함께 사용하는 경우가 많습니다.
예: 회원 가입/로그인 → REST API, 채팅 메시지 송수신 → WebSocket

| 구분 | RESTful API | WebSocket |
| --- | --- | --- |
| **통신 방식** | 요청-응답(Request/Response) | 양방향 실시간 통신(Full-duplex) |
| **연결** | 요청마다 새 연결(Stateless) | 한 번 연결 후 계속 유지(Stateful) |
| **사용 목적** | CRUD 작업, 리소스 기반 데이터 조작 | 실시간 알림, 채팅, 게임, 스트리밍 |
| **데이터 전송** | JSON, XML 등 (HTTP 기반) | 텍스트/바이너리 프레임 |
| **장점** | 단순, 표준화, 캐싱 용이 | 실시간성, 지연시간 최소화 |
| **단점** | 실시간 알림에 비효율적 | 상태 관리 필요, 서버 리소스 부담 |

---

![RESTful API](../images/restful-api.png)