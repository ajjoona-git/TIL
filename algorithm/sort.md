# 스스로 학습

## 정렬 심화 활용법

### `list.sort()` vs `sorted()`

| 특징 | `list.sort()` | `sorted()` |
| --- | --- | --- |
| 적용 대상 | 리스트 | 모든 이터러블(리스트, 튜플, 문자열 등) |
| 반환 값 | `None`  | 새로운 정렬된 리스트 |
| 원본 변경 여부 | 원본 리스트를 직접 변경 | 원본은 변경하지 않는다. |
| 사용 예시 | 메모리 효율이 중요할 때,
코드를 더 간결하게 작성하고 싶을 때 (리스트를 정렬한 후 바로 사용할 때) | 원본 데이터를 보존해야 할 때,
리스트가 아닌 다른 자료형을 정렬할 때 |

### 파라미터

`list.sort()`와 `sorted()` 둘 다 `reverse`와 `key`파라미터를 사용할 수 있다.

- `reverse`: `True`일 때 내림차순 정렬. 기본값은 `False`(오름차순)
- `key`: 정렬의 기준이 되는 함수. `lambda`함수를 많이 활용한다.

```python
words = ['apple', 'banana', 'cat']

# .sort()에 파라미터 적용: 원본 변경
words.sort(key=len, reverse=True)
print(f".sort() 결과: {words}") # ['banana', 'apple', 'cat']

# sorted()에 파라미터 적용: 새 리스트 반환
new_words = sorted(words, key=len, reverse=False)
print(f"sorted() 결과: {new_words}") # ['cat', 'apple', 'banana']
```

### 튜플 정렬

튜플은 불변(immutable)객체이므로 `.sort()`메서드를 사용할 수 없다.

`sorted()`함수를 사용한다. → 원본 튜플은 변경하지 않고, 정렬된 요소를 담은 새로운 리스트를 반환한다.

```python
my_tuple = (5, 2, 8, 1, 9)
sorted_list = sorted(my_tuple)

print(f"원본 튜플: {my_tuple}")
print(f"정렬된 결과 (리스트): {sorted_list}")

"""
원본 튜플: (5, 2, 8, 1, 9)
정렬된 결과 (리스트): [1, 2, 5, 8, 9]
"""
```

### 인스턴스 리스트 정렬

사용자 정의 클래스의 인스턴스로 이루어진 리스트를 정렬할 때는 `sorted()`함수의 `key`파라미터를 사용해 정렬 기준을 명시한다.

```python
class Student:
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def __repr__(self):
        # 객체를 print() 할 때 가독성 좋게 출력
        return f"Student(name='{self.name}', score={self.score})"

students = [
    Student('Alice', 85),
    Student('Charlie', 92),
    Student('Bob', 78)
]

# score를 기준으로 정렬
sorted_students = sorted(students, key=lambda student: student.score)

print(f"정렬된 학생 리스트 (점수 기준): {sorted_students}")

"""
정렬된 학생 리스트 (점수 기준): [Student(name='Bob', score=78), Student(name='Alice', score=85), Student(name='Charlie', score=92)]
"""
```

### 복합 조건 정렬

여러 가지 정렬 기준을 복합적으로 적용하려면 `key` 파라미터에 튜플을 반환하는 함수를 사용한다. 튜플의 첫 번째 요소부터 순서대로 비교하여 정렬한다.

```python
# 문자열 길이 우선, 같은 길이는 사전 순 정렬 예시
words = ['python', 'java', 'c', 'javascript', 'html']

# 1. 길이 우선으로 정렬 (len(word)를 첫 번째 기준으로)
# 2. 길이가 같으면 사전 순으로 정렬 (word를 두 번째 기준으로)
sorted_words = sorted(words, key=lambda word: (len(word), word))

print(f"정렬된 단어 리스트: {sorted_words}")

"""
정렬된 단어 리스트: ['c', 'html', 'java', 'python', 'javascript']
"""
```

<br><br>
# 수업 필기

## 정렬 sort

2개 이상의 자료를 키(특정 기준)에 의해 작은 값부터 큰 값(오름차순), 또는 그 반대의 순서대로(내림차순) 재배열하는 알고리즘

### 종류

- [버블 정렬](./bubble-sort.md)
- [카운팅 정렬](./counting-sort.md)
- [선택 정렬](./selection-sort.md)
- [병합 정렬](./merge-sort.md)
- [퀵 정렬](./quick-sort.md)

### 정렬 알고리즘 비교

|  | **Bubble Sort** | **Selection Sort** | **Counting Sort** |
| :---: | :---: | :---: | :---: |
| 동작 원리 | 인접한 두 요소를 교환하면서 맨 뒤부터 순서대로 정렬된 위치를 확정해나간다. | 최소값을 찾아 맨 앞부터 순서대로 정렬된 위치를 확정해나간다. | 각 요소의 빈도수와 그 누적합을 계산하여 정렬된 결과 배열을 확정해나간다. |
| 시간 복잡도 | $O(n^2)$ | $O(n^2)$ | $O(n + k)$ |

![image.png](../images/counting-sort_4.png)

### 병합 정렬 vs 퀵 정렬

|  | 병합 정렬 (Merge Sort) | 퀵 정렬 (Quick Sort) |
| --- | --- | --- |
| 분할 기준 | 배열을 반으로 나눈다. | 기준(pivot)을 중심으로 기준보다 작은 것을 왼편, 큰 것을 오른편으로  |
| 병합 처리 | 정렬된 부분을 다시 병합하는 과정이 필요 | 병합 과정 불필요 |