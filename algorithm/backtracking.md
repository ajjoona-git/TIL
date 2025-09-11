## 백트래킹 (Backtracking)

완전 탐색 기법 중 하나로, 깊이 우선 탐색(DFS)과 비슷한 방법으로 탐색하다가 유망하지 않다고 판단되면 그 즉시 다른 선택지로 이동한다.

- 순열, 조합, 부분집합처럼 **모든 가능한 경우**를 찾아야 하지만, 중간에 명확한 **'포기 조건'**이 있는 문제

### 백트래킹 vs DFS

- 가지치기 (Pruning)
    - **일반적인 DFS:** 막다른 길에 도달해야만 되돌아온다.
    - **백트래킹:** 탐색하는 도중, 현재 경로가 **"더 이상 정답이 될 가능성이 없다"**고 판단되면, 즉시 그 경로를 포기하고 이전 갈림길로 되돌아간다.

### **백트래킹의 3요소**

1. **상태 공간 트리 (State Space Tree):**
    - 문제가 가질 수 있는 모든 **'해 후보'**들을 트리 형태로 표현한 것
    - 이 트리의 모든 경로를 탐색하는 것을 목표로 한다.
2. **유망성 조사:**
    - 현재 노드(경로)가 해가 될 가능성이 있는지 검사하는 **'가지치기'** 조건
    - 이 조사를 통과하지 못하면 더 이상 깊이 탐색하지 않는다.
3. **기저 조건 (Base Case):**
    - 탐색이 성공적으로 끝나는 조건
    - 하나의 완전한 해를 찾았을 때 재귀를 멈추고, 찾은 해를 기록한다.

### **백트래킹의 구현**

`'선택 → 탐색 → 선택 취소'`의 과정을 재귀 호출하면서 반복하는 형태

```python
def backtrack(현재 상태):
    # 1. 기저 조건: 해를 찾았는가?
    if (해가 완성된 상태인가?):
        # 해를 기록하고 종료
        return

    # 2. 다음 선택지 탐색
    for (다음에 선택할 수 있는 모든 경우 in 선택지들):
        # 3. 유망성 조사 (가지치기)
        if (다음 선택이 유망한가?):
            # 3-1. 선택 (Choose)
            # 상태를 변경 (다음 선택을 기록)

            # 3-2. 탐색 (Explore)
            backtrack(변경된 상태)

            # 3-3. 선택 취소 (Un-choose)
            # 원래 상태로 되돌림 (다음 반복을 위해)

```

### 예제: N-Queens 문제

```python
def check(row, col):
    # 1. 같은 열에 놓은 적이 있는가?
    for i in range(row):
        if visited[i][col]:
            return False

    # 2. 좌상단 대각선에 놓은 적이 있는가? (\)
    i, j = row - 1, col - 1
    while i >= 0 and j >= 0:
        if visited[i][j]:
            return False

        i -= 1
        j -= 1

    # [참고] for문으로 하고싶다 !
    # for i, j in zip(range(row-1, -1, -1), range(col-1, -1, -1)):
    #     if visited[i][j]:
    #         return False

    # 3. 우상단 대각선에 놓은 적이 있는가? (/)
    i, j = row - 1, col + 1
    while i >= 0 and j < N:
        if visited[i][j]:
            return False

        i -= 1
        j += 1

    return True

# 종료 조건: N개의 행을 모두 고려하면 종료
# 가지의 수: N개의 열
def recur(row):
    global answer

    if row == N:
        answer += 1
        return

    for col in range(N):
        # 가지치기 : 같은 열을 못 고르도록
        #  --> 유망하지 않은 케이스를 모두 삭제 (세로, 대각선)
        if check(row, col) is False:
            continue

        # col을 선택했다
        visited[row][col] = 1
        recur(row + 1)
        visited[row][col] = 0

N = 4
answer = 0  # 가능한 정답 수
visited = [[0] * N for _ in range(N)]
recur(0)
print(f'N = {N} / answer = {answer}')  # N = 4 / answer = 2
```