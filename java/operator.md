
## 연산자 (Operator)

### 산술 연산자

- `+`, `-`, `*`, `/`, `%`(나머지)
- 정수와 정수를 연산하면 정수
- 정수와 실수를 연산하면 실수

### 비교 연산자

- `==`, `!=`, `>`, `<`, `>=`, `<=`, `instanceof`
- 두 값을 비교하여 `ture` or `false`으로 반환

### 논리 연산자

- `&&`, `||`, `!`
- 조건을 조합하여 `true` 또는 `false`을 반환
- 작성 순서에 따라 효율적인 연산 가능
    - **단축평가 (Short-Circuit Evaluation)**: 결과를 더 이상 확인할 필요가 없을 경우, 남은 조건을 연산하지 않고 넘어가는 방식

### 대입(복합) 연산자

- `=`, `+=`, `-=`, `*=`, `/=`, `%=`
- 변수에 값을 할당하는 연산자
- 산술 연산자와 대입 연산자를 축약해서 사용할 수 있다. (순서 주의할 것)

### 단항 연산자

- `+`, `-`, `++a`, `--a`, `a++`, `a--`, `!`, `~`, `(type)a`
- 하나의 피연산자에만 작용하는 연산자
- 변수의 값이 상태를 변경하거나 체크하는 데 사용

### 삼항 연산자

- `(조건식)?(참):(거짓)`

### 연산자 우선순위

(소)괄호 > 산술 > 비교 > 논리 > 대입 순

```java
package java01_operator;

public class operator {
	public static void main(String[] args) {
		// 1. 산술 연산자
		int a = 100;
		double b = 21.5;

		System.out.println(a/b);  // 4.651162790697675
		System.out.println(a%b);  // 14.0

		// 2. 비교 연산자
		int c = 100;
		int d = 1000;

		System.out.println(c == d);  // false
		System.out.println(c != d);  // true
		System.out.println(c >= d);  // false

		// 3. 논리 연산자
		System.out.println(c == d && c != d);  // false
		System.out.println(c == d || c != d);  // true
		System.out.println(!(c == d));         // true

		// 4. 대입 복합 연산자
		int e = 1000;
		e += 10;
		System.out.println(e);       // 1010
		System.out.println(e + 10);  // 1020

		// 5. 단항 연산자 (증감)
		int f = 100;
		System.out.println(f++);  // 100
		System.out.println(f);    // 101
		System.out.println(++f);  // 102

		// 6. 삼항 연산자
		int q = 1000;
		int w = 500;
		System.out.println(q > w ? q : w);  // 1000
	}

}

```
