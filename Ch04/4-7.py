"""
날짜 : 2020/08/11
이름 : 유효진
내용 : 머신러닝 - 서포트벡터머신(SVM) 분석 실습
"""
from sklearn import svm
from sklearn.linear_model import LogisticRegression

#학습데이터
train_data = [[0, 0], [0, 1], [1, 0], [1, 1]]
train_label = [0, 1, 1, 0]

#모델학습
svm_model = svm.SVC()
svm_model.fit(train_data, train_label)

logic_model = LogisticRegression()
logic_model.fit(train_data, train_label)

#모델검증
svm_result = svm_model.predict(train_data)
logic_result = logic_model.predict(train_data)

print('svm_result :', svm_result)
print('logic_result :', logic_result)