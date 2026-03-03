# Introduction to Derivatives and Their Role in Optimization
# • What are Derivatives?
# • Measures the rate at which a function changes with respect to its input
# • For a function f(x), the derivative f' (x) indicates the slope of the tangent line at a point x
# • Role in Optimization
# • Common Derivatives
#      For f(x) = x2, f' (x) = 2x.
#      For f(x) = sin(x), f' (x) = cos(x).


# Derivatives helps to find the direction to adjust the parameters to minimize the errors


import sympy as sp

x = sp.Symbol("x")

f = x**2

derivative = sp.diff(f, x)

print("Derivatives: ", derivative)


# • Partial Derivatives
# • Measures how a function changes with respect to one variable while keeping other variables constant
# • For f(x, y) = x2 + y2, partial derivatives are:
# https://www.udemy.com/course/ai-engineering-masterclass-from-zero-to-ai-hero/learn/lecture/47727535#overview

# Gradients
# • Gradient
# • Vector of all partial derivatives, indicating the direction of the steepest ascent
# For f(x, y) = x2 + y?, the gradient is:

x, y = sp.symbols("x,y")

f = x**2 + y**2

grad_x = sp.diff(f, x)
grad_y = sp.diff(f, y)

print("Partial deriv", grad_x, grad_y)

# Gradient Descent Optimization Algorithm
# • What is Gradient Descent?
# • Iterative optimization algorithm used to minimize a function
# • Updates parameters in the direction of the negative gradient to find the minimum
# • Update Rule: 0 = 0 - aVf(0)
# • 0: Parameters of the model
# • a: Learning rate (step size)
# • Why is Gradient Descent Important in Machine Learning?
