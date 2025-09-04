# 코드 리뷰

## [1221. GNS]

### 내 코드

```python
# 1221. GNS

# import sys
# sys.stdin = open("GNS_test_input.txt")

T = int(input())  # 테스트 케이스의 수

numbers = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]

def counting_sort(arr, K):
    """
    카운팅 정렬 방식으로 정렬한 배열을 반환하는 함수
        K: 주어진 배열의 요소 중 최대값
    """
    # 카운트 배열 생성
    count = [0] * (K+1)
    for num in arr:
        count[numbers.index(num)] += 1

    # 카운트 배열 누적합
    for i in range(1, K+1):
        count[i] += count[i-1]

    # 결과 배열에 저장
    sorted_arr = [0] * len(arr)
    for num in reversed(arr):
        count[numbers.index(num)] -= 1
        sorted_arr[count[numbers.index(num)]] = num

    return sorted_arr

for _ in range(T):
    # tc: 테스트 케이스의 번호(# 포함)
    # len_s: 테스트 케이스의 길이, 즉 단어의 개수
    tc, len_s = input().split()
    len_s = int(len_s)
    # s: 외계행성의 숫자들
    s = list(input().split())

    sorted_s = counting_sort(s, 9)

    print(tc)
    print(*sorted_s)
```

### 코드리뷰 피드백

카운팅 정렬에서 결과 배열에 값을 할당할 때, 해당 문제의 경우 **정렬의 안정성을 보장할 필요가 없기 때문**에 누적합한 카운트 배열의 값(int)을 arr의 값(str)의 `*` 반복으로 활용할 수 있다.

```python
# 누적합한 카운트 배열에서 바로 결과 출력
for num in numbers:
    num_cnt = count[numbers.index(num)]
    print((num + ' ') * num_cnt, end='')
```

## [5432. 쇠막대기 자르기]

### 내 코드

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

### 내 코드

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

## [1216. 회문2]
### 내 코드

**1번 코드**: 매번 가로, 세로 문자에 대한 회문검사 진행.

```python
# 1216. 회문2
# 시간이 너무 많이 걸림! (테스트케이스는 나오는데, 제출하면 output 안 나옴)

# import sys
# sys.stdin = open('input.txt')

def is_palindrome(word, k):
    for i in range(k//2):
        if word[i] != word[-1-i]:
            return False
    else:
        return True

T = 10
for _ in range(T):
    tc = input().strip()  # 테스트 케이스의 번호
    N = 100  # 배열의 크기
    arr = [input() for _ in range(N)]

    max_len = 0  # 회문의 최대 길이

    # 현재 위치(i, j)를 이동한다. 
    for i in range(N):
        for j in range(N):
            # k: 탐색할 단어의 길이 (N-j 부터 max_len 까지. 최대 길이부터 탐색)
            for k in range(N-j, max_len, -1):
                # 가로 문자
                # 최대 길이 갱신
                if is_palindrome(arr[i][j:j+k], k):
                    max_len = k
            
                # 세로 문자
                word = list(zip(*arr[j:j+k]))[i]
                if is_palindrome(word, k):
                    max_len = k
            
    
    print(f'#{tc} {max_len}')
```

**2번 코드**: 전치 행렬을 만들고 탐색 시작.

```python
# 1216. 회문2

# import sys
# sys.stdin = open('input.txt')

def is_palindrome(word, k):
    for i in range(k//2):
        if word[i] != word[-1-i]:
            return False
    else:
        return True

T = 10
for _ in range(T):
    tc = input().strip()  # 테스트 케이스의 번호
    N = 100  # 배열의 크기
    arr = [input() for _ in range(N)]
    rotated_arr = list(zip(*arr))  # 전치 행렬

    max_len = 0  # 회문의 최대 길이

    # 현재 위치를 이동하면서 가로, 세로 회문의 개수를 더한다.
    for i in range(N):
        for j in range(N):
            # k: 탐색할 단어의 길이 (N-j 부터 max_len 까지. 최대 길이부터 탐색)
            for k in range(N-j, max_len, -1):
                # 현재 탐색할 단어의 길이(k)가 최대 길이보다 짧으면 다음 위치로 넘어간다.
                # if k <= max_len:
                #     break
                # 최대 길이 갱신
                if is_palindrome(arr[i][j:j+k], k):
                    max_len = k
                if is_palindrome(rotated_arr[i][j:j+k], k):
                    max_len = k
    
    print(f'#{tc} {max_len}')
```

### 코드리뷰 피드백

전치 행렬 구할 때, 문자열 `.join()`메서드를 이용하여 다시 문자열로 합칠 수 있다.

```python
# 문자열로 구성된 배열의 전치 행렬
grid_T = list(map(''.join, zip(*grid)))
```

### 두 코드 비교

- 1번 코드의 시간 복잡도: 약 $O(N^5)$
    
    1번 코드는 세로 회문을 찾을 때마다 `word = list(zip(*arr[j:j+k]))[i]`와 같이 zip 함수를 이용해 전치 행렬(transposed matrix)을 매번 새롭게 생성합니다.
    
- 2번 코드의 시간 복잡도: 약 $O(N^4)$
    
    2번 코드는 메인 로직을 시작하기 전에 `rotated_arr = list(zip(*arr))`를 사용하여 전체 전치 행렬을 단 한 번만 미리 계산합니다.

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


### 회문

똑바로 읽어도, 거꾸로 읽어도 똑같은 문장이나 낱말

```python
def is_palindrome(txt):
		for i in range(1, len(txt) // 2):
				if txt[i] != txt[len(txt) - i]:
						return False
		return True
```

### `==` 연산자와 `is` 연산자

`==`는 값(value)이 같은지를 비교한다.

`is`는 객체의 정체성(identity), 즉 같은 객체(메모리 주소)인지 비교한다.

```python
a = [1, 2, 3]
b = [1, 2, 3]

print(a == b)  # True (값이 같음)
print(a is b)  # False(객체가 다름)
```

### 사전 순서 비교

비교 연산자(`<`, `>`, `=` 등)를 사용하여 유니코드 값을 비교한다.

```python
print('9' < '14')  # False (문자열일 때, '9'가 '1'보다 크다.)
print('Apple' < 'apple')  # True
```