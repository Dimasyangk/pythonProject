import numpy as np

var = np.poly1d([5, 2.5, 2, 4])
print("Polynomial function, f(x):\n", var)

deriv = var.deriv()
print("Deriv, f(x)'=", deriv)

print("f(x)'=", deriv(0.6))