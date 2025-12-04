## Lifecycle Hooks

### Lifecycle Hooks

![image.png](../images/computed-lifecycle_6.png)

- Vue  컴포넌트가 생성되고, DOM에 마운트되고, 업데이트되고, 소멸되는 각 생애주기 단계에서 실행되도록 제공되는 함수
- 개발자는 컴포넌트의 특정 시점에 원하는 로직을 실행할 수 있다.

### 주요 Hooks

- `onMounted`: 컴포넌트가 초기 렌더링을 마치고 DOM 노드가 생성된 직후 실행된다.
    - DOM 직접 접근, 초기 데이터 fetching 등
- `onUpdated`: 반응형 데이터 변경으로 DOM이 업데이트된 후 실행된다.
- `onUnmounted`: 컴포넌트가 해제(삭제)된 후 실행된다.
    - 타이머 제거, 이벤트 리스너 해제 등


```html
<!-- Lifecycle hooks를 활용한 Cat 애플리케이션 -->
<!-- mounted 시점에 api 요청하면서 애플리케이션 시작하기 -->
<div id="app">
  <button @click="getCatImage">냥냥펀치</button>
</div>

<script src="https://cdn.jsdelivr.net/npm/axios/dist/axios.min.js"></script>
<script src="https://unpkg.com/vue@3/dist/vue.global.js"></script>
<script>
  const { createApp, ref, onMounted } = Vue
  
  const app = createApp({
    setup() {
      const getCatImage = function () {
      const URL = 'https://api.thecatapi.com/v1/images/search'
      
        axios({
          method: 'get',
          url: URL,
        })
          .then((response) => {
            imgUrl = response.data[0].url
            return imgUrl
          })
          .then((imgData) => {
            imgElem = document.createElement('img')
            imgElem.setAttribute('src', imgData)
            document.body.appendChild(imgElem)
          })
          .catch((error) => {
            console.log('실패했다옹')
          })
      }

      // mounted 시점에 api 요청하기
      onMounted(() => {
        getCatImage()
      })

      return { getCatImage }
    }
  })

  app.mount('#app')
</script>
```

![image.png](../images/computed-lifecycle_7.png)

### Lifecycle Hooks 주의사항

- Lifecycle Hooks는 반드시 **동기적**으로 작성해야 한다.
    - Vue는 컴포넌트가 초기화될 때 모든 Hooks를 한 번에 스캔하고 준비하기 때문
- 비동기(예: setTimeout)로 훅을 등록하려고 하면, 이미 Lifecycle 단계가 지나간 후에 hooks를 설정하는 상황이 생긴다.
    - Vue는 해당 훅을 인식하지 못하며 원래 의도한 타이밍에 실행되지 않게 된다.

