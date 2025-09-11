## 힙 (heap)

**완전 이진 트리**에 있는 노드 중에서 **최대값 혹은 최소값**을 찾기 위해서 만든 자료구조

- **완전 이진 트리** 형태를 유지
- 삽입·삭제 시 **부모-자식 교환**(Swap)을 통해 **힙 성질**을 유지

### 힙의 종류

![힙의 예](../images/heap_1.png)

1. **최대 힙 (max heap)**
- 키 값이 가장 큰 노드를 찾기 위한 **완전 이진 트리**
- 부모 노드의 키 값 > 자식 노드의 키 값
- 키 값이 가장 큰 노드가 루트 노드

2. **최소 힙 (min heap)**
- 키 값이 가장 작은 노드를 찾기 위한 **완전 이진 트리**
- 부모 노드의 키 값 < 자식 노드의 키 값
- 키 값이 가장 작은 노드가 루트 노드

### 힙의 특성

1. **완전 이진 트리**
    - 노드가 **왼쪽부터** 차곡차곡 채워짐
    - 배열 인덱스로 부모/자식 관계를 빠르게 계산 가능
2. **부모 ↔ 자식 관계** (1-based index 가정)
    - 부모: `i//2`
    - 왼쪽 자식: `2*i`
    - 오른쪽 자식: `2*i + 1`
3. **탐색 시간**
    - **힙의 높이**는 약 **`$O(log n)$`** (완전 이진 트리이므로)
    - 최댓값(또는 최솟값)은 **루트 노드**에서 `$O(1)$`에 접근 가능
    - 삽입·삭제 모두 `$O(log n)$`
    - 정렬(힙 정렬) 시 전체 `$O(n log n)$`


### 삽입

1. **새 노드를** 힙의 **마지막 위치**에 삽입 (완전 이진 트리 구조 유지)
2. **부모 노드**와 비교해 힙 성질
(부모 > 자식 for Max-Heap / 부모 < 자식 for Min-Heap)이 **깨지면** **위로 올림(Swim)**
3. 루트 노드나 더 이상 교환이 필요 없을 때까지 반복
    
    ```python
    def heap_push(heap, value):
        # 1. 새로운 값은 힙 리스트의 끝(마지막 인덱스)에 추가
        heap.append(value)
        idx = len(heap) - 1
    
        # 2. 부모와 비교해 힙 성질 유지
        while idx > 1:  # 1-based index 가정, idx=1은 루트
            parent = idx // 2
            if heap[parent] < heap[idx]:
                # 부모보다 자식이 큰 경우(최대 힙)
                heap[parent], heap[idx] = heap[idx], heap[parent]
                idx = parent
            else:
                break
    
    ```
    

### 삭제

- 일반적으로 **루트 노드**(최대 힙: 최댓값 / 최소 힙: 최솟값)만 삭제 가능
- 과정:
    1. **루트 노드**를 삭제 → 반환할 값
    2. 힙의 **마지막 노드**를 **루트로 이동**
    3. **자식 노드들과** 비교해 힙 성질(부모가 더 큼/작음)이 깨지면, **아래로 내림(Sink)**
    4. 더 이상 교환할 필요가 없을 때까지 반복
    
    ```python
    def heap_pop(heap):
        # 1. 루트 노드(최대 힙이라면 최대값) 반환할 변수에 저장
        top = heap[1]
    
        # 2. 힙의 마지막 노드를 루트 자리에 가져옴
        heap[1] = heap[-1]
        heap.pop()  # 마지막 원소 제거
        idx = 1
        size = len(heap) - 1
    
        # 3. 힙 성질 복원: 자식과 비교, 교환하며 내려감
        while True:
            left = idx * 2
            right = idx * 2 + 1
            largest = idx
    
            if left <= size and heap[largest] < heap[left]:
                largest = left
            if right <= size and heap[largest] < heap[right]:
                largest = right
    
            if largest != idx:
                heap[idx], heap[largest] = heap[largest], heap[idx]
                idx = largest
            else:
                break
    
        return top
    
    ```
    

### 힙의 활용

1. 우선순위 큐(Priority Queue)의 구현
    - **우선순위 큐**: 들어오는 순서가 아니라, **우선순위가 높은 것**(또는 낮은 것)을 먼저 꺼내는 큐
    - **힙**으로 구현 시, 삽입·삭제 모두 `$O(log n)$`에 처리 가능
    - 최대 힙: **우선순위가 가장 높은(값이 가장 큰) 원소**를 루트로 → 최우선 제거
    - 최소 힙: **값이 가장 작은** 원소가 루트로 → 우선 제거
    - 파이썬의 `import heapq`는 **기본적으로 최소 힙** 제공
        - 최대 힙이 필요하면, 값을 **음수**로 바꿔 삽입하거나 별도 변환 로직 사용
2. 힙 정렬(Heap Sort)
    - 데이터의 삽입/삭제가 빈번한 경우 유리하다.
    - **힙을 이용하여 배열을 정렬**하는 알고리즘
    1. 모든 원소를 힙에 삽입(혹은 주어진 배열을 힙 구조로 만들기)
    2. **힙에서 루트 노드**(가장 큰 값/가장 작은 값)를 **pop**하여 결과 배열에 삽입
    3. 힙에서 원소가 빌 때까지 반복 → **정렬된 결과**
    - 시간 복잡도: **`$O(n log n)$`** (삽입·삭제 각각 `$O(log n) × n$`번)
        
        ```python
        def heap_sort(arr):
            # 1. 빈 힙 생성, 모든 원소 삽입 
            heap = [None]  # 1-based index 사용 가정
            for x in arr:
                heap_push(heap, x)
        
            sorted_arr = []
            # 2. 힙에서 최대(혹은 최소) pop하여 배열에 삽입 
            while len(heap) > 1:
                sorted_arr.append(heap_pop(heap))
            return sorted_arr
        
        ```

### `heapq` 모듈

`import heapq`
- 파이썬에서 힙은 리스트(list)로 구현

| 함수 | 설명 | 시간 복잡도 |
| --- | --- | --- |
| **`.heappush(heap, item)`** | 힙에 `item`을 삽입 | $O(log n)$ |
| **`.heappop(heap)`** | 힙에서 **가장 작은 원소**를 삭제 후 반환. 힙이 비어있을 경우 `IndexError` 발생 | $O(log n)$ |
| **`.heappushpop(heap, item)`** | 한 번에 `item`을 삽입 후, **가장 작은 원소**를 꺼냄 | $O(log n)$ |
| **`.heapreplace(heap, item)`** | 힙의 가장 작은 원소를 **바로 제거** 후 `item`을 삽입. `heappushpop`와 비교해, 꼭 `item`이 들어간 뒤 제거되는 것은 아니므로 주의 | $O(log n)$ |
| **`.heapify(x)`** | 기존 리스트 `x`를 **힙 구조**로 변환 | $O(n)$ |