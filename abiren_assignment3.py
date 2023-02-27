import numpy as np
import random

# Assignment 3

#
def gradientDescentFunction(data, iterations, learningRate):
    a = 0



# Question a)
print("Question a: Please check the code above \n")
print(">> Please check the codes", "\n\n")

# Question b)
print("Question b:  Generate some random data, and estimate b using gradient descent algorithm\n")
n = 1000
k = 2
beta = [1, 2, 5]
X = [[random.gauss(0, 1) for j in range(k)] for i in range(n)]
for i in range(n):
    X[i] = [1] + X[i]
noise = [random.gauss(0, 1) for i in range(n)]
Y = [sum([X[i][j]*beta[j] for j in range(k+1)]) + noise[i] for i in range(n)]
data = [X[i] + [Y[i]] for i in range(n)]
# print(X)
# print(Y)
# print(Y[9])

#

result = gradientDescentFunction(X, 100, 0.0001)
print(result)
