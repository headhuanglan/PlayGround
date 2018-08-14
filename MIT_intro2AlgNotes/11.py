balence="())(()()))()"


def detect(balence=balence):
    result=[]
    for c in balence:
        if c=="(":
            result.append(1)
        if c==")":
            result.append(-1)

    flag=0
    for i in result:
        flag+=i
        if flag<0:
            return False
    if flag==0:
        return True
    else:
        return False

print(detect(balence))


#newtown's method    quadratic convergence
#find root

# y=f(xi)+f'(xi)(x-xi)
#
# xi+1 is y==0
#
# xi+1=xi-f(xi)/f'(xi)






