# DI 설정 및 구현 방법

## Spring DI - XML

### 의존성 주입

- **생성자**: `constructor-arg`를 이용하여 의존성 주입
- **설정자**: `setter`를 이용하여 의존성 주입
- `<ref>`, `<value>`와 같은 하위 태그 혹은 속성을 이용하여 설정

```xml
<?xml version="1.0" encoding="UTF-8"?>
<beans xmlns="http://www.springframework.org/schema/beans"
	xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
	xmlns:context="http://www.springframework.org/schema/context"
	xsi:schemaLocation="
		http://www.springframework.org/schema/beans https://www.springframework.org/schema/beans/spring-beans.xsd
		http://www.springframework.org/schema/context https://www.springframework.org/schema/context/spring-context.xsd">

	<!-- bean 등록 (풀패키지명) -->
	<bean class="com.ssafy.di.Desktop" id="desktop"></bean>

	<!-- 생성자 주입 -->
	<bean class="com.ssafy.di.Programmer" id="programmer">
		<constructor-arg ref="desktop"></constructor-arg>
	</bean>
		
	<!-- 설정자 주입 -->
	<bean class="com.ssafy.di.Programmer" id="programmer">
		<property name="computer" ref="desktop"></property>
	</bean>

</beans>
```

## Spring DI - Annotation

### Bean 생성 및 설정 (`@Component`)

- `@Component`: 객체를 생성할 대상 클래스에 작성해주는 Annotation
- 생성되는 bean의 이름은 클래스의 첫 글자를 소문자로 바꾼 것
- `@Component(value = "bean-name")` 으로 이름 지정
- 스프링은 @Component, @Service, @Controller, @Repository의 Streotype Annotations를 제공한다.

```xml
<!-- applicationContext.xml -->

<beans xmlns="http://www.springframework.org/schema/beans"
	...
	<context:component-scan base-package="com.ssafy.di"></context:component-scan>
</beans>
```

```java
package com.ssafy.di;

import org.springframework.stereotype.Component;

@Component
public class Desktop implements Computer {
	...
}
```

```java
package com.ssafy.di;

import org.springframework.stereotype.Component;

@Component("p")
public class Programmer {
```

### 의존성 주입 (`@Autowired`)

- 객체들끼리 서로 필요한 것이 있다면 Spring이 중간에서 연결해 준다.
- 마치 커플 매니저처럼 `Programmer`에게 `Desktop`을 꽂아주는 식

- 생성자
    - 생성자를 하나만 정의한다면 `@Autowired` 생략 가능

```java
// 생성자를 이용한 의존성 주입
@Autowired
public Programmer(Computer computer) {
	this.computer = computer;
}
```

- Setter

```java
// setter를 이용한 의존성 주입
@Autowired	
public void setComputer(Computer computer) {
	this.computer = computer;
}
```

- field

```java
@Component("p")
public class Programmer {
	@Autowired
	private Computer computer;
	...
```

### Django/Python의 Decorator vs Spring/Java의 Annotation

| **비교 항목** | **Python Decorator (Django)** | **Java Annotation (Spring)** |
| --- | --- | --- |
| **작동 방식** | **코드를 감싸는 함수:** 원래 함수를 다른 함수로 감싸서 실행 전후에 로직을 추가함 (Wrapper) | **데이터를 설명하는 라벨:** 코드 자체를 바꾸지 않고, 메타데이터(설명)를 붙여둠 (Metadata) |
| **실행 주체** | 코드가 실행되는 순간 Decorator 함수가 즉시 실행됨 | **Spring 컨테이너**가 코드를 읽고(Reflection) 설정된 대로 객체를 생성하거나 연결 |
| **비중** | 필수라기보다는 편의를 위한 도구 (예: `@login_required`) | **Spring의 핵심:** 어노테이션 없이는 객체 생성이나 의존성 주입이 거의 불가능함 |

**Django Decorator vs Spring Annotation 매핑**

- **`@login_required` (Django) $\approx$ `@PreAuthorize("isAuthenticated()")` (Spring Security)**
    - 권한이 있는 사용자만 접근할 수 있게 제한하는 역할

- **`@csrf_exempt` (Django) $\approx$ `@CrossOrigin` 또는 Security 설정**
    - 특정 보안 규칙을 예외 처리하거나 설정할 때 사용
- **`@transaction.atomic` (Django) $\approx$ `@Transactional` (Spring)**
    - 함수 내부의 DB 작업을 하나의 트랜잭션으로 묶어주는 아주 중요한 역할

**Spring의 어노테이션 "라벨링"**

- Spring의 어노테이션은 단순히 기능을 추가하는 것을 넘어, **"이 객체는 Spring 너가 관리해!"**라고 선언하는 표식

- `@Component`, `@Service`, `@Controller`: Spring이 관리하는 Bean으로 등록하라는 라벨. 
	- Django는 `views.py`, `models.py` 등 파일 위치가 정해져 있지만, Spring은 이 어노테이션만 붙어있으면 어디에 있든 찾아내서 객체로 만든다.

- `@Autowired`: "여기에 필요한 객체를 꽂아줘!"라는 요청.
	- Django에서는 보통 `import` 후 직접 호출하거나 `self.something`으로 접근하지만, Spring은 이 라벨을 보고 컨테이너에 있는 객체를 자동으로 연결해준다.

## Spring DI - Java Config

### scan

```java
package com.ssafy.di_scan;

import org.springframework.context.annotation.ComponentScan;
import org.springframework.context.annotation.Configuration;

@Configuration
@ComponentScan(basePackages = {"com.ssafy.di_scan"})
public class ApplicationConfig {

}

```

```java
package com.ssafy.di_bean;

import org.springframework.context.ApplicationContext;
import org.springframework.context.annotation.AnnotationConfigApplicationContext;

public class Test {
	public static void main(String[] args) {
		// 설정파일에 대한 경로 작성
		ApplicationContext context = new AnnotationConfigApplicationContext(ApplicationConfig.class);
		
		Desktop d = context.getBean("desktop", Desktop.class);
		
		System.out.println(d.getInfo());
	}
}

```

### bean

```java
package com.ssafy.di_bean;

import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;

@Configuration
public class ApplicationConfig {

	@Bean
	public Desktop desktop() {
		return new Desktop();
	}
	
	@Bean
	public Programmer programmer() {
		// 설정자 주입
//		Programmer p = new Programmer();
//		p.setComputer(desktop());
//		
//		return p;
		
		// 생성자 주입
		Programmer p2 = new Programmer(desktop());
		return p2;
	}
}

```
