## 클래스 (Class)

### 함수 (Function)

- 관련된 문장들을 하나로 묶은 것 (이름을 붙인 것)
- 실행 가능한 단위
- 함수의 구성 요소: 반환타입 (또는 void), 함수 이름, 매개변수, 함수 내용
    - static: 메모리에 올려둬
    - void: 반환 값의 자료형(type)
    - return 구문은 반환 타입이 void인 경우 생략 가능

```java
package inclass;

import java.util.Random;

public class SsafyRoutine {
	public static void main(String[] args) {
		System.out.println("아침에 일어난다.");
		이동("교육장", "셔틀버스");
		boolean 과제 = 교육();
		이동("집", "어디로든 문");
		if(과제)
			System.out.println("과제를 해결한다.");
		System.out.println("잠을 잔다.");
	}
	
	// boolean: 반환 값의 타입
	public static boolean 교육() {
		System.out.println("오전 수업을 듣는다.");
		System.out.println("점심을 먹는다.");
		System.out.println("오후 수업을 진행한다.");
		
		return new Random().nextBoolean();
	}
	
	public static void 이동(String 장소, String 교통수단) {
		System.out.println(장소+"(으)로 "+교통수단+"를(을) 이용하여 이동한다.");
	}
}

```

### 클래스 (Class)

- 관련 있는 변수(필드)와 함수(메서드)를 묶어서 만든 사용자 정의 자료형 (데이터 타입)
- 객체를 생성하기 위한 설계도
- 인스턴스(instance): 클래스를 통해 생성된 객체

**1단계: 하드코딩 → 배열?**

- 한 사람의 정보 (이름, 나이, 취미)가 연관성이 없다.

```java
package class01;

public class PersonTest {
	public static void main(String[] args) {
		// 사람의 정보를 관리하자!
		
		String name1 = "Yang";
		int age1 = 45;
		String hobby1 = "Youtube";
		
		String name2 = "Park";
		int age2 = 23;
		String hobby2 = "Golf";
		
		// 배열!
		int size = 100;
		String[] names = new String[size];
		int[] ages = new int[size];
		String[] hobbies = new String[size];
		
		names[0] = "Yang";
		names[0] = "Park";
		ages[0] = 45;
		ages[1] = 23;
		hobbies[0] = "Youtube";
		hobbies[1] = "Golf";
	}
}

```

**2단계: Person 클래스에 데이터 추가**

```java
package class02;

public class Person {
	String name;
	int age;
	String hobby;
}

public class PersonTest {
	public static void main(String[] args) {
		// Yang을 생성해보자
		// Person: 사용자 정의 자료형
		// 클래스이름 변수이름 = new 클래스이름();
		Person yang = new Person();
		yang.name = "Yang";
		yang.age = 45;
		yang.hobby = "Youtube";

		System.out.printf("나의 나이는 %s입니다. %n나이는 %d세, 취미는 %s입니다.%n", yang.name, yang.age, yang.hobby);

		Person hong = new Person();
		hong.name = "Hong";
		hong.age = 23;
		hong.hobby = "Golf";

		info(hong.name, hong.age, hong.hobby);
	}
	
	public static void info(String name, int age, String hobby) {
		System.out.printf("나의 나이는 %s입니다. %n나이는 %d세, 취미는 %s입니다.", name, age, hobby);
	}
}

```

**3단계: Person 클래스에 기능도 추가**

```java
package class03;

public class Person {
	// 데이터
	String name;
	int age;
	String hobby;
	
	// 기능
	void info() {
		System.out.printf("나의 나이는 %s입니다. %n나이는 %d세, 취미는 %s입니다.%n", name, age, hobby);
	}
}

public class PersonTest {
	public static void main(String[] args) {
		// Yang을 생성해보자
		// Person: 사용자 정의 자료형
		// 클래스이름 변수이름 = new 클래스이름();
		Person yang = new Person();
		yang.name = "Yang";
		yang.age = 45;
		yang.hobby = "Youtube";

		Person hong = new Person();
		hong.name = "Hong";
		hong.age = 23;
		hong.hobby = "Golf";

		yang.info();
		hong.info();
	}
}
```

### 클래스의 구성 요소

- **필드 (Field)**: 클래스에 선언된 변수 (멤버 변수, 멤버 필드)
    - 클래스의 속성을 정의한다.
    - 각 인스턴스는 필드에 고유한 값을 가질 수 있다.
- **메서드 (Method)**: 특정 동작을 수행하는 코드 블록
    - 객체의 행동을 정의한다.
    - 입력(매개변수)를 이용하여 처리하고 결과(반환 값)를 반환한다.
    - 자바에서는 독립적으로 정의된 함수가 없기 때문에 `함수 == 메서드`라고 생각해도 된다.
    - 오버로딩 가능
- **생성자 (Constructor)**: 객체 생성 시 호출되는 특별한 메서드
    - 필드 초기화 또는 생성 시 필요한 작업을 수행한다.
    - 클래스 이름과 같고, 반환 타입이 없다. (void 작성 X)

### 클래스 선언

- 데이터 필드를 초기화하지 않으면, 기본 값이 들어가 있다.

```java
[제한자(Modifier)] class 클래스이름 {
		// 멤버 변수, 필드 (속성 정의)
		[제한자(Modifier)] 데이터타입 변수이름 [=초기값];
		
		// 생성자
		[제한자(Modifier)] 클래스이름([매개변수들]) {
				생성자 본문
		}
		
		// 메서드 (기능 정의)
		[제한자(Modifier)] 반환타입|void 메서드이름([매개변수들]) {
				메서드 본문
		}
}
```

```java
// 객체(인스턴스) 생성
클래스이름 객체이름 = new 클래스이름([생성자 매개변수들]);

// 필드 값 접근
객체이름.멤버변수이름

// 메서드 호출
객체이름.멤버메서드이름([매개변수들]);
```

### 변수의 종류

| 변수 종류 | 선언 | 생성 시기 | 특징 |
| --- | --- | --- | --- |
| 클래스 변수 (Class Variable) | 클래스에서 멤버 필드 선언 시 static 키워드를 사용 | 클래스가 메모리에 로드될 때 생성 | 모든 인스턴스가 공유하는 변수 |
| 인스턴스 변수 (Instance Variable) | 클래스에서 멤버 필드 선언 시 static 키워드를 사용하지 않음 | 인스턴스가 생성될 때 생성 | 각 인스턴스마다 별도로 생성 |
| 지역 변수 (Local Variable) | 메서드, 생성자, 또는 초기화 블록 내에서 선언 | 선언된 블록이 실행될 때 생성 | 블록이 끝나면 소멸 |

### 매개 변수 (Parameter)

- 메서드에 입력 데이터를 전달하는 역할 (생략 가능)
- 메서드 선언 시 타입과 이름을 지정한다.
- 호출할 때는 인자(Argument)라고 한다.
- 매개변수는 묵시적 형변환(자동 형변환)을 이용하여 전달된다.
    - 표현할 수 있는 범위가 작은 친구가 큰 친구로 갈 때, 자연스럽게 바뀐다.
    - 선언된 타입보다 더 큰 타입은 호출 불가능!

```java
package class03;

public class Person {
	// 데이터
	String name;
	int age;
	String hobby;
	
	// 기능 (매개변수 X)
	void info() {
		System.out.printf("나의 나이는 %s입니다. %n나이는 %d세, 취미는 %s입니다.%n", name, age, hobby);
	}
	// 기능 (매개변수 O)
	void study(int time) {
		//int time = ? (호출 시 넘겨준 값)
		System.out.println(time + "시간 만큼 공부를 했습니다.");
	}
}

public class PersonTest {
	public static void main(String[] args) {
		// Yang을 생성해보자
		// Person: 사용자 정의 자료형
		// 클래스이름 변수이름 = new 클래스이름();
		Person yang = new Person();
		yang.name = "Yang";
		yang.age = 45;
		yang.hobby = "Youtube";

		yang.study(100);  // 100시간 만큼 공부를 했습니다.
	}
}
```

### 가변인자 (Variable Arguments)

- 메서드에서 매개변수의 개수를 가변적으로 받을 수 있다.
- 배열처럼 처리되지만, 호출 시 배열을 명시적으로 생성할 필요가 있다.
- 가변 인자는 항상 마지막에 위치해야 한다.
- 여러 개의 가변 인자 불가

```java
리턴타입 메서드이름(타입... 변수명) {
//내부적으로 변수명은 배열처럼 사용 가능
}

public class VarArgsExample {
		public static void printNumbers(int... numbers) {
				for (int n : numbers) {
						System.out.println(n);
				}
		}
		
		public static void main(String[] args) {
				printNumbers(1, 2, 3);
				printNumbers(10);
				printNumbers(); // 0개도 가능
		}
}
```

### 반환 타입 (Return Type)

- 메서드가 수행한 결과를 반환
- 메서드 선언 시 타입을 지정, 없다면 void 작성 (**생략 불가능**)
- 반환 타입이 void가 아니라면 반드시 해당 타입의 값을 return 해야한다.
- 반환 타입은 메서드당 하나만 작성할 수 있다.
- 결과를 받을 때 묵시적 형변환 적용

```java
// 가능한 경우: double 타입이 int 타입보다 크다.
public double getAge() {
		return age;  // age의 타입은 int
}

// 불가능한 경우: short 타입이 int 타입보다 작기 때문에 불가능!
public short getAge() {
		return age;  // age의 타입은 int
}
```

### 메서드 오버로딩 (Overloading)

- 이름이 같고 매개변수가 다른 메서드를 여러 개 정의하는 것
- 중복 코드에 대한 효율적 관리 가능
- **파라미터의 개수 또는 순서, 타입이 달라야 한다.** (파라미터 이름만 다른 것은 X)
- 리턴 타입이 다른 것은 의미가 없다.

```java
package class03;

public class Person {
	...
	void study(int time) {
		//int time = ? (호출 시 넘겨준 값)
		System.out.println(time + "시간 만큼 공부를 했습니다.");
	}
	
	// 메서드 오버로딩
	// 이름이 같으면서, 매개변수가 다른 메서드 (파라미터의 타입, 개수, 순서가 달라야 함)
	
	// 타입이 다른 경우 (가능)
	void study(long time) {
	}
	void study(double time) {
	}
	// 개수가 다른 경우 (가능)
	void study(int time1, int time2) {
	}
	// 파라미터 이름만 다른 경우 (불가능)
	void study(int time2, int time1) {
	}
	
	// 순서가 다른 경우 (가능)
	void study(int time, String str) {
	}
	void study(String str, int time) {
	}
	
}
```