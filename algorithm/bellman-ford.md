## Bellman-Ford 알고리즘

음수 가중치가 있어도 사용 가능하며, 시작점에서 각 정점까지의 최단 거리를 모든 간선을 반복적으로 검사하여 갱신하는 알고리즘

### 특징

- 단일 출발 최단 경로
- **음수 사이클(Negative Cycle)** 판별
    - 총 `V-1`번의 전체 간선 확인을 마친 후, **한 번 더** 전체 간선을 확인했을 때 또다시 거리 갱신이 일어난다면, 이는 음수 사이클이 존재한다는 뜻.
- DP(동적 프로그래밍)과 유사

### 코드 구현

“모든 간선(Edge)을 한 번씩 확인하는 과정을, 전체 정점(Vertex) 개수만큼 반복하면서 최단 거리를 점진적으로 갱신한다.”

1. 출발점에서 각 정점까지의 거리를 기록할 `distance` 배열을 만듭니다. (출발점은 0, 나머지는 무한대(INF)로 초기화)
2. `정점의 개수 - 1` 번 만큼 반복을 진행 합니다.
    1. **모든 간선을 순회하며**(skip하는 간선 없음) 거리를 갱신합니다.
    2. 기존 값보다 더 작은 값으로 업데이트 된다면 거리를 갱신합니다.
3. 음의 사이클을 확인하기 위해 한 번 더 거리를 갱신하여 업데이트 되는지 확인합니다.
    1. 업데이트 된다면 음의 사이클이 존재하는 것입니다.
4. 최종적으로 구한 경로들이 출발점에서의 최단 경로 입니다.

```python
def bellman_ford(num_vertices, edges, start):
    """
    Bellman-Ford 알고리즘
    """
    INF = float('inf')
    distance = [INF] * (num_vertices + 1)
    distance[start] = 0

    # 1. (정점 개수 - 1)번 만큼, 모든 간선에 대해 완화(Relaxation) 작업 반복
    for _ in range(num_vertices - 1):
        for u, v, w in edges:  # u:시작, v:도착, w:가중치
            # u까지의 경로가 존재하고, u를 거쳐 v로 가는 것이 더 짧으면 갱신
            if distance[u] != INF and distance[v] > distance[u] + w:
                distance[v] = distance[u] + w

    # 2. 음수 사이클 확인: V번째 반복에서도 갱신이 일어나는지 확인
    for u, v, w in edges:
        if distance[u] != INF and distance[v] > distance[u] + w:
            # V번째에도 갱신이 발생하면 음수 사이클 존재
            return None

    return distance
```

```python
# --- 실행 예시 ---

# 예시 데이터 직접 입력 (음수 가중치 O, 음수 사이클 X)
V, E, start = 5, 6, 1
# (시작, 도착, 가중치) 형태의 간선 리스트
edges_info = [
    (1, 2, 6),
    (1, 3, 7),
    (2, 4, 5),
    (3, 2, -3),  # 음수 가중치
    (3, 4, 1),
    (4, 5, -2),  # 음수 가중치
]

# 벨만-포드 알고리즘 실행
shortest_distances = bellman_ford(V, edges_info, start)

# --- 결과 출력 ---
# 음수 사이클이 있는 경우와 없는 경우를 모두 처리
if shortest_distances is None:
    print("그래프에 음수 사이클이 존재합니다.")
else:
    print(f"--- 1번 노드로부터의 최단 거리 ---")
    for i in range(1, V + 1):
        if shortest_distances[i] == float('inf'):
            print(f"노드 {i}: 도달 불가")
        else:
            print(f"노드 {i}: {shortest_distances[i]}")
```

```
--- 1번 노드로부터의 최단 거리 ---
노드 1: 0
노드 2: 4
노드 3: 7
노드 4: 8
노드 5: 6
```