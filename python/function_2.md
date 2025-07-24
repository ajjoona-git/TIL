
## 유용한 함수들

### map 함수

`map(function, iterable)`

반복 가능한 데이터 구조(iterable)의 모든 요소에 **function을 적용**하고, 그 결과 값들을 map object로 묶어서 반환

- map object : 결과를 하나씩 꺼내 쓸 수 있는 반복 가능한 객체 자료형. 전체 값을 확인하려면 list나 tuple로 형변환 필요

```python
# map 함수 사용 기본
numbers = [1, 2, 3]
result = map(str, numbers)

print(result)  # <map object at 0x00000239C915D760>
print(list(result))  # ['1', '2', '3']

# map 함수 활용
numbers1 = list(map(int, input().split()))  # 1 2 3
print(numbers1)  # [1, 2, 3]
```

### zip 함수

`zip(*iterables)`

여러 개의 반복 가능한 데이터 구조를 묶어서 **같은 위치에 있는 값들을 하나의 tuple**로 만든 뒤, 그것들을 모아 zip object로 반환하는 함수

- 반복 가능한 자료형의 길이가 다른 경우, 가장 짧은 길이를 기준으로 묶어서 반환한다.
- 여러 개의 리스트를 동시에 조회할 때
- 2차원 리스트의 같은 컬럼 요소를 동시에 조회할 때, 행/열 변환

```python
# zip 함수 사용 기본
girls = ['jane', 'ashley']
boys = ['peter', 'jay']
pair = zip(girls, boys)

print(pair)  # <zip object at 0x000001C76DE58700>
print(list(pair))  # [('jane', 'peter'), ('ashley', 'jay')]

# zip 함수 활용
kr_scores = [10, 20, 30, 50]
math_scores = [20, 40, 50, 70]
en_scores = [40, 20, 30, 50]

for student_scores in zip(kr_scores, math_scores, en_scores):
    print(student_scores)
"""
(10, 20, 40)
(20, 40, 20)
(30, 50, 30)
(50, 70, 50)
"""    
```

### enumerate 함수

`enumerate(iterable, start=0)`

iterable 객체의 각 요소에 대해 **인덱스와 값을 함께 반환**하는 내장함수

- 인덱스 정보를 이용해 요소의 위치를 확인하는 경우
- 인덱스 정보를 이용해 넘버링으로 사용하는 경우

```python
# enumerate 함수 활용 1
# start 인자를 사용하여 인덱스 번호를 1부터 출력
movies = ['인터스텔라', '기생충', '인사이드 아웃', '라라랜드']
for idx, title in enumerate(movies, start=1):
    print(f"{idx}위: {title}")
"""
1위: 인터스텔라
2위: 기생충
3위: 인사이드 아웃
4위: 라라랜드
"""

# enumerate 함수 활용 2
# 인덱스 정보를 활용하여 특정 조건에 맞는 요소 찾기
respondents = ['은지', '정우', '소민', '태호']
answers = ['', '좋아요', '', '괜찮아요']

for i, response in enumerate(answers):
    if response == '':
        print(f"{respondents[i]} 미제출")
"""
은지 미제출
소민 미제출
"""    
```

```python
# zip과 enumerate 활용
kr_scores = [10, 20, 30, 50]
math_scores = [20, 40, 50, 70]
en_scores = [40, 20, 30, 50]

for i, student_scores in enumerate(zip(kr_scores, math_scores, en_scores)):
    print(f'{i}번 인덱스 값 : {student_scores}')
"""
0번 인덱스 값 : (10, 20, 40)
1번 인덱스 값 : (20, 40, 20)
2번 인덱스 값 : (30, 50, 30)
3번 인덱스 값 : (50, 70, 50)
"""    
```