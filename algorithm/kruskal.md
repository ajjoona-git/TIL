## Kruskal 알고리즘

**가중치가 가장 낮은 간선부터 순서대로** 선택하여 MST를 만드는 알고리즘

### 특징

- 간선(Edge) 중심
- 사이클 여부를 확인 → Union-Find 자료구조 활용
- 시간 복잡도: `$O(E log E)$`

### 코드 구현

1. 모든 가능한 간선을 **가중치가 낮은 순(오름차순)**으로 정렬
2. 가장 싼 간선부터 순서대로 확인하며, 이 간선을 추가했을 때 **사이클(순환 경로)이 생기지 않으면** MST에 포함시킴 → **서로소 집합 (`Union-Find` )**
3. 사이클이 생긴다면 그 간선은 무시하고 다음으로 넘어감
4. `정점의 수 - 1`개의 간선이 선택될 때까지 반복

```python
import sys
sys.stdin = open('input.txt')

def find_set(parent, x):
    """
    x의 루트(대표) 노드를 찾는 함수 (경로 압축 적용).
    """
    if parent[x] != x:
        parent[x] = find_set(parent, parent[x])
    return parent[x]

def union(parent, x, y):
    """
    두 원소 x, y를 같은 집합으로 합치는 함수.
    """
    root_x = find_set(parent, x)
    root_y = find_set(parent, y)
    if root_x < root_y:
        parent[root_y] = root_x
    else:
        parent[root_x] = root_y

def kruskal_mst(num_vertices, edges):
    """
    Kruskal 알고리즘으로 MST를 찾는 함수.
    """
    # 1. 간선들을 가중치(cost) 기준으로 오름차순 정렬
    edges.sort()

    # 2. Union-Find를 위한 parent 리스트 초기화 (각자 자신이 대표)
    parent = [i for i in range(num_vertices + 1)]

    mst_cost = 0  # MST의 총 가중치
    edges_count = 0  # MST에 포함된 간선의 수

    # 3. 가장 가중치가 낮은 간선부터 순회
    for cost, s, e in edges:
        # 4. 두 정점의 대표가 다른지 확인 (사이클 생성 여부 체크)
        if find_set(parent, s) != find_set(parent, e):
            # 5. 사이클이 생기지 않으면, 간선을 MST에 포함시키고
            #    두 정점을 같은 집합으로 합침 (union)
            union(parent, s, e)
            mst_cost += cost
            edges_count += 1

            # MST는 V-1개의 간선으로 이루어지므로, 다 찾았으면 종료
            if edges_count == num_vertices - 1:
                break

    return mst_cost

# --- 실행 로직 ---
V, E = map(int, input().split())
edges_info = []
for _ in range(E):
    # 크루스칼은 간선 리스트를 사용하므로, (가중치, 시작, 끝) 형태로 저장
    s, e, cost = map(int, input().split())
    edges_info.append((cost, s, e))

result_cost = kruskal_mst(V, edges_info)
print(f"Kruskal MST 총 비용: {result_cost}")

```

### 시간 복잡도
간선들을 정렬하고, 사이클 검사하면서 간선들을 선택한다.

- O(ElogE) + E * O(1) → O(ElogE)
    - ElogE : 정렬
    - E : 간선의 수만큼 union-find