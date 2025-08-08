# 코드 리뷰

## [5432. 쇠막대기 자르기]

## 내 코드

1. 쇠막대기의 끝점이 발견될 때마다 해당 쇠막대기의 조각 수를 더해준다.
- 2중 for문: $O(N^2)$ → 제한 시간 초과

```python
# 5432. 쇠막대기 자르기

# import sys
# sys.stdin = open("sample_input.txt")

T = int(input())  # 테스트 케이스의 수

for tc in range(1, T+1):
    info = input()  # 레이저와 쇠막대기의 배치 정보(str)
    stick = []  # 쇠막대기의 정보를 저장할 리스트
    laser = []  # 레이저의 정보를 저장할 리스트
    result = 0  # 조각의 수

    for i in range(len(info)):
        # 1. '('이면 일단 stick에 저장
        if info[i] == '(':
            stick.append(i)
        # 2. ')'이면
        else:
            # 2-1. stick의 마지막 값이 직전 인덱스라면 레이저
            if stick[-1] == (i - 1):
                stick.pop()
                laser.append(i)
            # 2-2. 아니라면 stick의 마지막 값이 현재 쇠막대기의 끝점
            else:
                result += 1
                # 현재 쇠막대기 조각이 몇 개인지 계산
                for j in range(stick.pop() + 1, i):
                    if j in laser:
                        result += 1

    print(f'#{tc} {result}')
```

2. 레이저를 발견할 때마다 쇠막대기 조각 수를 더해준다.
- 단일 for문: $O(N)$

```python
# 5432. 쇠막대기 자르기

import sys
sys.stdin = open("sample_input.txt")

T = int(input())  # 테스트 케이스의 수

for tc in range(1, T+1):
    info = input()  # 레이저와 쇠막대기의 배치 정보(str)
    stick = []  # 쇠막대기의 정보를 저장할 리스트
    result = 0  # 조각의 수

    for i in range(len(info)):
        # 1. '('이면 일단 stick에 저장
        if info[i] == '(':
            stick.append(i)
        # 2. ')'이면 가장 최근에 저장한 (의 인덱스 확인
        else:
            # 2-1. stick의 마지막 값이 직전 인덱스라면 레이저
            if stick.pop() == (i - 1):
                # 현재 stick에 있는 쇠막대기 수만큼 추가
                result += len(stick)
            # 2-2. 아니라면 stick의 마지막 값이 현재 쇠막대기의 끝점
            else:
                result += 1

    print(f'#{tc} {result}')
```

## [5356. 의석이의 세로로 말해요]

## 내 코드

```python
# 5356. 의석이의 세로로 말해요

# import sys
# sys.stdin = open("sample_input.txt")

from itertools import zip_longest

T = int(input())  # 테스트 케이스의 수

for tc in range(1, T+1):
    letters = [input() for _ in range(5)]
    result = ""

    # zip() 함수 이용하되, 빈 값을 빈 문자열('')로 처리해야 하므로
    # itertools 모듈의 zip_longest 함수를 사용함
    for letter in zip_longest(*letters, fillvalue=''):
        for char in letter:  # letter 예시: ('A', 'a', '0', 'F', 'f')
            result += char

    print(f"#{tc} {result}")
```

### `zip()`과 `zip_longest()`

zip() 함수 사용할 때 값의 크기가 다른 경우, 반복이 중단된다.

`zip()`함수는 여러 이터러블 객체를 인자로 받아 각 객체에서 동일한 인덱스에 있는 요소를 튜플로 묶어 반환합니다.
이때, 인자로 전달된 이터러블 객체들의 크기가 다르면,`zip()`함수는 **가장 짧은 이터러블 객체의 길이에 맞춰 동작**합니다.
즉, 길이가 짧은 이터러블 객체에 맞춰 나머지 이터러블 객체들의 요소는 잘려서 버려집니다.


대신, `itertools` 모듈의 `zip_longest()` 함수는 길이가 다른 이터러블들을 묶을 때 가장 긴 이터러블의 길이에 맞춰줍니다.
짧은 쪽이 먼저 끝나면, `fillvalue`로 지정한 값으로 빈 공간을 채웁니다. `fillvalue`를 지정하지 않으면 기본값인 `None`으로 채워집니다.



<br><br>

# 수업 필기

## 문자열 (String)

문자들이 순서대로 나열된 데이터

- Length-Controlled 문자열
    
    문자열의 길이 정보를 함께 저장해서 그 길이만큼 문자 데이터를 읽는 방식
    
    - Java, Python, 네트워크 패킷에 사용
- Delimited 문자열
    
    문자열의 끝을 나타내는 특정한 구분자(Delimiter)가 있어서, 구분자가 나올 때까지 문자열로 인식한다.
    
    - C언어는 널문자(`null`, `\0`)를 사용

### C언어에서의 문자열

- 문자열은 문자들의 배열 형태로 구현된 응용 자료형
- 문자배열에 문자열을 저장할 때는 항상 마지막에 끝을 표시하는 널문자(`\0`) 필요
- 문자열 처리에 필요한 연산을 함수 형태로 제공한다.
    - `strlen()`, `strcpy()`, `strcmp()`

### Java에서의 문자열

- 문자열 데이터를 저장, 처리해주는 클래스를 제공한다.
- String 클래스
- 문자열 처리에 필요한 연산자를 연산자, 메소드 형태로 제공한다.
    - `+`, `length()`, `replace()`, `split()`, `substring()`

### Python3에서의 문자열

- 텍스트 데이터의 취급방법이 통일되어 있다.
- 문자열 기호: `'`, `"`, `'''`, `"""`
- str 클래스
    - 길이 외에 다른 정보(예: 해시값, 같은 문자열을 관리하는 플래그, 문자열 인코딩의 크기, 메모리 주소를 가리키는 포인터 등)를 포함해서 저장한다.
- 문자열은 튜플과 같이 요소값을 **변경할 수 없다. (immutable)**
- 문자열은 데이터의 순서가 구분되는 **시퀀스** 자료형으로 분류된다.
    - **인덱싱, 슬라이싱** 연산 사용가능
- 문자열 클래스에서 제공되는 메소드
    - `replace()`, `split()`, `isalpha()`, `find()`
    - `+`연결 (Concatenation): 문자열을 이어 붙여주는 역할
    - `*` 반복: 수만큼 문자열이 반복된다.

### C, Java, Python3 문자열의 차이

| 프로그래밍 언어 | C언어 | Java | Python |
| --- | --- | --- | --- |
| 문자열 저장 | ASCII 코드 | 유니코드(UTF-16, 2-Byte) | 유니코드(UTF-8) |
| `name = "홍길동"`의 길이 | `strlen(name)` , 6 | `name.length()` , 3 | `len(name)`, 3 |