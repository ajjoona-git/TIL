## Numpy 실습

`np.identity(n)` n x n 크기의 단위행렬을 생성한다.

- 단위 행렬 (Identity Matrix): 주대각선(왼쪽 위에서 오른쪽 아래로 이어지는 대각선)의 원소가 모두 1이고 나머지 원소는 모두 0인 행렬

    ```
    [[1. 0. 0.]
     [0. 1. 0.]
     [0. 0. 1.]]
    ```

- `np.eye(N, M=none, k=0)` N x M 크기의 단위 행렬을 생성한다.
    - 행과 열의 수를 다르게 지정하여 정방 행렬이 아닌 행렬도 만들 수 있다.
    - 대각선의 위치를 옮겨 다른 대각 행렬을 만들 수도 있다.

`np.random.randn(3, 3)` 표준정규분포로부터 3x3 배열을 생성한다.

`x.astype(int)`: NumPy 배열 `x`의 모든 원소의 자료형을 정수(int)로 변경하여 새로운 배열을 생성한다.

`np.tile(v, (3, 1))` 배열 `v`를 지정된 횟수만큼 반복하여 타일처럼 쌓아 새로운 배열을 생성한다.

- 두 번째 인자 `(3, 1)`: `v`를 반복할 횟수를 지정한다.
    - `3`: 첫 번째 축(행 방향)으로 3번 반복한다.
    - `1`: 두 번째 축(열 방향)으로 1번 반복한다.

`V.flatten()` 다차원 배열인 `V`의 모든 원소를 순서대로 가져와 새로운 1차원 배열로 만든다.

- 원본 배열 V는 변경되지 않는다.

---

## NumPy

과학적 계산을 위한 python 의 기반적 라이브러리

- 수를 계산하는 다양한 기능을 제공한다.

```bash
pip install numpy
```

### ndarray

- 내부의 모든 원소들은 반드시 같은 데이터 타입을 저장해야 한다.
- N차원을 직관적으로 표현할 수 있다.
- Pandas, TensorFlow, PyTorch와 같은 다른 라이브러리들의 기반이 되는 핵심 데이터 구조
- 주요 속성


    | `.ndim` | 배열의 차원 수 |
    | --- | --- |
    | `.shape` | 각 차원의 크기 |
    | `.size` | 전체 원소의 크기 |
    | `.dtype` | 데이터 타입 |

### numpy 함수

```python
# 1. np.zeros(): 모든 원소가 0인 배열 생성
# 2행 4열의 모양으로, 모든 값이 0인 float 타입의 배열을 만듭니다.
zeros_array = np.zeros((2, 4))
print(zeros_array, '\n')
"""
[[0. 0. 0. 0.]
 [0. 0. 0. 0.]]
"""

# 2. np.ones(): 모든 원소가 1인 배열 생성
# 3행 3열의 모양으로, 모든 값이 1인 integer(정수) 타입의 배열을 만듭니다.
ones_array = np.ones((3, 3), dtype=int)
print(ones_array, '\n')
"""
[[1 1 1]
 [1 1 1]
 [1 1 1]]
"""

# 3. np.full(shape, fill_value): 지정한 모양의 배열을 만들고, 값을 채우기
# 2행3열의 모양으로, 모든 값이 2인 배열을 생성
full_array = np.full((2, 3), 2)
print(full_array)
"""
[[2 2 2]
 [2 2 2]]
"""

# 4. np.arange(): 연속적인 값을 가진 배열 생성
# 10부터 30 이전까지 5씩 건너뛰는 숫자로 배열을 만듭니다.
arange_array = np.arange(10, 30, 5)
print(arange_array, '\n')
"""
[10 15 20 25]
"""

# 5. np.linspace(): 균일한 간격을 가진 배열 생성
# 0부터 1까지의 구간을 총 5개의 원소로 균일하게 나눕니다.
linspace_array = np.linspace(0, 1, 5)
print(linspace_array, '\n')
"""
[0.   0.25 0.5  0.75 1.  ]
"""

```

### Indexing

- 인덱스는 0부터 시작한다.
- [행, 열] 형태로 접근한다.
    - 파이썬 리스트처럼 [행][열]의 형태로 접근 가능하나, 표준이 아니며 비효율적이다.

```python
# 2차원 배열 생성 (3행 4열)
arr2d = np.array([[1, 2, 3, 4],
                  [5, 6, 7, 8],
                  [9, 10, 11, 12]])

# 1행 2열의 요소에 접근 (0부터 시작하므로 두 번째 행, 세 번째 열)
element = arr2d[1, 2]  # 7

# 파이썬 리스트처럼 두 번 접근하는 것도 가능하지만,
# 콤마(,)를 사용하는 것이 NumPy의 표준 방식이며 더 효율적
list_element = arr2d[1][2] # 7
```

### Slicing

- 슬라이싱을 하면 새로운 객체를 생성하는 대신, 원본 데이터의 일부를 들여다보는 뷰(View)를 반환한다.
- **슬라이싱한 객체를 수정하면 원본도 수정된다.**

```python
arr2d = np.array([[1, 2, 3, 4],
                  [5, 6, 7, 8],
                  [9, 10, 11, 12]])

# 첫 두 행과 1열부터 2열까지
sub_arr = arr2d[:2, 1:3]
# [[2 3]
#  [6 7]]

# 특정 행 전체를 가져오기
row = arr2d[1, :]  # [5 6 7 8]

# 1. 파이썬 예시
python_list = [10, 20, 30, 40, 50]

sliced_list = python_list[1:4]  # [20, 30, 40]
sliced_list[0] = 999

print(python_list)  # 변경되지 않음 ( [10, 20, 30, 40, 50])

# 1. 넘파이 예시
numpy_array = np.array([10, 20, 30, 40, 50])

sliced_array_view = numpy_array[1:4]  # [20 30 40]
sliced_array_view[0] = 999

print(numpy_array)  # 변경 됨([ 10 999  30  40  50])
```

### Boolean Indexing

- 조건식을 사용해 True인 요소만 추출한다.

```python
data = np.array([[1, 2],
                 [3, 4],
                 [5, 6]])

# 조건에 맞는 boolean 배열 생성
bool_mask = data > 3
print("Boolean 마스크:\n", bool_mask)
# [[False False]
#  [False  True]
#  [ True  True]]

# 마스크를 사용해 True 위치의 값만 추출 (1차원 배열로 반환됨)
print("\n3보다 큰 값들:", data[bool_mask]) # 출력: [4 5 6]

# 조건을 직접 인덱스에 넣어도 동일하게 동작합니다.
print("짝수만 추출:", data[data % 2 == 0]) # 출력: [2 4 6]
```

### Fancy Indexing

- 인덱스를 담은 배열을 사용하여 원하는 요소만 가져온다.
- 비연속적으로 요소를 선택할 때 사용한다.

```python
arr = np.array([10, 20, 30, 40, 50, 60, 70])

# 인덱스 0, 2, 5에 해당하는 요소를 선택
indices = [0, 2, 5]
print("팬시 인덱싱 결과:", arr[indices]) # 출력: [10 30 60]

# 2차원 배열에서도 가능
arr2d = np.arange(9).reshape(3, 3)
print("\n원본 2차원 배열:\n", arr2d)
# [[0 1 2]
#  [3 4 5]
#  [6 7 8]]

# 행 인덱스 [0, 2], 열 인덱스 [1, 2]를 선택
# 즉, (0, 1) 위치의 요소와 (2, 2) 위치의 요소를 선택
print("\n2D 팬시 인덱싱:", arr2d[[0, 2], [1, 2]]) # 출력: [1 8]
```

### Reshape

- `reshape(row, col)`: 원소의 총 개수는 유지하고 배열의 행과 열 구조를 변경한다.
- 원본 배열의 총 원소 개수와 변경 후 배열의 총 원소 개수가 **반드시 같아야 한다.**
- `-1`을 입력하면 남은 차원 크기를 자동으로 계산해준다.

```python
# arr는 여전히 12개의 원소를 가짐
arr = np.arange(12)

# 1. 1D -> 2D로 변경 (3행 4열)
reshaped_arr = arr.reshape(3, 4)
print("reshape(3, 4) 결과 (2D):\n", reshaped_arr, reshaped_arr.shape)

# 1. 행을 4로 지정하면, 열은 알아서 3으로 계산됨 (4 * 3 = 12)
arr_m1 = arr.reshape(4, -1)
print("\nreshape(4, -1) 결과:\n", arr_m1, arr_m1.shape)

# 2. 열을 2로 지정하면, 행은 알아서 6으로 계산됨 (6 * 2 = 12)
arr_m2 = arr.reshape(-1, 2)
print("\nreshape(-1, 2) 결과:\n", arr_m2, arr_m2.shape)
```

### numpy 연산

```python
arr = np.array([[1, 2, 3],
                [4, 5, 6]])

# 덧셈: 모든 요소에 10을 더하기
add_result = arr + 10
print("덧셈 결과:\n", add_result)
# [[11 12 13]
#  [14 15 16]]

# 곱셈: 모든 요소에 3을 곱하기
mul_result = arr * 3
print("\n곱셈 결과:\n", mul_result)
# [[ 3  6  9]
#  [12 15 18]]

arr1 = np.array([[1, 2], [3, 4]])
arr2 = np.array([[5, 6], [7, 8]])

# 배열 간 덧셈
add_arr = arr1 + arr2
print("배열 간 덧셈:\n", add_arr)
# [[ 6  8]
#  [10 12]]

# 배열 간 곱셈
mul_arr = arr1 * arr2
print("\n배열 간 곱셈:\n", mul_arr)
# [[ 5 12]
#  [21 32]]

```

### 유니버셜 함수 (Universal Functions)

- 수학적인 연산을 빠르고 효율적으로 수행하는 함수 목록

```python
# 1. np.sqrt() : 배열의 각 요소에 제곱근을 계산
arr_basic = np.array([1, 4, 9, 16])
sqrt_result = np.sqrt(arr_basic)
print("## 1. np.sqrt() 결과 (제곱근) ##")
print(sqrt_result, '\n') # [1. 2. 3. 4.]

# 2. np.exp() : 배열의 각 요소에 지수 함수(e^x)를 적용
# e^0=1, e^1=2.718..., e^2=7.389...
arr_exp = np.array([0, 1, 2])
exp_result = np.exp(arr_exp)
print("## 2. np.exp() 결과 (지수 함수) ##")
print(exp_result, '\n')

# 3. np.log() : 배열의 각 요소에 자연로그(ln)를 계산
# np.exp()의 결과값을 다시 넣으면 원래 값이 나옵니다 (log(e^x) = x)
log_result = np.log(exp_result)
print("## 3. np.log() 결과 (자연로그) ##")
print(log_result, '\n') # [0. 1. 2.]

# 4. np.sin() : 배열의 각 요소에 사인(sin) 값을 계산
# sin(0)=0, sin(90도)=1, sin(180도)=0
arr_angles = np.array([0, np.pi/2, np.pi]) # 0, 90도, 180도를 라디안으로 표현
sin_result = np.sin(arr_angles)
print("## 4. np.sin() 결과 (사인 값) ##")
print(sin_result, '\n') # [0.0000000e+00 1.0000000e+00 1.2246468e-16]
# 참고: np.pi가 완벽한 무한소수가 아니므로 sin(pi)의 결과가
# 0이 아닌 아주 작은 값으로 나올 수 있습니다.

import numpy as np

# 5. 3x3 크기의 단위 행렬 생성
identity_matrix = np.eye(3)
print(identity_matrix)
# [[1. 0. 0.]
#  [0. 1. 0.]
#  [0. 0. 1.]]

# 6. 2행 3열 크기의 배열을 생성하고 난수로 채우기
# 표준정규분포(평균 0, 분산 1)을 따르는 무작위 실수를 채운다.
random_matrix = np.random.randn(2, 3)
print(random_matrix)
# [[-0.53689437  1.23293836 -0.2343209 ],
#  [ 0.8310389   0.38950982 -0.6869436 ]]

# 7. 내적
# 2x3 행렬 A 생성
matrix_a = np.array([[1, 2, 3],
                     [4, 5, 6]]) # shape: (2, 3)

# 3x2 행렬 B 생성
matrix_b = np.array([[7, 8],
                     [9, 10],
                     [11, 12]]) # shape: (3, 2)

# 행렬 곱 계산 (A @ B 와 동일)
result_matrix = np.dot(matrix_a, matrix_b) # 결과 shape: (2, 2)
print(result_matrix)
# [[ 58  64]
#  [139 154]]
```

- 브로드캐스팅(Broadcasting): 크기가 작은 배열이 자동으로 확장되어 큰 배열의 모양에 맞춰 연산이 수행된다.
    - 편향(bias)을 더하는 연산에서 핵심적인 역할

### numpy 집계 함수

- axis 축 매개변수
    - `axis=0` (세로 방향): 각 열(column)에 대해 연산을 수행한다.
    - `axis=1` (가로 방향): 각 행(row)에 대해 연산을 수행한다.
    - 지정하지 않는 경우, 배열 전체의 모든 원소를 대상으로 연산한다.

```python
arr = np.array([0, 10, 20, 30, 40])

# 주요 집계 함수 예시
print(f"합계 (sum): {np.sum(arr)}")  # 100
print(f"평균 (mean): {np.mean(arr)}")  # 20.0
print(f"최댓값 (max): {np.max(arr)}")  # 40
print(f"최솟값 (min): {np.min(arr)}")  # 0
print(f"표준편차 (std): {np.std(arr):.2f}")  # 14.14
print(f"분산 (var): {np.var(arr)}")  # 200.0
print(f"최댓값의 인덱스 (argmax): {np.argmax(arr)}")  # 4
print(f"최솟값의 인덱스 (argmin): {np.argmin(arr)}")  # 0

arr2d = np.array([[1, 2, 3],
                  [4, 5, 6],
                  [7, 8, 9]])

# 1. 전체 합계 (axis 지정 안 함)
total_sum = arr2d.sum() # 또는 np.sum(arr2d)
print(f"전체 합계: {total_sum}") # 1+2+...+9 = 45

# 2. axis=0 (열 기준 합계)
sum_axis_0 = arr2d.sum(axis=0)
print(f"열(axis=0) 기준 합계: {sum_axis_0}") # [12 15 18]

# 3. axis=1 (행 기준 합계)
# [1+2+3, 4+5+6, 7+8+9]
print(f"행(axis=1) 기준 합계: {sum_axis_1}") # [ 6 15 24]

# 4. 각 열에서 최댓값의 인덱스 찾기
# [0, 0, 0] 열: 7 (인덱스 2)
# [1, 1, 1] 열: 8 (인덱스 2)
# [2, 2, 2] 열: 9 (인덱스 2)
max_indices = np.argmax(arr2d, axis=0)
print(f"각 열의 최댓값 인덱스: {max_indices}") # [2 2 2]
```