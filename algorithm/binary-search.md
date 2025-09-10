# 스스로 학습
## Lower Bound, Upper Bound

### Lower Bound (하한)

- 정렬된 리스트에서 `key` 값과 같거나 `key`보다 큰 값들 중 가장 왼쪽에 있는 값의 인덱스
- 중복된 값이 여러 개 있을 때, 그 값들이 시작되는 첫 번째 위치를 찾을 때 유용하다.
- 예: `[1, 2, 2, 2, 3, 4]`에서 `key=2`의 lower bound는 첫 번째 `2`가 있는 인덱스 `1`

### Upper Bound (상한)

- 정렬된 리스트에서 `key` 값보다 큰 값들 중 가장 왼쪽에 있는 값의 인덱스
- 중복된 값이 여러 개 있을 때, 그 값들이 끝나는 지점의 바로 다음 인덱스를 찾을 때 유용하다.
- 예: `[1, 2, 2, 2, 3, 4]`에서 `key=2`의 upper bound는 `2` 다음인 `3`이 있는 인덱스 `4`

### 활용

정렬된 리스트에서 특정 값이 몇 개 존재하는지를 효율적으로 구할 수 있다.

**개수 = (Upper Bound의 인덱스) - (Lower Bound의 인덱스)**

예시: `[1, 2, 2, 2, 3, 4]`에서 `key=2`의 개수

- **Lower Bound**: `key=2` 이상인 첫 번째 원소는 인덱스 `1`의 `2`
- **Upper Bound**: `key=2`보다 큰 첫 번째 원소는 인덱스 `4`의 `3`
- **개수**: `4 - 1 = 3` (실제로 `2`는 세 개 존재합니다)

### 이진 탐색

이진 탐색이 '값을 찾았다'는 순간 멈추는 반면, Lower/Upper Bound를 찾는 알고리즘은 '값을 찾았더라도 더 왼쪽에 동일한 값이 있을 수 있는지', 또는 '오른쪽으로 넘어가서 더 큰 값이 있는지'를 계속 탐색한다.

### `bisect` 모듈

`bisect` 모듈을 활용하면 파이썬에서 이진 탐색, 특히 Lower/Upper Bound를 쉽게 구현할 수 있다.

- `bisect.bisect_left(a, x)`: `lower bound`
- `bisect.bisect_right(a, x)`: `upper bound`

<br><br>

# 수업 필기

## 이진 검색 (Binary Search)

**정렬된 자료**에서 **중간 지점(mid)**을 기준으로 탐색 범위를 **반씩 줄여가며** 목표 값을 찾는 검색 알고리즘

- **전제 조건**: 데이터가 반드시 **정렬**되어 있어야 한다.
- **시간 복잡도**: `$O(logn)$` (순차 검색의 `$O(n)$`보다 훨씬 빠름)
- **단점**: 데이터의 삽입/삭제가 잦을 경우, 정렬 상태를 유지하는 비용이 추가로 발생한다.

### 이진 검색 과정

1. 자료의 중앙에 있는 원소를 고른다.
2. 중앙 원소의 값과 찾고자 하는 목표 값을 비교한다.
3. 목표 값이 중앙 원소의 값보다 
작으면 자료의 왼쪽 반에 대해서 새로 검색을 수행하고, 
크다면 자료의 오른쪽 반에 대해서 새로 검색을 수행한다.
4. 찾고자 하는 값을 찾을 때까지 ①~③의 과정을 반복한다.

### 이진 검색 코드 구현
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