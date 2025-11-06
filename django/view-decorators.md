## View Decorators

### View Decorators

- view 함수의 동작을 수정하거나 추가 기능을 제공하는 데 사용되는 python 데코레이터
- 뷰 함수 위에 붙어서 작동되며, 코드 흐름을 방해하지 않고 깔끔하게 조건을 설정 가능
- **View decorators 종류**
    - `@login_required` 로그인 여부
    - Allowed HTTP methods: 뷰가 허용하는 HTTP 요청 방식 (GET, POST 등)을 제한
    - Conditional view processing: 클라이언트가 보낸 조건을 확인 후, 조건에 따른 응답 처리
    - GZip compression: 서버에서 응답 데이터를 압축해서 전송

### Allowed HTTP methods

- 특정 HTTP method로만 View 함수에 접근할 수 있도록 제한하는 데코레이터
- 요청 방식을 제한하면 보안이 강화되고, 코드의 역할도 명확하게 분리된다.
- 허용되지 않은 method로 요청하는 경우 `405 (Method Not Allowed)` 오류 반환

- **`require_http_methods(["METHID1", "METHOD2", ...])`**: 지정된 HTTP method만 허용
    - 인자는 list이고, list의 요소는 HTTP method를 **문자열(대문자)**로 작성
- `require_safe()`: **GET**과 HEAD method만 허용
    - GET과 HEAD는 서버 상태를 변경하지 않고 조회를 수행
    - 사용 예: `views.detail`, `views.index`
- `require_POST()`: **POST** method만 허용
    - 사용 예: `views.delete`

```python
from django.views.decorators.http import require_http_methods, require_safe, require_POST

@require_http_methods(['GET', 'POST'])
def func(request):
	pass
	
@require_safe
def detail(request):
	pass
	
@require_POST
def delete(request):
	pass
```