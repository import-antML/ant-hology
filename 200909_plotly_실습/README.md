## import ant - Plotly 실습

### 20.09.09 18:00 ~ 19:30 진행
- 코로나19 이슈로 MS TEAMS로 진행 대체
- 각자 확보한 Dataset으로 다양한 그래프 그려보기

### Plotly
1. plotly는 Interactive한 그래프를 그릴 수 있는 Visulization Library 입니다.

2. 참고자료
  - https://plotly.com/python/
  - https://medium.com/dataseries/data-visualization-with-plotly-71af5dd220b5
  
### Technical Issue
1. Github에서는 ipynb상의 plotly가 보이지 않습니다.
  - github에서는 interactive 그래프를 보여주는 기능을 지원하지 않습니다.
  - ```fig.show("png")```나 ```fig.show("svg")``` 같은 코드를 사용하여 일반적인 이미지 형식의 정적 그래프 옵션을 사용해야 Github에서도 볼 수 있습니다.

2. Github에서의 ipynb가 보이지않고 "Sorry, something went wrong. Reload?" 메세지가 나옵니다.
  - Github 서버의 고질적인 ipynb 렌더링 오류로 알려져있습니다.
  - 업로드나 push에 문제가 있는 것은 아니므로 다음과 같이 nbviewer를 사용하면 됩니다.
  - 해당 주피터 노트북 링크가 https://github.com/import-antML/ant-hology/blob/master/kjh/LOL_game_data.ipynb 라면,
    https://github.com/ 를 https://nbviewer.jupyter.org/github/로 바꾸면 됩니다.
