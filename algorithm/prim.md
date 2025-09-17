## Prim 알고리즘

**임의의 시작 정점**에서 시작해, **가장 가중치가 낮은 다음 정점**을 선택해 나가며 MST를 점차 확장하는 방식

### 특징

- 정점(Vertex) 중심
- Prim’s Algorithm = Pick a node
- 탐욕 알고리즘 (Greedy)
- 서로소인 2개의 집합 정보를 유지
    - tree vertices: MST를 만들기 위해 선택된 정점들
    - non-tree vertices: 선택되지 않은 정점들
- 시간 복잡도: `$O(E log V)$`

### 코드 구현

1. **임의의 시작 정점**을 선택 → MST 집합에 넣음
2. 현재 MST 집합에 속한 모든 정점들로부터, 아직 방문하지 않은 외부 정점으로 연결되는 모든 간선 중 **가장 가중치가 낮은 간선**을 찾음 → **우선순위 큐 (`heapq`)**
3. 찾은 간선과 연결된 새로운 정점을 MST 집합에 추가
4. 모든 정점이 MST 집합에 포함될 때까지 2~3번 과정을 반복

```
7 11
0 1 32
0 2 31
0 5 60
0 6 51
1 2 21
2 4 46
2 6 25
3 4 34
3 5 18
4 5 40
4 6 51
```

**인접 행렬 코드 구현 예시**

```python
from heapq import heappush, heappop
import sys
sys.stdin = open("input.txt", "r")

def prim(start_node):
    """특정 정점을 기준으로 시작해서 갈 수 있는 노드들 중 가중치가 가장 작은 노드를 선택한다.
        -> 작은 노드를 먼저 꺼내기 위해 우선순위큐(heapq)를 활용한다."""
    # 우선순위 큐: (가중치, 노드) 형태
    pq = [(0, start_node)]
    # MST: 선택한 노드를 표시한다. (visited와 동일한 역할)
    MST = [0] * V
    min_weight = 0  # 최소 비용

    while pq:
        # 가중치가 가장 작은 노드를 꺼낸다.
        weight, node = heappop(pq)  

        # 이미 방문한 노드라면 pass
        if MST[node]:
            continue

        # node로 가는 최소 비용이 선택되었다면 누적합 갱신
        MST[node] = 1  
        min_weight += weight

        # 인접한 노드를 순회한다.
        for next_node in range(V):
            # 연결되어 있지 않으면 pass
            if graph[node][next_node] == 0:
                continue

            # 이미 방문한 노드라면 pass
            if MST[next_node]:
                continue
            
            # 원래 BFS에서는 push(append) 전 방문 처리 
            # -> MST에서는 최소 비용을 선택해야하기 때문에 heappop한 후에 방문 처리
            heappush(pq, (graph[node][next_node], next_node))

    return min_weight

V, E = map(int, input().split())
graph = [[0] * V for _ in range(V)]  # 인접 행렬

for _ in range(E):
    start, end, weight = map(int, input().split())
    graph[start][end] = weight
    graph[end][start] = weight

# 출발 정점을 바꾸어도 최소 비용은 똑같다.
# 단, 그래프가 다르게 나올 수는 있다.
result = prim(0) 

print(f"Prim MST 총 비용: {result}")  # Prim MST 총 비용: 175
```

**인접 리스트 코드 구현 예시**

```python
import sys
import heapq

sys.stdin = open('input.txt')

def prim_mst(num_vertices, adj_list, start=1):
    """
    Prim 알고리즘으로 MST를 구하는 함수.
    """
    visited = [False] * (num_vertices + 1)  # 정점의 방문(MST 포함) 여부
    priority_queue = []  # (가중치, 시작점, 도착점)을 담을 최소 힙

    mst_cost = 0  # MST의 총 가중치
    edges_count = 0  # MST에 포함된 간선의 수

    # 1. 시작 정점과 연결된 모든 간선을 우선순위 큐에 넣음
    for cost, next_node in adj_list[start]:
        heapq.heappush(priority_queue, (cost, start, next_node))
    visited[start] = True

    # 2. 큐가 비거나, MST가 완성될 때까지 반복
    while priority_queue and edges_count < num_vertices - 1:
        # 3. 현재 MST 집합과 연결된 간선 중, 가장 가중치가 낮은 간선을 꺼냄
        cost, _, end = heapq.heappop(priority_queue)

        # 4. 도착 정점이 이미 MST에 포함된 경우, 이 간선은 사이클을 유발하므로 무시
        if visited[end]:
            continue

        # 5. 새로운 정점을 MST에 포함
        visited[end] = True
        mst_cost += cost
        edges_count += 1

        # 6. 새로 추가된 정점과 연결된, 아직 방문 안 한 정점으로 가는 간선들을 큐에 추가
        for next_cost, next_node in adj_list[end]:
            if not visited[next_node]:
                heapq.heappush(priority_queue, (next_cost, end, next_node))

    return mst_cost

# --- 실행 로직 ---
V, E = map(int, input().split())
# 프림은 인접 리스트를 사용
adj_list = [[] for _ in range(V + 1)]
for _ in range(E):
    s, e, cost = map(int, input().split())
    # (가중치, 연결된 정점) 형태로 저장
    adj_list[s].append((cost, e))
    adj_list[e].append((cost, s))

result_cost = prim_mst(V, adj_list, start=1)
print(f"Prim MST 총 비용: {result_cost}")  # Prim MST 총 비용: 175

```

### 시간 복잡도
힙에 간선 후보를 넣고, 최소값을 계속 뽑는다.
- O(VlogV + ElogV) → O(ElogV)
    - VlogV : 정점의 수만큼 우선순위 큐에 삽입/삭제한다.
    - ElogV : 간선의 수만큼 힙에 추가한다.
        - 우리가 배운 코드는 정점이 중복되게 삽입된다: O(ElogE)
          -> decrease key까지만 들어가 있다.
        - 최적화 기법을 써야한다.
    - 피보나치 힙을 쓰면 훨씬 빨라진다.
- 밀집 그래프 간선이 많을수록 유리하다.