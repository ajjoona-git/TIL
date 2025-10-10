## Pandas

데이터 분석과 조작을 위한 여러가지 기능을 제공하는 라이브러리

- series 시리즈: 1차원 하나의 열(column)
- dataframe 데이터프레임: 2차원 데이터
- 딕셔너리 형태로 생성하는 것이 일반적

```bash
pip install pandas
```

### inspecting

- 사분위 수: 전체 데이터를 크기 순으로 정렬한 뒤, 데이터의 양이 똑같도록 4등분하는 기준점

```python
data = {'과목': ['영어', '수학', '과학', '사회', '국어'],
        '점수': [92, 78, 88, 95, 100],
        '응시자 수': [200, 150, 180, 210, 220]}
df = pd.DataFrame(data)

print(df)
"""
   과목   점수  응시자 수
0  영어   92    200
1  수학   78    150
2  과학   88    180
3  사회   95    210
4  국어  100    220
"""

print(df.head(3)) # 처음 3개 행만 보기
print(df.tail(3)) # 마지막 3개 행만 보기

print(df.info())  # 데이터프레임 요약 정보
"""
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 5 entries, 0 to 4
Data columns (total 3 columns):
 #   Column  Non-Null Count  Dtype
---  ------  --------------  -----
 0   과목      5 non-null      object
 1   점수      5 non-null      int64
 2   응시자 수   5 non-null      int64
dtypes: int64(2), object(1)
memory usage: 252.0+ bytes
None
"""

print(df.describe())  # 수치형 열에 대한 요약 통계
"""
               점수       응시자 수
count    5.000000    5.000000
mean    90.600000  192.000000
std      8.294577   27.748874
min     78.000000  150.000000
25%     88.000000  180.000000
50%     92.000000  200.000000
75%     95.000000  210.000000
max    100.000000  220.000000
"""

# (행 개수, 열 개수)
print(df.shape)  # (5, 3)

# 열 이름들
print(df.columns)  # Index(['과목', '점수', '응시자 수'], dtype='object')

# 행 인덱스들
print(df.index)  # RangeIndex(start=0, stop=5, step=1)
```

### indexing

- 행(row) 선택
    - .loc: 이름(label) 기반 선택
        - 끝점을 포함한다!
    - .iloc: 인덱스(integer position) 기반 선택
        - 끝점을 포함하지 않는다.

```python
# 인덱스 이름이 'b'인 행 선택
print(df.loc['b'], '\n')
"""
이름    영희
학년     3
과목    영어
점수    92
Name: b, dtype: object
"""

# 인덱스 이름이 'a'부터 'c'까지인 행들 선택 (c 포함!)
print(df.loc['a':'c'], '\n')
"""
   이름  학년  과목  점수
a  철수   2  수학  85
b  영희   3  영어  92
c  민준   1  수학  78
"""

# 0번째 위치의 행 선택 (첫 번째 행)
print(df.iloc[0], '\n')
"""
이름    철수
학년     2
과목    수학
점수    85
Name: a, dtype: object
"""

# 0번째부터 3번째 이전까지 (0, 1, 2) 위치의 행들 선택 (3 미포함!)
print(df.iloc[0:3], '\n')
"""
   이름  학년  과목  점수
a  철수   2  수학  85
b  영희   3  영어  92
c  민준   1  수학  78
"""
```

- 열(Column) 선택
    - df[’컬럼명’]: 한 개의 열을 시리즈 형태로 반환한다.
    - df[[’컬럼1’, ‘컬럼2’]]: 여러 개의 열을 데이터프레임 형태로 반환한다.

```python
# '이름' 열만 선택
names = df['이름']
print(names, '\n')
"""
a    철수
b    영희
c    민준
d    지아
e    서준
Name: 이름, dtype: object
"""

# '이름'과 '점수' 열 선택
info = df[['이름', '점수']]
print(info, '\n')
"""
   이름  점수
a  철수  85
b  영희  92
c  민준  78
d  지아  88
e  서준  95
"""
```

- 행과 열을 함께 선택
    - [행, 열] 형태로 인자를 전달하여 원하는 셀의 값을 선택한다.

```python
# 인덱스 'c'인 학생의 '과목' 정보
subject_c = df.loc['c', '과목']
print(f"\n인덱스 'c' 학생의 과목: {subject_c}", )  # 인덱스 'c' 학생의 과목: 수학

# 1, 2번 행과 0, 2번 열에 해당하는 데이터 조각 선택
sub_df = df.iloc[[1, 2], [0, 2]]
print(sub_df)
"""
   이름  과목
b  영희  영어
c  민준  수학
"""
```

### Boolean Indexing filtering

- 특정 조건에 따라 True/False 값으로 구성된 Boolean Series를 생성하고, 이 시리즈를 데이터프레임에 적용하여 True인 행만 추출한다.

```python
data = {'이름': ['철수', '영희', '민준', '지아', '서준'],
        '학년': [2, 3, 1, 3, 2],
        '과목': ['수학', '영어', '수학', '영어', '과학'],
        '점수': [85, 92, 78, 88, 95]}

df = pd.DataFrame(data, index=['a', 'b', 'c', 'd', 'e'])

# '서준'의 '과목'과 '점수'를 NaN으로 설정
df.loc['e', '과목'] = np.nan
df.loc['e', '점수'] = np.nan

# '점수'가 90점 이상인 행 필터링
filt = df['점수'] >= 90
df_high_score = df[filt]
print(df_high_score, "\n")
# 또는 한 줄로: df_high_score = df[df['점수'] >= 90]
"""
   이름  학년  과목    점수
b  영희   3  영어  92.0
"""
```

### 특수 조건 필터링

- 특정 값의 포함 여부나 결측치(NaN)를 처리할 때 사용한다.
- .isin(리스트): 해당 칼럼의 값이 주어진 리스트에 포함되는 행을 선택한다.
- .isnull(값): 해당 컬럼 값이 ‘결측치인 경우’에 True를 반환한다.
- .notnull(값): 해당 컬럼 값이 ‘결측치가 아닌 경우’에 True를 반환한다.

```python
# '학년'이 2학년 또는 3학년인 행 필터링
target_grades = [2, 3]
filt_isin = df['학년'].isin(target_grades)
print(df[filt_isin], '\n')
"""
   이름  학년   과목    점수
a  철수   2   수학  85.0
b  영희   3   영어  92.0
d  지아   3   영어  88.0
e  서준   2  NaN   NaN
"""

# '과목'이 NaN인 행 필터링
filt_isnull = df['과목'].isnull()
df_is_null = df[filt_isnull]
print(df_is_null, '\n')
"""
   이름  학년   과목  점수
e  서준   2  NaN NaN
"""

# '점수'가 NaN이 아닌 행 필터링
filt_notnull = df['점수'].notnull()
df_not_null = df[filt_notnull]
print(df_not_null)
"""
   이름  학년  과목    점수
a  철수   2  수학  85.0
b  영희   3  영어  92.0
c  민준   1  수학  78.0
d  지아   3  영어  88.0
"""
```

### 복합 조건 필터링

- 여러 조건을 동시에 적용할 때 논리 연산자를 사용한다.
- 각 조건은 반드시 괄호로 묶어야 한다.

```python
# '과목'이 '수학'이고 '점수'가 80점 이상인 행 필터링
df_seoul_high = df[(df['점수'] >= 80) & (df['과목'] == '수학')]
print(df_seoul_high, "\n")
"""
   이름  학년  과목    점수
a  철수   2  수학  85.0
"""

# '점수'가 92점이거나 '과목'이 '과학'인 행 필터링
df_perfect_or_busan = df[(df['점수'] == 92) | (df['과목'] == '과학')]
print(df_perfect_or_busan, "\n")
"""
   이름  학년  과목    점수
b  영희   3  영어  92.0
"""

# '과목'이 '과학'이 아닌 행 필터링
df_not_seoul = df[~(df['과목'] == '과학')]
print(df_not_seoul, "\n")
"""
   이름  학년   과목    점수
a  철수   2   수학  85.0
b  영희   3   영어  92.0
c  민준   1   수학  78.0
d  지아   3   영어  88.0
e  서준   2  NaN   NaN
"""
```

### 결측치 처리

- .dropna(): 결측치가 있는 행 또는 열을 제거한다.
    - 데이터의 손실이 발생한다.
- .fillna(): 결측값을 특정 값으로 대체한다.
    - 제거보다 데이터 손실이 적다.

```python
df = pd.DataFrame(data)
print(df, '\n')
"""
     A     B   C   D
0  1.0   6.0  11 NaN
1  2.0   NaN  12 NaN
2  NaN   8.0  13 NaN
3  4.0   NaN  14 NaN
4  5.0  10.0  15 NaN
"""

# 결측치(NaN)가 하나라도 있는 행을 제거
df_dropped_rows = df.dropna()
print( df_dropped_rows, '\n')
"""
Empty DataFrame
Columns: [A, B, C, D]
Index: []
"""

# 결측치(NaN)가 하나라도 있는 열을 제거
df_dropped_cols = df.dropna(axis=1)
print(df_dropped_cols, '\n')  # 출력 안됨
"""
    C
0  11
1  12
2  13
3  14
4  15
"""

# 모든 값이 결측치인 행을 제거
df_dropped_all_rows = df.dropna(how='all')
print(df_dropped_all_rows, '\n')
"""
     A     B   C   D
0  1.0   6.0  11 NaN
1  2.0   NaN  12 NaN
2  NaN   8.0  13 NaN
3  4.0   NaN  14 NaN
4  5.0  10.0  15 NaN
"""

```

### 데이터 변환 및 수정

- 새로운 컬럼 형성

```python
data = {'이름': ['철수', '영희', '민수', '지아'],
        '수학': [95, 80, 60, 100],
        '영어': [88, 92, 70, 95]}

df = pd.DataFrame(data)

# 기존 두 컬럼을 더하여 '총점' 컬럼 생성
df['총점'] = df['수학'] + df['영어']

# 조건에 따라 새로운 컬럼의 값 할당 (예: 90점 이상이면 'A', 아니면 'B')
df['학점'] = np.where(df['총점'] >= 180, 'A', 'B')

print(df)
"""
   이름   수학  영어   총점 학점
0  철수   95  88  183  A
1  영희   80  92  172  B
2  민수   60  70  130  B
3  지아  100  95  195  A
"""
```

- .astype(): 데이터 타입 변환이 잘못 지정된 경우, 타입을 변경한다.

```python
data2 = {
    '이름': ['철수', '영희', '민수', '지아'],
    '점수': [85.0, 92.5, np.nan, 78.0]
}

df2 = pd.DataFrame(data2)

# 1. 결측치 처리: NaN을 0으로 채웁니다.
df2['점수'] = df2['점수'].fillna(0)

# 2. '점수' 컬럼을 정수형(int)으로 변경
df2['점수'] = df2['점수'].astype(int)

# 3. 데이터 타입이 너무 커 메모리 효율을 위해 축소 (int64 -> int16)
df2['점수_int16'] = df2['점수'].astype('int16')

print(df2)
"""
   이름  점수  점수_int16
0  철수  85        85
1  영희  92        92
2  민수   0         0
3  지아  78        78
"""
```