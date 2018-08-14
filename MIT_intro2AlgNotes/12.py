#sqrt newtown's method

# f(x)=x2-a

# y=f(xi)+df(xi)(x-xi)
# xi+1=xi-f(xi)/df(xi)
#     =xi-(x2-a)/2x
#


a=2

x=1 # inital guess

for _ in range(100):
    x=x-(x**2-a)/(2*x)

print(x)



