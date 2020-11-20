# 1. Lime이란
*****
Local Interpretable Model-Agnostic Explanation의 약어로,
- Model-Agnostic : 모델(알고리즘)이 무엇이든 상관없이
- Local Interpretable : **지역적**으로 해석가능하도록
- Explanation : 설명해주는 방법론

여기서 말하는 **지역적**의 의미는 다음과 같다.

<img src="./image/cubic_function.png" width=600 height=400><sup>[1](#footnote_1)</sup>

기존 Tree 모델의 변수 중요도가 <font color="green">초록색</font> 선에 해당하는 **전역적(global)** 부분에서 X 변수가 얼마나 중요한 지를 설명했다면,<br>
Lime의 변수 중요도는 <font color="red">빨간색</font> 선에 해당하는 **지역적(local)** 부분에서 X 변수가 얼마나 중요한지 를 설명한다.

---

Iris 데이터로 예를 들어보면,

<img src="./image/iris_pairplot.png" width=600 height=400><sup>[2](#footnote_2)</sup>

setosa를 분류하기 위해선 sepal_width가 필수적이지만,<br>
verginica와 versicolor를 분류할 때 sepal_width는 전혀 중요하지 않다.<br>

단순히 변수 중요도만 본다면, sepal_width가 꽤 중요한 변수로 나올 것이고,<br>
그것만 봐서는 verginica와 versicolor를 분류할 때는 sepal_width가 중요하지 않다는 것은 알 수 없다.

verginica 혹은 versicolor에 국한해서 지역적으로 변수의 중요도를 확인해야만 알 수 있다.




# 2. Lime 예제
*****

# 3. Lime 파이썬 라이브러리
*****


1. <a name="footnote_1"> http://norman3.github.io/prml/docs/chapter01/1.html </a>
2. <a name="footnote_2"> https://pinkwink.kr/1128 </a>
3.
