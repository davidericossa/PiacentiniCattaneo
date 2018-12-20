from polynomial import Polynomial

x=Polynomial([1,1,1])

y=Polynomial([0,1,2])

print(x.plus(y).coefficients)


x=Polynomial([1,1])

y=Polynomial([1,-2])

z=x.multiplied(y)

print(z.coefficients)

# 1 -x -2x^2
# D=1 + 8 =9
# x_1,2= 1 #3 /-4
#(x+1)*(-2x+1)=-2x^2-x+1=-2(x+1)(x-0.5)