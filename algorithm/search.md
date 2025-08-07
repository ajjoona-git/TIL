# 수업 필기


## 검색 Search

- 검색(Searching): 저장되어 있는 자료 중에서 원하는 항목을 찾는 작업
- 탐색 키(Search Key): 자료를 구별하는 데 사용하는 키(값)
- 자료의 규모, 정렬 여부, 삽입/삭제 발생 빈도 등을 고려해 적절한 검색 방식을 선택한다.

### 순차 검색 (Sequential Search)

일렬로 되어 있는 자료(예: 배열, 연결 리스트 등)를 순서대로 검색하는 방법

- 자료의 정렬 여부와 상관없이 사용할 수 있다.
- 알고리즘이 단순하여 구현이 쉽다.
- 검색 대상의 수가 많은 경우, 수행시간이 급격히 증가하여 비효율적이다.
- 시간 복잡도: `$O(n)$`

1. **정렬되지 있지 않은 경우**
- 첫 번째 원소부터 키 값과 비교 → 완전 탐색

```python
# 정렬되어 있지 않은 배열의 순차 검색
def unordered_sequential_search(arr, key):
		'''
    정렬되지 않은 리스트(arr)에서 key를 순차적으로 검색한 뒤
    찾으면 해당 인덱스를, 없으면 -1을 반환
    '''
    for index, value in enumerate(arr):
		    if value == key:  
				    return index  # 값 발견 시 인덱스 반환
				    break
		else:
				return -1  # 끝까지 찾지 못했으면 -1
```

2. **정렬되어 있는 경우**
- 첫 번째 원소부터 키 값과 비교하다가, 키 값보다 원소의 값이 크면 검색을 종료한다.

```python
def ordered_sequential_search(arr, key):
		'''
    정렬된 리스트(arr)에서 key를 순차적으로 검색한 뒤
    찾으면 해당 인덱스를, 없으면 -1을 반환
    이때 arr[index] > key 이면 더 이상 비교할 필요가 없다.
    '''
    for index, value in enumerate(arr):
		    if value == key:  
				    return index  # 값 발견 시 인덱스 반환
				    break
				elif value > key:
						return -1  # value가 key보다 커지면 이후 원소들 역시 key보다 클테니 탐색 종료
						break  
		else:
				return -1  # 끝까지 찾지 못했으면 -1
```

- **실전 팁**
    - 자료 크기가 작거나, 정렬이 안 된 상태에서 임시로 빠르게 탐색해야 한다면 유용.
    - 크게 효율이 중요하지 않은 소규모 데이터에서도 간편하게 사용할 수 있음.
    - 대규모 데이터 및 빈번한 검색에서는 **`이진 검색`** 또는 해시, 트리 구조 등을 고려.

### 이진 검색 (Binary Search)

탐색 키를 찾을 때까지 **검색 범위를 반으로** 줄여가면서 검색을 진행하는 방법

- 자료의 중앙에 있는 원소를 기준으로, 키 값이 원소의 값보다 작다면 왼쪽 그룹, 크다면 오른쪽 그룹에서 검색을 반복한다.
- 자료가 **정렬된 상태**여야 한다.
- 데이터의 삽입/삭제가 발생했을 때, 정렬 상태로 유지하는 추가 작업이 필요하다.
- 시간 복잡도:  `$O(logn)$`

1. **반복문 방식**

```python
def binary_search(arr, key):
		# 1. 검색 범위의 시작점과 종료점을 설정
		start = 0
		end = len(arr) - 1
		
		while start <= end:
				# 2. 중앙값을 찾는다.
				middle = (start + end) // 2
				
				# 3-1. 값이 같다면 검색 성공, 종료
				if arr[middle] == key:
						return middle
				
				# 3-2. 찾는 값(key)보다 크면, 왼쪽 구간 선택
				elif arr[middle] > key:
						end = middle - 1
				
				# 3-3. 찾는 값(key)보다 작으면, 오른쪽 구간 선택
				else:
						start = middle + 1
		
		# 검색 실패 시, -1 반환
		return -1
```

2. **재귀 방식**

```python
# 재귀함수를 이용한 이진 검색
def binary_search_recursive(arr, left, right, key):
		'''
    - arr  : 정렬된 리스트 (오름차순)
    - left : 현재 검색 범위의 시작 인덱스
    - right: 현재 검색 범위의 끝 인덱스
    - key: 찾고자 하는 값
    '''
    
    # 1. 종료 조건: 탐색 범위가 더 이상 유효하지 않으면 검색 실패
    if left > right:
		    return -1
		    
		# 2. 중앙 인덱스 계산
		middle = (left + right) // 2
		
		# 3-1. 값이 같다면 검색 성공, 종료
		if arr[middle] == key:
				return middle
		
		# 3-2. 찾는 값(key)보다 크면, 왼쪽 구간 [left, middle - 1]를 재귀 탐색
		elif arr[middle] > key:
				return binary_search_recursive(arr, left, middle - 1, key)
		
		# 3-3. 찾는 값(key)보다 작으면, 오른쪽 구간을 대상 [middle + 1, right]를 재귀 탐색
		else:
				return binary_search_recursive(arr, middle + 1, right, key)
		
```