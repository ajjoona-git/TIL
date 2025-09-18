## Floyd-Warshall 알고리즘

그래프의 **‘모든 정점 쌍’** 사이의 최단 경로를 한 번에 구하는 알고리즘

### 특징

- 모든 쌍 최단 경로
- 동적 프로그래밍(DP)
- $D_(i, j) = min ( D_(i, j), D_(i, k) + D_(k, j) )$

### 코드 구현

"모든 정점 k에 대하여, i에서 j로 바로 가는 기존의 경로와, k를 거쳐 가는 경로(i → k → j) 중 더 짧은 것을 선택해 거리를 갱신한다."

1. 각 정점에서 각 정점까지의 거리를 기록할 `distance` 2차원 배열을 만듭니다. 
    1. 자기 자신으로 가는 경로는 0, 나머지는 무한대(INF)로 초기화합니다.
    2. 간선 정보를 입력합니다.
2. 3중 for문으로 각 노드가 거쳐가는 노드 `k`와 출발 노드 `i`, 도착 노드 `j`일 때를 순회합니다.
    1. i에서 j로 가는 기존 경로보다, k를 거쳐가는 경로가 더 짧으면 갱신합니다.
3. 최종적으로 구한 경로들이 출발점에서의 최단 경로 입니다.

```python
def floyd_warshall(num_vertices, graph_matrix):
    """
    Floyd-Warshall 알고리즘
    """
    # 2차원 거리 리스트를 초기 그래프 정보로 복사
    distance = [row[:] for row in graph_matrix]

    # k: 거쳐가는 노드
    for k in range(1, num_vertices + 1):
        # i: 출발 노드
        for i in range(1, num_vertices + 1):
            # j: 도착 노드
            for j in range(1, num_vertices + 1):
                # i에서 j로 가는 기존 경로보다, k를 거쳐가는 경로가 더 짧으면 갱신
                if distance[i][k] + distance[k][j] < distance[i][j]:
                    distance[i][j] = distance[i][k] + distance[k][j]

    return distance
```

```python
# --- 실행 예시 ---

# 예시 데이터 직접 입력
V = 4
INF = float('inf')

# 1. 그래프 정보를 인접 행렬로 초기화
#    graph[i][j]는 i에서 j로 가는 직접 간선의 가중치를 의미
#    (V+1) x (V+1) 크기로 생성하여 1번 노드부터 사용
graph_matrix = [[INF] * (V + 1) for _ in range(V + 1)]

# 2. 자기 자신으로 가는 경로는 비용이 0
for i in range(1, V + 1):
    graph_matrix[i][i] = 0

# 3. 간선 정보 입력
#    graph_matrix[출발][도착] = 가중치
edges_info = [
    (1, 2, 4),
    (1, 3, 2),
    (2, 3, 3),
    (2, 4, 2),
    (3, 2, 1),
    (3, 4, 4),
    (4, 1, 1),
]

for start_node, end_node, cost in edges_info:
    graph_matrix[start_node][end_node] = cost

# 플로이드-워셜 알고리즘 실행
shortest_distances = floyd_warshall(V, graph_matrix)

# --- 결과 출력 ---
# shortest_distances[i][j]는 i번 노드에서 j번 노드까지의 최단 거리를 의미
print("--- 모든 쌍 최단 경로 결과 ---")
for i in range(1, V + 1):
    for j in range(1, V + 1):
        if shortest_distances[i][j] == INF:
            print("INF", end="\t")
        else:
            print(shortest_distances[i][j], end="\t")
    print()
```

```
--- 모든 쌍 최단 경로 결과 ---
0       3       2       5
3       0       3       2
4       1       0       3
1       4       3       0
```