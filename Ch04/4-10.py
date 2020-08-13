"""
날짜 : 2020/08/12
이름 : 유효진
내용 : 머신러닝 - 결정트리 실습
"""
from sklearn import tree
import pydotplus

#데이터준비
train_data = [[180, 70], [167, 52], [159, 62], [174, 65], [172, 58],
              [162, 55], [177, 62], [186, 72], [175, 60], [156, 52]]

train_label = [1, 2, 2, 1, 2, 2, 1, 1, 2, 2]

#학습하기
model = tree.DecisionTreeClassifier()
model.fit(train_data, train_label)

#검증하기
test_data = [[181, 62], [171, 62], [162, 52], [160, 64], [169, 59]]
result = model.predict(test_data)
print(result)

#시각화
graph_data = tree.export_graphviz(model,
                                  out_file=None,
                                  feature_names=['height', 'weight'],
                                  filled=True)

graph = pydotplus.graph_from_dot_data(graph_data)
graph.write_png('./result_tree.png')