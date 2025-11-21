# JavaScript 실습

## DOM 조작

### DOM

- 웹 페이지의 모든 내용을 JavaScript가 이해하고 조작할 수 있도록 만든 구조화된 모델
- DOM 조작과 Event 처리는 웹페이지를 단순히 정적인 문서가 아니라, 사용자와 끊임없이 대화하고 반응하는 살아있는 인터페이스로 만들어준다.

### DOM 조작과 Event 처리

- 즉각적인 피드백: 사용자와 상호 작용, 실시간 유효성 확인
- 효율적인 정보 관리: 평소에는 숨겨두었다가 필요할 때 보여준다.
- 시각적 매력과 몰입감: 사용자 서비스 이용 경험 개선

## CSS

### CSS animation

- 시작부터 끝까지 애니메이션의 전반적인 규칙을 정의한다.
    - `animation-name`: 어떤 동작을 할지 (Keyframes이름 지정)
    - `animation-duration`: 몇 초 동안 진행할지
    - `animation-timing-function`: 속도 변화 (느리게, 시작/끝 등)
- `@keyframes`: CSS 애니메이션의 개별 동작 단계와 변화 지점을 정의하는 규칙

```css
@keyframes pulse {
	0% {
		transform: scale(1);
		opacity: 1;
	}
	50% {
		transform: scale(1.2);
		opacity: 0.5;
	}	
	100% {
		transform: scale(1);
		opacity: 1;
	}
```

### CSS transforms

- 요소를 이동, 회전, 크기 조절, 기울이기 등
- `[function]([value]);`
    - `translate(x, y)`: x축과 y축으로 이동
    - `rotate(각도)`: 회전
    - `scale(x, y)`: x축과 y축 배율 조절
    - `skew(x각도, y각도)`: x축과 y축 기준으로 기울이기

```css
/* 움직임을 정의 이름은 shake */
/* 실행되면 제자리에서 좌로 갔다가 우로 갔다가 제자리로 돌아오는 움직임 정의 */
@keyframes shake {
    0%, 100% { transform: translateX(0); }  /* 시작과 끝은 제자리 */
    25% { transform: translateX(-5px); }    /* 25% 시점은 -5px 이동 (좌측) */
    75% { transform: translateX(5px); }     /* 75% 시점은 5px 이동 (우측) */
}
```

## Input Event

### Input Event

- 데이터를 입력할 때마다 발생하는 이벤트
- 요소의 값(value)이 변경될 때
- 붙여넣기에도 반응하는 유효성 검사 가능

### Keyup Event

- 키보드 키가 눌렸다가 떼어질 때
- 특정 키 (예: `Enter`)를 눌렀을 때만 동작 수행

 

### [실습] 텍스트 입력 제한

```html
<h1>텍스트 입력 제한 (20자)</h1>
<input type="text" class="text-input" id="textInput" placeholder="최대 20자">
<div class="counter" id="counter">0 / 20</div>

<script>
  const maxLength = 20  // 최대 문자 개수
  // (코드 작성) 사용자의 입력을 확인하기 위해 입력창 선택
  const textInput = document.querySelector('#textInput')
  // (코드 작성) 입력 문자 개수를 조작하기 위해 해당 요소 선택
  const counter = document.querySelector('#counter')

  // 사용자의 입력이 있으면
  textInput.addEventListener('input', function (e) {
    // 최대 길이를 넘기면 더 이상 입력을 받지 않고 class에 error를 추가하여 스타일링
    //   단, 일시적으로 스타일이 적용될 수 있도록 setTimeout 사용하여 class error 제거
    // (코드 작성) 

    // 입력 값을 확인
    // console.log(e.target.value.length)
    
    if (e.target.value.length > 20) {
      // 0~20까지의 값만 슬라이싱해서 value 덮어쓰기 (20자까지만 출력)
      e.target.value = e.target.value.substring(0, 20)

      // error 클래스(shake 애니메이션) 추가 후, 0.5초 지나면 클래스 제거
      e.target.classList.add('error')
      setTimeout(function () {
        e.target.classList.remove('error')
      }, 500)
    }

    // 글자 수 표시
    counter.textContent = `${e.target.value.length} / ${maxLength}`
  })
</script>
```

### Drag Event

- 웹 페이지의 요소를 끌어서 이동시키는 과정에서 발생하는 이벤트
- 드래그 하려는 HTML 요소에 `draggable="true"` (기본값: false) 속성을 추가해야 요소가 드래그될 수 있다.
- 끌기 시작부터 끌기 종료까지 모든 단계에서 순서대로 발생하는 여러 개의 이벤트 그룹
    - `dragstart`: 사용자가 요소를 끌기 시작하는 순간 끌리는 요소에서 발생
    - `drag`: 사용자가 요소를 끌고 다니는 과정 동안 끌리는 요소에서 계속 발생
    - `dragend`: 사용자가 마우스 버튼을 놓거나 드래그가 끝나는 순간 끌리는 요소에서 발생
    - `dragenter`: 끌고 있는 요소가 대상 영역 위로 들어올 때 해당 영역에서 발생
    - `dragover`: 끌고 있는 요소가 대상 영역 위에 머물고 있는 동안 해당 영역에서 발생
        - 기본 동작을 취소해야 drop 가능
    - `dragleave`: 끌고 있는 요소가 대상 영역 밖으로 벗어날 때 해당 영역에서 발생
    - `drop`: 끌고 있던 요소를 대상 영역 위에 놓는 순간 해당 영역에서 발생

### [실습] 카드 순서 바꾸기

- 현재 드래그 중인 마우스 포인터의 위치와 바닥의 카드의 중심의 위치를 계산
    - 포인터가 가운데보다 앞쪽이면, 드래그 카드는 **바닥 카드 앞**에 위치
    - 포인터가 가운데보다 뒤쪽이면, 드래그 카드는 **바닥 카드 뒤**에 위치

```jsx
// 드래그 이벤트를 추가하기 위해 선택
const container = document.querySelector('#card-container')
let draggedCard = null  // 드래그 중인 카드 저장 변수

// 1. 드래그 시작 리스너
// 현재 드래그 중인 것을 표시하기 위함
container.addEventListener('dragstart', (e) => {
  // (코드 작성) 드래그 카드 저장
  draggedCard = e.target
  e.target.classList.add('dragging')
})

// 2. 드래그 중
// 드래그 위치를 계산해서 카드가 들어갈 곳을 표시하기 위함
// 모든 카드의 위치를 가져온 다음
// 드래그 중인 카드의 위치와 가장 가까운 카드를 찾고
// 드래그 중인 카드가 해당 카드 앞에 있는지 뒤에 있는지를 판단하여 위치를 이동
container.addEventListener('dragover', (e) => {
  // (코드 작성) 기본 이벤트 중지
  e.preventDefault()
  // (코드 작성) 드래그 중이 아닌 카드를 전부 선택
  const otherCards = container.querySelectorAll('.card:not(.dragging)')
  // (코드 작성) 드래그 중인 카드와 가장 가까운 카드찾기 위한 초기화
  const mouseX = e.clientX  // 드래그 중인 마우스 x좌표
  // 가장 가까운 카드를 찾자
  let closestCard = null
  let closestCardCenter = null
  let minDistance = Infinity

  // (코드 작성) 가장 가까운 카드 찾는 알고리즘 구현
  otherCards.forEach(function (card) {
    const rect = card.getBoundingClientRect()
    const cardCenter = rect.left + rect.width/2

    const distance = Math.abs(mouseX - cardCenter)

    if (distance < minDistance) {
      minDistance = distance
      closestCard = card
      closestCardCenter = cardCenter
    } 
  })

  // (코드 작성) 드래그 중인 카드 위치 변경
  if (closestCard) {
    if (mouseX < closestCardCenter) {
      container.insertBefore(draggedCard, closestCard)
    } else {
      container.insertBefore(draggedCard, closestCard.nextSibling)
    }
  }
    
})

// 3. 드래그 종료
// 드래그 중 표시를 제거하기 위함
container.addEventListener('dragend', (e) => {
  // (코드 작성) 드래그 카드 초기화
  draggedCard = null
  e.target.classList.remove('dragging')
})
```

### Scroll Event

- 웹 페이지의 콘텐츠를 상하좌우로 이동(스크롤)할 때마다 지속적으로 발생하는 이벤트
- `window.scrollY`: 브라우저 창의 수직 스크롤 위치
- `element.scrollHeight`: 요소에 포함된 전체 콘텐츠의 높이로 스크롤되지 않은 부분까지 포함되며, 총 길이를 파악하여 스크롤 막대의 끝에 도달했는지 확인할 때 사용

### [실습] 스크롤시 나타나는 요소

- 투명하게 설정된 요소의 상단 위치를 스크롤 이벤트가 발생할 때마다 확인
- 특정 위치에 도달하면 투명도를 JS 로 조절

```jsx
// (코드 작성) 카드 요소들 선택
const cards = document.querySelectorAll('.card')
// 스크롤 이벤트 처리 함수
function checkScroll() {
  const windowHeight = window.innerHeight  // 현재 창의 높이

  // (코드 작성) 카드 별로 특정 위치에 오면 나타나도록 설정
  cards.forEach(function (card) {
    const cardTop = card.getBoundingClientRect().top
    
    if (cardTop < windowHeight) {
      card.classList.add('visible')
    }
  })
}

// 스크롤 이벤트 리스너
window.addEventListener('scroll', checkScroll)
```

### [실습] 스크롤 진행도 표시

- 스크롤 진행률 = 현재 스크롤 위치 / 스크롤 이동 가능 범위
    - 스크롤 이동 가능 범위 = 전체 높이 - Viewport 높이

```jsx
const progressFill = document.querySelector('.progress-fill')

function updateProgress (e) {
  // (코드 작성) 현재 스크롤의 위치
  const scrollY = window.scrollY

  // (코드 작성) 진행률 계산
  const scrollHeight = document.documentElement.scrollHeight - window.innerHeight
  const progress = scrollY / scrollHeight
  
  // DOM에 진행률 업데이트
  progressFill.style.transform = `scaleX(${progress})`
}

// 스크롤 이벤트는 윈도우에서 발생하는 이벤트
window.addEventListener('scroll', updateProgress)

```

### [실습] Parallax Scroll

- 스크롤할 때 화면의 배경과 앞에 보이는 내용(레이어들)이 **서로 다른 속도**로 움직여, 화면에 깊이나 3D같은 입체감을 주는 시각적 효과
- 예시 사이트: https://www.cyclemon.com/

```jsx
// (코드 작성) 각 요소 선택
const layerBack = document.querySelector('.layer-back')
const layerMiddle = document.querySelector('.layer-middle')
const layerFront = document.querySelector('.layer-front')
// 각 레이어의 속도 설정
const speeds = {
  back: 0.2,
  middle: 0.3,
  front: 0.4
}

window.addEventListener('scroll', () => {
  const scrolled = window.scrollY // 현재 스크롤 위치

  // (코드 작성) 각 레이어를 다른 속도로 이동
  layerBack.style.transform = `translateY(${-scrolled * speeds.back}px)`
  layerMiddle.style.transform = `translateY(${-scrolled * speeds.middle}px)`
  layerFront.style.transform = `translateY(${-scrolled * speeds.front}px)`
})
```

### [실습] 가로, 세로 스크롤 혼합

- 스크롤하다가 horizontal-container 영역에서 가로 스크롤이 동작할 영역
- 스크롤을 하게 되면 horizontal-container의 top 위치가 이동함
- horizontal-container의 top의 위치가 스크롤되어 이동하는 거리만큼 horizontal-track의 위치도 이동하여 화면에 출력된다.

```jsx
// 필요한 요소들 가져오기
const horizontalContainer = document.querySelector('.horizontal-container')
const horizontalTrack = document.querySelector('.horizontal-track')

// 가로 스크롤 위치 업데이트 함수
function updateHorizontalPosition() {
  // getBoundingClientRect: 요소의 화면상 위치 정보
  const containerRect = horizontalContainer.getBoundingClientRect()
  const containerHeight = horizontalContainer.offsetHeight // 컨테이너 전체 높이 (500vh)
  const windowHeight = window.innerHeight // 브라우저 창 높이

  // 가로 스크롤 영역(horizontal-container)이 화면에 보이는 동안만 실행
  if (containerRect.top <= 0 && containerRect.bottom >= windowHeight) {
    // 스크롤 진행률 계산 (0에서 1 사이 값)
    // Math.abs: 절댓값, containerRect.top은 음수가 됨 (요소가 화면을 벗어나기 때문)
    const scrollProgress = Math.abs(containerRect.top) / (containerHeight - windowHeight)

    // 가로 이동 거리 계산
    const maxMove = 400 // 4페이지 이동 (페이지1은 고정, 2~5페이지 이동 = 400vw)
    const moveDistance = scrollProgress * maxMove

    // translateX로 가로 이동 적용 (-는 왼쪽으로 이동)
    horizontalTrack.style.transform = `translateX(-${moveDistance}vw)`
  }
}

// 스크롤 이벤트 리스너 등록
window.addEventListener('scroll', updateHorizontalPosition)
```