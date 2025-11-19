# JavaScript의 객체

## 객체 (Object)

### 구조 및 속성

- `{key: value,}`
    - key는 문자형만 허용
    - value는 모든 자료형 허용 (함수도 가능)
- 점(`.`) 표기법 또는 대괄호(`[]`) 표기법으로 객체 속성에 접근
    - key 이름에 띄어쓰기 같은 구분자가 있으면 대괄호 접근만 가능

```jsx
const user = {
  name: 'Alice',
  'key with space': true,
  greeting: function () {
    return 'hello'
  }
}

// 조회
console.log(user.name) // Alice
// console.log(user.'key with space')
console.log(user['key with space']) // true

// 추가
user.address = 'korea'
console.log(user) // {name: 'Alice', key with space: true, address: 'korea', greeting: ƒ}

// 수정
user.name = 'Bella'
console.log(user.name) // Bella

// 삭제
delete user.name
console.log(user) // {key with space: true, address: 'korea', greeting: ƒ}

// 1. 객체 표기법 
// 점 표기법: 정적인 변수
// 대괄호 표기법: 동적인 변수
const user = { name: "Alice", age: 30 };

for (let key in user) {
    console.log(user.key); // undefined 
    console.log(user[key]); // "Alice", 30
}
```

- `in` 연산자: 속성이 객체에 존재하는지 여부를 확인
    - 객체에서 값의 포함 여부를 확인하려면 `hasOwnProperty()` 메서드를 사용

```jsx
// 2. in 연산자 (key 값이 object에 들어있는지를 알 수 있다)
const user2 = { name: "Alice" };

console.log("name" in user2);  // true
console.log("toString" in user2);  // true

// 방법 1 (Classic): .hasOwnProperty()
console.log(user.hasOwnProperty("name"));     // true
console.log(user.hasOwnProperty("toString")); // false (이건 조상님 꺼!)

// 방법 2 (ES2022): Object.hasOwn()
// Object.create() 로 객체를 생성한 경우, hasOwnProperty 속성이 없을 수 있음 => 에러 
console.log(Object.hasOwn(user, "name"));     // true
console.log(Object.hasOwn(user, "toString")); // false
```

### Method

- `object.method()`
- 객체 속성에 정의된 함수
- 메서드는 객체가 행동할 수 있게 한다.
- 메서드는 자신이 속한 객체의 다른 속성들에 접근할 수 있다.
    - 이를 위한 방법이 `this` (파이썬 class의 self)

### this

- 함수나 메서드를 호출한 객체를 가리키는 키워드
- `this` 키워드를 사용해 객체에 대한 특정한 작업을 수행할 수 있다.
- 함수를 **호출하는 방법**에 따라 this가 가리키는 대상이 동적으로 결정된다.
    - 함수(메서드)를 하나만 만들어 여러 객체가 공유하여 각자 자신의 데이터로 동작하게 할 수 있다.

| 호출 방법 | this가 가리키는 대상 |
| --- | --- |
| 일반 함수에서의 단순 호출 | 전역 객체 (JS가 실행되는 환경, 최상위 객체) |
| 객체에서의 메서드 호출 | 메서드를 호출한 객체 |

```jsx
// 1.1 단순 호출
const myFunc = function () {
  return this
}
console.log(myFunc()) // window

// 1.2 메서드 호출
const myObj = {
  data: 1,
  myFunc: function () {
    return this
  }
}
console.log(myObj.myFunc()) // myObj
```

- 중첩된 함수에서의 this
    - 문제점: `forEach`의 인자로 전달된 콜백 함수는 일반 함수로 호출되므로, this는 전역 객체를 가리킨다.
    - 해결책: **화살표 함수는 자신만의 this를 가지지 않는다.** 따라서 외부 함수(`myFunc`)에서의 this 값을 가져온다.

```jsx
// 2. 중첩된 함수
// 2.1 일반 함수
const myObj2 = {
  numbers: [1, 2, 3],
  myFunc: function () {
    this.numbers.forEach(function (number) {
      console.log(this) // window (전역 변수)
    })
  }
}

// 2.2 화살표 함수
const myObj3 = {
  numbers: [1, 2, 3],
  myFunc: function () {
    this.numbers.forEach((number) => {
      console.log(this) // myObj3
    })
  }
}
```

### 단축 속성

- 키 이름과 값으로 쓰이는 변수의 이름이 같은 경우, 단축 구문을 사용할 수 있다.

```jsx
// 1. 단축 속성
const name = 'Alice'
const age = 30

// 단축 속성 전
const user = {
	name: name,
	age: age
}

// 단축 속성 후
const user = {
  name, age
}
```

### 단축 메서드

- 메서드 선언 시 function 키워드 생략 가능

```jsx
// 2. 단축 메서드

// 단축 메서드 전 
	const myObj1 = {
	myFunc: function () {
		return 'Hello'
	}
}

// 단축 메서드 후 
const myObj1 = {
  myFunc() {
    return 'Hello'
  }
}
```

### 계산된 속성 (Computed Property Name)

- 키가 대괄호로 둘러싸여 있는 속성
- 고정된 값이 아닌 변수 값을 사용할 수 있다.
- 대괄호 안의 표현식이 너무 복잡해지면, 가독성이 떨어질 수 있다.
- 동적으로 키를 만들다보면 의도치 않게 같은 이름의 키가 생성되어 (unique하지 않음), 기존 값이 덮어써질 위험이 있다.

```jsx
// 3. 계산된 속성
const product = prompt('물건 이름을 입력해주세요')
const prefix = 'my'
const suffix = 'property'

const bag = {
  [product]: 5,
  [prefix + suffix]: 'value'
}

console.log(bag) // {연필: 5, myproperty: 'value'}
```

### 구조 분해 할당 (Destructing Assignment)

- 배열 또는 객체를 분해하여 객체 속성을 변수에 쉽게 할당할 수 있는 문법
- ‘함수의 매개변수’로 객체 구조 분해 할당 활용 가능

```jsx
// 4. 구조 분해 할당
const userInfo = {
  firstName: 'Alice',
  userId: 'alice123',
  email: 'alice123@gmail.com'
}

// 구조 분해 할당 전 
// const firstName = userInfo.firstName
// const userId = userInfo.userId
// const email = userInfo.email

// 구조 분해 할당 후 
// const { firstName } = userInfo
// const { firstName, userId } = userInfo
const { firstName, userId, email } = userInfo

// 구조 분해 할당 활용 - 함수 매개변수
// 구조 분해 할당 활용 전 
function printInfo(userInfo) {
  console.log(`이름: ${userInfo.firstName}, 나이: ${userInfo.age}, 도시: ${userInfo.city}`)
}
printInfo(userInfo)

// 구조 분해 할당 활용 후
function printInfo({ firstName, email }) {
  console.log(`이름: ${firstName}, 이메일: ${email}`)
}
printInfo(userInfo)
```

### 객체와 전개 구문 (Spread Syntax, `...`)

- 객체 복사: 객체 내부에서 객체 전개
- 얕은 복사에 활용 가능

```jsx
// 5. 전개 구문
const obj = { a: 2, c: 3, d: 4 }
const newObj = {...obj, a: 1,  e: 5 }
console.log(newObj) // {a: 1, b: 2, c: 3, d: 4, e: 5}
```

### 유용한 객체 메서드

- `Object.keys()`: Object의 Key 값들을 리스트로 반환
- `Object.values()`: Object의 Value 값들을 리스트로 반환
- `Object.entries()`: Object의 Key와 Value 값들을 한 쌍으로 묶은 리스트로 반환

```jsx
// 6. 유용한 객체 메서드
const profile = {
  name: 'Alice',
  age: 30
}

console.log(Object.keys(profile)) // ['name', 'age']
console.log(Object.values(profile)) // ['Alice', 30]
console.log(Object.entries(profile)) // [['name', 'Alice'], ['age', 30]]
```

### Optional Chaining (`?.`)

- 속성이 없는 중첩 객체에 접근하려 할 때, 에러 발생없이 안전하게 접근하는 방법
- 만약 참조 대상이 **null 또는 undefined**라면 에러가 발생하는 것 대신, 평가를 멈추고 undefined를 반환
    - 참조가 누락될 가능성이 있는 경우 연결된 속성으로 접근할 때, 더 간단한 표현식을 작성할 수 있다.
- optional chaining 앞의 변수는 반드시 선언되어 있어야 한다.
- 체인 중간이 null인 경우, 그 뒤의 코드는 실행되지 않는다. (단락 평가)
- optional chaining은 존재하지 않아도 괜찮은 대상에만 사용해야 한다. (**남용하지 말 것**)
    - 왼쪽 평가대상이 없어도 괜찮은 경우에만 선택적으로 사용
    - 중첩 객체를 에러 없이 접근하는 것이 사용 목적이기 때문

```jsx
// 7. Optional Chaining
const userData = {
  name: 'Alice',
  greeting: function () {
    return 'hello'
  }
}

// 예전 방식: 단축 평가 활용
console.log(userData.address && userData.address.street) // undefined

// 변수 옵셔널 체이닝 
console.log(userData.address.street) // Uncaught TypeError: Cannot read properties of undefined (reading 'street')
console.log(userData.address?.street) // undefined

// 함수 옵셔널 체이닝 
console.log(userData.nonMethod()) // Uncaught TypeError: user.nonMethod is not a function
console.log(userData.nonMethod?.()) // undefined

// 위 예시 코드 논리상 user는 반드시 있어야 하지만 address는 필수 값이 아님
// user에 값을 할당하지 않은 문제가 있을 때 바로 알아낼 수 있어야 하기 때문
// Bad
userData?.address?.street

// Good 
userData.address?.street
```

- `obj?.prop`: obj가 존재하면 obj.prop을 반환하고, 그렇지 않으면 undefined를 반환
- `obj?.[prop`]: obj가 존재하면 obj[prop]을 반환하고, 그렇지 않으면 undefined를 반환
- `obj?.method()`: obj가 존재하면 obj.method()를 호출하고, 그렇지 않으면 undefined를 반환

### JSON (JavaScript Object Notation)

- key-value 형태로 이루어진 자료 표기법 (“**문자열**” 타입)
- JavaScript에서 JSON을 사용하기 위해서는 Object 자료형으로 변경해야 한다.
    - Object → JSON: `JSON.stringfy()` 를 사용해 객체를 문자열로 변환
    - JSON → Object: `JSON.parse()` 를 사용해 문자열을 객체로 변환

```jsx
const jsObject = {
  coffee: 'Americano',
  iceCream: 'Cookie and cream'
}

// Object -> JSON
const objToJson = JSON.stringify(jsObject)
console.log(objToJson)  // {"coffee":"Americano","iceCream":"Cookie and cream"}
console.log(typeof objToJson)  // string

// JSON -> Object
const jsonToObj = JSON.parse(objToJson)
console.log(jsonToObj)  // { coffee: 'Americano', iceCream: 'Cookie and cream' }
console.log(typeof jsonToObj)  // object
```

---

## 참고

### 클래스 (class)

- 객체를 생성하기 위한 템플릿
- 객체의 속성, 메서드를 정의
- `class` 호이스팅되지만, 선언 전에 접근하면 에러가 발생한다. (TDZ)
    - TDZ (Temporal Dead Zone): let, const 선언 전, 변수 접근을 막는 일시적 사각지대
- 클래스 이름은 파스칼 케이스 (PascalCase)로 작성
- 생성자 메서드 (`constructor()`): 속성 값의 초기 설정을 담당
    - `new`로 객체 생성 시 자동으로 호출된다.
    - `constructor`라는 이름을 가진 메서드가 단 하나만 존재할 수 있다.
- `new`연산자: 클래스나 생성자 함수를 사용하여 새로운 객체를 생성
    - new 없이 클래스를 호출하면 TypeError 발생

```jsx
// 클래스
class Member {
  constructor(name, age) {
    this.name = name
    this.age = age
  }
  sayHi() {
    console.log(`Hi, I am ${this.name}`)
  }
}

const member1 = new Member('Alice', 20)

console.log(member1) // Member { name: 'Alice', age: 20 }
console.log(member1.name) // Alice
member1.sayHi() // Hi I am Alice
```

### **🧐 세미콜론(;)의 사용 규칙 (ASI)**

JavaScript에서 세미콜론(`;`)은 **명령문(statement)의 끝**을 나타냅니다. 코드를 해석할 때 왜 언제는 세미콜론을 쓰고 언제는 안 쓰는지에 대한 의문은 JavaScript의 **자동 세미콜론 삽입 (Automatic Semicolon Insertion, ASI)**이라는 메커니즘 때문입니다.

**1. 세미콜론을 사용하는 경우 (권장)**

대부분의 **단일 명령문** 끝에는 세미콜론을 붙이는 것이 **일관성과 안정성** 측면에서 가장 좋은 방법이며, 이는 **명령문의 끝**을 명확히 합니다.

• 변수 선언: `const x = 10;`
• 표현식: `a = b + c;`
• 함수 호출: `console.log(x);`

**2. 세미콜론을 생략하는 경우**

ASI 규칙에 따라 세미콜론이 **자동으로 삽입되는** 경우가 있습니다.

**A. 블록문 `{}`의 끝**

`if`, `for`, `function` 등의 **블록문**이 닫히는 중괄호(>}</ 뒤에는 세미콜론을 사용하지 않습니다.

• `if (true) { console.log('Hi') }` **(세미콜론 없음)**
• `students.forEach((book) => { availableBooks.push(book.title) })` **(닫는 괄호 뒤에 세미콜론 없음)**

**B. 다음 명령문이 새 줄에 시작할 때**

JavaScript 엔진은 **명령문이 끝났다고 판단될 때** (주로 줄 바꿈이 있을 때) 세미콜론을 자동으로 삽입합니다.

• `const availableBooks = []` (엔진이 이 줄 끝에 `;`를 자동 삽입)
• `library.books.forEach((book) => { ... })` (엔진이 이 줄 끝에 `;`를 자동 삽입)

**🚨 ASI의 위험성 (세미콜론을 생략하면 안 되는 이유)**

| **상황** | **오류 발생 코드** | **해석** |
| --- | --- | --- |
| **줄 시작이 괄호일 때** | `return` **줄 바꿈** `x + y;` | 엔진은 `return;`으로 해석하고 `x+y`는 실행되지 않습니다. (의도: `return (x+y);`) |
| **즉시 실행 함수 (IIFE)** | `const a = 5` **줄 바꿈** `(function() { ... })()` | `5(function() { ... })()`로 해석하여 **함수가 아닌 값**을 함수처럼 호출하려 시도하는 오류 발생. |

**결론적으로, JavaScript에서는 ASI 규칙이 있지만, 대부분의 개발자는 예상치 못한 오류를 방지하고 코드의 일관성을 위해 블록문( `{}` ) 뒤를 제외한 모든 명령문 끝에 세미콜론을 명시적으로 사용할 것을 권장합니다.**
