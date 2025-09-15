## 동적 계획법 (DP, Dynamic Programming)

이전에 계산한 결과(부분 문제)를 **메모**하여 **중복 계산을 방지**하는 방법

- 최적화 문제에 자주 사용된다.

### **DP를 적용하기 위한 조건**

1. **겹치는 부분 문제**
    - 큰 문제를 작은 문제로 쪼갤 때, **동일한 작은 문제가 반복적으로 나타나는** 경우
    - 예시: 피보나치 수열에서 `fibo(5)`를 구하기 위해 `fibo(3)`이 두 번 호출되는 것
2. **최적 부분 구조**
    - 큰 문제의 최적 해답을, **작은 문제들의 최적 해답들을 통해** 구할 수 있다.
    - 예시: `fibo(5)`의 해답이 `fibo(4)`와 `fibo(3)`의 해답으로 구성되는 것

### 메모이제이션 (Memoization)

이전에 계산한 결과를 메모리에 저장해두고, 동일한 계산이 반복될 때 다시 계산하지 않고 저장된 값을 바로 꺼내 쓰는 프로그래밍 기술

### 예제: 피보나치 수열

1. **재귀를 이용한 접근**

```python
def fibo_recursion(num):
    if num <= 1:
        return num
    # fibo(n) = fibo(n-1) + fibo(n-2)
    return fibo_recursion(num - 1) + fibo_recursion(num - 2)

fibo_recursion(40) # 실행 시 약 30~60초 소요
```

1. **Top-Down 방식 (하향식, 메모이제이션)**
- 이전에 계산한 결과를 저장해두고 재활용한다.

```python
# 메모를 위한 리스트 또는 딕셔너리 준비 (0으로 초기화)
memo = [0] * 101

def fibo_memo(num):
    # 기저 조건
    if num <= 1:
        return num
    
    # 이미 메모한 값이 있다면, 계산하지 않고 바로 반환
    if memo[num] != 0:
        return memo[num]
    
    # 아직 계산한 적 없다면, 계산 후 메모
    memo[num] = fibo_memo(num - 1) + fibo_memo(num - 2)
    return memo[num]

fibo_memo(40) # 실행 시 0.001초 미만 소요
```

1. **Bottom-Up 방식 (상향식, 타뷸레이션)**
- 반복문을 이용해 결과를 테이블에 저장한다.

```python
def fibo_dp(num):
    # 결과를 저장할 테이블(리스트) 생성
    dp_table = [0] * (num + 1)
    dp_table[1] = 1 # 초기값 설정

    # 2부터 num까지, 작은 문제부터 순서대로 테이블을 채워나감
    for i in range(2, num + 1):
        dp_table[i] = dp_table[i - 1] + dp_table[i - 2]
    
    return dp_table[num]

fibo_dp(40) # 실행 시 0.001초 미만 소요
```