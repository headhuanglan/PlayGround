#dynamic programming

def fib(n):
    if n<=2:
        return 1
    else:
        return fib(n-1)+fib(n-2)

#O(2^n) bad

#memorized DP alg #  O(n)
memo=dict()
def fib_mem(n):
    if n in memo.keys():
        return memo[n]
    if n<=2:
        return 1
    else:
        fib=fib_mem(n-1)+fib_mem(n-2)
        memo[n]=fib
        return fib

#------
def fib_fast(n):
    if n<=2:
        return 1
    a,b=1,1
    for i in range(n-2):
        a,b=b,a+b

    return b

#------------------------------


for i in range(1,6):
    print(fib_fast(i))

print(fib_fast(117))