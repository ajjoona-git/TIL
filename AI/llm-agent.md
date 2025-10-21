# Tool Augmented LLM (Agent)

## LLM Agent

- Agent: 센서를 통해 환경 (environment)을 인지하고, Actuator를 통해 환경에 대해 액션(action)을 통해 영향을 미치는 것으로 간주될 수 있는 모든 것
- LLM Agent: LLM을 핵심 구조로 삼아 환경을 이해하고 행동을 수행하는 에이전트
- LLM-first view: 기존 LLM을 활용한 시스템을 에이전트로 만든다.
    - 서치 에이전트, 심리상담 에이전트, 코드 에이전트
- Agent-first view: LLM을 AI에이전트에 통합하여 언어를 활용한 추론과 의사소통을 가능하게 한다.
    - 로봇, embodied 에이전트
- 성공적인 에이전트가 갖추어야 할 요건들: 도구 사용 (Tool Use), 추론과 계획 (Reasoning and Planning), 환경 표현, 환경 이해, 상호작용/의사소통

![LLM Agent 프레임워크](../images/llm-agent_1.png)

LLM Agent 프레임워크


## Tool Usage in LLMs

### Tool이란?

- LLM 에이전트에서 Tool은 언어모델 외부에서 실행되는 프로그램에 연결되는 함수 (function) 인터페이스를 의미한다.
- LLM은 함수 호출과 입력 인자를 생성함으로써 이 도구를 활용할 수 있다.

![LLM 에이전트에서 Tool의 의미](../images/llm-agent_2.png)

LLM 에이전트에서 Tool의 의미

### 도구 사용 패러다임 (Tool Use Paradigms)

- 도구 사용 (Tool Use): 두 모드 간의 전환
    - 텍스트 생성 모드 (text-generation mode)
    - 도구 실행 모드 (tool-execution mode)
- 도구 사용을 유도하는 방법
    - 추론 시 프롬프트 (inference-time prompting)
    - 학습 (Training; Tool Learning)

### 툴 러닝 (Tool Learning) 방식

- 모방 학습 (Imitation Learning): 인간의 도구 사용 행동 데이터를 기록함으로써, 언어모델이 인간의 행동을 모방하도록 학습
    - 가장 간단하고 직관적인 방식
    - OpenAI: WebGPT (2022): 지도 학습 (Supervised fine-tuning) + 강화 학습 (Reinforcement Learning)
    - Meta: Toolformer (2023): self-supervised, 지도 학습 (Supervised fine-tuning)
- 멀티 모달 툴 러닝 (Multi-modal Tool Learning): 멀티모달 대규모 언어모델(MLLM)을 기반으로 도구를 정의하고 활용하는 연구
    - GUI 에이전트, Embodied 에이전트
- 강화 학습: 지도 학습을 넘어 에이전트에서의 강화 학습을 도입하는 연구

## Environment Representaion & Understanding

### 환경 이해를 위해 필요한 것

- 환경에 접근하기 위한 툴 (Tool)
- 환경의 표현 (Representation)
- 환경을 이해, 탐색하기 위한 방법론들

### 환경의 표현 (Representaion)

- 텍스트 (Text): 물리적 세계에 대한 정보를 언어모델이 텍스트 기반으로 이해하고 명령을 수행할 수 있도록 환경을 표현
- 이미지 (Image): 시각적 환경을 텍스트와 연결하여 지시 수행 및 환경 이해를 가능하게 함
    - Touchdown: Google Street View 기반 내비게이션 및 지시 따르기 데이터셋
    - 에이전트로서 좋은 성능을 내려면 세부적인 이해가 중요하다.
    - 예: OCR(광학 문자 인식), 복잡한 레이아웃에서의 그라운딩
- 텍스트 기반 웹 (Textual Web Representaion): 웹 환경을 텍스트 (HTML, DOM, Accessibility Tree)로 표현하여 에이전트가 상호 작용 가능
    - WebArena

### 복잡한 환경에 대한 이해

- 환경 특화 프롬프트 (Environment-specific Prompts): 환경에 맞게 수동으로 프롬프트를 제작하여 에이전트가 지시를 따르도록 유도
    - 일반화가 잘 안 됨.
- 비지도 프롬프트 유도 (Unsupervised Induction of Prompts): 에이전트가 경험을 통해 프롬프트 자동 생성 및 일반화
    - Agent Workflow Memory: 환경에서의 상호작용을 메모리에 통합
- 환경 탐색 (Environment Exploration): 모델이 환경을 탐색할 때 보상 (reward)ㅇ르 부여하여 학습을 유도
- 탐색 기반 궤적 기억 (Exploration-based Trajectory Memorization): 탐색과 자기 교정(Self-correction)을 통해 데이터 생성

## Reasoning & Planning

### Planning

- Local Planning (국소적 계획): step by step 계획을 세우고, 매 스텝마다 사용할 하나의 툴(tool) 결정
    - 단순하고 직관적이나, 장기 의존성 문제
    - ReACT: 추론과 액션을 결합하여 에이전트가 환경과 상호작용하도록 하는 방식
- Global Planning (전역적 계획): 실행 가능한 전체 계획 경로 (planning path)를 한 번에 생성
    - 여러 개 툴을 조합하여 시퀀스 형태로 결정
    - 효율적이나, 복잡한 환경에서 실패 가능성
    - Plan-and-Solve Prompting

### Reasoning

- 오류 식별과 회복 (Error identification and Recovery): 에이전트는 에러/실수에서 회복할 방법이 필요
    - Reflexion: 수행한 궤적을 평가 후 잘못된 부분을 Reflection 단계에서 분석하여 재시도하는 방식
- 계획 재검토 (Revisting Plans): 에이전트가 실행 도중 계획을 재검토(revisit)하고 수정 가능
    - CoAct: 두 개의 에이전트가 서로 협력하여 오류 발생 시 재계획과 피드백을 수행
    - 장기 작업에서 안전성과 성공률 향상

## Langchain

- LLM 기반 애플리케이션을 빠르게 개발할 수 있는 오픈 소스 프레임워크
- LLM을 다양한 데이터/툴과 연결하여 강력한 애플리케이션 개발 가능
- 다양한 LLM provider (OpenAI, Anthropic, Google, etc)와 통합하여 모델/회사별 API 차이를 공통 인터페이스로 관리 가능