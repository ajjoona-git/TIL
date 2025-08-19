# 수업 필기

## Stack 기반 문제 해결 기법

### 재귀호출

함수가 자신과 같은 작업을 반복해야 할 때, 자신을 다시 호출하는 구조

**예시**

- factorial `f(n) = n * f(n-1)`, `f(1) = 1`
- 피보나치 수열 `f(n) = f(n-1) + f(n-2)`, `f(0) = 0, f(1) = 1`

**기본형**

```python
def f(i, N):
"""
재귀 함수의 기본형
- params
	i: 현재 단계
	N: 목표 단계
"""
		# 재귀호출 중단 조건
		if i == N:
				return
		# 재귀 호출
		else:
				f(i + 1, N)
```

재귀함수의 문제점

- 중복 호출이 너무 많다. → 메모이제이션

### Memoisation

이전에 계산한 값을 메모리에 저장해서 매번 다시 계산하지 않도록 하여 전체적인 실행속도를 빠르게 하는 기술

- 동적 계획법(DP)의 핵심

### 동적 계획법 DP (Dynamic Programming)

입력 크기가 작은 부분 문제들을 먼저 해결한 뒤, 그 결과를 바탕으로 더 큰 부분 문제를 순차적으로 해결해 나가며 최종적으로 전체 문제의 해답을 도출하는 알고리즘

- 최적화 문제를 해결하는 알고리즘
- 동일한 하위 문제가 여러 번 반복되어 나타날 경우
- 문제의 최적 해가 그 하위 문제의 최적 해로부터 쉽게 구성될 수 있는 최적 부분 구조인 경우

### 깊이 우선 탐색 DFS (Depth First Search)

한 방향으로 가능한 한 깊게 탐색한 후, 더 이상 갈 곳이 없으면 되돌아와 다른 방향을 탐색하는 방법

- 비선형 구조(그래프)
- 후입선출(LIFO) 구조의 스택 사용
1. 시작 정점의 한 방향으로 갈 수 있는 경로가 있는 곳까지 깊이 탐색
2. 더 이상 갈 곳이 없다면, 가장 마지막에 만났던 갈림길 간선이 있는 정점으로 되돌아와서 갈림길의 다른 방향으로 깊이 탐색
3. 탐색을 계속 반복하여 결국 모든 정점을 방문하게 된다.


### 백트래킹 (Backtraking)

후보 해를 구성해 나가다가 더 이상 해가 될 수 없다고 판단되면 되돌아가서 다른 경로를 시도하는 완전 탐색 기법

- 유망하지 않은 경로는 더 이상 탐색하지 않고 되돌아가며 해결책을 찾는 방식
- 가지치기(prunning): 유망하지 않은 노드가 포함되는 경로는 더 이상 고려하지 않는다.
- 최적화(optimization) 문제와 결정(decision) 문제에 적용
    - N-Queens
        - NxN 체스판에 가로, 세로, 대각선 방향으로 겹치지 않도록 N개의 queen을 배치
    - 미로 찾기
    - 순열/조합 생성
    - 부분집합 탐색
    - 스도쿠 풀이

1. **정답 후보를 하나씩** 만드는 방식으로 문제를 푼다.
2. 만약, **현재 후보가 조건에 어긋나면**(유망하지 않으면) **더 이상 진행하지 않고** 되돌아가며(백트랙).
3. 조건을 만족한다면 **계속해서 재귀**를 진행, 필요 시 완성된 해를 기록


### Backtracking과 DFS의 차이

|  | 백트래킹 (Backtracking) | 깊이 우선 탐색 (DFS) |
| :---: | --- | --- |
| 목적 | 해답을 찾는 과정에서 **최적화**를 목표로 함 | 그래프/트리의 모든 노드나 경로를 **빠짐없이 탐색**하는 것이 주 목적 |
| 가지치기 | **가지치기(Pruning)**를 수행하여 불필요한 탐색을 중단함 | 일반적으로 가지치기 없이 **모든 경로를 탐색**함 |
| 탐색 범위 | 해답이 없는 경로를 조기에 차단해 탐색 범위를 크게 줄임 | 특정 조건이 없는 한 모든 경로를 끝까지 탐색함 |
| 주요 사용처 | N-Queen, 스도쿠, 조합 문제 등 **경우의 수가 많은 문제** | 그래프/트리의 완전 탐색, 사이클 감지, 연결 요소 찾기 등 |


### 부분집합 powerset

```python
def backtrack(a, k, n):
	""" 
	powerset을 구하는 backtracking 알고리즘 구현 
	- Args
		a: 주어진 배열
		k: 결정할 원소
		n: 원소 개수
	"""
	c = [0] * MAXCANDIDATES
	
	if k == n:
		process_solution(a, k)  # 답이면 원하는 작업을 한다
	else:
		ncadidates = construct_cadidates(a, k, n, c)
		for i in range(ncandidates):
			a[k] = c[i]
			backtrack(a, k + 1, n)
			

def construct_candidates(a, k, n, c):
	c[0] = True
	c[1] = False
	return 2
	
	
def process_solution(a, k):
	for i in range(k):
		if a[i]:
			print(num[i], end=' ')
	print()
	
	
MAXCANDIDATES = 2
NMAX = 4
a = [0] * MAX
num = [1, 2, 3, 4]
backtrack(a, 0, 3)
```

### 순열

```python
def backtrack(a, k, n):
	c = [0] * MAXCANDIDATES
	
	if k == n:
		for i in range(0, k):
			print(a[i], end=' ')
		print()
	else:
		ncandidates = construct_candidates(a, k, n, c)
		for i in range(ncandidates):
			a[k] = c[i]
			backtrack(a, k + 1, n)

			
def construct_candidates(a, k, n, c):
	in_perm = [False] * (NMAX + 1)
	
	for i in range(k):
		in_perm[a[i]] = True
		
	ncandidates = 0
	for i in range(1, NMAX + 1):
		if in_perm[i] == False:
			c[ncandidates] = i
			ncandidates += 1
			
	return ncandidates
	
	
MAXCANDIDATES = 3
NMAX = 3
a = [0] * NMAX
backtrack(a, 0, 3)
```