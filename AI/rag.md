## Information Retrieval (정보 검색)

### IR (정보 검색)

- 목표: 검색 질의 (Query)와 가장 관련성 높은 정보를 제공하는 것
- 정보 검색 (IR): 사용자의 질의 (Query)에 맞는 정보를 대규모 데이터에서 찾아 제공하는 과정
    - 사용자가 질문하면, IR이 관련 문서를 찾아 제공한다.
- Retrieval (검색): datastore에 있는 수 많은 정보 중에서, 주어진 쿼리와 가장 관련성이 높은 정보를 찾아내는 과정

![IR (정보 검색)](../images/agi_2.png)

IR (정보 검색)

### IR의 활용

- Web Search, Item Search
    - Search Engines: 구글, 네이버
    - E-Commerce: 아마존, 쿠팡
- 추천 시스템
    - OTT 서비스, E-Commerce
- RAG (Retrieval-augmented Generation, 검색 증강 생성)
    - 사용자의 질문에 답하기 위해 datastore에서 관련 정보를 검색(Retrieval)해와서, 이를 언어모델이 생성 (Generation) 단계에 활용하는 방법
    - 검색된 문서를 활용하여 더 정확하고 최신의 답변을 생성한다.

![RAG (검색 증강 생성)](../images/agi_3.png)

RAG (검색 증강 생성)

### Retriever

- 사용자의 질의에 맞는 후보 문서를 저장소에서 찾아오는 모듈. RAG에서 첫 단계 역할
- Sparse Retriever (어휘적 유사도 기반)
    - TF-IDF, BM-25
- Dense Retriever (의미적 유사도 기반)
    - DPR, Contriever, Openai-embeddings

### Sparse Retriever

- 전통적인 IR 기법. 쿼리와 문서 간의 정확한 용어 일치, 즉 **어휘적 유사도**에 기반한다.
- 단순성, 효율성, 투명성
- 제한된 의미 이해
    - 예를 들어, 쿼리에는 ‘bad guy’라는 표현이 쓰였지만, 실제 문서에서는 ‘villain’이라는 단어가 사용되어 매칭되지 않는다.
- TF-IDF: 문서 내 특정 단어의 중요도를 나타내는 가중치 방식
    - TF (Term Frequency): 단어가 문서에 얼마나 자주 등장하는지 → 중요하다.
    - IDF (Inverse Document Frequency): 단어가 전체 코퍼스에서 얼마나 드물게 등장하는지 → 너무 많은 문서에 등장하는 단어는 덜 중요하다. (예: this, is ,and)

### Dense Retriever

- 쿼리와 문서를 표현하기 위해 dense vector를 활용해 **의미적 유사도**에 기반한다.
- 글의 문맥과 의미를 포착한다. 특히 복잡한 쿼리와 긴 검색 쿼리의 의미를 더 잘 포착할 수 있다.
- dense retriever는 블랙박스처럼 작동할 수 있어, 특정 문서가 왜 검색되었는지 해석하기 어렵다.
- 임베딩 모델 (Embedding Models): 단어, 문장의 의미를 표현할 수 있다.
- Bi-encoder: 두 문장을 따로 인코딩한다.
    - 대조 학습을 통해 학습되며, 쿼리가 긍정적인 문서와 가깝게 유지되도록 하고 부정적인 문서에서는 멀어지도록 유도한다.
- Cross-encoder: 두 개의 텍스트를 하나의 시퀀스로 결합해, 두 문장을 함께 처리한다.
    - self-attention을 통해 모든 쿼리와 문서 토큰이 완전히 상호작용할 수 있어, bi-encoder보다 더 높은 정확도를 얻을 수 있지만, 계산 비용이 크고 처리 속도가 느리다.

## RAG (Retrieval-augmented Generation, 검색 증강 생성)

### Retrieval-augmented LM

- 추론 시 외부 데이터 저장소를 불러와 활용하는 언어모델
- RAG (Retrieval-augmented Generation): 정보 검색부터 답변 생성까지의 프레임워크

### Retrieval-augmented LM의 구성 요소

- 구성 요소: Datastore, Query, Index, Language Model

![Retrieval-augmented LM의 구성](../images/agi_4.png)

Retrieval-augmented LM의 구성

- Datastore: 가공되지 않은 텍스트 코퍼스
    - 라벨링된 데이터셋이 아니다.
    - 지식베이스(Knowledge base)와 같은 구조화된 데이터가 아니다.
- Query: 검색 질의. Retrieval input
    - 언어모델의 질의 (input)와 같아야 하는 것은 아니다.
- Index: 문서나 단락과 같은 검색 가능한 항목들을 체계적으로 정리하여 더 쉽게 찾을 수 있도록 하는 것
    - 각 정보 검색 (information retrieval) 메서드는 인덱싱 과정에서 구축된 인덱스를 활용해 쿼리와 관련 있는 정보를 식별한다.
    - Nonparametric Knowledge는 parametric knowledge와 상호 보완적인 관계

### Retrieval-augmented LM를 사용하는 이유

- 거대 언어 모델은 모든 지식을 다 자신의 파라미터에 저장하지 못한다.
    - 거대 언어 모델은 사전학습 데이터에 자주 나타나는 쉬운 정보를 기억하는 경향성이 있다.
    - RAG는 자주 등장하지 않는 정보에 대해서 큰 효과를 가져다 준다.
- 거대 언어 모델이 보유한 지식은 금세 시대에 뒤쳐지며, 갱신이 어렵다.
    - 현재의 지식 편집 (Knowledge editing) 메서드들은 확장성이 부족하다.
    - 저장소 (Datastore)는 쉽게 업데이트가 가능하며, 확장성을 만족한다.
- 답변의 해석과 검증이 어렵다.
    - 환각 (Hallucination) 문제를 해결할 수 있다.
- 기업 내부 정보와 같은 보안 정보는 언어모델 학습에 활용되지 않는다.
    - 사내 챗봇/기업 내부 시스템에 언어모델을 사용하는 경우 내부 데이터를 학습 시 정보 유출의 위험성이 있다.

### Retrieval-augmented LM의 한계

- Context를 어떻게 구성해야 하는가?
    - 언어모델의 컨텍스트 길이 (Context length)를 늘려야 한다.
- 검색 노이즈에 취약하다.
    - RAG의 결과는 검색 모델 성능에 의존하기 때문
    - Context 안의 정보를 이용하려는 LLM의 경향성 때문에, 검색에서의 노이즈(정확하지 않은 유사 정보)가 Hallucination을 증가시킨다.
    - Training with Noises로 극복할 수 있다.
        - Noise Robustness: 노이즈가 포함되어 있어도 올바른 답을 찾아내는 능력
        - Negative Rejection: 없는 정보에 대해서 답변을 거부하는 능력

![Training with Noises 예시](../images/agi_5.png)

Training with Noises 예시

- LLM의 사전 지식과 컨텍스트 간의 충돌 발생
    - Context 위에서 Gronding 학습 강화
    - Context가 없을 때, 답변 회피/거절 학습
- 복잡한 추론이 필요하고 문서가 명확한 사실에 대한 오류를 포함할 때

### Tool Augmented LLM (Agent)

- Visual Programming
    - 언어 모델의 추가 학습 없이 주어진 툴을 사용하여 사용자가 텍스트로 요청한 영상 처리를 수행
- Claude Compute Use
    - 텍스트를 기반으로 컴퓨터를 사람처럼 사용할 수 있는 서비스
    - 컴퓨터가 수행하길 바라는 지시사항을 텍스트로 입력하면 자동으로 명령 수행


## Multi-Agent 시스템으로의 확장

![agent laboratory](../images/agi_1.png)

