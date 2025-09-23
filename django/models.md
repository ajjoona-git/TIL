## 실습
### Database Client - VSCode 확장자

- SQLite로 데이터베이스를 연결하면 다음과 같이 확인 가능
- 필드 옵션 중 `null=True`이면 파란색으로 표현된다!

![database client](../images/models_1.png)

### Validator (유효성 검사)

- min_length 필드 옵션은 없음.

```python
from django.db import models
from django.core.validators import MinLengthValidator

class APIInfo(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    api_url = models.URLField(max_length=60, validators=[MinLengthValidator(15)])
    documentation_url = models.URLField()
    auth_required = models.BooleanField()
    additional_info = models.JSONField(black=True, null=True, default=None)
    created_at = models.DateTimeField(auto_now_add=True)

```

<hr>

## Model

### SQLite

데이터베이스 관리 시스템 중 하나로, django의 기본 데이터베이스로 사용된다.

- 데이터베이스가 하나의 파일로 저장되어 설치/설정 없이 간편하게 복사/이동/백업이 가능하다.
- 별도 서버 없이 파일로 직접 데이터를 처리한다. 소규모 앱이나 모바일 환경에 최적화
- 호환성이 높다.
- `db.sqlite3` 파일은 git 등 버전 관리 시스템에서 관리하지 않는다.
    - 데이터가 변경될 때마다 파일 전체가 변경되기 때문
    - SQLite 파일은 로컬 컴퓨터에 저장된 데이터 기록
    - `.gitignore` 파일에 `db.sqlite3` 추가

### Model

**데이터베이스**와 python 클래스(**객체**)로 추상화된 형태로 상호작용

- **model ≠ DB**
- Django의 강력한 기능: 개발자가 데이터베이스에 대한 깊은 지식 없이도 쉽게 데이터 관리 가능
- 유지보수 및 확장성 증대: 데이터베이스 변경 시에도 코드 수정 최소화, 재사용 가능한 데이터 모델을 통해 개발 효율성 향상

### Model을 통한 DB(데이터베이스) 관리

![프로젝트 구조](../images/models_2.png)

- `urls.py` 사용자 요청의 시작점
- `views.py` 요청을 처리하고 models.py를 통해 데이터를 다룬다.
- `models.py` 데이터베이스를 정의하고, 데이터베이스와 상호작용한다.
- `templates` views.py로부터 받은 데이터를 사용자에게 보여줄 화면을 구성한다.

### Model class

DB의 테이블을 정의하고 데이터를 조작할 수 있는 기능들을 제공한다.

![model class](../images/models_3.png)

- 앱 폴더의 `models.py`에 작성한다.
- 데이터베이스 **테이블의 구조를 설계**하는 ‘청사진(blueprint)’ 역할
- 어떤 데이터(컬럼)를 저장할 지, 그 데이터는 어떤 형태(타입, 길이 등)인지를 python 코드로 정의
- id 필드는 django가 자동 생성한다.

### Model class 정의

```python
# articles/models.py
# 내장된 django 패키지 안에 db 서브 패키지 안에 models.py라는 모듈을 import
from django.db import models

# 게시글을 저장받기 위한 테이블 하나
class Article(models.Model):
		title = models.CharField(max_length=10)
		content = models.TextField()
```

- 모델 클래스로 정의하며, **Model 클래스를 상속**받는다.
    - Model은 model에 관련된 모든 코드가 이미 작성되어 있는 class.
    - ‘테이블 구조를 어떻게 설계할지’에 대한 코드만 작성할 수 있도록 ‘상속’을 활용해 프레임워크 기능을 제공해준다.
- 클래스 변수명(`title`, `content`)은 테이블의 각 “**필드(column)명**”이 된다.
- Model Field는 **“데이터의 유형”과 “제약 조건”**을 정의한다.
    - 데이터베이스 테이블의 열(column)을 나타내는 중요한 구성 요소
    - `CharField`의 `max_length` 매개변수는 선택 사항
        - 유효성 검사 및 데이터의 명확성을 위해 명시적으로 설정하는 것을 권장한다.

### Model Field

- DB 테이블의 필드(열) 정의
- 데이터 타입 (field types) 및 제약 조건 (field options) 명시
- django는 필드 정의를 바탕으로 데이터베이스 컬럼을 자동으로 생성하고 데이터 입력 시 유효성 검사 등 필요한 기능을 제공한다.

- **Field Types :** 데이터베이스에 저장될 ‘데이터의 종류’를 정의한다.
    - models 모듈의 클래스로 정의되어 있다.
    - 문자열 필드
        - `CharField()` 제한된 길이의 문자열을 저장
        - `TextField()` 길이 제한이 없는 대용량 텍스트를 저장
    - 숫자 필드: IntegerField, FloatField
    - 날짜/시간 필드: DataField, TimeField, DateTimeField
    - 파일 관련 필드: FileField, ImageField

- **Field Options :** 필드의 동작과 제약 조건을 정의한다.
    - `max_length`
    - `null` 데이터베이스에서 NULL값을 허용할지 여부를 결정 (기본값: False)
    - `blank` form에서 빈 값을 허용할지 여부를 결정 (기본값: False)
    - `default` 필드의 기본값을 설정