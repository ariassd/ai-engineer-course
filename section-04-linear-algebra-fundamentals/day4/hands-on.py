# Hands-On Exercises
# • Exercise 1: Compute Derivatives of Basic Functions
# • Exercise 2: Compute Gradients
# • Exercise 3: Implement Gradient Descent for Linear Regression
# • Additional Practice
#    • Use sympy to compute second-order derivatives (Hessian matrix)
#    • Implement gradient descent with multiple learning rates and compare convergence speeds
#    • Visualize the gradient descent process on a quadratic function.


import sympy as sp
import numpy as np

print("============ EX1")
x = sp.Symbol("x")
f = x**3 - 5 * x + 7

derivative = sp.diff(f, x)
print("Function ", f)
print("Derivative ", derivative)


print("============ EX2")

# Define a multivariable function
x, y = sp.symbols("x,y")
f = x**2 + 3 * y**2 - 4 * x * y


# Compute partial derivatives.
grad_x = sp.diff(f, x)
grad_y = sp.diff(f, y)

print("Gradients: ", grad_x, grad_y)

print("============ EX3")
# Define gradient descent func


def gradient_descent(X, y, theta, learning_rate, iterations):
    m = len(y)
    for _ in range(iterations):
        predictions = np.dot(X, theta)
        errors = predictions - y
        gradients = (1 / m) * np.dot(X.T, errors)
        theta -= learning_rate * gradients
    return theta


# Sample data
x = np.array([[1, 1], [1, 2], [1, 3]])
y = np.array([2, 2.5, 3.5])
theta = np.array([0.1, 0.1])
learning_rate = 0.1
iterations = 1000

# Perform the gradient descent
optimize_theta = gradient_descent(x, y, theta, learning_rate, iterations)

print("Optimize", optimize_theta)
