## admin 등록 시 인자의 순서 주의!
### 실습

```python
# accounts/admin.py
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

# admin.site.register(UserAdmin, User) -> 아래와 같은 오류 발생
admin.site.register(User, UserAdmin)
```

![오류 메시지](../images/custom-user-model_1.png)

`admin.site.register()` 함수는 **첫 번째 인자**로 **모델 클래스**(`User`)를 받고, **두 번째 인자**로 해당 모델의 관리자 페이지를 커스터마이징할 **Admin 클래스**(`UserAdmin`)를 받습니다. 현재 코드에서는 이 두 인자의 순서가 바뀌어 있습니다.


## Django Authentication System

### 인증 (Authentication)

사용자를 식별하기 위해서 필요한 과정

- 클라이언트와 서버 간의 상태 정보를 유지하기 위해 쿠키와 세션을 사용한다.
- 인증 방법 예시: 아이디와 비밀번호, 소셜 로그인 (OAuth), 생체 인증

### Django Authentication System

Django에서 사용자 인증과 관련된 기능을 모아 놓은 시스템

- User Model: 사용자 인증 후 연결될 User Model 관리
- Session 관리: 로그인 상태를 유지하고 서버에 저장하는 방식을 관리
- 기본 인증 (ID/PW): 로그인/로그아웃 등 다양한 기능을 제공


## Custom User Model

### 기본 User Model의 한계

- 인증 후 사용되는 User Model은 별도의 User 클래스 정의 없이 **내장된 auth 앱**에 작성된 User 클래스를 사용했다.
    - username, password, email 등의 필드를 가진 User 모델을 제공한다.
    - 사용자별 또는 그룹별로 특정 행동에 대한 권한 부여가 가능하다.
- 추가적인 사용자 정보 (예: 생년월일, 주소, 나이 등)가 필요하다면 이를 위해 기본 User Model을 변경하기 어렵다. 개발자가 직접 수정하기 어렵다.

⇒ 프로젝트 특정 요구사항에 맞춰 사용자 모델을 확장할 수 있게 커스텀하자!

### User Model 대체하기

- [Django 공식 문서](https://docs.djangoproject.com/en/5.2/topics/auth/customizing/#substituting-a-custom-user-model)
- django는 기본 User 모델이 충분하더라도 **커스텀 User 모델을 설정하는 것을 강력하게 권장**한다.
    - 커스텀 User 모델은 기본 User 모델과 동일하게 작동하면서도 나중에 맞춤 설정(필드 추가 등)할 수 있기 때문

1. 새로운 app `accounts` 생성 및 등록
    - auth와 관련한 경로나 키워드들은 `accounts`로 지정하는 것을 권장한다.

```python
# settings.py
INSTALLED_APPS = [
    'accounts',
    ...
]
```

```python
# accounts/urls.py
from django.urls import path
from . import views

app_name = 'accounts'
urlpatterns = []
```

2. AbstractUser 클래스를 상속받는 커스텀 User 클래스 생성
    - 기존 User 클래스도 AbstractUser를 상속받기 때문에 커스텀 User 클래스도 기존 User 클래스와 완전히 같은 모습을 가지게 된다.

```python
# accounts/models.py
from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    pass
```

3. django 프로젝트에서 사용하는 기본 User 모델을 커스텀 User 모델로 사용할 수 있도록 `AUTH_USER_MODEL` 값을 변경
    - 수정 전 기본 값은 `auth.User`
    - django는 프로젝트 중간에 AUTH_USER_MODEL을 변경하는 것을 강력하게 권장하지 않는다.
        - **프로젝트의 모든 migrations 혹은 첫 migrate를 실행하기 전에 user 모델 대체 작업을 마쳐야 한다.**
        - 이미 프로젝트가 진행되고 있을 경우 데이터베이스 초기화 후 진행한다.

```python
# settings.py

# django의 기본 유저 모델을 설정(대체)
AUTH_USER_MODEL = 'accounts.User'
```

4. admin site에 대체한 User 모델 등록
    - 기본 User 모델이 아니기 때문에 등록해야 admin 페이지에 출력된다.

```python
# accounts/admin.py
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

admin.site.register(User, UserAdmin)
```
