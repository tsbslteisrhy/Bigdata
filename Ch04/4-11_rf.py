"""
날짜 : 2020/08/12
이름 : 유효진
내용 : 머신러닝 - Random 실습
"""
import pandas as pd
from sklearn import metrics
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split

#데이터프레임 생성
df_iris = pd.read_csv('./data/iris.csv')

#학습데이터 준비
iris_data = df_iris.iloc[:, 0:4]
iris_label = df_iris.iloc[:, 4]

train_data, test_data, train_label, test_label = train_test_split(iris_data, iris_label)

#학습하기
rf_model = RandomForestClassifier()
rf_model.fit(train_data, train_label)

#검증하기
rf_result = rf_model.predict(test_data)

#학습률 확인
rf_score = metrics.accuracy_score(rf_result, test_label)

print(rf_score)
