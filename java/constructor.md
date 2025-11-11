## 생성자 (Constructor)

### 생성자

- 필드 초기화 또는 생성 시 필요한 작업을 수행한다.
- 클래스 이름과 같고, 반환 타입이 없다. (void 작성 X)
- `new` 키워드와 함께 호출하여 객체를 생성한다.
- 객체 생성 시 반드시 호출되어야 한다.
- 생성자 미작성 시, **기본 생성자**를 자동으로 제공한다.
- 매개변수의 개수가 다르거나 자료형이 다른 여러 개의 생성자가 있을 수 있다. (생성자 오버로딩)
- 생성자의 첫 번째 라인으로 `this()` 생성자를 사용하여 또다른 생성자를 하나 호출할 수 있다.

### 기본 생성자

- 매개 변수가 없는 생성자
- 개발자가 따로 정의하지 않으면 컴파일러가 자동으로 추가한다.
- 생성자가 하나라도 정의되어 있으면 컴파일러는 기본 생성자를 추가하지 않는다.

```java
package class04;

public class Dog {
	// 기본 생성자가 자동으로 추가된다!
	public Dog() {
		System.out.println("기본 생성자 호출");
	}
}

public class DogTest {
	public static void main(String[] args) {
		Dog dog = new Dog(); // 기본 생성자 호출
	}
}
```

### 매개변수 생성자

- 매개변수를 받아 객체를 초기화하는 생성자
- 생성자 호출 시 인자를 넘겨주어야 한다.
- 작성 시 컴파일러는 기본 생성자를 작성하지 않는다.
    - 기본 생성자도 오버로딩이 가능하므로, 습관적으로 기본 생성자를 작성하기를 권장!
        - `Ctrl + Space + Enter`
    - 그렇지 않으면 기본 생성자가 자동으로 생성되지 않기 때문에, 기본 생성자 호출 시 에러 발생

```java
package class04;

public class Dog {
	
	String name;
	int age;

	// 기본 생성자 (오버로딩 가능)
	// Ctrl + Space + Enter
	public Dog() {
		System.out.println("기본 생성자 호출");
	}
	
	// 매개변수 생성자
	public Dog(String name, int age) {
		this.name = name;
		this.age = age;
	}
}

public class DogTest {
	public static void main(String[] args) {
		Dog dog = new Dog(); // 기본 생성자
		Dog dog2 = new Dog("마리", 5);  // 매개변수 생성자
	}
}

```

### 생성자 오버로딩

- 같은 이름의 생성자를 매개 변수의 개수나 타입이 다르게 여러 개 정의하는 것
- **매개 변수의 타입, 개수, 순서** 등이 달라야 한다.

### `this.`

- 참조 변수로써 현재 인스턴스 자기자신을 가리킨다.
- 매개변수의 이름과 필드의 이름이 같을 때, 필드를 구분하기 위해서 사용한다.
- static 영역에서 사용 불가능

```java
package class04;

public class Dog {
	
	String name;
	int age;
	
	// 기본 생성자가 자동으로 추가된다!
	public Dog() {
		System.out.println("기본 생성자 호출");
	}
	
	public Dog(int age) {
		this.age = age;
	}
	
	// 매개변수 생성자
	public Dog(String name, int age) {
		this.name = name;
		this.age = age;
	}
}

public class DogTest {
	public static void main(String[] args) {
		Dog dog3 = new Dog(10);
		System.out.println(dog3.name);  // null
	}
}
```

### `this()`

- 해당 키워드를 통해 같은 클래스의 다른 생성자 호출
- 같은 클래스 내에서만 호출 가능
- 반드시 생성자의 **첫 번째 줄**에 위치
- 중복 코드를 제거하거나 생성자 체인을 통해 간결하고 유지보수하기 쉬운 코드 작성에 도움

```java
package class04;

public class Dog {
	
	String name;
	int age;
	
	public Dog() {
		System.out.println("기본 생성자 호출");
	}
	
	public Dog(int age) {
		this("뽀삐", age); // public Dog(String name, int age)를 호출한다!
	}

	public Dog(String name, int age) {
		this.name = name;
		this.age = age;
	}
}

public class DogTest {
	public static void main(String[] args) {
		Dog dog3 = new Dog(10);
		System.out.println(dog3.name);  // 뽀삐
	}
}
```
