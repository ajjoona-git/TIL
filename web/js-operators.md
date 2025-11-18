# JavaScript의 연산자

## 연산자

### 할당 연산자

- 오른쪽에 있는 피연산자의 평가 결과를 왼쪽 피연산자에 할당하는 연산자
- 단축 연산자 지원

```jsx
// 할당 연산자 
let a = 0

a += 10
console.log(a) // 10

a -= 3
console.log(a) // 7

a *= 10
console.log(a) // 70

a %= 7
console.log(a)  // 0
```

### 증가/감소 연산자

- **증가 연산자 (`++`)**: 피연산자를 증가(+1)시키고 연산자의 위치에 따라 증가하기 전이나 후의 값을 반환
- **감소 연산자 (`--`)**: 피연산자를 감소(-1)시키고 연산자의 위치에 따라 감소하기 전이나 후의 값을 반환
- 코드의 가독성을 위해 `a += 1`, `a -= 1`과 같이 더 명시적인 표현을 권장!

```jsx
// 증감 연산자
let x = 3
const y = x++  // 할당 후 증가
console.log(x, y)  // 4 3

let m = 3
const n = ++m  // 증가 후 할당
console.log(m, n)  // 4 4
```

### 비교 연산자

- 피연산자들(숫자, 문자, Boolean 등)을 비교하고 결과 값을 Boolean으로 반환하는 연산자

```jsx
// 비교 연산자
console.log(3 > 2)  // true
console.log(3 < 2 )  // false
console.log('A' < 'B' )  // true
console.log('Z' < 'a' )  // true
console.log('가' < '나')  // true
```

### 동등 연산자 (==)

- 두 피연산자가 **같은 값**으로 평가되는지 비교한 후 boolean 값을 반환
- **(주의)암묵적 타입 변환**을 통해 타입을 일치시킨 후 같은 값인지 비교한다.
    - 0 == false, ‘’ == []가 true 가 되는 등 직관과 다르게 진행될 수 있다.
- 두 피연산자가 모두 객체일 경우 메모리의 같은 객체를 바라보는지 판별한다.

```jsx
// 동등 연산자
console.log(1 == 1)  // true
console.log('hello' == 'hello')  // true
console.log('1' == 1)  // true
console.log(0 == false)  // true
```

### 일치 연산자 (===)

- 두 피연산자의 값과 타입이 모두 같은 경우 true를 반환
- 같은 객체를 가리키거나, 같은 타입이면서 같은 값인지를 비교
- 엄격한 비교가 이뤄지며 암묵적 타입 변환이 발생하지 않는다.
- 특별한 경우를 제외하고는, **예측하지 못한 결과를 방지하기 위해 일치 연산자 (===) 사용을 권장!!!**

```jsx
// 일치 연산자
console.log(1 === 1)  // true
console.log('hello' === 'hello')  // true
console.log('1' === 1)  // false
console.log(0 === false)  // false
```

### 논리 연산자

- and (`&&`), or (`||`), not (`!`)
- 단축 평가 지원
    - `&&` (AND): **왼쪽 값이 Truthy일 경우에만** 오른쪽 값을 평가
    - `||` (OR):  **왼쪽 값이 Falsy일 경우에만** 오른쪽 값을 평가
- Null 병합 연산자 (Nullish Coalescing Operator) (`??`): null 혹은 undefined이 아니면 첫 번째 (?? 기준 왼쪽) 값을, null 혹은 undefined이면 왼쪽 값을 그대로 사용
    - 파이썬의 defaultdict 느낌

```jsx
// 논리연산자
console.log(true && false);  // false
console.log(true && true);  // true

console.log(false || true);  // true
console.log(false || false);  // false

console.log(!true);  // false

// --- (중요) 단축 평가 (Short-circuit Evaluation) ---
// && (AND) 연산
console.log(1 && 0);  // 0
console.log(0 && 1);  // 0
console.log(4 && 7);  // 7

// || (OR) 연산
console.log(1 || 0);  // 1
console.log(0 || 1);  // 1
console.log(4 || 7);  // 4
```

```jsx
// 단축평가 활용 예시
// 1. 단축평가 활용 예시(Positive)
let user = null;  // 유저
// user에 관한 어떤 쿼리!
const name = user || "Guest"; // user가 Falsy(null)이므로 "Guest" => default 값을 설정해주는 것이다.
console.log(name); // "Guest"

// 2. 단축평가 활용 예시2(Negative)
let score = 0; // 0점은 유효한 점수
let currentScore = score || 50; // 0이 Falsy라서 50이 됨 (버그!)
console.log(currentScore); // 50

// 3. 단축평가 활용 예시3(해결책)
// default 값을 어떻게 설정하느냐...
// null, undefined 인 경우에는 단축평가로 default 값을 잘 설정할 수 있는데,
// 0과 같은 값은 의도하지 않아도 default 값으로 바뀐다ㅜ
let score = 0;
let currentScore;

if (score === null || score === undefined) {
    currentScore = 50; // null이나 undefined일 때만 기본값
} else {
    currentScore = score;
}
console.log(currentScore); // 0 (정상!)

// 4. 최종(ES2020 도입) Null 병합 연산자 (Nullish Coalescing Operator) ??  
let score = 0;
// score가 null이나 undefined가 아니므로(0임), 왼쪽 값(0)을 그대로 사용
const currentScore = score ?? 50;
console.log(currentScore); // 0 

let user = null;
const name = user ?? "Guest";
console.log(name); // "Guest"
```