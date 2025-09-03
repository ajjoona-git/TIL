## 비트 연산

### 비트 연산자

| 비트 연산자 | 설명 | 활용 |
| --- | --- | --- |
| `&` | 비트 AND | `i & (1<<j)` i의 j번째 비트가 1인지 아닌지를 검사 |
| `\|` | 비트 OR |  |
| `<<: *= 2`  | 비트를 왼쪽으로 이동 | `1 << n: $2^n$` 원소가 n개일 경우의 모든 부분집합의 수 |
| `>>: //= 2`  | 비트를 오른쪽으로 이동 |  |
| `^` | 비트 XOR (Exclusive) |  |
| `~`  | 비트 NOT |  |


### 비트 연산 응용 → 부분 집합

- `1 << n` 2^n 의 값을 갖는다.
- `i & (1 << n)` i의 n번째 비트가 1인지 아닌지를 확인할 수 있다.

### 음수 표현 방법

- 컴퓨터는 “2의 보수”를 활용하여 음수를 관리한다.
    - 뺄셈의 연산 속도를 올릴 수 있고, +0과 -0을 따로 취급하지 않기 위함
- 맨 앞자리 bit (MSB)는 음수/양수를 구분하는 비트
- 수를 모두 뒤집고 +1한다.

**예시**

`10001`의 2의 보수 → 01110 + 1 = `01111`

`1111000`의 2의 보수 → 0000111 + 1 = `0001000`

### 상태값 관리 활용 예시

조건문으로 구현한다면 조건문이 매우 많아지는데, 비트 연산을 활용하면 성능을 향상시킬 수 있다.

```python
# 상태를 나타내는 플래그들 (각 상태는 1비트를 사용)
WALK = 1 << 0    # 1번 비트: 걷기 상태
ATTACK = 1 << 1  # 2번 비트: 공격 상태
JUMP = 1 << 2    # 3번 비트: 점프 상태

# 현재 상태를 나타내는 변수 (초기 상태는 아무것도 하지 않음)
character_state = 0

# 상태 설정 함수 (비트 연산을 사용하여 상태를 추가)
def set_state(state, flag):
    return state | flag

# 상태 제거 함수 (비트 연산을 사용하여 상태를 제거)
def unset_state(state, flag):
    return state & ~flag

# 상태 확인 함수 (비트 연산을 사용하여 상태를 확인)
def is_state_active(state, flag):
    return state & flag != 0

# 1. 상태 설정: "걷기 중"과 "점프 중" 설정
character_state = set_state(character_state, WALK)
character_state = set_state(character_state, JUMP)

# 상태 확인: "걷기 중"인지, "점프 중"인지 확인
print("현재 캐릭터의 상태:")
if is_state_active(character_state, WALK):
    print("- 캐릭터는 걷고 있습니다.")
if is_state_active(character_state, JUMP):
    print("- 캐릭터는 점프 중입니다.")

# 2. 상태 변경: "공격 중" 추가
character_state = set_state(character_state, ATTACK)

# 상태 확인: "공격 중"인지 확인
print("\n상태 변경 후 캐릭터의 상태:")
if is_state_active(character_state, ATTACK):
    print("- 캐릭터는 공격 중입니다.")

# 3. 상태 제거: "점프 중" 상태를 제거
character_state = unset_state(character_state, JUMP)

# 상태 확인: "점프 중" 상태가 제거되었는지 확인
print("\n상태 제거 후 캐릭터의 상태:")
if is_state_active(character_state, JUMP):
    print("- 캐릭터는 점프 중입니다.")
else:
    print("- 캐릭터는 점프 중이지 않습니다.")
```

## 실수

### 소수점 출력 방법

- f-string 예: `{t2: .2f}` t2 값을 소수점 셋째 자리에서 반올림하여 표현

### 파이썬의 실수 표현 범위

- 64비트 부동소수점으로 실수를 표현
- 최대로 표현할 수 있는 값은 약 `+/- 1.8e308`, 이 이상은 `inf`로 표현한다.
- 컴퓨터는 내부적으로 이진법으로 표현할 수 없는 실수는 정확한 값이 아니라, 근사치로 저장한다. 이때 생기는 작은 오차가 계산 과정에서 다른 결과를 가져올 수 있다.
    - `print(0.1 + 0.1 + 0.1 == 0.3)  # False`

### 부동소수점

- 소수점의 위치를 고정시켜 표현하는 방식
- 소수점의 위치를 왼쪽의 가장 유효한 숫자 다음으로 고정시키고 밑 수의 지수승으로 표현
- `1001.0011` 의 부동소수점 표기 → `1.0010011 * 2^3`

### 실수를 저장하기 위한 형식

- 32-bit 구조
    - 부호 1비트: 0이면 양수, 1이면 음수
    - 지수부 8비트(exponent): 부동소수점의 크기 + bias 값
    - 가수부 23비트(mantissa): 실질적 수