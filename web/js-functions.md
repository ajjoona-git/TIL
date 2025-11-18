# JavaScript의 함수

## 함수

### 함수 정의

- return 문이 없거나 return 뒤에 값이 없으면, `undefined`를 반환한다.
- **선언식 (function declaration)**
    - 호이스팅된다 (negative)
    - 코드의 구조와 가독성
- **[권장] 표현식 (function expression)**: 함수를 변수에 할당
    - 호이스팅의 영향을 받지 않는다.
    - 변수 선언만 호이스팅되고 함수 할당은 실행 시점에 이루어진다.
    - 함수 이름이 없는 ‘익명 함수’를 사용할 수 있다.
    - 블록 스코프를 가지는 let이나 const와 함께 사용하여 더 엄격한 스코프 관리가 가능하다.

```jsx
// 선언식
function add (num1, num2) {
	return num1 + num2
}
add(1, 2)  // 3

// 표현식
const sub = function (num1, num2) {
	return num1 - num2
}
sub(2, 1)  // 1
```

### 매개변수

- 기본 함수 매개변수 (Default function parameter)
    - 함수 호출 시 인자를 전달하지 않거나 undefined를 전달할 경우, 지정된 기본 값으로 매개변수를 초기화
- 나머지 매개변수 (Rest parameter) `...`
    - 정해지지 않은 개수의 인자들을 배열로 모아서 받는 방법
    - 함수 정의 시 나머지 매개변수는 **마지막 위치에, 하나만** 작성할 수 있다.

```jsx
// 기본 함수 매개변수
const greeting = function (name = 'Anonymous') {
 return `Hi ${name}`
}

greeting() // Hi Anonymous

// 나머지 매개변수 
const myFunc = function (param1, param2, ...restPrams) {
  return [param1, param2, restPrams]
}

myFunc(1, 2, 3, 4, 5) // [1, 2, [3, 4, 5]]
myFunc(1, 2)  // [1, 2, []]
```

### 매개변수와 인자 개수가 불일치할 때

- 매개변수 > 인자: 누락된 인자는 undefined로 할당
- 매개변수 < 인자: 초과 입력한 인자는 사용하지 않음

```jsx
// 매개변수 > 인자 (나머지는 undefined 할당)
const threeArgs = function (param1, param2, param3) {
  return [param1, param2, param3]
}

threeArgs() // [undefiend, undefiend, undefiend]
threeArgs(1) // [1, undefiend, undefiend]
threeArgs(2, 3) // [2, 3, undefiend]

// 매개변수 < 인자 ( 넘치면 사용하지 않음 ) 
const noArgs = function () {
  return 0
}
noArgs(1, 2, 3) // 0

const twoArgs = function (param1, param2) {
  return [param1, param2]
}
twoArgs(1, 2, 3) // [1, 2]
```

### Spread syntax `...`

- 배열이나 문자열처럼 반복 가능한(iterable) 항목들을 개별 요소로 펼치는 것
- 전개 대상에 따라 역할이 다르다.
    - 배열이나 객체의 요소를 개별적인 값으로 분리하거나 다른 배열이나 객체의 요소를 현재 배열이나 객체에 추가하는 등
- 활용처:
    - 함수와의 사용: 함수 호출 시 인자 확장, 나머지 매개변수 (압축)
    - 객체와의 사용
    - 배열과의 사용

```jsx
// 함수 호출 시 인자 확장
function myFunc(x, y, z) {
  return x + y + z
}

let numbers = [1, 2, 3]
console.log(myFunc(...numbers)) // 6

// 나머지 매개변수의 압축 용도로 활용
function myFunc2(x, y, ...restArgs) {
  return [x, y, restArgs]
}
console.log(myFunc2(1, 2, 3, 4, 5)) // [1, 2, [3, 4, 5]]
console.log(myFunc2(1, 2)) // [1, 2, []]
```

### 화살표 함수 표현식 (Arrow Function Expressions)

- 함수 표현식의 간결한 표현법
- `function` 키워드 제거 후 매개변수와 중괄호 사이에 화살표(`=>`) 작성
- 함수 본문의 표현식이 한 줄이라면, `{}`와 `return` 제거 가능

```jsx
// 원래 함수 작성법
const arrow1 = function (name) {
	return `hello, ${name}`
}

// 화살표 함수 표현식
const arrow2 = (name) => { return `hello, ${name}` }
const arrow3 = name => { return `hello, ${name}` }
const arrow4 = name => `hello, ${name}`

// 1. 인자가 없다면 () or _ 로 표시 가능
const noArgs1 = () => 'No args'
const noArgs2 = _ => 'No args'

// 2-1. object를 return 한다면 return 을 명시적으로 작성해야 함
const returnObject1 = () => { return { key: 'value' } }

// 2-2. return을 작성하지 않으려면 객체를 소괄호로 감싸야 함
const returnObject2 = () => ({ key: 'value' })
```