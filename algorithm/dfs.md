## DFS (깊이 우선 탐색, Depth-First Search)

- 시작 노드에서 출발해 **갈 수 있는 경로를 한 방향으로 끝까지** 탐색한 뒤, 
더 이상 진행할 수 없으면 **직전에 방문했던 노드로 되돌아가** 다른 경로를 다시 탐색하는 방식
- ‘**되돌아가는**’(Backtracking) 과정은 **마지막에 추가된 노드**를 먼저 방문해야 하므로, 
자료구조 중 스택(Stack)의 **후입선출(LIFO)** 특성과 잘 맞습니다.
- 실제로 재귀 함수를 사용하는 DFS 구현에서는 컴퓨터 내부 호출 스택(Call Stack)을 활용해 동일한 동작을 수행합니다.

### DFS 구현 - 재귀 방식

재귀에서는 인접 리스트 방식이 더 선호된다.

- 인접 행렬은 모든 노드를 매번 확인해야 하므로, **`$O(V^2)$`**
- 인접 리스트는 실제 연결된 노드만 확인하므로,  **`$O(V+E)$`**

1. **인접 행렬 코드 예시**

```python
def dfs_recursive_matrix(current_node, adj_matrix, visited, path):
    """
    특정 노드를 시작으로 연결된 모든 노드를 재귀적으로 탐색하고,
    탐색 경로를 path 리스트에 추가합니다.

    Args:
        current_node (int): 현재 방문(탐색)하고 있는 노드
        adj_matrix (list): 그래프의 인접 행렬
        visited (list): 노드 방문 여부를 기록하는 리스트
        path (list): 탐색한 노드 순서를 기록할 리스트
    """
    # 1. 현재 노드 방문 처리, 경로에 추가
    visited[current_node] = True
    path.append(current_node)

    # 2. 현재 노드와 인접한 다른 노드들을 순회
    # V는 adj_matrix의 크기(len)로 알 수 있으므로, 전역변수 V에 의존하지 않음
    for next_node in range(1, len(adj_matrix)):
        # 1) 현재 노드와 인접해 있고, 2) 아직 방문하지 않았는지
        # 두 조건을 만족하면 탐색 가능 (재귀 호출 가능)
        if adj_matrix[current_node][next_node] == 1 and not visited[next_node]:
            dfs_recursive_matrix(next_node, adj_matrix, visited, path)
```

```python
result_path = []

# 1번 노드부터 DFS 시작!
dfs_recursive_matrix(1, adj_matrix, visited, result_path)
print(result_path)  # [1, 2, 4, 6, 5, 7, 3]
```

1. **인접 리스트 코드 예시**

```python
def dfs_recursive_list(current_node, adj_list, visited, path):
    """
    인접 리스트와 재귀를 이용한 DFS
    """
    # 1. 현재 정점을 방문 처리 & 경로 추가
    visited[current_node] = True
    path.append(current_node)

    # 2. 현재 정점에 인접한 정점을 직접 순회
    # 인접 행렬처럼 모든 정점을 확인할 필요 없이, 인접한 정점을 바로 탐색 가능
    for next_node in adj_list[current_node]:
        # 인접 정점이 아직 방문하지 않았다면 재귀 호출 진행
        if not visited[next_node]:
            dfs_recursive_list(next_node, adj_list, visited, path)
```

```python
result_path = []

# 1번 정점부터 탐색 시작!
dfs_recursive_list(1, adj_list, visited, result_path)
print(result_path)  # [1, 2, 4, 6, 5, 7, 3]
```

### DFS 구현 - 스택 방식

1. pop 시점에 방문 처리
    
    "스택에 넣을 때는 방문 여부를 신경 쓰지 않고, 스택에서 꺼낼 때 비로소 방문 여부를 확인한다. 
    이는 재귀 호출 시, 함수에 진입한 후에야 로직을 처리하는 것과 같다.”
    
2. push 시점에 방문 처리
    
    "그런데 스택에 이미 방문한 노드를 또 넣는 건 비효율적이지 않을까? 
    스택에 넣기 전에 미리 방문 체크를 하면, 스택의 공간을 아낄 수 있다.”
    

**1번과 2번 방식 비교**

| 구분 | 1번 방식 (Pop 후 방문 처리) | 2번 방식 (Push 전 방문 처리) |
| --- | --- | --- |
| **개념적 유사성** | **재귀 DFS**의 동작 원리와 매우 유사 | **BFS**의 구현 방식과 매우 유사 |
| **스택의 상태** | 방문 예정인 노드가 **중복 저장**될 수 있음 | 각 노드는 **최대 한 번만** 스택에 저장됨 |
| **장점** | "일단 갈 수 있는 곳을 모두 저장하고, 나중에 방문 여부를 확인한다"는 원리가 직관적 | 메모리 사용이 더 효율적이고 코드가 간결해질 수 있음 |
| **교육적 위치** | DFS의 기본 원리 이해 | DFS의 최적화 및 BFS와의 연결고리 |

**인접 행렬 코드 예시 - pop 시점에 방문 처리**

```python
def DFS_stack_pop_style(start):
    '''
    스택을 활용한 DFS (Pop 시점 방문 처리)
    '''
    visited = [False] * (V + 1)
    # 방문할 노드를 저장할 스택 (시작 노드 삽입)
    stack = [start]
    result_path = []

    # 탐색 시작 (스택이 빌 때 까지)
    while stack:
        # 1. 스택에서 노드를 pop
        current_node = stack.pop()

        # 2. [핵심] 스택에서 꺼낸 후, 방문 했었는지를 확인
        if not visited[current_node]:
            # 3. 방문 처리 및 경로 추가
            visited[current_node] = True
            result_path.append(current_node)

            # 4. 현재 노드와 인접한 노드들을 스택에 바로 삽입
            #    (방문 했었는지 확인하지 않고 일단 넣음. 꺼낼 때 확인함.)
            #    V부터 1까지 역순으로 확인 (작은 번호의 정점을 스택의 위쪽에 위치시키기 위함)
            #    만약, 큰 번호의 정점을 우선적으로 방문하고 싶다면 정방향으로 스택에 push
            for next_node in range(V, 0, -1):
                # 현재 노드와 인접한 노드를 스택에 push
                if adj_matrix[current_node][next_node] == 1:
                    stack.append(next_node)

    return result_path
```

```python
# --- DFS 실행 ---
result_path = DFS_stack_pop_style(1)
print(' '.join(map(str, result_path)))  # 1 2 4 6 5 7 3
```

**인접 행렬 코드 예시 - push 시점에 방문 처리**

```python
def DFS_stack_push_style(start):
    '''
    스택을 활용한 DFS (Push 시점 방문 처리)
    '''
    visited = [False] * (V + 1)  # 방문 기록 리스트
    stack = []  # 방문할 노드를 저장할 스택
    path = []  # 최종 탐색 경로를 저장할 리스트

    # 1. 시작 노드를 방문 처리하고 스택에 push
    visited[start] = True
    stack.append(start)

    while stack:
        # 2. 스택에서 노드를 pop. 이 노드는 방문이 '확정'된 노드
        current_node = stack.pop()
        path.append(current_node)

        # 3. 현재 노드의 인접 노드들을 확인
        # 작은 번호를 우선 방문하고 싶다면, 스택에는 큰 번호부터 push
        for next_node in range(V, 0, -1):
            # 현재 노드와 연결되어 있고, 아직 방문하지 않았다면
            if (
                adj_matrix[current_node][next_node] == 1
                and not visited[next_node]
            ):
                # 4. 즉시 방문 처리('예약')하고 스택에 push
                visited[next_node] = True
                stack.append(next_node)

    return path  # 최종 탐색 경로를 반환
```

```python
# --- DFS 실행 ---
result_path = DFS_stack_push_style(1)
print(' '.join(map(str, result_path)))  # 1 2 4 6 7 5 3
```

**인접 리스트 코드 예시 - pop 시점에 방문 처리**

```python
def DFS_stack_pop_style(start):
    """
    스택과 인접 리스트를 사용한 DFS (Pop 시점 방문 처리)
    """
    visited = [False] * (V + 1)
    stack = [start]
    result_path = []

    # 탐색 시작
    while stack:
        current_node = stack.pop()
        
        # 이 정점을 방문한 적이 있는지 확인
        if not visited[current_node]:
            # 방문한 적이 없다면 방문 처리 + 경로 추가
            visited[current_node] = True
            result_path.append(current_node)

            # 현재 정점과 인접한 정점들을 스택에 추가
            for next_node in adj_list[current_node]:
                # 이미 방문 처리된 노드라도 스택에 들어가도 상관 없음
                # 위에 if 문에서 걸러지므로 탐색 순서에는 영향을 주지 않음
                if not visited[next_node]:
                    stack.append(next_node)

    return result_path
```

```python
# 방문 순서를 결정하기 위해, 인접 리스트를 각 노드별로 내림차순 정렬
# 내림차순 정렬해두면, 스택에서 pop할 때 작은 번호를 먼저 방문하도록 유도 가능
# 문제 요구사항(‘노드를 작은 번호부터 방문해야 한다’)과 스택의 LIFO 구조를 맞추기 위함
for i in range(1, V + 1):
    adj_list[i].sort(reverse=True)

# --- DFS 실행 ---
result_path = DFS_stack_pop_style(1)
print(' '.join(map(str, result_path)))  # 1 2 4 6 5 7 3
```

**인접 리스트 코드 예시 - push 시점에 방문 처리**

```python
def DFS_stack_push_style(start_node):
    """
    스택과 인접 리스트를 사용한 DFS (Push 시점 방문 처리)
    """
    visited = [False] * (V + 1)  # 방문 여부 리스트
    stack = []  # 방문할 노드를 저장할 스택
    path = []  # 최종 탐색 경로를 저장할 리스트

    # 1. 시작 노드를 먼저 방문 처리하고 스택에 push
    visited[start_node] = True
    stack.append(start_node)

    while stack:
        # 2. 스택에서 노드를 pop하여 경로에 추가
        current_node = stack.pop()
        path.append(current_node)

        # 3. 현재 노드의 인접 노드들을 확인
        # adj_list가 내림차순 정렬되어 있으므로, 큰 번호부터 확인
        for next_node in adj_list[current_node]:
            # 4. 아직 방문하지 않은 노드를 발견하면,
            if not visited[next_node]:
                # 5. 즉시 방문 처리('예약')하고 스택에 push
                visited[next_node] = True
                stack.append(next_node)

    return path
```

```python
# --- DFS 실행 ---
result_path = DFS_stack_push_style(1)
print(' '.join(map(str, result_path)))  # 1 2 4 6 7 5 3
```

### 재귀와 스택 방식 비교

| 구분 | 재귀 (Recursion) | 스택 (Iteration) |
| --- | --- | --- |
| **구현 방식** | 함수가 자기 자신을 호출하는 방식 | `while` 반복문과 `list` (스택) 자료구조 사용 |
| **핵심 원리** | **시스템 콜 스택**을 암시적으로 사용 | **자료구조 스택**을 명시적으로 사용 |
| **코드 가독성** | DFS의 '깊이 파고드는' 원리가 직관적으로 보여 간결함 | 동작 방식이 눈에 보이지만, 코드가 상대적으로 길어질 수 있음 |
| **메모리** | 호출 스택이 시스템 메모리를 사용 | 스택 리스트가 힙 메모리를 사용 |
| **오류 가능성** | 탐색 깊이가 매우 깊어지면 **스택 오버플로우** 발생 가능 | 스택 오버플로우 위험은 없으나, 메모리가 부족할 수는 있음 |
- **재귀 방식**: 길을 따라가다가 갈림길이 나오면, **기억력에 의존해** 한쪽 길로 끝까지 갑니다. 막다른 길에 다다르면, **기억을 되짚어** 이전 갈림길로 돌아와 다른 길을 탐색합니다.
    - 대부분의 경우, 코드가 **훨씬 간결하고 직관적**이므로 추천됩니다. DFS의 원리를 가장 잘 표현하는 방식입니다.
- **스택 방식**: 기억력 대신 **수첩(스택)**을 사용합니다. 갈림길에서 갈 수 있는 모든 길을 수첩에 적어두고, 가장 마지막에 적은 길부터 하나씩 지워가며 탐색합니다.
    - 탐색해야 할 그래프의 깊이가 매우 깊어 **스택 오버플로우**가 우려될 때, 또는 스택에 저장되는 데이터를 직접 제어해야 하는 특별한 경우에 사용합니다.