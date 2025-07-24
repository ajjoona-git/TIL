# 스스로 학습

## 제어문 활용

### 리스트 컴프리헨션 (list comprehension)

`num = [x for x in range(10)]` 

- for 문(+ if 문)을 축약해서 표현하는 문법. 수학의 조건제시법처럼 표현한다.
  
- 파이썬에서 데이터를 변환, 필터링, 수집하는 데 사용

- 딕셔너리, 튜플, 셋에도 적용 가능

```python
# 원본
missing_book = []
for book in rental_book:
	if book not in list_of_book:
		missing_book.append(book)

# 리스트 컴프리헨션
missing_book = [x for x in rental_book if x not in list_of_book]
```

## 실습

### **[형변환] [1689. 도서관 사용자 관리 서비스 - 데이터 처리_Lv3]**

```python
import requests
from pprint import pprint as print

dummy_data = []

for number in range(1, 11):
# 무작위 유저 정보 요청 경로
    API_URL = 'https://jsonplaceholder.typicode.com/users/' + str(number)
    # API 요청
    response = requests.get(API_URL)
    # JSON -> dict 데이터 변환
    parsed_data = response.json()

    # 사용자 정보를 dict로 구성
    user_info = {
        'company': parsed_data['company']['name'],
        'name': parsed_data['name'],
    }

    # lat, lng 범위 지정 후 추가
    lat = float(parsed_data['address']['geo']['lat'])
    lng = float(parsed_data['address']['geo']['lng'])

    if lat < 80 and lat > -80:
        user_info['lat'] = lat
    if lng < 80 and lng > -80:
        user_info['lng'] = lng

    # dummy_data 리스트에 사용자 정보 추가
    dummy_data.append(user_info)

print(dummy_data)
```
** `lat = float(parsed_data['address']['geo']['lat'])`에서 `int()`로 하면 에러 발생하는 이유?**

`parsed_data['address']['geo']['lat']`에서 가져오는 lat 값은 API 응답에서 **문자열 형태의 실수**로 제공되기 때문

`int()` 함수는 기본적으로 정수 형태의 문자열 (예: '123')이나 실수형 숫자 (예: 37.3159)를 정수로 변환할 때 사용된다. 하지만 **`int()` 함수는 소수점을 포함하는 문자열 (예: '37.3159')을 직접 정수로 변환하려고 하면 에러**를 발생시킵니다. 왜냐하면 문자열 안에 점(.)이 있어서 이를 온전한 정수 형태의 문자열로 인식하지 못하기 때문이다.


### **[1691. 도서관 사용자 관리 서비스 - 데이터 유효성 검사_Lv5]**

> create_user 함수는 하나의 리스트를 인자로 넘겨받는다.
> 
> - 넘겨받은 사용자 목록을 순회하며 각각 올바른 데이터로 이루어져있는지 확인하기 위해 is_validation 함수를 구성하고 확인한다.
> - is_validation 함수에서 확인하여야 하는 목록은 다음과 같다.
>   1. blood_group의 값이 blood_types에 포함되어 있는가.
>   2. company의 값이 black_list에 포함되어 있지 않은가.
>   3. mail의 값에 @ 문자열이 포함되어 있는가.
>   4. name의 값의 길이가 최소 2글자 이상 최대 30글자 이하인가.
>   5. website가 최소 1개 이상 있는가.
>
> - 만약, 하나라도 잘못된 값이 있다면 False를 반환하고, 어떤 데이터가 잘못 기록되었는지도 함께 반환한다. 2개 이상의 데이터가 잘못 되었다면 리스트 형태로 목록을 반환한다. 모두 정상이라면 True를 반환한다.
>   - 반환 예시) (False, ['blood_group', 'name'])
>   - 단, black_list에 company가 포함된 경우에는 'blocked' 를 반환하고, 검사를 종료한다.
>
> - create_user는 is_validation 함수의 반환 결과를 토대로 새로운 사용자 목록 user_list를 생성한다.
> - 이때, 반환 받은 값이 False인 경우, 잘못된 데이터에는 None을 할당하여 데이터를 생성한다.
> - 또한, 반환 받은 값이 False이거나 'blocked'인 경우를 모두 세어, '잘못된 데이터로 구성된 유저의 수는 {개수} 입니다.' 를 출력한다.
> - 단,'blocked'가 반환된 경우, 해당 유저 정보는 user_list에 추가하지 않는다.
> - 완성된 user_list를 출력한다.


- 오류 해결 내역

**validation_result 의 가능한 값은 `True, 'blocked', (False, [user_list])` 모두 자료형이 다르다.**

```python
# 처음 작성한 코드 -> TypeError
def create_user(user_data_list):
    for user in user_data_list:
        validation_result = is_validation(user)
        user_list = []
        invalid_count = 0

        # 새로운 사용자 목록 user_list 생성
        if validation_result == True:
            user_list.append(user)
        elif validation_result == 'blocked':
            invalid_count += 1
        else:
            invalid_count += 1
            # TypeError: 'bool' object is not iterable
            for invalid_data in validation_result[1]:
                user[invalid_data] = None
                user_list.append(user)
        
    print(f'잘못된 데이터로 구성된 유저의 수는 {invalid_count}입니다.')
    return user_list

def is_validation(user_data):
    is_valid = True
    invalid_list = []

    # black_list에 company가 포함된 경우에는 'blocked' 를 반환하고, 검사를 종료한다.
    if user_data['company'] in black_list:
        is_valid = False
        return 'blocked'
    
    # blood_group의 값이 blood_types에 포함되어 있는가.
    if user_data['blood_group'] not in blood_types:
        invalid_list.append('blood_group')
        is_valid = False
    # mail의 값에 @ 문자열이 포함되어 있는가.
    if '@' not in user_data['mail']:
        invalid_list.append('mail')
        is_valid = False
    # name의 값의 길이가 최소 2글자 이상 최대 30글자 이하인가.
    if len(user_data['name']) < 2 or len(user_data['name']) > 30:
        invalid_list.append('name')
        is_valid = False
    # website가 최소 1개 이상 있는가.
    if not user_data['website']:
        invalid_list.append('website')
        is_valid = False
    else:
        return is_valid
    
    return False, invalid_list

```

**→ 수정**

1. 조기 반환 로직 삭제:
    
   `def is_validation(user_data):` 내부 `else:` 문이 website 검사 부분에 물려있었다. 이 구문 때문에 조기 반환되는 경우 에러가 발생했다. 자료형이 여러 가지라서 에러가 발생했다기보다는, website 제외한 부분에서 값이 이상할 경우에 `False`가 반환되기 때문에 이 경우에 에러가 발생한 것.

2. 코드 간결화: 
   
   `def is_validation(user_data):` 에서 불필요한 상태 변수인 `is_valid`를 삭제했다. 대신 모든 검사를 마친 후, 최종적으로 `invalid_list` 가 비어있는지에 따라 유효성을 판단하는 것으로 수정했다.

```python
def create_user(user_data_list):
    user_list = []
    invalid_count = 0

    for user in user_data_list:
        validation_result = is_validation(user)

        # 새로운 사용자 목록 user_list 생성
        if validation_result == True:
            user_list.append(user)
        elif validation_result == 'blocked':
            invalid_count += 1
        else:
            invalid_count += 1
            invalid_list = validation_result[1]
            for invalid_data in invalid_list:
                user[invalid_data] = None
                user_list.append(user)
        
    print(f'잘못된 데이터로 구성된 유저의 수는 {invalid_count}입니다.')

    return user_list

def is_validation(user_data):
    invalid_list = []

    # black_list에 company가 포함된 경우에는 'blocked' 를 반환하고, 검사를 종료한다.
    if user_data['company'] in black_list:
        return 'blocked'
    
    # blood_group의 값이 blood_types에 포함되어 있는가.
    if user_data['blood_group'] not in blood_types:
        invalid_list.append('blood_group')

    # mail의 값에 @ 문자열이 포함되어 있는가.
    if '@' not in user_data['mail']:
        invalid_list.append('mail')

    # name의 값의 길이가 최소 2글자 이상 최대 30글자 이하인가.
    if len(user_data['name']) < 2 or len(user_data['name']) > 30:
        invalid_list.append('name')

    # website가 최소 1개 이상 있는가.
    if not user_data['website']:
        invalid_list.append('website')

    # 모든 검사가 끝난 후 invalid_list에 항목이 있는지 확인한다.
    if not invalid_list:
        return True
    else:
        return False, invalid_li
```



<br><br>

# 수업 필기

## 제어문

코드의 실행 흐름을 제어하는 데 사용되는 구문

조건에 따라 코드 블록을 실행하거나 반복적으로 코드를 실행

## 1. 조건문 (if)

주어진 조건식을 평가하여 해당 조건이 참(True)인 경우에만 코드 블록을 실행하거나 건너뜀

- 조건은 **표현식**으로 작성한다.
  
- `if / elif / else`
  
    - if 문이 참인 경우, 하단 elif, else 블록은 실행하지 않는다.
  
- 조건식은 ‘순차적’으로 비교하기 때문에 순서가 중요하다.

```python
# 복수 조건문
## 순서 1. 결과: 매우 나쁨
dust = 155

if dust > 150:
    print('매우 나쁨') # 출력 후 종료
elif dust > 80:
    print('나쁨')
elif dust > 30:
    print('보통')
else:
    print('좋음')

## 순서 2. # 결과: 보통
dust = 155

if dust > 30:
    print('보통') # 출력 후 종료
elif dust > 80:
    print('나쁨')
elif dust > 150:
    print('매우 나쁨')
else:
    print('좋음')
```

## 2. 반복문 (for, while)

주어진 코드 블록을 여러 번 반복해서 실행하는 구문

### for문

반복 가능(iterable)한 객체의 요소 개수만큼 반복

- 반복 **횟수**가 정해져 있다.
  
- `for 임시변수 in iterable:`
  
- iterable: 요소를 하나씩 반환할 수 있는 모든 객체
  
    - 시퀀스(list, tuple, str), 비시퀀스(dict, set)
  
    - `range(len(iterable))` 인덱스로 접근할 때 많이 사용

```python
# dictionary 순회 -> 기본적으로 key를 반환
my_dict = {
    'x': 10,
    'y': 20,
    'z': 30,
}

for key in my_dict:
    print(key, my_dict[key])
    
    
# 인덱스 순회
numbers = [4, 6, 10, -8, 5]

for i in range(len(numbers)):
    numbers[i] = numbers[i] * 2
```

- 중첩 반복문: 안쪽 for문 → 바깥쪽 for문

```python
# 중첩 반복문
outers = ['A', 'B']
inners = ['c', 'd']

for outer in outers:
    for inner in inners:
        print(outer, inner)
'''
A c
A d
B c
B d
'''
```

- 중첩 리스트

```python
# 중첩 리스트 순회
elements = [['A', 'B'], ['c', 'd']]

# 1
for elem in elements:
    print(elem)
"""
['A', 'B']
['c', 'd']
"""

# 2
for elem in elements:
    for item in elem:
        print(item)
"""
A
B
c
d
"""
```

### while문

while **조건**이 참(True)인 동안 반복. False가 되면 종료.

- 반복 횟수가 정해지지 않음 → 무한 반복 이슈 주의!
  
- 반드시 **종료 조건**이 필요하다.
  
- `while 조건식:` 조건식을 잘 짜는 것이 중요하다.

```python
# while문 작동 원리
input_value = ''
while input_value != 'exit':  # exit 를 입력하면 반복 종료
    input_value = input("Enter a value: ")
    print(input_value)
"""
Enter a value: ssafy
ssafy
Enter a value: exit
exit
"""
```

| for | while |
| --- | --- |
| iterable 요소를 하나씩 순회하며 반복 | 주어진 조건식이 참(True)인 동안 반복 |
| 반복 횟수가 정해져 있는 경우 | 반복 횟수가 불명확하거나 조건에 따라 반복을 종료해야 할 경우 |
| `for 임시변수 in iterable:`<br>list, tuple, str, dict, set, range() 등 | `while 조건식:` |


### 반복 제어 (break, continue, pass)

- `break` : 남은 코드를 무시하고 **반복 즉시 종료**
  
- `continue` : 다음 코드는 무시하고 **다음 반복을 수행**

```python
# break 키워드
for i in range(10):
	if i == 5:
		break
	print(i)  # 0 1 2 3 4

# continue 키워드
for i in range(10):
	if i % 2 == 0:
		continue
	print(i)  # 1 3 5 7 9
```

- `pass` : 코드의 틀을 유지하거나 나중에 내용을 채우기 위한 용도. ‘아무 동작도 하지 않음’을 명시적으로 나타낸다.

    - 반복문, 함수, 조건문에서 사용

### for-else / while-else

- for/while 루프가 break를 만나 중단되지 않고, 끝까지 정상적으로 완료되었을 때만 else 블록이 실행

- break 문을 만나 반복문이 종료되면 else의 코드 블록은 실행되지 않는다.
  
- 즉, break 문에 대한 else

```python
# for-else 구문 활용 1
# 중복 아이디 찾기 - 찾은 경우
registered_ids = ['admin', 'user01', 'guest', 'user02']
id_to_check = 'guest'  # 이미 리스트에 존재하는 아이디

for existing_id in registered_ids:
    if existing_id == id_to_check:
        print('이미 사용 중인 아이디입니다.')
        break  # 중복 아이디를 찾았으므로 확인 절차를 중단
else:
    # for 루프가 break로 중단되었기에 이 부분은 실행되지 않음
    print('사용 가능한 아이디입니다.')

print('아이디 확인 절차를 종료합니다.')
"""
이미 사용 중인 아이디입니다.
아이디 확인 절차를 종료합니다.
"""

# for-else 구문 활용 2
# 중복 아이디 찾기 - 찾지 못한 경우
registered_ids = ['admin', 'user01', 'guest', 'user02']
id_to_check = 'new_user'  # 리스트에 없는 새로운 아이디

for existing_id in registered_ids:
    if existing_id == id_to_check:
        print('이미 사용 중인 아이디입니다.')
        break
else:
    # for 루프가 break 없이 마무리 되어 else 블록 실행
    print('사용 가능한 아이디입니다.')
"""
사용 가능한 아이디입니다.
"""
```