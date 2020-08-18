"""
날짜 : 2020/08/18
이름 : 유효진
내용 : 텐서플로 1.x HelloWorld 실습
"""
import tensorflow.compat.v1 as tf
tf.disable_v2_behavior()

#텐서플로 버전 확인
#print(tf.__version__)

#그래프 생성
hello = tf.constant('Hello Tensorflow!')

#세션 생성
sess = tf.Session()

#그래프 실행
result = sess.run(hello)
print(result)

#세션 종료
sess.close()