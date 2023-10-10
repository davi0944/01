import scipy.integrate as integrate

result, error = integrate.quad(lambda x: (100 - x**2)**(1/2), 0, 10)
a = result
a = float(a)
z = 4*a/100

print(z)

