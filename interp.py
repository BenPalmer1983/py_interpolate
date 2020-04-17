from f_interp import interp
import numpy

def f(x):
  #return 0.001 * x**5 + 0.03 * x**4 - 1.63 * x**3 + 1.22 * x**2 - 0.0001 * x + 3.7
  return 4*x**3 - 2*x**2 - 3* x + 7
  
def g(x):
  return 2.3 - 1.2 * x + 0.2 * x**2
  
  
x = numpy.linspace(0,10, 101)
y = f(x[:])


print(x)
print(y)

xi = 2.773
yi = interp.interpolate(xi, x, y)

print(xi, yi, f(xi))



x = numpy.linspace(0,10, 11)
y = f(x[:])

print(x)
print(y)

xi = 0
yi = interp.trap(xi, x, y)
print(xi, yi)

xi = 5
yi = interp.trap(xi, x, y)
print(xi, yi)

xi = 10
yi = interp.trap(xi, x, y)
print(xi, yi)

xi = 5.5
yi = interp.trap(xi, x, y)
print(xi, yi)





#interpndydxn(xi, x, y, interp_n, y_out)
print(x[3:7])
print(y[3:7])

xi = 4.5
yi = interp.interpndydxn(xi, x[3:7], y[3:7], 0)
dyi = interp.interpndydxn(xi, x[3:7], y[3:7], 1)
ddyi = interp.interpndydxn(xi, x[3:7], y[3:7], 2)
dddyi = interp.interpndydxn(xi, x[3:7], y[3:7], 3)

print(xi, yi, dyi, ddyi, dddyi)






