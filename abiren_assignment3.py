import numpy as np

# Assignment 3

#
def gradientDescentFunction(data, iterations, learningRate):
    #coefficients = np.zeros(data.shape[1]-1)
    num_features =  len(data[0]) - 1
    coefficients = [0.0] * num_features

    X = data[:, :-1]
    y = data[:, -1]

    for i in range(iterations):

        # y_pred = np.dot(X, coefficients)
        y_pred = []
        for row in X:
            pred = 0.0
            for j in range(num_features):
                pred += coefficients[j] * row[j]
            y_pred.append(pred)

        # error = y_pred - y
        error = [y_pred[i] - y[i] for i in range(len(y))]

        # gradient = np.dot(X.T, error) / len(y)
        gradient = [0.0] * num_features
        for j in range(num_features):
            for i in range(len(y)):
                gradient[j] += error[i] * X[i][j]
            gradient[j] /= len(y)

        # coefficients -= learningRate * gradient
        for j in range(num_features):
            coefficients[j] -= learningRate * gradient[j]

    return coefficients


# Question a)
print("Question a: Please check the code above \n")
print(">> Please check the codes", "\n\n")

# Question b)
print("Question b:  Generate some random data, and estimate b using gradient descent algorithm\n")
n = 10
k = 2
beta = np.array([1, 2, 5])
X = np.random.randn(n, k)
X = np.hstack((np.ones((n, 1)), X))
noise = np.random.randn(n)
Y = X.dot(beta) + noise
# print(X)
# print(Y)
# print(Y[9])

#

result = gradientDescentFunction(X, 100, 0.0001)
print(result)
