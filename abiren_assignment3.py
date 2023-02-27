import random

# Assignment 3

def gradientDescentFunction(data, iterations, learningRate):
    X = [d[:-1] for d in data]
    Y = [d[-1] for d in data]
    n = len(Y)
    k = len(X[0])
    coefficients = [0] * k
    for i in range(iterations):
        predictions = [sum([X[j][p] * coefficients[p] for p in range(k)]) for j in range(n)]
        errors = [predictions[j] - Y[j] for j in range(n)]
        gradients = [2 * sum([X[j][p] * errors[j] for j in range(n)]) / n for p in range(k)]
        coefficients = [coefficients[p] - learningRate * gradients[p] for p in range(k)]
    return coefficients


# Question a)
print("Question a: Estimate the regression coefficients 𝒃 by applying the gradient descent algorithm with Python.  \n")
print(">> Please check the codes", "\n\n")

# Question b)
print("Question b:  Generate some random data, and estimate b using gradient descent algorithm\n")
n = 2000
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

iterations = 1000
learningRate = 0.01

result = gradientDescentFunction(data, iterations, learningRate)
print(">>", result)
