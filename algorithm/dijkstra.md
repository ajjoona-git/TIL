## Dijkstra 알고리즘

한 정점에서 다른 모든 정점으로의 최단 경로를 구하는 알고리즘

### 특징

- **음의 가중치가 없는 그래프**에서 단일 출발 최단 경로를 구할 때
    - 음수 가중치가 있다면 벨만-포드 알고리즘을 사용한다.
- 탐욕 알고리즘 (Greedy)
- Prim 알고리즘과 유사
- 우선순위 큐(힙)
- 시간 복잡도: `$O(ElogV)$` (우선순위 큐 사용 시)

### 코드 구현

1. 출발점에서 각 정점까지의 거리를 기록할 `distance` 배열을 만듭니다. (출발점은 0, 나머지는 무한대(INF)로 초기화)
2. **현재까지 알려진 가장 가까운(최단 거리가 가장 짧은) 노드**를 하나 선택합니다. → **우선순위 큐 (`heapq`)**
3. 선택한 노드를 거쳐 다른 노드로 가는 경로가, 기존에 알려진 경로보다 더 짧다면 `distance` 배열의 값을 **갱신**합니다.
4. 모든 노드를 방문할 때까지 2~3번 과정을 반복합니다.

```
6 8
6 1 2
6 2 4
1 2 1
1 3 7
2 4 3
3 4 2
3 5 1
4 5 5
```

```python
import heapq

def dijkstra(start_node, num_vertices, adj_list):
    """
    Dijkstra 알고리즘 (우선순위 큐 활용)
    """
    # 1. 초기화 작업
    # 시작 정점으로부터 모든 정점까지의 거리를 기록할 리스트
    INF = float('inf')
    distance = [INF] * (num_vertices + 1)

    # 우선순위 큐(최소 힙) 생성
    priority_queue = []

    # 2. 시작 노드 처리
    # 시작 노드까지의 거리는 0으로 설정
    # 우선순위 큐에 삽입 (가중치, 정점 번호)
    distance[start_node] = 0
    heapq.heappush(priority_queue, (0, start_node))

    # 3. 메인 과정 (큐가 빌 때까지 반복)
    while priority_queue:
        # 4. 현재까지 가장 거리가 짧은 노드를 힙에서 꺼낸다.
        current_dist, current_node = heapq.heappop(priority_queue)

        # 이미 처리된 노드라면(더 짧은 경로를 이미 발견했다면) 무시
        # 내가 과거에 현재 노드에 더 짧게 방문한 적이 있다면 더 이상의 탐색은 무의미하기 때문
        if distance[current_node] < current_dist:
            continue

        # 5. 현재 노드와 인접한 노드들을 확인한다.
        for adj_node, next_dist in adj_list[current_node]:
            # 새로운 경로
            new_dist = current_dist + next_dist
            
            # 6. 새로운 경로가 기존 경로보다 더 짧으면 갱신한다.
            if new_dist < distance[adj_node]:
                distance[adj_node] = new_dist
                # 갱신된 정보를 우선순위 큐에 추가
                heapq.heappush(priority_queue, (new_dist, adj_node))

    return distance
```

```python
# --- 실행 예시 ---
V, E = map(int, input().split())
adj_list = [[] for _ in range(V + 1)]
for _ in range(E):
    u, v, w = map(int, input().split())
    adj_list[u].append((v, w))
    
# 다익스트라 알고리즘 실행
start = 1
shortest_distances = dijkstra(start, V, adj_list)

# 1번 노드에서 각 노드까지의 최단 거리
print(shortest_distances)  # [inf, 0, 1, 7, 4, 8, inf]
```