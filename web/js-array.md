# JavaScript의 배열

## 배열 (Array)

### 배열 구조

- 대괄호 (`[]`)를 이용해 작성
- 요소의 자료형은 제약 없음
- `length` 속성: 배열에 담긴 요소 개수 확인 가능

```jsx
const names = ['Alice', 'Bella', 'Cathy']

console.log(names[0]) // Alice
console.log(names[1]) // Bella
console.log(names[2]) // Cathy

// 길이
console.log(names.length) // 3

// 수정
names[1] = 'Dan'
console.log(names)
```

### 배열 주요 메서드

- 아래 메서드 모두 원본 배열을 직접 수정한다.

| 메서드 | 설명 | 반환 값 | 비고 |
| --- | --- | --- | --- |
| `push()` | 배열 끝에 요소를 추가 | 추가된 후의 새로운 배열의 길이 |  |
| `pop()` | 배열 끝 요소를 제거 | 제거한 요소 |  |
| `unshift()` | 배열 앞에 요소를 추가  | 추가된 후의 새로운 배열의 길이 | 배열의 모든 요소를 뒤로 한 칸씩 밀어야 하므로, 배열이 클수록 성능이 저하된다. (가급적 사용 X) |
| `shift()` | 배열 앞 요소를 제거하고 제거한 요소를 반환 | 제거한 요소 | 배열의 모든 요소를 당겨와야 하므로, 배열이 클수록 성능이 저하된다. (가급적 사용 X) |

```jsx
const names = ['Alice', 'Bella', 'Cathy']

// pop
console.log(names.pop()) // Cathy
console.log(names) // ['Alice', 'Bella']

// push
names.push('Dan')
console.log(names) // ['Alice', 'Bella', 'Dan']

// shift
console.log(names.shift()) // Alice
console.log(names) // ['Bella', 'Dan']

// unshift
names.unshift('Eric')
console.log(names) // ['Eric', 'Bella', 'Dan']
```

## Array Helper Method

### Array Helper Methods

- 배열 조작을 보다 쉽게 수행할 수 있는 특별한 메서드 모음
    - 예: forEach(), map(), filter(), reduce(), some() 등
- 배열의 각 요소를 순회하며 각 요소에 대해 **콜백함수를 호출**한다.
    - 메서드 호출 시 인자로 콜백함수를 받는 것이 특징

### 콜백함수 (Callback Function)

- 다른 함수에 인자로 전달되는 함수
- 외부 함수 내에서 호출되어 일종의 루틴이나 특정 작업을 진행한다.
    - 특정 작업이 완료된 후, 시스템에 의해 나중에 호출(callback)된다.

```jsx
// 콜백함수 예시 1
const numbers = [1, 2, 3]
numbers.forEach(function (num) {
  console.log(num)
})
// 1
// 2
// 3

// 콜백함수 예시 2
const callBackFunction = function (num) {
  console.log(num)
}
numbers.forEach(callBackFunction)
// 1
// 2
// 3
```

- **함수 유연성**: 함수를 호출하는 코드에서 콜백함수의 동작을 자유롭게 변경할 수 있다.
- **비동기**

```jsx
const numbers = [1, 2, 3, 4];

// 콜백 함수 1: 각 요소를 두 배로 만드는 함수
const double = function (number) {
return number * 2;
};

// 콜백 함수 2: 각 요소를 제곱하는 함수
const square = function (number) {
return number * number;
};

// 1. double 콜백을 사용
const doubledNumbers = numbers.map(double);
console.log(doubledNumbers); // 출력: [2, 4, 6, 8]

// 2. square 콜백을 사용
const squaredNumbers = numbers.map(square);
console.log(squaredNumbers); // 출력: [1, 4, 9, 16]
```

```jsx
// 비동기적 측면
console.log('a')

setTimeout(() => {
  console.log('b')
}, 3000)

console.log('c')

// 출력 결과
// a
// c
// b
```

### forEach

- 배열 내의 모든 요소 각각에 대해 함수(콜백함수)를 호출
- **반환 값이 없다. (undefined)**
    - Array를 **탐색**하는 것이 목적
- `arr.forEach(callback(item[, index[, array]]))`
    - `item`: 처리할 배열의 요소 (`{}`덩어리 하나의 변수명이라고 생각)
    - `index`: (선택) 처리할 배열 요소의 인덱스
    - `array`: (선택) forEach를 호출한 배열

```jsx
// forEach
// 일반 함수 표기
const names = ['Alice', 'Bella', 'Cathy']
names.forEach(function (name) {
  console.log(name)
})
// Alice
// Bella
// Cathy

// 화살표 함수 표기 (권장)
names.forEach((name) => {
  console.log(name)
})
// Alice
// Bella
// Cathy

// 활용
const result = names.forEach(function (name, index, array) {
  console.log(`${name} / ${index} / ${array}`)
  return 'aaa'
})
console.log(result)
// Alice / 0 / Alice,Bella,Cathy
// Bella / 1 / Alice,Bella,Cathy
// Cathy / 2 / Alice,Bella,Cathy
// undefined
```

- forEach에서는 break 키워드를 사용할 수 없다.
- 대신 some과 every의 특징을 활용해 break를 흉내낼 수 있다.
    - some: 콜백함수가 true를 반환하면 즉시 순회를 중단
    - every: 콜백함수가 false를 반환하면 즉시 순회를 중단

```jsx
// [forEach를 break 하는 대안]
// some과 every의 특징을 이용하여 마치 forEach에서 break를 사용하는 것처럼 구현할 수 있음
const names = ['Alice', 'Bella', 'Cathy']

// 1. some
// - 콜백 함수가 true를 반환하면 some 메서드는 즉시 중단하고 true를 반환
names.some(function (name) {
  console.log(name) // Alice, Bella
  if (name === 'Bella') {
    return true
  }
  return false
})

// 2. every
// - 콜백 함수가 false를 반환하면 every 메서드는 즉시 중단하고 false를 반환
names.every(function (name) {
  console.log(name) // Alice, Bella
  if (name === 'Bella') {
    return false
  }
  return true
})
```

### map

- 배열 내의 모든 요소 각각에 대해 함수(콜백함수)를 호출하고, 반환된 함수 호출 결과를 모아 **새로운 배열을 반환**한다.
    - Array를 **탐색하고 재가공**하는 것이 목적
- `arr.map(callback(item[, index[, array]]))`
- map() 은 배열 반환이라는 의도가 명확하기 때문에, for문보다 코드가 간결하고 직관적
- 새로운 배열을 반환하므로, 다른 메서드를 체이닝할 수 있다.

```jsx
// map 
// 1. for...of 와 비교
const persons = [
  { name: 'Alice', age: 20 },
  { name: 'Bella', age: 21 }
]

// 1.1 for...of
let result1 = []
for (const person of persons) {
  result1.push(person.name)
}
console.log(result1) // ['Alice', 'Bella']

// 1.2 map
const result2 = persons.map(function (person) {
  return person.name
})
console.log(result2) // ['Alice', 'Bella']

// 2. 화살표 함수 표기
const result3 = names.map(function (name) {
  return name.length
})
console.log(result3) // [5, 5, 5]

const result4 = names.map((name) => {
  return name.length
})
console.log(result4) // [5, 5, 5]
```

- 커스텀 콜백 함수를 변수에 담아두면, map 외 다른 곳에서도 활용할 수 있다.
    - map이나 forEach에 활용하는 콜백함수는 인자 설정할 때 객체임을 고려할 것

```jsx
// 3. 커스텀 콜백 함수
const numbers = [1, 2, 3]

const myCallbackFunc = function (number) {
  return number * 2
}
const doubleNumber = numbers.map(myCallbackFunc)
console.log(doubleNumber) // [2, 4, 6]
```

### 배열 순회

| 방식 | 특징 | break, continue | 비고 |
| --- | --- | --- | --- |
| `for loop` | 배열의 인덱스를 이용하여 각 요소에 접근 | 사용 가능 |  |
| `for … of` | 배열 요소에 바로 접근 가능 | 사용 가능 |  |
| `forEach` | 간결하고 가독성이 높음
callback 함수를 이용하여 각 요소를 조작하기 용이 | 사용 불가 | 사용 권장 |

### 기타 Array Helper Methods

| 메서드 | 역할 |
| --- | --- |
| `filter` | 콜백 함수의 반환 값이 참인 요소들만 모아서 새로운 배열을 반환 |
| `find` | 콜백함수의 반환 값이 참이면 해당 요소를 반환 |
| `some` | 배열의 요소 중 적어도 하나라도 콜백함수를 통과하면 true를 반환하며, 즉시 배열 순회 중지
모두 통과하지 못하면 false를 반환 |
| `every` | 배열의 모든 요소가 콜백함수를 통과하면 true를 반환,
하나라도 통과하지 못하면 즉시 false를 반환하고 배열 순회 중지 |

```jsx
const array = [1, 2, 3, 4, 5]

// some
// - 배열의 요소 중 적어도 하나라도 콜백 함수를 통과하는지 테스트
// - 콜백 함수가 배열 요소 적어도 하나라도 참이면 true를 반환하고 순회 중지
// - 그렇지 않으면 false를 반환
const isEvenNumber = array.some(function (element) {
  return element % 2 === 0
})

console.log(isEvenNumber) // true

// every
// - 배열의 모든 요소가 콜백 함수를 통과하는지 테스트
// - 콜백 함수가 모든 배열 요소에 대해 참이면 true를 반환
// - 그렇지 않으면 false를 반환하고 순회 중지

const isAllEvenNumber = array.every(function (element) {
  return element % 2 === 0
})

console.log(isAllEvenNumber) // false
```

### 전개 구문

- `...`은 배열의 괄호를 없애고 내용물만 꺼내기 때문에, 배열을 합치거나 중간에 삽입할 때 유용하다.
- 전개구문은 항상 새로운 배열을 만든다. 원본 배열은 전혀 변경되지 않는다.
- 배열 안의 객체는 데이터가 아닌, **주소값만 복사**된다.
    - **복사본의 객체를 수정하면 원본도 바뀐다. (얕은 복사)**

### reduce

- 배열의 각 요소에 대해서 콜백 함수를 실행하고, 하나의 결과값을 반환
- 배열을 원하는 특정 형태의 값으로 변환 (숫자, 문자열, 객체, 배열)
- `array.reduce(callBackFunction, initialValue)`
    - `callBackFunction`: 배열을 처리할 콜백함수
        - `accumulator`(acc, 필수): **누적값**이며, 이전 콜백 함수가 return한 값이 다음 순회의 accumulator로 전달
        - `currentValue`(cur, 필수): 현재 순회에서 처리중인 요소
        - `currentIndex`(idx, 선택): 현재 처리 중인 currentValue의 인덱스
        - `array`(arr, 선택): reduce를 호출한 원본 배열
    - `initialValue`: **누적을 시작할 초기값**

```jsx
// 예시1. 숫자 합계 구하기 
const numbers = [1, 2, 3, 4, 5];

const sum = numbers.reduce((accumulator, current) => {
  console.log(`누적값(acc): ${accumulator}, 현재값(cur): ${current}`);
  return accumulator + current;
}, 0);
// 누적값(acc): 0, 현재값(cur): 1
// 누적값(acc): 1, 현재값(cur): 2
// 누적값(acc): 3, 현재값(cur): 3
// 누적값(acc): 6, 현재값(cur): 4
// 누적값(acc): 10, 현재값(cur): 5

console.log('최종 결과:', sum); // 최종 결과: 15

// 예시2. 배열 -> 객체로 변환 
// '이름'을 key로, '등장 횟수'를 value로 하는 객체를 만들자!
const names = ['Alice', 'Bob', 'Alice', 'Charlie', 'Bob', 'Alice'];

const nameCounts = names.reduce((countMap, name) => {
  countMap[name] = (countMap[name] ?? 0) + 1;

  return countMap;  // 수정된 객체를 다음 순회에 반환 
}, {});  // 초기값은 빈 객체({})

console.log(nameCounts); // { Alice: 3, Bob: 2, Charlie: 1 }

// 예시3. 배열 -> 배열 (map과 filter 한 번에 reduce로 적용하기)
// 체이닝으로 한다면? 
//   - const result = nums.filter(n => n % 2 === 0).map(n => n * 2);
const nums = [1, 2, 3, 4, 5];
const result = nums.reduce((newArray, current) => {
  // 짝수인지 검사 (filter 역할)
  if (current % 2 === 0) {
    // 2배를 해서 newArray에 추가 (map 역할)
    newArray.push(current * 2);
  }

  // 다음 순회에 수정된 배열을 반환 
  return newArray;
}, []); // 초기값은 빈 배열([])

console.log(result); // [4, 8]
```
