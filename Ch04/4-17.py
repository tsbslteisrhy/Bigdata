"""
날짜 : 2020/08/13
이름 : 유효진
내용 : 머신러닝 모델평가 - K교차검증
"""
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn import svm, metrics
from sklearn.model_selection import train_test_split, cross_val_score

#붓꽃 데이터프레임 생성
df_iris = pd.read_csv('./data/iris.csv')
#print(df_iris)

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

#모델평가 k교차검증
cross_score = cross_val_score(model, train_data, train_label, cv=10)
cross_score_mean = cross_score.mean()
print('모델성능 점수 :', cross_score)
print('모델성능 평균 :', cross_score_mean)

