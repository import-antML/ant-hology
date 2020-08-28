import pandas as pd
import plotly.offline as py
import plotly.graph_objects as go
import plotly.express as px
import datetime

# DACON 아파트 실거래가 예측 데이터 사용
df_apt = pd.read_csv("train.csv")
df_park = pd.read_csv("park.csv")
df_dcc = pd.read_csv("day_care_center.csv")
#서울특별시 데이터만 사용
df_apt['city'].unique()
df_seoul = df_apt[df_apt['city']=='서울특별시']
#데이터 타입변환
df_seoul.dtypes
df_seoul["transaction_year_month"].unique()
df_seoul.loc[:,"transaction_year_month"] = pd.to_datetime(df_seoul.loc[:,"transaction_year_month"],format='%Y%m').dt.strftime('%Y-%m')
df_seoul.to_csv("train_seoul.csv")