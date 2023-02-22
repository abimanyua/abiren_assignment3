import numpy as np

#test

# Assignment 3

def gradientDescentFunction(data, iterations, learningRate):
    i = 0


# Question a)
print("Question a: Please check the code above \n")

# Question b)
print("Question b:  Generate some random data, and estimate b using gradient descent algorithm\n")
n = 10
k = 2
beta = np.array([1, 2, 5])
X = np.random.randn(n, k)
X = np.hstack((np.ones((n, 1)), X))
noise = np.random.randn(n)
Y = X.dot(beta) + noise
# print(Y[9])

