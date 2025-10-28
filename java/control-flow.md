
## 제어문

### 조건문 - if

```java
**package java01_operator;

public class conditional_statement {
	public static void main(String[] args) {
		// 1. if
		int age = 10;

		if (age > 10) {
			System.out.println("나는 10살 초과입니다.");
		}
		System.out.println("이건 하나요?");
		// 이건 하나요?

		// 2. if-else
		boolean isOk = true;

		if (isOk) {
			System.out.println("할 수 있어");
		} else {
			System.out.println("할 수 없어");
		}
		// 할 수 있어

		// 3. if-else if-else
		int score = 97;
		if (score >= 90) {
			System.out.println("A");
		} else if (score >= 80) {
			System.out.println("B");
		} else if (score >= 70) {
			System.out.println("C");
		} else {
			System.out.println("F");
		}
		// A
	}
}**
```

### 조건문 - switch

- 표현식을 통해 값을 반환할 수 있다. (break 불필요)
- 동일한 case를 묶어서 처리 가능 (예: `3, 4, 5`)

```java
package java01_operator;

public class if_conditional_statement {
	public static void main(String[] args) {
		int month = 12;

		switch (month) {
		case 3, 4, 5: {
			System.out.println("봄");
		}
		case 6, 7, 8: {
			System.out.println("여름");
		}
		case 9, 10, 11: {
			System.out.println("가을");
		}
		case 12, 1, 2: {
			System.out.println("겨울");
		}
		default:
			break;
		}
		// 겨울
	}
}
```

### 반복문 - for

- `for (1.초기화; 2.조건식; 4.증감식) { 3.반복할 코드 블록 }`
- 초기화는 반복문이 시작될 때 딱 한 번 실행
- 조건식이 false이면 반복문 종료
- 증감식은 반복문의 반복이 끝나면 실행

```java
public class for_statement {
	public static void main(String[] args) {
		for (int i = 0; i < 5; i++) {
			System.out.print(i);
		}
		// 01234

		for (int i = 0, j = 10; i < 10 && j >= 20; i += 10, j--) {
			System.out.print(j);
		}
		// None
	}
}
```

### 반복문 - while

- `do-while`문: 블록 내용을 먼저 수행 후 조건식 판단 (최소 한 번은 실행)

```java
package java01_operator;

public class while_statement {
	public static void main(String[] args) {
		// 1. while
		int i = 0;
		while (i < 5) {
			System.out.print(i++);
		}
		// 01234

		// 2. do-while
		int j = 10;

		do {
			System.out.println(j++);
		} while (j < 10);
		// 10
	}
}

```

### 분기문 - break

- 가장 가까운 반복문을 빠져나간다.
- 중첩된 반복문 구조에서 반복문에 이름(라벨)을 붙여 한번에 빠져나올 수 있다.

### 분기문 - continue

- 현재 반복의 나머지 부분을 건너뛰고 다음 반복으로 간다.
- 중첩된 반복문에서 이름(라벨)을 붙여 특정 반복을 건너 뛸 수 있다.
