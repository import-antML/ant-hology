# LOL 바텀 데이터 분석
API로 데이터를 받아서 바텀 듀오의 조합에 대한 데이터 분석
1. Plotly를 이용한 바텀 조합별 승률 시각화
2. 바텀 조합 + 스펠로 머신러닝 학습 및 승패 예측
-----------------------------------------------

### 기본 세팅
###### 파이썬 환경설정
```
pip install pipenv
pipenv --python==3.7
pipenv install
pipenv install --dev
```

###### 환경 변수 설정
.env 파일 생성해서 API_KEY='KEY'
KEY는 https://developer.riotgames.com/ 에서 생성

###### 커널 설정
```
python -m ipykernel install --user --name=my-virtualenv-name
```

###### tqdm 환경설정
```
jupyter nbextension enable --py widgetsnbextension --sys-prefix
```