# JavaScript의 조건문과 반복문

## 조건문

### if

- 조건 표현식의 결과값을 boolean 타입으로 변환 후 참/거짓을 판단

```jsx
// if 문
const name = 'customer'

if (name === 'admin') {
  console.log('관리자님 환영해요')
} else if (name === 'customer') {
  console.log('고객님 환영해요')
} else {
  console.log(`반갑습니다. ${name}님`)
}
```

### 삼항 연산자

- 간단한 조건부 로직을 간결하게 표현할 때 유용
- `condition ? expression1 : expression2`
    - condition: 평가할 조건 (true 또는 false)
    - expression1: 조건이 **true**일 경우 반환할 값 또는 표현식
    - expression2: 조건이 **false**일 경우 반환할 값 또는 표현식

```jsx
// 삼항 연산자
// 조건이 2개가 넘어가면 가급적 if 문을 쓰자!
const age = 20
const message = (age >= 18) ? '성인' : '미성년자'
console.log(message) // '성인'
```

## 반복문

### while

- 조건문이 참이면 문장을 계속해서 수행

```jsx
// while
while (조건문) {
	// do something
}

let i = 0

while (i < 6) {
  console.log(i)
  i += 1
} // 0 1 2 3 4 5
```

### for

- 특정한 조건이 거짓으로 판별될 때까지 반복
- 초기문의 변수 i는 `let`으로 설정
    - 최초 정의한 **i를 재할당**하면서 사용하기 때문
    - 변수 i는 기본적으로 block scope 이기 때문에 for문 이외의 공간에서 i를 출력하면 error가 발생한다.

```jsx
// for
for ([초기문]; [조건문]; [증감문]) {
	// do something
}

for (let i = 0; i < 6; i++) {
  console.log(i)
} // 0 1 2 3 4 5

console.log(i)  // ReferenceError: i is not defined
```

### for … in

- **객체(object, key-value 형식)**의 열거 가능한(enumerable) 속성(property)의 **키(key)**에 대해 반복
- 실무에서 잘 안쓰인다…

```jsx
// for...in
for (variable in object) {
	// statement
}

const fruits = {
  a: 'apple',
  b: 'banana'
}

for (const property in fruits) {
  console.log(property)  // a, b
  console.log(fruits[property])  // apple, banana
}
```

### for … of

- **반복 가능한(iterable)** 객체(**배열, 문자열** 등)의 **값(value)**에 대해 반복

```jsx
// for...of
for (variable of iterable) {
	statement
}

const numbers = [0, 1, 2, 3]
for (const number of numbers) {
  console.log(number) // 0, 1, 2, 3
}

const myStr = 'apple'
for (const str of myStr) {
  console.log(str) // a, p, p, l, e
}
```

### for … in 과 for … of

- 매 반복마다 다른 속성 이름이 변수에 지정되는 것이므로 const를 사용해도 에러가 발생하지 않는다.
    - 단, const의 경우 블록 내부에서 변수를 수정할 수 없다.

|  | `for … in` | `for … of` |
| :---: | :---: | :---: |
| 반복 대상 | 객체 (enumerable) | 배열, 문자열 (iterable) |
| 반환 | 키 key | 값 value |

```jsx
// for...in 과 for...of 의 차이
const arr = ['a', 'b', 'c']

for (const i in arr) {
  console.log(i) // 0, 1, 2 (type: String)
}

for (const i of arr) {
  console.log(i) // a, b, c
}
```

- `for … in`을 배열에서도 사용할 수 있지만, 순서에 따라 인덱스를 반환하는 것을 보장할 수 없기 때문에 사용하지 않음.
    - 배열의 인덱스를, ‘문자열’로 반환
    - 내부적으로 `for … in`은 배열의 반복자가 아닌 속성 열거를 사용하기 때문
    - 배열의 프로토타입에 추가된 속성까지 순회할 수 있어, 예기치 않은 버그를 유발할 수 있다.