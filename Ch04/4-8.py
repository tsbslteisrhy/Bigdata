"""
날짜 : 2020/08/12
이름 : 유효진
내용 : 머신러닝 - iris 서포트벡터머신 분석 실습
"""
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn import svm, metrics
from sklearn.model_selection import train_test_split

#붓꽃 데이터프레임 생성
df_iris = pd.read_csv('./data/iris.csv')
print(df_iris)

#붓꽃 상관분석 차트 출력
sns.pairplot(df_iris, hue='variety')
#plt.show()

#학습데이터 준비
iris_data = df_iris[['sepal.length', 'sepal.width', 'petal.length', 'petal.width']]
iris_label = df_iris['variety']

train_data, test_data, train_label, test_label = train_test_split(iris_data, iris_label)

#학습하기
model = svm.SVC()
model.fit(train_data, train_label)

#검증하기
result = model.predict(test_data)
print(result)

#정답률(학습률) 확인
score = metrics.accuracy_score(test_label, result)
print('학습률 : ', score)