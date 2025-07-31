# 스스로 학습

## 실습

### [1467. 사용자 정보 클래스 예외 처리_Lv4]

| 내 코드 | 강사님 코드 |
| --- | --- |
| `if name.strip(' ') == '':` | `if not name.strip():`  |
| `if len(self.user_data) > 0:` | `if self.user_data:`  |

- 파이썬에서 빈 시퀀스(문자열, 리스트, 튜플 등)가 `False`로 평가되는 특성을 적극 활용하자!
- input()에서 미입력과 공백 입력
    - 미입력: `''` 빈 문자열
    - 공백 입력: `'  '` 공백을 요소로 가지는 문자열 → str.strip() 메서드 활용해서 양옆 공백을 제거

<br><br>


# 수업 필기

## 에러와 예외

### 디버깅 (Debugging)

소프트웨어에서 발생하는 버그를 찾아내고 수정하는 과정

- 버그(bug) : 소프트웨어에서 발생하는 오류 또는 결함
- print(), python tutor, 개발 환경(text editor, IDE) 등에서 제공하는 기능 활용

### 에러

1. 문법 에러 (Syntax Error): 프로그램의 구문이 올바르지 않은 경우
    1. 오타, 괄호 및 콜론 누락 등
2. 예외 (Exception): 프로그램 실행 중에 감지되는 에러
    1. 내장 예외: 예외 상황을 나타내는 예외 클래스들
        1. ZeroDivisionError, FileNotFoundError, NameError, TypeError, IndexError 등

## 예외 처리

### try-except

- `try:` 예외가 발생할 수 있는 코드
- `except:` 예외가 발생했을 때 실행
- `else:` 예외가 발생하지 않았을 때 실행
- `finally:` 예외 발생 여부와 상관없이 **항상 실행**

```python
try:
    x = int(input('숫자를 입력하세요: '))
    y = 10 / x
except ZeroDivisionError:
    print('0으로 나눌 수 없습니다.')
except ValueError:
    print('유효한 숫자가 아닙니다.')
else:
    print(f'결과: {y}')
finally:
    print('프로그램이 종료되었습니다.')

'''
숫자를 입력하세요: 0
0으로 나눌 수 없습니다.
프로그램이 종료되었습니다.
'''

'''
숫자를 입력하세요: hi
유효한 숫자가 아닙니다.
프로그램이 종료되었습니다.
'''

'''
숫자를 입력하세요: 5
결과: 2.0
프로그램이 종료되었습니다.
'''
```

### 예외 처리 순서

except **작성 순서대로 실행**된다.

- `except Exception:` 을 첫 번째 except로 작성한다면, 그 아래에 있는 ZeroDivisionError 전용 처리 코드에 영원히 도달하지 못한다.
    - 내장 예외 클래스는 상속 계층구조를 가지기 때문
- **반드시 하위 클래스를 먼저 확인**할 수 있도록 작성해야 한다.
- 그래서 항상 범용적인 예외 처리 (Exception)는 마지막에 두어야 한다.

## 참고

### 예외 객체 다루기

- as 키워드 활용

```python
try:
    number = my_list[1]
except IndexError as error:
    # list index out of range가 발생했습니다.
    print(f'{error}가 발생했습니다.')
```

- try-except와 if-else를 함께 사용

### EAFP & LBYL

- Easier to Ask for Forgiveness than Permission
    - 예외처리를 중심으로 코드를 작성하는 접근 방식
    - try - except : 일단 실행하고 예외를 처리
    - 예외 상황을 예측하기 어려운 경우에 유용
- Look Before You Leap
    - 값 검사를 중심으로 코드를 작성하는 접근 방식
    - if - else : 실행하기 전에 조건을 검사
    - 예외 상황을 미리 방지하고 싶을 때 유용