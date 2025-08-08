# 수업 필기

## 코드 체계

문자에 대응되는 숫자를 정한 것

- 전 세계의 모든 문자를 컴퓨터가 일관되게 표현하고 처리하는 것
- 각 지역 별로 코드체계가 달라 해석이 달라지는 문제 발생

### **ASCII**

문자 인코딩 표준

- 7-bit 인코딩으로 128문자를 표현
- 출력 불가능한 제어문자 33개 + 공백을 비롯한 출력 가능한 문자 95개 = 128문자
- 예: `A` = 65
- `ord(c)`: 문자 → 아스키 코드
- `chr(i)`: 아스키 코드 → 문자
```python
print(ord('A')) # 65
print(ord('B')) # 66
print(ord('0')) # 48
print(chr(65))  # A
print(chr(66))  # B
print(chr(48))  # 0
```

### **유니코드(Unicode)**

다국어 처리를 위한 표준 코드체계

- 이모지(Emoji)도 유니코드 문자임
- 예: `A` = 0041(16진수) = 65(10진수), `'덤'` = B364(16진수)
- 유니코드 Character Set: 유니코드를 저장하는 변수의 크기를 정의함

### 유니코드 인코딩(UTF, Unicode Transformation Format)

- **UTF-8**, UTF-16, UTF-32 (최소 비트수를 나타내며, 최대는 모두 32bit)
- **UTF-8** (in web)
    - 최소 8-bit, 최대 32-bit(1 Byte * 4)
        
        ```
        # UTF-8 필요한 크기에 따른 저장 방법 예시
        0xxxxxxx
        110xxxxx 10xxxxxx
        1110xxxx 10xxxxxx 10xxxxxx
        11110xxx 10xxxxxx 10xxxxxx 10xxxxxxx
        ```
        
- UTF-16 (in windows, java)
- UTF-32 (in unix)

### 바이트 단위 저장 순서

- **Endian**: 여러 바이트로 이루어진 데이터를 저장하는 방식
    - Big-Endian : 상위 바이트(MSB, Most Significant Byte)를 가장 낮은 주소에 저장
    - Little-Endian : 하위 바이트(LSB, Least Significant Byte)를 가장 낮은 주소에 저장