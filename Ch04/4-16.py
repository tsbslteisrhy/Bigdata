"""
날짜 : 2020/08/13
이름 : 유효진
내용 : 머신러닝 - 신경망 실습
"""
import numpy as np
from scipy.special import expit as sigmoid

#신경망 클래스 정의
class NeuralNetwork:
    def __init__(self, inputnodes, hiddennodes, outputnodes, learningrate):
        #멤버선언
        self.inodes = inputnodes
        self.hnodes = hiddennodes
        self.onodes = outputnodes
        self.lr = learningrate
        
        #가중치 초기화
        self.wih = np.random.rand(self.hnodes, self.inodes) - 0.5
        self.who = np.random.rand(self.onodes, self.hnodes) - 0.5
        
        #활성화 함수설정
        self.activation_function = lambda x: sigmoid(x)
        
    def fit(self, input_list, target_list):
        #입력 데이터를 2차원 행렬로 변환
        inputs = np.array(input_list, ndmin=2).T
        target = np.array(target_list, ndmin=2).T

        #은닉계층으로 들어오는 데이터 계산
        hidden_inputs = np.dot(self.wih, inputs)

        #은닉계층에서 나가는 데이터 계산
        hidden_outputs = self.activation_function(hidden_inputs)

        #최종 출력계층으로 들어오는 데이터 계산
        final_inputs = np.dot(self.who, hidden_outputs)

        #최종 출력계층에서 나가는 데이터 계산
        final_output = self.activation_function(final_inputs)

        #출력계층 오차 구하기
        output_error = target - final_output

        #은닉계층 오차 구하기
        hidden_errors = np.dot(self.who.T, output_error)

        #은닉계층과 출력계층간의 가중치 업데이트
        self.who += self.lr * np.dot((output_error * final_output * (1.0 - final_output)), np.transpose(inputs))

        #입력계층과 은닉계층간의 가중치 업데이트
        self.wih += self.lr * np.dot((hidden_errors * hidden_outputs * (1.0 - hidden_outputs)), np.transpose(inputs))

    def predict(self, input_list):
        #입력데이터를 2차원 행렬로 변환
        inputs = np.array(input_list, ndmin=2).T

        #은닉계층으로 들어오는 데이터 계산
        hidden_inputs = np.dot(self.wih, inputs)

        #은닉계층에서 나가는 데이터 계산
        hidden_outputs = self.activation_function(hidden_inputs)

        #출력계층으로 들어오는 데이터 계산
        final_input = np.dot(self.who, hidden_outputs)

        #출력계층에서 나가는 데이터 계산
        final_outputs = self.activation_function(final_input)

        #최종값 리턴
        return final_outputs


#프로그램 시작
if __name__ == '__main__':
    #입력, 은닉, 출력 노드 개수
    INPUT_NODES = 2
    HIDDEN_NODES = 2
    OUTPUT_NODES = 1
    
    #학습률
    learning_rate = 0.01
    
    #학습횟수
    epochs = 500000
    
    #신경망 생성
    nn = NeuralNetwork(INPUT_NODES, HIDDEN_NODES, OUTPUT_NODES, learning_rate)
    
    #학습하기
    for i in range(epochs):
        nn.fit([0, 0], [0])
        nn.fit([0, 1], [1])
        nn.fit([1, 0], [1])
        nn.fit([1, 1], [0])
        print('학습횟수 :', i)
        
    #검증하기
    print('XOR 결과')
    print('0, 0 :', nn.predict([0, 0]))
    print('0, 1 :', nn.predict([0, 1]))
    print('1, 0 :', nn.predict([1, 0]))
    print('1, 1 :', nn.predict([1, 1]))