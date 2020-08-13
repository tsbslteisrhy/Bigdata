"""
날짜 : 2020/08/13
이름 : 유효진
내용 : 머신러닝 - 퍼셉트론 실습
"""
import numpy as np

def AND(x1, x2):
    x = np.array([x1, x2])
    w = np.array([0.5, 0.5])
    b = -0.7

    y = np.sum(x * w) + b
    if y <= 0:
        return 0
    else:
        return 1

def OR(x1, x2):
    x = np.array([x1, x2])
    w = np.array([2, 2])
    b = -1

    y = np.sum(x * w) + b
    if y <= 0:
        return 0
    else:
        return 1

def NAND(x1, x2):
    x = np.array([x1, x2])
    w = np.array([-0.5, -0.5])
    b = 0.7

    y = np.sum(x * w) + b
    if y <= 0:
        return 0
    else:
        return 1

def XOR(x1, x2):
    z1 = NAND(x1, x2)
    z2 = OR(x1, x2)
    y  = AND(z1, z2)
    return y

#출력
print('AND')
print('0, 0 :', AND(0, 0))
print('0, 1 :', AND(0, 1))
print('1, 0 :', AND(1, 0))
print('1, 1 :', AND(1, 1))

print('OR')
print('0, 0 :', OR(0, 0))
print('0, 1 :', OR(0, 1))
print('1, 0 :', OR(1, 0))
print('1, 1 :', OR(1, 1))

print('NAND')
print('0, 0 :', NAND(0, 0))
print('0, 1 :', NAND(0, 1))
print('1, 0 :', NAND(1, 0))
print('1, 1 :', NAND(1, 1))

print('XOR')
print('0, 0 :', XOR(0, 0))
print('0, 1 :', XOR(0, 1))
print('1, 0 :', XOR(1, 0))
print('1, 1 :', XOR(1, 1))