# NLP (Natural Language Processing, 자연어 처리)

## 허깅페이스 (Hugging Face)

- 최신 NLP 딥러닝 기술을 누구나 쉽게 사용할 수 있도록 도와주는 플랫폼/라이브러리
- Models: 전세계 개발자들이 미리 학습시켜 둔 AI모델들
    - `klue/bert-base`: 한국어 처리를 위해 잘 학습된 모델. Transformer의 Encoder 구조를 기반으로 만들어짐.
- Tokenizer: 각 모델에 맞는 토크나이저
- Transformers: 모델과 토크나이저를 파이썬 코드로 사용할 수 있도록하는 시스템

### 모델 검색 및 필터링

- 허깅페이스 [Models 페이지](https://www.google.com/url?q=https%3A%2F%2Fhuggingface.co%2Fmodels)에서 검색할 때, 다양한 기준으로 검색 해 봅시다.

| **검색 기준** | **설명** | **필터링 예** |
| --- | --- | --- |
| 태스크 | 모델이 수행하는 처리 유형에 따라서 필터링 | text-classification (문장 분류), question-answering (질의응답), translation (번역) |
| 언어 | 모델이 지원하는 언어를 기준으로 필터링 | ko (한국어), en (영어), zh (중국어) 등 |
| 라이브러리 | 모델이 구현된 주요 라이브러리를 기준으로 필터링 | PyTorch, scikit, TensorFlow, JAX 등 |
| 모델 이름 | 특정 모델 이름, 저자, 또는 기술적 특징 등 | bert, gpt, google |

## 토큰화 (Tokenization)

### 토큰화 (Tokenization)

- 텍스트를 숫자로 변환하는 과정
- 딥러닝 모델은 숫자만 입력받을 수 있으므로, 텍스트를 모델이 이해할 수 있는 숫자 형태로 변환해야 한다.

### 말뭉치 (Corpus)

- 모델을 학습시키기 위해 사용하는 원본 텍스트 데이터 전체
    - 위키피디아 전체 텍스트, 뉴스 기사 10년 치, 특정 소설책 모음 등
- 모델이 언어의 패턴, 문법, 의미 등을 배우는 기반이 되는 학습 자료
- 문장, 문단, 문서 등 텍스트의 원본 형태를 그대로 유지한다.

### 단어 집합 (Vocabulary)

- 말뭉치에 있는 모든 텍스트를 단어 단위로 쪼갠 뒤, 중복을 제거하여 만든 고유한 단어들의 목록
    - 개별 단어들의 집합(Set) 형태
    - "나는 사과를 먹는다. 너는 바나나를 먹는다." (말뭉치) → `Vocabulary = {나, 는, 사과, 를, 먹는다, 너, 바나나}`
- 모델이 "알고 있는" 단어들의 공식적인 리스트
- 모델이 텍스트를 이해하고 처리할 수 있도록, 각 단어에 고유한 번호(인덱스)를 부여하는 기준

### 토크나이저 (Tokenizer)

- 문장을 토큰(Token) 단위로 나누고, 각 토큰을 정수(ID)로 변환하는 도구
    - 토큰 ID 시퀀스로 데이터를 변환하는 역할
- 컴퓨터가 글자를 이해하기 위한 첫 번째 번역 작업
- `special_tokens`: 모델이 문장의 구조를 이해하거나 특정 과제를 수행하기 위해 사용하는 특수 목적의 토큰
    1. `[CLS]`(Classification): 문장의 시작을 의미. 문장 전체 정보를 요약하는 역할
    2. `[SEP]` (Separator): 두 문장을 구분
    3. `[PAD]` (Padding): 여러 문장을 한번에 처리(배치 처리)할 때, 길이를 맞춰주기 위해 짧은 문장 뒤에 채워 넣음
        - ex) 배치 사이즈가 2일 때, 2개의 데이터. [’안녕’, ‘하세요.’] 문장과 [’저는’, ‘개발자’, ‘입니다.’] 문장을 한 번에 처리한다면, [’안녕’, ‘하세요.’, ‘[PAD]’] 와 같이 처리한다.
    4. `[UNK]` (Unknown): 사전에 없으면서 WordPiece로도 분해할 수 없는 단어를 위해 사용
    5. `[MASK]` (Masking): BERT의 사전 학습(Pre-training) 시, 단어를 가리는 용도로 사용

### Tokenizer 학습

```python
from tokenizers import BertWordPieceTokenizer

# 빈 tokenizer 생성 : vocabulary_size = 0 인 것을 확인하실 수 있습니다.
tokenizer = BertWordPieceTokenizer(
    lowercase=False,
    strip_accents=False,
)
tokenizer

data_file = 'naver_review.txt'
vocab_size = 30000
min_frequency = 2
initial_alphabet = []
limit_alphabet = 6000
special_tokens = ["[PAD]", "[UNK]", "[CLS]", "[SEP]", "[MASK]"]
wordpieces_prefix = "##"
show_progress=True

tokenizer.train(
    files = data_file,
    vocab_size = vocab_size,
    min_frequency = min_frequency,
    initial_alphabet = initial_alphabet,
    limit_alphabet = limit_alphabet,
    special_tokens = special_tokens,
    wordpieces_prefix = wordpieces_prefix,
    show_progress = True,
)

vocab = tokenizer.get_vocab()
print("vocab size : ", len(vocab))  # vocab size :  30000
print(sorted(vocab, key=lambda x: vocab[x])[:20])
# ['[PAD]', '[UNK]', '[CLS]', '[SEP]', '[MASK]', '!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/']
```

- `data_file` : 데이터 경로를 지정해줍니다. list 형태로 여러개의 파일을 지정해줄수도 있습니다.
- `vocab_size (default: 30000)` : 단어사전 크기를 지정할 수 있습니다. 어떠한 값이 가장 좋다는 것은 없지만, 값이 클수록 많은 단어의 의미를 담을 수 있습니다.
- `initial_alphabet` : 꼭 포함됐으면 하는 initial alphabet을 학습 전에 추가해줍니다.
    - initial은 학습하기 이전에 미리 단어를 vocab에 넣는 것을 의미합니다.
    - special token들도 initial에 vocab에 추가됩니다.
- `limit_alphabet (default: 1000)` : initial tokens의 갯수를 제한합니다.
- `min_frequency (default: 2)` : 최소 빈도수를 의미합니다. 만약 어떤 단어가 1번 나오면 vocab에 추가하지 않습니다.
- `special_tokens` : 특수 토큰을 넣을 수 있습니다.. BERT에는 다음과 같은 토큰이 들어가야 합니다.
    - `[PAD]` : 패딩을 위한 토큰
    - `[UNK]` : OOV 단어를 위한 토큰
    - `[CLS]` : 문장의 시작을 알리고 분류 문제에 사용되는 토큰
    - `[SEP]` : 문장 사이사이를 구별해주는 토큰
    - `[MASK]` : MLM 태스크를 위한 마스크 토큰
- `wordpiece_prefix(default: '##')` : sub-word라는 것을 알려주는 표시입니다.
    - BERT는 기본적으로 '##'을 씁니다.
    - 예를 들어, `SS, ##AF, ##Y` 처럼 sub-word를 구분하기 위해 '##'을 사용합니다.
- `show_progress` : 학습 과정을 보여줍니다.

### 코드 구현

- AutoTokenizer: 모델 이름만 알려주면 허깅페이스에서 해당 모델에 맞는 토크나이저를 자동으로 찾아주는 클래스

```python
# 1. 토크나이저 불러오기

from transformers import AutoTokenizer

# 'klue/bert-base'라는 책(모델)에 맞는 단어 사전을 빌려옵니다.
tokenizer = AutoTokenizer.from_pretrained("klue/bert-base")
```

```python
# 2. 문장 인코딩 및 결과 분석

text = "안녕하세요. 이 실습은 허깅페이스 토크나이저 사용법을 익히는 좋은 예제입니다."

# 토크나이저로 문장을 인코딩합니다.
encoded_input = tokenizer(text)

print(encoded_input)
# {'input_ids': [2, 5891, ...], 'token_type_ids': [...], 'attention_mask': [...]}
```

- `input_ids`: 각 토큰에 해당하는 정수 ID 리스트
- `token_type_ids`, `attention_mask`: 여러 문장을 처리하거나 문장 길이를 맞출 때 사용되는 추가 정보

```python
# 3. 토큰 직접 확인하기

# 정수 ID를 다시 토큰으로 변환합니다.
tokens = tokenizer.convert_ids_to_tokens(encoded_input['input_ids'])

print(tokens)
# ['[CLS]', '안녕', '##하', '##세요', '.', ..., '[SEP]']
```

- `[CLS], [SEP]`: 문장의 시작과 끝을 알리는 토큰
- `##세요`: 단어가 더 작은 의미인 서브워드(subword)로 나뉜 것
    - 사전에 없는 새로운 단어가 등장해도 유연하게 대처할 수 있게 해준다. (OOV 문제 해결)

### OOV (Out-of-Vocabulary)

- 모델을 학습시킬 때 사용했던 단어 집합 (Vocabulary)에 존재하지 않는 새로운 단어
- 전통적인 토큰화 방식에서는 모델이 OOV 단어를 만나면 보통 `[UNK]`(Unknown) 로 처리해버린다.
    - 모델의 성능을 저하하는 주요 원인
- **서브워드(Subword) 토큰화 방식**
    - 단어를 더 작은 의미 단위로 분리하여, OOV 문제를 해결할 수 있는 방법
    - 처음 보는 단어라도 익숙한 조각들의 조합으로 만들어 의미를 유추할 수 있다.

---

## 임베딩 (**Embedding)**

### 임베딩 (**Embedding)**

- 토큰에 부여된 단순한 정수 ID를, 단어의 의미를 함축한 고차원의 벡터 (Vector)로 변환하는 과정
- 임베딩 벡터는 단어의 의미, 문맥, 관계성을 **벡터 공간의 좌표값**으로 표현한다.
    - 정수 ID는 의미 관계를 담고 있지 않다.
    - 의미가 비슷한 단어들은 벡터 공간에서 가까운 위치에 존재한다.
    - 단어 간의 관계를 벡터 연산으로 표현할 수 있다.

### 토크나이저와 모델

- **반드시 토큰화에 사용한 토크나이저와 짝이 맞는 모델을 사용해야 한다.**
- 임베딩은 모델이 수행하는 작업
- klue/bert-base 토크나이저(사전)는 ‘안녕’을 8192번으로 번역
- klue/bert-base 모델(전문서적)은 8192번 단어가 어떤 의미인지 학습한 상태

### 코드 구현

- AutoModel: 모델 이름을 알려주면 허깅페이스에서 해당 모델 본체를 자동으로 찾아주는 클래스

```python
# 모델 불러오기
from transformers import AutoModel

# 토크나이저와 '똑같은 이름'의 모델을 빌려옵니다. 짝꿍!
model = AutoModel.from_pretrained("klue/bert-base")
```

- 인코딩된 input_ids를 모델에 넣어 최종 임베딩 벡터를 추출

```python
# ---- 토큰화 ----
# 1. 인코딩 시, 결과를 PyTorch 텐서 형태로 반환하도록 옵션을 추가합니다.
encoded_input = tokenizer(text, return_tensors='pt')

# ---- 임베딩 ----
# 2. 인코딩된 딕셔너리를 모델에 통째로 전달합니다. (**)
output = model(**encoded_input)

# 3. 모델의 여러 출력 중, 'last_hidden_state'가 우리가 원하는 최종 임베딩 벡터입니다.
embedding_vector = output.last_hidden_state

print(embedding_vector.shape) # torch.Size([1, 26, 768])
```

- `return_tensors='pt'`: 결과를 PyTorch 텐서 형태로 반환
- `torch.Size([1, 26, 768])`
    - `1 (Batch Size)`: 한 번에 처리한 문장의 개수
    - `26 (Sequence Length)`: 문장이 토큰화된 후의 토큰 개수 ([CLS] … [SEP])
    - `768 (Hidden Size)`: 하나의 토큰을 표현하는 벡터의 차원(숫자의 개수)
    - “문장을 구성하는 26개의 모든 토큰이 각각 768개의 숫자로 이루어진 ‘의미 벡터’로 성공적으로 변환되었습니다.”

### 임베딩 벡터

- 임베딩 벡터는 문장의 의미를 풍부하게 담고 있는 핵심 재료
- 임베딩 벡터를 시계열 모델(예: RNN, LSTM)이나, 오늘날 NLP의 표준이 된 Transformer 아키텍처에 입력으로 넣어주면, 모델이 문장의 맥락과 흐름을 깊이 이해하게 된다.
    - 내부적으로 Encoder, Decoder, Attention  메커니즘을 사용한다.
- NLP 작업: 감성 분석, 챗봇, 기계 번역 등
- 단어 간의 유사성을 측정할 수 있다.
    - **코사인 유사도**: 두 벡터가 고차원 공간에서 얼마나 같은 방향을 향하고 있는지를 측정하는 지표
    - 각도가 작을수록 코사인 값은 1에 가깝다. (같은 방향을 바라본다.)
    - 각도가 클수록 코사인 값은 -1에 가깝다. (완전히 반대 방향을 바라본다.)

```python
embedding_vector: Tensor2D[VocabSize, EmbeddingSize] = nn.Embedding(vocab_size, 768)
embedding_vector.weight.shape
```

- `num_embeddings`: 임베딩 사전의 크기 (size of the dictionary of embeddings)
- `embedding_dim`: 각 임베딩 벡터의 차원 (the size of each embedding vector)

### 임베딩 층(Embedding Layer)

- pytorch의 `nn.Embedding` 모듈을 활용하여 변환 과정을 진행 할 것
    - 학습 가능한 거대한 Lookup Table (가중치 행렬**)**
- 행렬 구성: `(단어 사전의 크기, 임베딩 벡터의 차원)`
    - 행: 단어 사전에 있는 토큰 하나하나에 해당한다. (전체 샘플)
    - 열: 벡터의 차원을 나타낸다. 차원의 크기가 클수록 더 복잡한 관계를 벡터에 담을 수 있다.
    - ex) `45`번 ID의 토큰 `나는` 을 10차원 벡터화 한다면, 이 가중치 행렬의 45번 행에 [1, 62, 4, 22, 81, 57, 7, 9, 10, 0] 형태의 벡터가 저장되는 셈

```python
import torch
import torch.nn as nn

vocab_size = 30000     # 챕터 1에서 정의한 단어 사전의 크기
embedding_dim = 768    # 각 단어를 표현할 벡터의 차원

# (30000, 768) 크기의 룩업 테이블(가중치 행렬)을 생성.
# 처음에는 임의의 값으로 초기화되어 있음.
embedding_layer = nn.Embedding(num_embeddings=vocab_size, embedding_dim=embedding_dim)

# 학습 과정에서 단어 간의 의미 관계를 포착하도록 업데이트 될 예정임.
# 현재는 초기화된 상태이므로, 임의의 값이 들어있음
print(embedding_layer.weight.shape)

# 예시: 단어 인덱스 45에 해당하는 단어의 임베딩 벡터 추출
word_index = 45
word_vector = embedding_layer.weight[word_index]
print(word_vector)
```
