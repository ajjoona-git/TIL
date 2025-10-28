
## 1차원 배열 (1D Array)

### 배열 (Array)

- 동일한 데이터 타입의 값(0개 이상)을 저장하기 위한 자료구조
- 인덱스를 이용하여 각 요소에 접근 가능
- **고정된 크기** (생성된 배열의 크기를 바꿀 수 없음)
    - 새로운 크기의 배열을 생성한 후에 기존 데이터를 복사해야 함
- 메모리에 연속적으로 저장됨

### 배열 선언

- `데이터타입[] 배열이름` (권장)
- `데이터타입 배열이름[]`

### 배열의 초기화

- `자료형[] 배열이름 = new 자료형[길이];` 자료형의 초기값(기본값)으로 초기화
    - `false` (boolean), `‘\u0000’`(char, 공백 문자), `0` (byte, short, int), `0L` (long), `0.0f` (float), `0.0` (double)
    - `null` (참조형 변수)
- `자료형[] 배열이름 = new 자료형[] {값1, 값2, 값3, ...};` 배열 생성 및 값 초기화
    - `new int[] {1, 2, 3, 4, 5}` "내가 지금 주는 값들({1, 2, 3, 4, 5})을 보고, **알아서 크기를 정해서(5칸)** 배열을 만들어줘"
    - 길이를 직접 명시할 수 없다!
- `자료형[] 배열이름 = {값1, 값2, 값3, ...};` 선언과 동시에 초기화
    - 초기화하지 않고 재할당할 수 없다!

```java
package java02_array;

import java.util.Arrays;

public class create_array {
	public static void main(String[] args) {
		// 배열의 선언
		int[] arr1;  // 권장
		int arr2[];  // 비권장

		// 배열의 초기화
		// 1. 기본값으로 초기화
		int[] arr3 = new int[10];
		String[] arr4 = new String[5];

		System.out.println(Arrays.toString(arr3));  // [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
		System.out.println(Arrays.toString(arr4));  // [null, null, null, null, null]


		// 2. 생성과 초기화
		int[] arr5 = new int[] {1, 2, 3, 4, 5};
		System.out.println(Arrays.toString(arr5));  // [1, 2, 3, 4, 5]

		// 크기를 지정하는 것과 초기값을 제공하는 것은 동시에 실행할 수 없다!
//		int[] arr6 = new int[10] {1, 2, 3, 4, 5};
//		System.out.println(Arrays.toString(arr6));
		// Exception in thread "main" java.lang.Error: Unresolved compilation problem:
		// Cannot define dimension expressions when an array initializer is provided
		// 배열 초기화 값이 제공될 때는 차원 표현식[크기]을 정의할 수 없다.


		// 3. 선언과 동시에 초기화
		String[] arr7 = {"바나나", "오렌지", "사과"};  // 선언과 동시에 이루어질 때만 가능!
		System.out.println(Arrays.toString(arr7));   // [바나나, 오렌지, 사과]

		arr7 = new String[] {"포도", "복숭아"};      // 재할당 가능
		System.out.println(Arrays.toString(arr7));  // [포도, 복숭아]
//		arr8 = {"수박", "토마토", "배"};	          // 재할당 불가능
		// Exception in thread "main" java.lang.Error: Unresolved compilation problems:
		// arr8 cannot be resolved to a variable
		// Array constants can only be used in initializers
	}
}
```

```java
// 0. 선언 + 기본값 초기화
int[] a = new int[5]; // 가능 a = [0, 0, 0, 0, 0]

// 1. 선언 + 생성 + 대입
int[] a = new int[]{3, 4, 5}; // 가능

// 2. 선언 -> 생성(할당)
int[] a;
a = new int[]{3, 4, 5}; // 가능

// 3. 선언 + 초기화
int[] a = {3, 4, 5}; // 가능

// 4. 선언 -> 축약형 할당(재할당)
int[] a;
a = {3, 4, 5}; // 불가능!!
```

### 배열의 메모리 생성 과정

- 기본 자료형 배열 (Primitive Type Array)
    - `int[]`, `double[]`, `boolean[]`, `char[]` 등
    - 연속된 메모리 공간에 **값(Value) 자체**가 저장됨

```python
int[] nums = new int[3];
nums[0] = 11;
nums[1] = 7;
nums[2] = 23;

메모리는 [11 | 7 | 23]
```

- 참조 자료형 배열 (Reference Type Array)
    - `String[]`, `MyObject[]` 등
    - 연속된 메모리 공간에 **값이 실제 저장된 힙 메모리의 주소(reference)**가 저장됨
    - `MyObject[] a = {new MyObject()}; MyObject[] b = {new MyObject()};` 일 때,
    `a[0] == b[0]`는 `false` **(서로 다른 객체의 '주소'를 비교하기 때문)**

```python
String[] names = new String[3];
names[0] = "lime";
names[1] = "pear";
names[2] = "grape";

메모리 예: [700번지 주소 | 800번지 주소 | 900번지 주소]
```

### 배열의 인덱스

- 인덱스는 0부터 시작
- 음수를 사용할 수 없음
- 접근 가능한 배열의 인덱스 범위를 벗어나면 오류 발생 `java.lang.ArrayOutOfBoundsException`
- `.length`를 이용하여 배열의 길이를 구할 수 있음

### 배열의 순회

- 반복문을 이용해 배열의 요소를 순회할 수 있음
- for-each문: `for(element : iterable)`
    - 배열 및 Collections에서 index 대신 직접 요소(elements)에 접근하는 변수를 제공
    - Python의 `for item in my_list:`와 똑같은 역할
    - naturally Read-Only (copied value)

```java
package java02_array;

public class traverse_array {
	public static void main(String[] args) {
		int intArray[] = { 1, 3, 5, 7, 9 };

		// for 문
		for (int i = 0; i < intArray.length; i++) {
			System.out.print(intArray[i]);
		} // 13579

		// for-each 문
		for (int x : intArray) {
			System.out.print(x);
		} // 13579

		// read-only
		for (int x : intArray) {
			x *= 2;
		}
		System.out.println(Arrays.toString(intArray)); // [1, 3, 5, 7, 9]
	}
}

```

## 배열의 복사

### 얕은 복사 (Shallow Copy)

- 객체 내부의 참조형 변수는 원본 객체의 **참조를 복사**
- 원본 객체와 복사본이 같은 참조를 가리키므로, **하나를 수정하면 다른 객체에도 영향을 미친다.**

```java
package java02_array;

import java.util.Arrays;

public class copy_array {
	public static void main(String[] args) {
		int[] original = {1, 2, 3};
		int[] shallowCopy = original;

		shallowCopy[0] = 10;

		System.out.println("원본 배열: " + Arrays.toString(original));
		System.out.println("복사본 배열: " + Arrays.toString(shallowCopy));
		// 원본 배열: [10, 2, 3]
		// 복사본 배열: [10, 2, 3]
	}
}
```

### 깊은 복사 (Deep Copy)

- 객체의 모든 필드 값을 새로 복사하여 **독립적인 객체**를 생성
- 원본 객체와 복사본은 완전히 별개의 메모리 공간을 가지므로, **한 객체의 변경이 다른 객체에 영향을 미치지 않는다.**

```java
package java02_array;

import java.util.Arrays;

public class deepcopy_array {
	public static void main(String[] args) {
		int[] original = { 1, 2, 3 };
		int[] deepCopy = new int[original.length];

		for (int i = 0; i < original.length; i++) {
			deepCopy[i] = original[i];
		}
		deepCopy[0] = 10;

		System.out.println("원본 배열: " + Arrays.toString(original));
		System.out.println("복사본 배열: " + Arrays.toString(deepCopy));
		// 원본 배열: [1, 2, 3]
		// 복사본 배열: [10, 2, 3]
	}
}

```

### 배열의 복사

- 배열은 **고정된 크기**이므로 배열의 크기를 변경하고 싶다면 **새로운 배열을 생성하여 복사**해야 한다.
- `Arrays.copyOf(원본배열, 새로운 배열의 크기)` 배열을 복사하여 새로운 배열을 생성
    - 지정된 새 크기만큼 공간을 만들고, 원본의 앞에서부터 채워 넣되
    - **공간이 남으면 기본값**으로 채우고, **공간이 모자라면 원본의 뒷부분을 버린다.**

```java
int[] original = {10, 20, 30};

// 1. 새 배열 크기 > 원본 배열 크기
// 크기를 6으로 늘려서 복사
int[] largerCopy = Arrays.copyOf(original, 6);
System.out.println(Arrays.toString(largerCopy));  // 결과: [10, 20, 30, 0, 0, 0]

// 2. 새 배열 크기 < 원본 배열 크기
// 크기를 2로 줄여서 복사
int[] smallerCopy = Arrays.copyOf(original, 2);
System.out.println(Arrays.toString(smallerCopy));  // 결과: [10, 20]
```

- `Arrays.copyOfRange(원본배열, from, to)` 배열의 특정 범위를 복사하여 새로운 배열을 생성
    - 새 배열은 **`to - from` 크기만큼** 생성된다.
    - **복사할 수 없는 영역은 해당 타입의 기본값**(`0`, `null`, `false` 등)으로 채워진다.
    - python의 slicing과 동일
    - from 인덱스가 음수이거나 범위를 초과하는 경우, `ArrayIndexOutOfBoundsException`
    - from 인덱스가 to 인덱스보다 클 경우 (시작점이 끝점보다 뒤에 있을 때), `IllegalArgumentException`

```java
// Arrays.copyOfRange()
int[] numbers = { 10, 20, 30, 40, 50 };
int[] subArray = Arrays.copyOfRange(numbers, 1, 4);
System.out.println(Arrays.toString(subArray));  // [20, 30, 40]

// 1. to가 원본 길이를 초과할 때
// 3번 인덱스부터 7번 인덱스 '전'까지 복사 요청
// 새 배열의 크기 = 7 - 3 = 4
int[] copyNumbersTo = Arrays.copyOfRange(numbers, 3, 7);
System.out.println(Arrays.toString(copyNumbersTo));  // 결과: [40, 50, 0, 0]
// 원본[3] -> copy[0] (40)
// 원본[4] -> copy[1] (50)
// 원본[5] -> 없음 (기본값 0) -> copy[2] (0)
// 원본[6] -> 없음 (기본값 0) -> copy[3] (0)
```

- `System.arraycopy(원본배열, 원본배열 시작점, 복사배열, 복사배열 시작점, 복사 길이)` 이미 존재하는 두 배열 사이에서 데이터를 복사
    - 범위를 벗어난 경우 "기본값으로 채워주기" 같은 편의를 제공하지 않고 즉시 예외를 발생
    - 인덱스 혹은 길이가 음수인 경우, `srcPos + length > src.length`, `destPos + length > dest.length`인 경우 **`IndexOutOfBoundsException`**
    - `src` 또는 `dest` 배열이 `null`일 때, **`NullPointerException`**
    - `src` 배열과 `dest` 배열의 타입이 호환되지 않을 때, `ArrayStoreException`

```java
**// System.arraycopy()
int[] tmp = new int[numbers.length * 2];
System.arraycopy(numbers, 0, tmp, 0, numbers.length);
tmp[0] = 1003;
System.out.println(Arrays.toString(tmp));  // [1003, 20, 30, 40, 50, 0, 0, 0, 0, 0]**
```
