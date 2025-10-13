## Matplotlib

```python
from matplotlib import pyplot as plt
```

1. **파이썬의 대표적인 시각화 라이브러리**
    - 데이터를 다양한 그래프(선 그래프, 막대 그래프, 히스토그램, 산점도 등)로 표현
    - 데이터 과학과 AI에서 **EDA**(탐색적 데이터분석) 단계에 반드시 필요한 도구
2. `pyplot`
    - matplotlib의 서브 모듈로, 간단한 명령어로 **빠르게 그래프를 그릴 수 있게 해주는 인터페이스**
3. matplotlib 기본 구조
    - `plt.plot()`: 선 그래프
    - `plt.hist()`: 히스토그램
    - `plt.scatter()`: 산점도
    - `plt.bar()`: 막대 그래프

### 분포 (Distribution)

데이터가 어떤 값 주위에 얼마나 **모여있는지, 퍼져있는지, 치우쳐 있는지**를 나타내는 개념

- **정규분포**: 데이터가 평균 근처에 고르게 분포하는지 나타내는 척도
- **왜도**: 데이터가 한쪽으로 치우쳐 있는지 나타내는 척도
- **첨도**: 분포가 정규분포보다 얼마나 뾰족하거나 완만한지의 정도를 나타내는 척도

```python
# 3개의 데이터를 한 번에 비교
plt.figure(figsize=(12, 8))
plt.hist(score_normal, bins=20, alpha=0.5, label='Normal', edgecolor='black')
plt.hist(score_left_skew, bins=20, alpha=0.5, label='Left Skew', edgecolor='black')
plt.hist(score_right_skew, bins=20, alpha=0.5, label='Right Skew', edgecolor='black')
plt.title('Comparison of Different Score Distributions')
plt.xlabel('Score')
plt.ylabel('Frequency')
# 범례 표시
plt.legend()
plt.show()
```

### **산점도 (Scatter Plot)와 상관 계수 (Correlation Coefficient)**

- **산점도**: 두 변수(특성)간의 관계를 파악하기 위해, 각 데이터 포인트를 2차원 평면에 **점으로 나타낸 그래프**
    - 변수들이 어떤 패턴(선형, 비선형, 무작위 등)을 보이는지 시각적으로 확인
    - `plt.scatter()`: Matplotlib을 사용하여 `assignment_rate`와 `final_score` 두 변수 간의 관계를 산점도로 시각화

```python
# scatter 함수로 산점도 생성
    # x축: assignment_rate, y축: final_score
    # s, c, marker 등 다양한 옵션 설정 가능
        # s: 점 크기(size)
        # c: 점 색상(color)
        # marker: 점 모양(marker style)
        # alpha: 점 투명도(transparency)
        # edgecolor: 점 테두리 색상
        # cmap: 색상 맵(color map)
        # linewidth: 점 테두리 두께
        # vmin, vmax: 색상 범위 설정
        # norm: 색상 정규화 방법
plt.scatter(assignment_rate, final_score, alpha=0.7) # alpha는 점의 투명도
```

- **상관관계**: 두 변수가 함께 변화하는 **경향성을** 나타내는 통계적 척도
    - **양의 상관관계 (1에 가까움):** 한 변수가 증가할 때 다른 변수도 증가하는 경향
    - **음의 상관관계 (-1에 가까움):** 한 변수가 증가할 때 다른 변수는 감소하는 경향
    - **상관관계 없음 (0에 가까움):** 두 변수 사이에 뚜렷한 선형 관계가 없음
    - `df.corr()`: Pandas의 `.corr()` 메서드를 사용하여 데이터 프레임의 모든 숫자형 변수 간의 상관계수를 계산

```python
# final_score와 assignment_rate의 상관관계 추출
    # corr: 상관계수 계산 함수
    # 상관계수는 -1에서 1 사이의 값으로 나타나며, 1에 가까울수록 강한 양의 상관관계, -1에 가까울수록 강한 음의 상관관계를 의미
correlation_matrix = df_main_copy.corr()
print("final_score와 assignment_rate의 상관관계: ", final_score_assignment_rate_corr)
# final_score와 assignment_rate의 상관관계:  0.48677915713898284
```

## 선형 회귀 모델

### $Y=WX+b$

1. **가중치(Weight, W)**
    - 각 입력 변수가 결과 변수에 미치는 **영향력 또는 중요도**를 나타내는 게수
    - 가중치의 절대값이 클수록 해당 특성이 예측에 더 큰 영향을 미침
2. **편향(Bias, b)**
    - 모든 입력 변수가 0일 때의 **기본 예측값**
    - 모델이 데이터 전체의 기본적인 편향을 학습할 수 있도록 돕는 절편(intercept) 역할

### `pandas.DataFrame.select_dtypes(include=None, exclude=None)`

- 파라미터: include, exclude (scalar or list-like)
- Returns: DataFrame

```python
# 범주형 변수 추출 (dtype이 'category'인 열)
categorical_cols: List[str] = df.select_dtypes(include='category').columns
# 연속형 변수 추출 (숫자형 dtype인 열)
continuous_cols: List[str] = df.select_dtypes(include=['int64', 'float64']).columns
```

### 표준화(Standardization)

$Z = \frac{x - \mu}{\sigma}$

데이터의 분포를 평균이 0, 표준편차가 1이 되도록 변환하는 전처리 기법

```python
# 1. 앞에서 만들어낸 `continuous_cols`를 이용하여 연속형 변수만 담겨져있는 `X_raw`를 만들어주세요.
X_raw: np.ndarray = df[continuous_cols].values

# 2. 각 열의 평균을 계산하여 mu에 할당하세요.
mu: np.ndarray = X_raw.mean(axis=0)

# 3. 각 열의 표준편차를 계산하여 sigma에 할당하세요.
sigma: np.ndarray = X_raw.std(axis=0)
# 표준화 과정에서 분모에 등장하는 sigma에 0이 포함되는 경우 문제가 생깁니다.
# 추가로 혹시 모를 안전 장치를 취해볼까요? (별도의 테스트코드는 없습니다)
sigma[sigma == 0] = 1e-8

# 4. 브로드캐스팅을 활용해 (X_raw - mu) / sigma 형태로 표준화를 수행하고 X_norm에 저장하세요.
X_norm: np.ndarray = (X_raw - mu) / sigma
```

### 정규 방정식

```python
# 1. X_norm에서 feature인 X와 예측해야하는 대상인 `price` y를 분리해봅시다.
X: np.ndarray = X_df.values
y: np.ndarray = df['price'].values

# 2. 절편항을 추가해줍니다.
m, n = X_norm.shape
# m개의 행을 가진 1짜리 열벡터를 X의 맨 앞에 추가합니다.
X_b = np.c_[np.ones((m, 1)), X] # shape = (m, n+1)

# 3. 요소별로 계산을 진행해봅시다.
# .T는 전치행렬(Transpose)을 의미하며, @는 행렬 곱셈(dot product)입니다.
# 3-1. 역행렬의 대상인 `X_b^T @ X_b`를 구해 XT_X에 할당해주세요.
XT_X  = X_b.T @ X_b # shape = (n+1, n+1)
# 3-2. 역행렬과 곱해지는 X_b^T @ y`를 구해 XT_y에 할당해주세요.
XT_y  = X_b.T @ y # shape = (n+1, 1)

# 4. 해를 구해주세요.
# np.linalg.inv()는 역행렬(Inverse)을 계산하는 함수입니다.
theta = np.linalg.inv(XT_X) @ XT_y # shape = (n+1, 1)

# 5. 마지막으로 모델을 평가해봅시다.
# 얻어낸 `theta`와 데이터의 행렬곱을 통하여 예측값인 `y_pred`를 구해보고
y_pred = X_b @ theta # shape = (m, 1)
# 예측값과 실제값 차이를 나타내는 MSE를 계산해봅시다.
# (예측값 - 실제값)의 제곱의 평균을 계산합니다.
mse    = np.mean((y_pred - y.reshape(-1, 1))**2)
```

### `numpy.linalg.lstsq(*a*, *b*, *rcond=None*)`

```python
# TODO: `lstsq`를 이용하여 `theta_lstsq`를 구해주세요.
theta_lstsq = np.linalg.lstsq(X_b, y, rcond=None)
```