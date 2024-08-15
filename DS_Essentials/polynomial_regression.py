import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
from sklearn.preprocessing import PolynomialFeatures

x = 4 * np.random.rand(100, 1)-2
y = 4 + 2 * x + 5*x**2 + 12 * x**3 + 2*x**4 + 14*np.random.randn(100, 1)

poly_features = PolynomialFeatures(degree=4, include_bias=False)
x_poly = poly_features.fit_transform(x)


reg = LinearRegression()
reg.fit(x_poly, y)


x_vals = np.linspace(-2, 2, 100).reshape(-1, 1)
x_vals_poly = poly_features.transform(x_vals)
y_vals = reg.predict(x_vals_poly)

plt.scatter(x, y)
plt.plot(x_vals, y_vals, color="r")
plt.show()
