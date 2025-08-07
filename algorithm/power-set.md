# 스스로 학습

## [비트연산]
### 질문. `for i in range(1 << n):` 에서  `i`는 2진수의 형태(`1000000`)와 10진수 형태(`256`) 중 어떤 것을 받아오는가?

`for i in range(1 << n):`에서 `i`는 **10진수 형태의 정수**를 받아온다.

파이썬의 `range()` 함수는 항상 정수(int) 형태의 시퀀스를 생성한다. `1 << n`이라는 비트 연산의 결과 역시 정수(int)다. 예를 들어, `n=3`일 때 `1 << n`은 `1 << 3`, 즉 `8`이다. 따라서 `range(1 << n)`은 `range(8)`과 같고, `i`는 `0, 1, 2, 3, 4, 5, 6, 7`이라는 10진수 정수를 차례대로 갖게 된다.

하지만 `i`가 10진수 형태일지라도, `if i & (1 << j):`와 같은 비트 연산자를 사용하면 파이썬은 내부적으로 **두 피연산자를 2진수 형태로 변환하여 연산을 수행**한다.


<br><br>

# 수업 필기

## 부분집합 (Power Set)

집합 S의 모든 원소를 **포함/미포함**해 만들 수 있는 모든 하위 집합

- 모든 부분집합을 전부 나열하는 방식: `$O(N * 2^N)$`

### 부분집합 문제 접근 방식

1. 완전검색
    
    모든 부분집합을 생성한 후에 각 부분집합의 합을 계산한다.
    
    → 집합의 원소가 N개일 때, 공집합을 포함한 부분집합의 수는 **`$2^N$`**개 (조합)
    
2. 그리디
    
    조건에 맞는 경우 주어진 집합의 부분집합을 생성하는 방법을 생각해본다.
    

### 부분집합을 생성하는 방법

1. **반복문 (중첩 loop)**
- N=3, 4일 때 직관적인 접근

```python
arr = [1, 2, 3]
bit = [0] * len(arr)

# arr[i]의 원소가 부분집합에 포함되지 않으면 bit[i] == 0
# arr[i]의 원소가 부분집합에 포함되면 bit[i] == 1

for i in range(2):  # [0, 1]
		bit[0] = i
		for j in range(2):
				bit[1] = j
				for k in range(2):
						bit[2] = k
						print(bit)
						# [0, 0, 0], [0, 0, 1], [0, 1, 0], [0, 1, 1], ... , [1, 1, 1]
```

2. **재귀(Backtracking) 방식**
- 원소가 많아질 때 가장 직관적인 접근, 확장 가능

```python
def generate_subset(depth, included):
    """
    현재 원소를 "포함한다/포함하지 않는다" 두 갈래로 재귀 호출하며 부분집합을 생성한다.
    depth: 현재 확인할 원소 인덱스
    included: 각 원소가 포함됐는지(True/False)를 기록
    """
    # 모든 원소를 결정한 시점
    if depth == len(input_list):
        # included 상태에 따라 부분집합 생성
        current_subset = [
            input_list[i] for i in range(len(input_list)) if included[i]
        ]
        subsets.append(current_subset)
        return

    # (1) 현재 원소를 포함하지 않는 경우
    included[depth] = False
    generate_subset(depth + 1, included)

    # (2) 현재 원소를 포함하는 경우
    included[depth] = True
    generate_subset(depth + 1, included)
```

3. **비트마스크 (binary counting)**
- `i`의 2진수 표현을 각 원소를 포함시킬지 말지에 대한 ‘체크리스트’로 활용하는 것
- N이 최대 20~30까지면 효율적

```python
arr = [3, 6, 7, 1, 5, 4]

n = len(arr) 		# n : 원소의 개수

for i in range(1 << n) : 		# 1<<n == 2**n : 부분 집합의 개수
		subset = []
		for j in range(n):		  # 각 원소에 접근하기 위한 인덱스 j
		    # i의 j 번째 비트가 1이면 True
        if i & (1 << j):
            subset.append(arr[j])
```

### [참고] 비트 연산

| 비트 연산자 | 설명 | 활용 |
| --- | --- | --- |
| `&` | 비트 AND | `i & (1<<j)` i의 j번째 비트가 1인지 아닌지를 검사 |
| `|` | 비트 OR |  |
| `<<: *= 2`  | 비트를 왼쪽으로 이동 | `1 << n: $2^n$` 원소가 n개일 경우의 모든 부분집합의 수 |
| `>>: //= 2`  | 비트를 오른쪽으로 이동 |  |
| `^` | 비트 XOR (Exclusive) |  |
| `~`  | 비트 NOT |  |