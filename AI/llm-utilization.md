## 환경 설정 및 라이브러리

### **HTTPX (비동기 통신)**

- Python용 HTTP 클라이언트 라이브러리
- 기존 `requests` 라이브러리와 유사한 사용법을 제공하면서 **비동기(Asynchronous)** 통신을 지원한다.
    - **비동기 통신:** 여러 개의 API 요청을 보낼 때, 하나의 요청이 끝날 때까지 기다리지 않고 여러 요청을 **동시에 병렬적으로 처리**하는 방식. 이를 통해 전체 작업 시간을 크게 단축시킬 수 있다.
- `async def`: 함수가 **비동기 함수**임을 선언. 이 함수 내에서는 `await` 키워드를 사용할 수 있다.
- `await`: 비동기 작업(예: API 요청)이 완료될 때까지 기다리면서, 프로그램의 다른 비동기 작업은 계속 실행되도록 한다. 즉, **"기다리는 동안 다른 일 먼저 하고 있어!"** 라는 의미.

### **JSON (JavaScript Object Notation)**

- 데이터를 저장하거나 주고받을 때 사용하는 가볍고 사람이 읽기 쉬운 데이터 형식.
- 파이썬의 딕셔너리와 유사한 `"키": 값` 형태의 쌍으로 구성됨.
- 대부분의 프로그래밍 언어와 API 통신에서 표준처럼 사용됨.
- LLM에게 답변을 정해진 형식으로 받기 위해 `response_format` 옵션을 사용하여 출력을 JSON 구조로 강제할 수 있음.

## 프롬프트 엔지니어링 (Prompt Engineering)

### **프롬프트의 기본 구조**

1. **역할(role): AI의 “정체성”과 “관점”**
    1. AI에게 특정 역할을 부여하여 답변의 전문성과 톤앤매너를 설정.
    2. "당신은 세계적인 영화 평론가입니다."
2. **목표(task): 무엇을 해야 하는지**
    1. AI가 수행해야 할 작업을 구체적이고 명확하게 지시.
    2. 표가 명확할수록 결과물의 품질이 높아집
    3. "사용자의 취향에 맞는 영화를 추천해 주세요."
3. **조건(constraints)**
    1. 답변의 형식, 스타일, 내용 등에 대한 제약 조건을 설정.
    2. "영화는 반드시 한 편만 추천하고, 추천 이유는 세 문장 이내로 작성하세요."
    3. 원하는 결과물을 일관되게 얻을 수 있음
4. **예시(Examples): (Few-shot Prompting)**
    1. 원하는 답변 패턴을 보여주면 AI가 비슷하게 답변함

### 좋은 프롬프트를 작성하려면?

결과물의 **다양성**과 **일관성**을 모두 확보해야 함!

- `temperature`: 확률 분포의 모양을 조절하는 매개변수
    - 값이 **0에 가까울수록(온도가 낮을수록)**, 모델은 확률이 가장 높은 단어를 선택하려는 경향이 강해져 일관되고 결정적인 답변을 생성. 항상 동일한 질문에 거의 동일한 답변이 나오게 됨
    - 값이 **1에 가까울수록(온도가 높을수록)**, 확률이 낮은 단어들도 선택될 가능성이 커져 창의적이고 다양한 답변이 생성. 같은 질문에도 매번 다른 스타일의 답변을 기대할 수 있음
- `top_p`; **핵심 샘플링(Nucleus Sampling):** 후보 단어의 범위를 동적으로 조절
    - 모델이 다음 단어를 예측할 때, 확률이 높은 순서대로 단어들의 누적 확률을 계산. 이 누적 확률이 우리가 설정한 `top_p` 값에 도달하는 순간, 그 단어들까지만 후보군으로 사용
    - 예를 들어, `top_p=0.5`로 설정하면, 상위 단어들의 누적 확률이 50%가 될 때까지의 단어들 중에서만 다음 단어를 선택. 이를 통해 문맥에 따라 후보군의 크기를 유연하게 조절하여, 너무 엉뚱한 단어는 배제하면서도 적절한 수준의 다양성을 확보할 수 있음
- 일관된 구조를 갖도록 프롬프트 내에 **JSON 형식**을 명시해야 함

### JSON 출력 형식 정의

- **코드 1: `response_format` 파라미터 사용**

```python
import json

# LLM의 응답을 구조화된 JSON 형식으로 강제하기 위한 설정.
response_format = {
    "type": "json_schema",
    "json_schema": {
        "name": "수도 정보",
        "strict": True,
        "schema": {
            "type": "object",
            "properties": {
                "capital": {"type": "string"},
                "translation": {"type": "string", "description": "수도의 영어 번역"},
            },
            "required": ["capital", "translation"],
        },
    },
}

# client.chat.completions.create 메서드를 호출하여 LLM에 요청.
response = client.chat.completions.create(
    model="solar-pro2",
    messages=[
        {
            "role": "user",
            "content": "한국의 수도는 어디야?",
        }
    ],
    # 위에서 정의한 JSON 스키마를 적용하여 응답 형식을 강제.
    response_format=response_format,
)
```

이 코드는 `client.chat.completions.create` 메서드를 호출할 때 **`response_format`이라는 API의 공식 파라미터를 사용**합니다.

- **작동 방식:** LLM API(서버)단에서 응답이 반드시 `response_format`에 정의된 JSON 스키마를 따르도록 **강제**합니다.
- **프롬프트:** `messages`에 들어가는 사용자 프롬프트("한국의 수도는 어디야?")는 순수하게 질문 내용만 담고 있습니다. 형식에 대한 언급이 없습니다.
- **장점:** 모델이 지시를 따르지 않을 가능성을 원천적으로 차단하므로 매우 안정적이고 신뢰할 수 있는 방법입니다.

- **코드 2: 프롬프트 엔지니어링 사용**

```python
from openai import OpenAI
import json

client = OpenAI(
    api_key=UPSTAGE_API_KEY,
    base_url="https://api.upstage.ai/v1"
)

user_prompt = """가상의 데이터를 만들려고 합니다.

아래 output_format에 따라 JSON 데이터를 1개만 반환해주세요.
{output_format}
"""

# TODO: output_format을 정의해주세요.
output_format = {
    'type': 'json_schema',
    'json_schema': {
        'name': "유저 정보",
        "strict": True,
        'schema': {
            'type': "object",
            "properties": {
                "name": {
                    "type": "string",
                    "description": "유저의 이름",
                },
                "age": {
                    "type": "integer",
                    "description": "유저의 나이",
                },
                "is_student": {
                    "type": "boolean",
                    "description": "유저가 학생인지 여부",
                },
            },
        },
    },
}

messages=[
    {
        "role": "user",
        "content": user_prompt.format(output_format=output_format)
    }
]

response = client.chat.completions.create(
    model="solar-pro2",
    messages=messages,
)
```

이 코드는 `response_format` 파라미터를 사용하지 않습니다. 대신, **사용자 프롬프트(`user_prompt`) 안에 JSON 스키마(`output_format`)를 텍스트로 직접 삽입**합니다.

- **작동 방식:** "아래 `output_format`에 따라 JSON 데이터를 반환해줘. {output_format}..."처럼 모델에게 **일반 텍스트로 지시**하는 방식입니다.
- **프롬프트:** 프롬프트 자체가 "이런 형식으로 응답해줘"라는 *지시 사항*과 *형식 예시(스키마)*로 구성됩니다.
- **단점:** 이는 **프롬프트 엔지니어링**에 의존하는 방식입니다. 모델이 지시 사항을 정확하게 이해하고 따라야만 원하는 JSON 형식을 얻을 수 있습니다. `response_format` 파라미터를 사용하는 것보다 신뢰성이 떨어질 수 있습니다.

| 구분 | 코드 1 (response_format 파라미터) | 코드 2 (프롬프트 엔지니어링) |
| --- | --- | --- |
| 요청 방식 | API 파라미터로 형식 지정 | 프롬프트 텍스트로 형식 지시 |
| 강제성 | 강제적 (Enforced) (API 레벨) | 권고적 (Requested) (모델 레벨) |
| 신뢰성 | 매우 높음 | 모델의 지시 이행 능력에 의존 |
| 프롬프트 내용 | 순수한 사용자 질문 | 형식 지시 사항 + 스키마 포함 |

## 데이터 합성 (Synthesis)

### **Synthesis 란?**

- 실제 수집한 데이터가 아닌, LLM(거대 언어 모델)과 같은 모델을 통해 인공적으로 만들어낸 데이터
- 단순히 기존 데이터를 약간 변형하여 양을 늘리는 **데이터 증강(Data Augmentation)**과는 다른 개념.
    - 데이터 증강이 원본 이미지의 밝기를 조절하거나 문장의 단어 순서를 바꾸는 것이라면,
    - 데이터 합성은 세상에 없던 완전히 새로운 데이터 쌍(예: 새로운 질문과 그에 대한 답변)을 창조해내는 방식
- 데이터 합성은 학습 데이터가 부족하거나, 실제 데이터를 수집하기 어려운 민감한 정보(개인정보, 의료정보 등)를 다뤄야 할 때 매우 유용

### 합성 데이터 평가 (LLM as a Judge)

- 사람이 직접 수많은 합성 데이터의 품질을 하나하나 검수하는 것은 시간과 비용이 많이 드는 비효율적인 작업
- **LLM as a Judge**는 이러한 검수 과정을 자동화하기 위해, **다른 LLM을 '평가자'로 활용**하는 기법
- 단순히 "좋다/나쁘다"와 같은 정량적인 평가를 넘어, **"왜 그렇게 평가했는지"에 대한 이유까지 생성**하여 데이터의 어떤 부분을 개선해야 할지 구체적인 피드백을 얻을 수 있다.

1. **평가 기준 설정**
    - 평가의 목적을 명확히 해야 함. 이번 실습에서는 생성된 영화 정보의 사실 여부를 검증하는 것이 아니라, 사전에 우리가 지시했던 `RULE`(친근한 말투, 호들갑 떠는 설명 등)을 얼마나 잘 이행했는지를 평가하는 데 초점을 맞춤
2. **일관성 확보 (temperature=0)**
    - `평가자` 역할을 맡은 LLM은 창의적이거나 다양한 답변을 할 필요가 없음. 오히려 동일한 입력에 대해 항상 **일관되고 객관적인 평가**를 내려야 신뢰할 수 있음
    - 따라서 평가자 LLM을 호출할 때는 `temperature` **값을 항상 0으로 설정**하는 것이 권장됨
3. **체계적인 평가 프롬프트 설계**
    - 평가자에게 필요한 모든 정보를 명확하게 제공해야 함
    - **입력:** 평가자 LLM에게 **[우리가 내렸던 지시사항], [생성 모델의 답변]**, 그리고 **[평가 기준]**을 모두 명시적으로 전달해야 함
    - **출력:** 평가자 역시 답변을 `score`(점수)와 `comment`(평가 이유)를 포함하는 **JSON 형식**으로 생성하도록 엄격하게 지시하여, 평가 결과를 쉽게 파싱하고 활용할 수 있도록 해야 함

## 데이터 증강 (Data Augmentation)

### Augmentation 이란?

- 데이터 증강은 **기존에 보유한 데이터를 기반으로 변형** (예: 이미지 회전, 텍스트 동의어 교체)을 가해 데이터 양을 늘리는 방식.
    - 데이터 합성이 '무(無)'에서 '유(有)'를 창조하는 것이라면,
    데이터 증강은 '유(有)'에서 '또 다른 유(有)'를 만들어내는 과정으로 볼 수 있음.
- 모델의 강건성(robustness)을 높이고 과적합을 방지하는 데 도움을 줌.
- 데이터 증강 기법의 **실질적인 효과**(예: 모델 성능 향상 기여도)를 검증하기 위해서는, 증강된 데이터를 활용하여 **모델을 재학습하고 성능 변화를 면밀히 비교·분석하는 추가적인 과정**이 필요함.

### 페르소나 설정

- 다양한 페르소나를 정의해 다양한 스타일의 데이터를 얻을 수 있습니다.

```python
# 다양한 번역 결과물을 얻기 위해서 다양한 페르소나를 정의합니다. (초등학생, 개발자, PM 등)
personas = [
    "Friendly Adult – Kind and polite tone, like an older sibling giving advice.",
    "Elementary Student – Simple, cheerful, and naive tone, like a 10-year-old child.",
    "Formal Business – Polite, professional tone suitable for documents or work emails.",
    "Casual Friend – Relaxed, informal tone, as if chatting with a close friend.",
    "Elderly Person – Gentle, old-fashioned, and wise tone, like a kind grandparent."
]

SYSTEM_PROMPT_WITH_PERSONA = """
You are a translation assistant.
Your task is to translate English sentences into Korean.
You must keep the meaning accurate, but adapt the tone and style according to the requested persona.

{persona}
"""
```

### 증강 데이터 평가 (LLM as a Judge)

- 모델 학습 데이터를 얻기 위해서 데이터를 증강했다는 의미는 **모델의 성능이 올랐냐**가 가장 중요한 평가 기준이 됩니다. 따라서, task, 모델 등에 따라서 모델의 성능이 각기 달라지기 때문에 명확한 정답이 있는 것은 아닙니다.
- LLM as a Judge를 이용하여 GPT를 통해 한번 필터링을 하는 방법으로 간단하게 평가해 볼 수 있습니다.
- 그 이후에는 모델 영역으로도 평가하기 어려운 부분은 직접 ML 엔지니어가 판단할 수 있어야 합니다.