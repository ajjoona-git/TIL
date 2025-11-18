# JavaScript의 데이터 타입

## 원시 자료형 (Primitive Type)

### 원시 자료형 (Primitive Type)

- **값(value) 자체**가 변수에 직접 저장되는 자료형
- **불변 (immutable)**, 즉 값의 일부를 직접 수정할 수 없다.
- 변수에 할당될 때 값이 복사되므로, 변수 간에 서로 영향을 미치지 않는다.
- Number, String, Boolean, null, undefined

```jsx
// 원시 자료형
const a = 'bar'
console.log(a) // bar

console.log(a.toUpperCase()) // BAR
console.log(a) // bar

let b = 10
let c = b
c = 20
console.log(b) // 10
console.log(c) // 20
```

### Number

- 정수 또는 실수형 숫자
- 문자열과 + 연산 시, 숫자가 문자열로 자동 형 변환되어 연결
- 정수와 실수의 구분이 없고, 모든 숫자를 단일 타입으로 처리한다.

```jsx
// number
const a = 13 
const b = -5 
const c = 3.14 
const d = 2.998e8
const e = Infinity 
const f = -Infinity
const g = NaN

const k = 13.0
console.log(a == k)  // true
console.log(a === k)  // true
console.log(0.1 + 0.2)  // 0.30000000000000004
```

### String

- 텍스트 데이터를 표현하는 자료형
- `+` 연산자를 사용해 문자열끼리 결합
- 뺄셈, 곱셈, 나눗셈 불가능

```jsx
// string
const firstName = 'Tony'
const lastName = 'Stark'
const fullName = firstName + lastName  // + 로 문자열 결합 가능
console.log(fullName) // Tony Stark
```

### Template Literals (템플릿 리터럴)

- 내장된 표현식을 허용하는 향상된 문자열 저장 방식
- 백틱(```)을 사용하여 여러 줄에 걸쳐 문자열을 정의하고, JavaScript의 변수를 문자열 안에 바로 연결 가능
    - 파이썬의 f-string
- 표현식은 `$`와 중괄호 (`{expression}`)로 표기

```jsx
// 템플릿 리터럴(Template literals)
const age = 100 
const message = `홍길동은 ${age}세입니다.`
console.log(message) // 홍길동은 100세입니다.
```

### null 과 undefined

- **null**: 프로그래머가 의도적으로 **‘값이 없음’**을 나타낼 때 사용
    - null 의 타입은 object (역사적인 이유)
    - 산술 연산 시 0으로 취급된다.
- **undefined**: 시스템이나 JavaScript 엔진이 **‘값이 할당되지 않음’**을 나타낼 때 사용
    - return이 없는 함수나 인자가 전달되지 않은 매개변수는 기본적으로 undefined가 할당된다.
    - 산술 연산 시 계산 불가능한 NaN 값을 만든다.
- (참고) NaN: ‘숫자가 아님’이라는 뜻
    - `NaN === NaN  // false`: 자기자신과 비교해도 false가 나오는 유일한 값
    - ‘숫자가 아님’이라는 뜻이지만, 타입을 확인하면 ‘number’가 반환된다.

```jsx
// null(값이 없음을 의도적으로 나타냄)
let x = null
console.log(x) // null
console.log(typeof x)  // object
console.log(10 + x)  // 10

// undefined(값이 할당되지 않은 상태)
let y 
console.log(y)  // undefined
console.log(typeof y)  // undefined
console.log(10 + y)  // NaN
```

### Boolean

- 참과 거짓을 나타내는 논리적인 자료형

```jsx
// boolean(true, false)
let m = true
let n = false
console.log(typeof m)  // boolean
console.log(10 > 5)  // true
console.log(10 < 5)  // false
```

### 자동 형변환 규칙

- 조건문 또는 반복문에서 Boolean이 아닌 데이터 타입은 **자동 형변환 규칙**에 따라 true 또는 false로 변환된다.
- 결국 false ⇒ 0, “”, null, undefined, NaN 이외의 모든 값은 true로 평가된다.
- 하지만 헷갈리니까,, 암묵적인 변환보다는 명시적인 게 좋다!

| 데이터 타입 | false | true |
| --- | --- | --- |
| undefined | 항상 false | - |
| null | 항상 false | - |
| Number | 0, -0, NaN | 나머지 모든 경우 |
| String | '’ (빈 문자열) | 나머지 모든 경우 |

```jsx
console.log(Boolean(0));  // false
console.log(Boolean(10));  // true
console.log(Boolean(NaN));  // false

console.log(Boolean(""));  // false
console.log(Boolean("hello"));  // true
console.log(Boolean("0"));  // true

console.log(Boolean(null));  // false
console.log(Boolean(undefined));  //false
console.log(Boolean([]));  // true
console.log(Boolean({}));  // true
```

### 💡 Truthy와 Falsy (참/거짓 같은 값)

JavaScript에서 **Falsy (거짓 같은 값)**로 취급되는 값

- `false`
- `0` (숫자 0)
- `0` (마이너스 0)
- `0n` (BigInt 0)
- `""` (빈 문자열)
- `null`
- `undefined`
- `NaN` (Not a Number)

**Truthy (참 같은 값)**는 Falsy가 아닌 **모든 값**

- 예: `13`, `"hello"`, `[]`(빈 배열), `{}`(빈 객체), `true` 등

## 참조 자료형 (Reference Type)

### 참조 자료형 (Reference Type)

- 데이터가 저장된 **메모리의 주소가 변수에 저장**되는 자료형
- **가변 (mutable)**이며, 변수 간 할당 시 주소가 복사된다.
- 복사본을 수정하면 원본의 값도 함께 변경될 수 있다.
- Objects(Object, Array, Function)

```jsx
// 참조 자료형
const arr1 = [1, 2, 3]
const arr2 = arr1
arr2.push(4)

console.log(arr1) // [1, 2, 3, 4]
console.log(arr2) // [1, 2, 3, 4]

const obj1 = { name: 'Alice', age: 30 }
const obj2 = obj1

obj2.age = 40

console.log(obj1.age) // 40
console.log(obj2.age) // 40
```

### Function

- 참조 자료형에 속하며, 모든 함수는 Function object