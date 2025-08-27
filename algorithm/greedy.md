# 스스로 학습

### (참고) set의 시간복잡도

검색(`in` , `for` 등)을 사용할 때는 set을 활용하는 것이 시간복잡도가 빠르다.

```python
# 리스트 사용 예시 -> O(N)
a = [1, 2, 3, 4]
if 1 in a:

# 세트 사용 예시 -> O(1)
b = {1, 2, 3, 4}
if 1 in b:
```

ex) 0과 1로 이루어진 리스트(switches)에 1이 있는지 확인하는 경우

```python
# 리스트 사용 예시
for switch in switches:
	if switch == 1:

# 세트 사용 예시
if len(set(switches)) == 2:
```

# 수업 필기

## 탐욕 알고리즘 (Greedy)

각 순간에 최적이라고 생각되는 것을 선택해 나가는 방식

- 최적화 문제(optimization): 가능한 해들 중에서 가장 좋은 (최대 또는 최소) 해를 찾는 문제
- 각 선택 시점에서 이루어지는 결정은 지역적으로는 최적이지만,
그 선택들을 계속 수집하여 최종적인 해답을 만들었다고 하여 그것이 최적이라는 보장은 없다.
- 일반적으로 머리 속에 떠오르는 생각을 검증 없이 바로 구현하면 Greedy접근이 된다.
- 단순하며 제한적인 문제들에 적용된다.

### 탐욕 알고리즘의 필수 요소

**“원문제의 최적해 = 탐욕적 선택 + 하위 문제의 최적해”** 임을 증명할 것.

1. 탐욕적 선택 속성 (greedy choice property)
    - 탐욕적 선택이 최적해로 갈 수 있음을 보여라.
2. 최적 부분 구조 (optimal substructure property)
    - 최적화 문제를 정형화하라
    - 하나의 선택을 선택하면 풀어야 할 하나의 하위 문제가 남는다.

### 대표적인 탐욕 알고리즘

- Prim: 서브트리를 확장하면서 MST를 찾는다.
- Kruskal: 사이클이 없는 서브그래프를 확장하면서 MST를 찾는다.
- Dijkstra: 가장 가까운 정점을 찾고, 그 다음 정점을 반복해서 찾는다.

### 예제: 거스름돈

**문제 설명**

거스름돈으로 주는 동전의 개수를 최소한으로 하는 방법

- Case 1: 500, 100, 50, 10
- Case 2: 500, 400, 50, 10

**greedy 접근**

큰 동전부터 최대한 거슬러 준다. 

- case 1의 최적 방법
- case 2에서는 400 * 2가 최적임
    
    → 거스름돈이 배수관계가 아니면 적용 불가하다.
    

**case 1에 대한 코드 예제**

```python
def get_minimum_coins(coins, amount):
    result = {}
    # 가장 큰 잔돈부터 거슬러줄 것이므로 내림차순으로 정렬
    coins.sort(reverse=True)

    # 각 동전에 대해서 가장 큰 잔돈부터 최대로 거슬러준다.
    for coin in coins:
        # 거스름돈이 잔돈보다 작으면, 해당 잔돈으로는 줄 수 없다.
        if amount < coin:
            continue

        # 거스름돈 // 잔돈으로 해당 동전의 개수를 구한다.
        count = amount // coin
        # 거슬러준 잔돈만큼 거스름돈을 갱신한다.
        amount -= (coin * count)
        # 거슬러준 동전과 그의 개수를 저장한다.
        result[coin] = count

    return result
```

```python
coins = [1, 5, 10, 50, 100, 500]  # 동전 종류
amount = 482  # 거스름돈

result = get_minimum_coins(coins, amount)
for coin, count in result.items():
    print(f"{coin}원: {count}개")
    
"""
실행 예시

100원: 4개
50원: 1개
10원: 3개
1원: 2개
"""
```

### 예제: Knapsack

**문제 설명**

W를 넘지 않으면서 만들 수 있는 최대 가치 합

- **0-1 Knapsack**: 물건을 쪼갤 수 없는 경우
    1. **완전 탐색**
        
        모든 부분 집합을 구한다.
        
        부분집합의 총 무게가 W를 초과하면 버리고, 나머지 집합에서 총 값이 가장 큰 집합을 선택한다.
        
        → 물건의 개수가 증가하면 시간 복잡도가 지수적으로 증가한다. 
        
        - 시간 복잡도: $O(2^N)$
    2. **Greedy (풀이 불가)**
        - 값이 비싼 물건부터 채운다. → 최적이 아니다.
        - 무게가 가벼운 물건부터 채운다. → 최적이 아니다.
        - 무게당 값이 높은 순서로 물건을 채운다. → 최적이 아니다.
    
    ⇒ 분할 정복, DP로 풀 수 있다..
    

- **Fractional Knapsack**: 물건을 쪼개 부분적으로 담는 것이 허용되는 문제
    1. **Greedy**
        
        물건의 일부를 잘라서 담을 수 있다.
        

### 예제: 활동 선택 문제

**문제 설명**

시작시간과 종료시간이 있는 n개의 활동들의 집합에서 서로 겹치지 않는(non-overlapping) 최대 개수의 활동 집합을 구하는 문제

양립 가능한 활동들의 크기가 최대가 되는 $S_{0, n+1}$의 부분집합을 선택하는 문제

**Greedy**

종료 시간이 빠른 순서대로 활동들을 정렬한다.

첫 번째 활동(A1)을 선택한다.

선택한 활동(A1)의 종료시간보다 빠른 시작 시간을 가지는 활동은 무시하고, 같거나 늦은 시작시간을 갖는 활동을 선택한다.

선택된 활동의 종료시간을 기준으로 뒤에 남은 활동들에 대해 앞의 과정을 반복한다.

### 예제: 스위치 조작

```python
T = int(input())
for tc in range(1, T+1):
    n = int(input())  # 스위치의 개수
    prev_switches = list(map(int, input().split()))  # 초기 스위치 상태
    next_switches = list(map(int, input().split()))  # 바꿀 스위치 상태

    # 최소 버튼을 누르는 횟수
    result = 0

    # 각 스위치를 순회
    for i in range(N):
        # 현재 초기 스위치와 목표 스위치의 상태가 같으면 skip
        if prev_switches[i] == next_switches[i]:
            continue
        # 상태가 다른 경우, 상태를 맞추기 위해서 스위치를 누른다.
        result += 1
        for j in range(i, n):
            prev_switches[j] = 1 - prev_switches[j]

    print(f'#{tc} {result}')
```
