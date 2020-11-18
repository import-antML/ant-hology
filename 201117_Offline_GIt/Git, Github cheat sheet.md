### Git / Github

1. Git 기초

   1. Git 로컬 저장소

      1. `git init` : 시작
      2. `git status` : git의 상태 확인하기
      3. `git add` : staging area에 담기
         1. `git add .`
         2. `git add '*.py'`
         3. `git add 'test.py'`
      4. `git reset` : commit한 것 되돌리기
         1. `git reset --soft`: commit만 되돌리기
         2. `git reset`: staging한 것 까지 되돌리기
         3. `git reset --hard` : working dir 까지 다 날려버림
         4. `git reset HEAD xxx.txt` : 해당 파일 add한 것을 취소하겠음.
      5. `git commit ` : 버전 업데이트 하기
         1. `git commit -m '커밋할 내용'`
         2. `git commit --amend` : 방금 전 커밋한 것의 메세지를 바꿔 덮어 쓰겠다.
            1. 아 맞다 이거도 커밋해야함. 이라는 메시지를 남기지 않기 위함
      6. `.gitignore 파일` : 해당 파일에 git에 어떠한 영향을 받지 않는 파일 목록을 기록
         1. 보통 Dataset이나 로컬 설정, 보안이 필요한 파일 등을 표시한다.
      
2. Git 원격 저장소
   
   1. 일반적으로는 Github, Gitlab, Bitbucket
      2. 로컬에 있어도 remote라고 한다.
      3. 접속가능한 주소가 있고 해당 저장소를 remote로 등록한다면 pull push 할 수 있다.
      4. `git remote add {리모트별명지정} {주소}` : 해당 원격 저장소를 내 로컬에 등록한다.
   
3. 브랜치
   
   ![브랜치](https://git-scm.com/book/en/v2/images/advance-testing.png)
   
   1. `git branch [이름] ` : 브랜치 생성
         1. `git branch -d [이름]  `: 브랜치 삭제하기
      2. `git checkout` : 브랜치로 이동하기 (HEAD를 바꾸기)
         1. 브랜치를 이동하면 워킹 디렉토리가 변경됨.
         2. `git checkout -- xxx.txt` : 해당 파일 수정 add한것을 취소하겠음.
      3. `git merge [A커밋] ` : 현재위치의 브랜치에 A커밋을 merge 시킨다. 
         1. 충돌
            1. 다른 커밋에서 같은 부분을 수정하면 conflict 발생.
            2. 충돌이 난 부분이 `<<<<<<<`, `=======`, `>>>>>>>` 가 포함되어 수정을 요구함
            3. 해당 부분을 수정하고 다시 add, commit하면 된다.
            4. 충돌을 해결할 경우, commit 메세지에 어떤 부분을 수정했는지 적어주는 것이 좋다
      4. `git rebase` : commit 한 가지를 가지치기하고 깔끔하게 하나의 줄기로 만든다. 커밋내용 자체는 살림
         1. ![ㅁ](https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2FmU5MO%2FbtqBjUYGtyc%2FfgYXMAb0Xwl2g3IvqA5c30%2Fimg.jpg)
         2. 이미 공개된 브랜치에 대해서는 하지 말 것.
      5. `git squash` : commit 한 가지를 가지치기하고 깔끔하게 하나의 줄기로 만든다. 커밋내용을 전부 합쳐버림
         1. ![img](https://blog.kakaocdn.net/dn/bmjZJm/btqBlhZGBsX/PwIk1jRflsybvvDQQImqyk/img.jpg)
         2. 이 것 또한 이미 공개된 브랜치에 대해서는 하지 말 것.
      6. 개발 플젝에서의 효율적인 브랜치 관리
         1. ![사진](https://git-scm.com/book/en/v2/images/lr-branches-2.png)
      7. 분석 플젝에서의 효율적인 브랜치 관리
         1. ![사진](https://git-scm.com/book/en/v2/images/topic-branches-1.png)

   4. `git pull request`

      1. 해당 브랜치(저장소)에 push나 merge 권한이 없을 때 언제든지 사용.
      2. 상황별 설명
         1. 타인의 리포짓토리나 오픈소스 프로젝트에 기여하고 싶다.
            1. folk하여 내 것을 복사해오기
            2. branch는 따도 되고 안따도 된다. 어떤 것을 바꾸고 싶은지를 설명하는 브랜치면 좋다.
               1. hotfix, addfunc 등등 대표적인 단어로.
            3. 수정 한 후 내 리포짓에 커밋
            4. 타인 리포짓의 어느 브랜치든간에 pull request
            5. 관리자가 해당 리퀘스트 확인 후 merge
         2. 공용 리포짓토리인데 master에 합칠 권한은 없음
            1. 내 branch나 권한이 있는 branch에서 작업
            2. 커밋 한뒤, 메인 브랜치에 pull request
            3. 브랜치 관리자가 해당 리퀘스트를 확인 후 merge
      3. Collaborator에 등록되면, 공동 관리자로 인정되어 push가 가능해진다.
      4. gitlab의 merge request와 동일작업
         1. A가 B의 코드를 수정하여 request 했다면
         2. A는 B에게 '내 코드를 merge 해달라' 라고 request 한 것.
         3. B는 A에 의해 '내 코드를 너의 코드에 pull 해달라' 라고 request 받은 것.

   5. `git cherry-pick` : 특정 커밋의 변경사항만을 가져오기

      1. 특정 커밋이 언급하고 있는 파일만 가져온다.
      2. 자신만의 브랜치에 push하기
         1. 새로운 사설 브랜치 추가
         2. 로컬에 remote 추가
         3. 원하는 시점에서 branch 생성하여 거기에 자기파일 커밋하는 것만 cherry-pick
         4. git push remote branch 하기
