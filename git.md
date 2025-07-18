
# 추가 학습

Working Directory -> Staging Area -> Repository
- Working Directory: 현재 작업 공간
- Staging Area: commit 하기 전에 버전으로 만들 후보들을 가지고 있다가 선택하기까지 대기하는 곳
- Repository: 선택한 변경 사항들이 저장되는 공간

<br>
하나의 로컬 저장소에서 여러 개의 원격 저장소<br>→ 가능. 별칭을 다르게 함(origin, second, …)

하나의 원격 저장소에 여러 개의 로컬 저장소<br>→ 가능. 협업할 때 그렇게 쓰라고 만든 거.

<br>
git은 파일만을 추적한다. 디렉토리의 생성/삭제는 관심없고, 디렉토리 내부의 파일에만 관심이 있다.

<br>

### *Q1. commit history 중 중간에 있는 commit을 삭제해도 되는가? 가능하다면 사라진 commit에 대한 공백은 어떻게 처리되는가?*

### A1. 가능하다. commit hash가 바뀐다.
*(아래는 ChatGPT의 답변)*
>#### 1. **히스토리에서 해당 커밋은 완전히 사라짐**
>
>Git은 커밋 간을 연결 리스트처럼 관리합니다. 커밋 A → B → C → D라고 하면, B를 삭제하면 Git은 A에서 바로 C로 연결되는 새 히스토리를 만들어요.
>즉, 삭제된 커밋은 Git 객체 저장소에는 남아 있을 수 있지만, **브랜치 히스토리에서는 더 이상 참조하지 않게 됩니다.**
>
>#### 2. **커밋 ID(해시)가 바뀜**
>
>Git 커밋은 부모 커밋 ID와 커밋 내용에 따라 해시가 결정되므로, 중간 커밋을 삭제하면 그 이후 모든 커밋의 ID가 달라집니다.
>즉, **"공백"은 생기지 않고, 대신 새로운 히스토리로 재구성**돼요.
>
>#### 3. **협업 중이라면 매우 주의해야 함**
>
>이미 원격(`origin`)에 푸시한 상태에서 히스토리를 변경하고 다시 푸시하면, `git push --force` 또는 `--force-with-lease`를 사용해야 하고 **다른 사람의 로컬 저장소와 충돌 가능성**이 큽니다.
>이로 인해 협업자들이 충돌 해결을 해야 하므로, 공유 브랜치(main, develop 등)에서는 가급적 피해야 해요.
    
<br>

### *Q2. 협업할 때(하나의 원격, 여러 개의 로컬), 로컬 A와 로컬 B가 각각 commit한 내용을 push하면 충돌이 일어나는가? (예를 들어, 두 로컬이 같은 commit1,2 기반으로 다른 commit3을 만든 경우)*
### A2. 충돌이 발생한다. 먼저 push한 쪽은 성공, 나중에 push하려는 쪽은 실패한다.
*(아래는 ChatGPT의 답변)*
    
> 두 로컬에서 다른 커밋을 같은 브랜치에 push하려고 할 때, Git은 히스토리가 일치하지 않으면 push를 거부합니다. 이를 non-fast-forward 업데이트라고 해요.
>
>### 해결방법
>
>로컬 B는 push 전에 **먼저 원격 변경사항을 병합하거나 리베이스**해야 합니다:
>
>#### 🔁 방법 1: merge
>
>```bash
>bash
>복사편집
>git pull origin main       # 병합
>git push origin main       # 이제 push 가능
>```
>
>#### 🔁 방법 2: rebase (히스토리 정리형)
>
>```bash
>bash
>복사편집
>git fetch origin
>git rebase origin/main     # 원격 기준으로 재정렬
>git push origin main       # 이제 push 가능
>```
>
>※ 리베이스는 커밋 로그를 깔끔하게 만들 수 있지만, 협업 중에는 충돌 해결이 필요하므로 주의해서 사용해야 해요.

<br>

### *Q3. GitHub 원격 저장소에서 브랜치 이름을 `main`에서 `master`로 변경했을 경우*

### A3. 로컬 저장소의 터미널에 다음을 입력한다.
```bash
git branch -m main master #브랜치 이름을 main → master로 바꿈
git fetch origin #원격 저장소의 최신 정보(특히 브랜치)를 받아옴
git branch -u origin/master master #로컬 master 브랜치가 원격 origin/master를 따라가게 설정
git remote set-head origin -a #로컬 Git이 인식하는 원격 저장소의 기본 브랜치 정보를 갱신함
```

<br>

### *Q4. commit 1,2,3까지 있을 때 commit 1로 reset한 경우. commit 4를 만들고 난 후에 commit 3을 복구할 수 있을까?*

### A4. 복구할 수 있다. 그러나 commit 4는 사라진다. commit 1-2-3과 commit 1-4는 각각 다른 세계관에 있기 때문에 공존할 수 없다!
*(아래는 terminal 입력 내용)*
```bash
# commit 1,2,3 이 있는 상황
SSAFY@2□□PC049 MINGW64 ~/Downloads/revert-reset-practice/reset-revert-practice/reset/soft (master)
$ git log --oneline
d7c8501 (HEAD -> master) third
91cbd74 second
f7b3a3d first

# commit 1로 돌아감. commit 2,3은 삭제됨.
SSAFY@2□□PC049 MINGW64 ~/Downloads/revert-reset-practice/reset-revert-practice/reset/hard (master)
$ git reset --hard f7b3
HEAD is now at f7b3a3d first

# 4.txt 생성
SSAFY@2□□PC049 MINGW64 ~/Downloads/revert-reset-practice/reset-revert-practice/reset/hard (master)
$ touch 4.txt

# 변경사항 staging area에 추가
SSAFY@2□□PC049 MINGW64 ~/Downloads/revert-reset-practice/reset-revert-practice/reset/hard (master)
$ git add .

# commit 4 생성
SSAFY@2□□PC049 MINGW64 ~/Downloads/revert-reset-practice/reset-revert-practice/reset/hard (master)
$ git commit -m 'four'
[master 66037a7] four
 2 files changed, 0 insertions(+), 0 deletions(-)
 create mode 100644 4.txt
 create mode 100644 untracked.txt

# commit history 확인 -> commit 1,4
SSAFY@2□□PC049 MINGW64 ~/Downloads/revert-reset-practice/reset-revert-practice/reset/hard (master)
$ git log
commit 66037a76c923b673d523054d4a2a2608d1601177 (HEAD -> master)
Author: ajjoona <ajjoona@gmail.com>
Date:   Fri Jul 18 10:37:07 2025 +0900

    four

commit f7b3a3d879dbfcab4ae90f1c3c7050ef0cd29913
Author: eduharryjjun <eduharryjjun@gmail.com>
Date:   Thu Oct 12 21:23:08 2023 +0900

    first

# commit 3 복구
SSAFY@2□□PC049 MINGW64 ~/Downloads/revert-reset-practice/reset-revert-practice/reset/hard (master)
$ git reset --hard d7c8
HEAD is now at d7c8501 third

# commit history 확인 -> commit 1,2,3 / commit 4 없어짐
SSAFY@2□□PC049 MINGW64 ~/Downloads/revert-reset-practice/reset-revert-practice/reset/hard (master)
$ git log
commit d7c85015ea5776d87ee6b494f869644d065af6ee (HEAD -> master)
Author: eduharryjjun <eduharryjjun@gmail.com>
Date:   Thu Oct 12 21:24:20 2023 +0900

    third

commit 91cbd74ec969ce40577658673789755440b7bd18
Author: eduharryjjun <eduharryjjun@gmail.com>
Date:   Thu Oct 12 21:24:04 2023 +0900

    second

commit f7b3a3d879dbfcab4ae90f1c3c7050ef0cd29913
Author: eduharryjjun <eduharryjjun@gmail.com>
Date:   Thu Oct 12 21:23:08 2023 +0900

    first

# commit 이력 확인
SSAFY@2□□PC049 MINGW64 ~/Downloads/revert-reset-practice/reset-revert-practice/reset/hard (master)
$ git reflog
d7c8501 (HEAD -> master) HEAD@{0}: reset: moving to d7c8
66037a7 HEAD@{1}: commit: four
f7b3a3d HEAD@{2}: reset: moving to f7b3
d7c8501 (HEAD -> master) HEAD@{3}: reset: moving to d7c8
f7b3a3d HEAD@{4}: reset: moving to f7b3
d7c8501 (HEAD -> master) HEAD@{5}: commit: third
91cbd74 HEAD@{6}: commit: second
f7b3a3d HEAD@{7}: commit (initial): first

# 다시 commit 4를 복구
SSAFY@2□□PC049 MINGW64 ~/Downloads/revert-reset-practice/reset-revert-practice/reset/hard (master)
$ git reset --hard 66037
HEAD is now at 66037a7 four

# commit history 확인 -> commit 1,4 / commit 1,2,3 없어짐
SSAFY@2□□PC049 MINGW64 ~/Downloads/revert-reset-practice/reset-revert-practice/reset/hard (master)
$ git log --oneline
66037a7 (HEAD -> master) four
f7b3a3d first
```

<br><br>

# 학습 내용
## git | 분산 버전 관리 시스템
### 버전 관리

- **변화**를 기록하고 추적하는 것
- 일반 문서를 저장하면 최종본만 확인할 수 있음 그러나 버전 관리를 하면 특정 과거로 돌아갈 수 있음
- 변화(변경사항)만 기록하기 때문에 **용량 관리**도 효율적

ex. google docs - 버전 기록

### 분산 구조의 장점

- 중앙서버에 의존하지 않아 동시에 다양한 작업 수행가능
    - 개발자들 간의 작업 충돌을 줄여주고 개발 생산성을 향상
- 중앙 서버의 장애나 손실에 대비하여 백업과 복구 용이
- 인터넷에 연결되지 않은 환경에서도 작업을 계속할 수 있음
    - 로컬 저장소에 기록했다가 나중에 중앙 서버와 동기화

> **로컬 Local**<br>
> : 현재 사용자가 직접 접속하고 있는 기기 또는 시스템. 개인 컴퓨터, 노트북, 태블릿 등 사용자가 직접 조작하는 환경

### git의 역할

- 코드의 버전(히스토리) 관리
- 개발되어 온 과정 파악
- 이전 버전과의 변경 사항 비교 → 과거로의 회귀 가능

⇒ 코드의 **‘변경 이력’**을 기록하고 **‘협업’**을 원활하게 하는 도구

## git의 영역

### Working Directory

실제 작업 중인 파일들이 위치하는 영역 (보임)<br>
개발자와 함께 바라보고 있는 환경

### Staging Area

working directory에서 **변경된 파일 중**, 다음 버전에 포함할 파일들을 **선택적으로 추가하거나 제외**할 수 있는 중간 준비 영역 <br>
변경 사항들을 추적하고 있다가 버전으로 만들게 되는데, 그 중간 단계 (보이지 않음)<br>

### Repository

버전 이력과 파일들이 **영구적으로 저장**되는 영역 (보이지 않음) <br>
**모든 버전과 변경 이력**이 기록됨 <br>
협업에서 중요함

버전 = commit; 변경된 파일들을 저장하는 행위 like a snapshot

## git의 동작

### git +명령어

`git init` (initialization) 로컬 저장소 설정(초기화)

- git 버전 관리를 시작할 **디렉토리**에서 진행. git은 각 프로젝트에서 실행한다.

- `(master)` git 저장소 영역. 현재 git 사용 중

`git add sample.txt` 변경 사항이 있는 파일을 staging area에 추가. [working directory → staging area]

`git add .` 현재 디렉토리 내의 전체 파일을 추가

- 파일 내용을 수정했다면 저장을 꼭 한 후에 add하자. 저장하지 않으면 변경사항이 반영되지 않음(파일을 새로 생성한 경우 제외. 이 경우에도 빈 파일로 올라감)

`git status` working directory, staging area의 상태를 볼 수 있음

- 빨간색 : working directory → untracked, modified
- 초록색 : staging area


`git commit` 저장소에 기록. 해당 시점의 버전을 생성하고 변경 이력을 남기는 것. [staging area → repository]

- `-m 'message name'` (message) commit message name. 변경 사항을 간단히 표시
    - commit은 hash값으로 구분되므로 메시지명이 같아도 저장할 수 있다.

- `--amend` Vim 에디터를 통해 1)commit 메시지 수정, 2)commit 전체 수정 

    → commit의 hash 값이 바뀜. 기존 commit이 새로운 commit으로 **덮어쓰기** 되는 것.

    - 불필요한 commit을 생성하지 않고 직전 commit을 수정할 수 있다.

    - 버전 관리 측면에서 사소한 실수(앗, 빠진 파일 넣었음, 이전commit에서 오타 살짝 고침)는 유효한 commit으로 보기 어려워서 생긴 기능 

    >### Vim 에디터
    >1. 수정 모드: 내용을 작성하는 모드
    >2. 명령 모드: 쓰기, 삭제, 나가기, …
    >
    >- 명령 → 수정 : `i`
    >- 수정 → 명령 : `ESC`
    >- 명령은 `:` 콜론 이후에 특정 키워드를 입력하여 작성
    >- `w` 쓰기, `q` 나가기


`git config` (configuration) 설정 변경

- `--global user.email "abc@example.com"` 책임자의 서명 필요 → 이메일, 이름

- `--global user.name "name"`

- `--global -l` git global 설정 정보 보기

`git log` commit history 출력. repository의 상태 확인

- `--oneline`commit 목록 한 줄로 보기



## git 주의사항

### 1. git 저장소 내부에 git 저장소는 위치할 수 없다.

- 상위 git 저장소가 더 이상 트랙킹할 수 없기 때문

- (master)인 상태에서는 git을 만들지 마라.

### 2. git init을 하는 순간 어떤 숨김 폴더가 생성된다.

- 잘못 init한 git은 숨김 폴더(.git)를 삭제하면 됨


## Remote Repository

### 원격 저장소 (≠드라이브)

코드와 버전 관리 이력을 온라인 상의 특정 위치에 저장하여 여러 개발자가 협업하고 코드를 공유할 수 있는 저장공간
ex. GitLab(기업체에서 많이 사용), GitHub

### Local Repository → GitHub Repository

`git remote add origin remote_rep_url` 

- `git remote` 로컬 저장소에 원격 저장소 추가
- `origin` 추가하는 원격 저장소 별칭
    - 별칭을 사용해 로컬 저장소 한 개에 여러 원격 저장소를 추가할 수 있음
    - 대부분 첫 번째 별칭은 origin
    - 별칭은 사용자(나)를 위해 정하는 것. 원격 저장소는 전혀 모르는 내용.
- `remote_repo_url` 추가하는 원격 저장소 주소(URL)
- remote ≠ 연결

`git remote -v` 등록된 remote repository 확인


`git push origin master` 원격 저장소에 **commit 목록**을 업로드

“git아, push해줘. origin이라는 이름의 원격 저장소에 master 라는 이름의 브랜치를”

- 최초 push할 때는 인증서(git credential) 발급이 필요. 권한을 확인하는 과정
    
- 변경사항 만큼만 업로드 → **commit 히스토리가 같지 않다면 push 불가**
- 원격 저장소에는 commit(변경사항)만이 올라가는 것 → commit 이력이 없다면 push 할 수 없다!!
- repository 생성 시에 README.md 자동 생성 했을 경우 → clone부터 진행해야 한다.

### Local Repository ← GitHub Repository

`git pull origin master` 원격 저장소의 **변경사항만**을 받아옴(**업데이트**) / 이어가는 상황

`git clone remote_repo_url` 원격 저장소 **전체를 복제(다운로드)** / 처음 받는 상황

- clone으로 받은 프로젝트는 이미 git init이 되어 있음


## .gitignore

git에서 특정 파일이나 디렉토리를 추적하지 않도록 설정하는 데 사용되는 텍스트 파일

프로젝트에 따라서 공유하지 않아야 하는 것들도 존재하기 때문

한번이라도 commit을 받은(git의 관리를 받은 이력이 있는) 파일이나 디렉토리는 나중에 gitignore에 작성해도 적용되지 않음 → 초기에 설정하자.

(비상시) `git rm --cached` 통해 git 캐시에서 삭제 필요

[gitignore 목록 생성 서비스](https://www.toptal.com/developers/gitignore/)

## GitHub은 어디에 활용할까?

### 협업

### 포트폴리오

1. **TIL** (Today I learned)
    - 매일 내가 배운 것을 마크다운으로 정리해서 문서화하는 것
    - 단순필기 **+ 스스로 더 나아가 어떤 학습을 했는지**
    - ‘문서화’ 능력; 내 생각을 정리하고 팀에게 공유할 수 있는 능력
        - 개발도구의 공식 레퍼런스를 보고 사용법을 스스로 익힐 수 있음
        - 자신이 경험한 사용법을 문서화해서 팀 내에 전파할 수 있음
2. 프로필 꾸미기
    - user name 과 repository name이 같아야 함
    - README.md 파일 생성됨
3. 개인, 팀 프로젝트 코드를 공유
4. 오픈 소스 프로젝트에 기여

## git 수정하기
### Git revert

`git revert <commit id>` 특정 commit을 없었던 일로 만드는 작업 = “재설정”

- 기본적으로 commit은 지우지 않는다.
- 대신 프로젝트 기록에서 commit을 없었던 일로 처리하고 그 결과를 새로운 commit으로 추가한다. 기록에서 commit이 사라지지는 않는다.
- commit은 유기적으로 연결되어 있고 commit history가 변하면 꼬이기 때문.
- `<commit id>` 는 commit의 hash값 (4자 이상 작성)
- 변경사항을 쌓아 올리는 순방향 실행 취소 작업. 과거로 돌아가는 대신 새로운 미래를 쌓는다.
- git에서 기록이 손실되는 것을 방지하며 기록의 무결성과 협업의 신뢰성을 높인다.


### Git reset

`git reset [option] <commit id>` 특정 commit으로 되돌아가는 작업 = “되돌리기”

- 현업에서는 사용하지 않는다. 개인적인 사용에서는 간혹 쓰임.
- 특정 commit으로 되돌아 갔을 때, 되돌아간 commit 이후의 commit은 기록에서 모두 삭제된다.
- 과거로 돌아가 다시 시작한다.
- `[option]` 삭제되는 commit들의 **기록을 어떤 영역에 남겨둘 것인지**를 조정
    - `--soft` staging area에 남김
    - `--mixed(default)` working directory에 남김
    - `--hard` 삭제된 commit의 기록을 남기지 않음
- 단, 한번도 등록되지 않은 파일은 영향을 받지 않는다. (untracked.txt)

`git reflog` HEAD가 이전에 가리켰던 모든 commit을 보여줌

### Git restore

`git restore` modified 상태의 파일 되돌리기

- working directory 에서 파일을 수정한 뒤, 파일의 수정 사항을 취소하고, 원래 모습대로 되돌리는 작업
- 파일을 수정하고 저장(`ctrl+S`)하면 → modified 상태
- `git restore` 하면 수정하기 전 상태로 돌아간다.
- 원래 파일로 “덮어쓰는” 원리이기 때문에 수정한 내용은 전부 사라진다.
- 수정 취소 후에는 해당 내용을 **복구할 수 없다**.

### Unstage 하기

`git rm --cached` staging area에서 working directory로 되돌리기

- git 저장소에 commit이 없는 경우
- to unstage and remove paths only from the staging area

`git restore --staged` 

- git 저장소에 commit이 존재하는 경우
- the contents are restored from HEAD

### branch

- branch는 각각의 독립된 작업 영역이라고 볼 수 있다.
- master 에는 사용자에게 서비스할 수 있는 완성본만 올린다.