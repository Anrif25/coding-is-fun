
#print fibonacci list
def fib(n):
        if n < 0: return []
        if n == 1: return [1]
        if n == 2: return [1,1]
        prevArray = fib(n-1)
        return prevArray + [ prevArray[-1]+prevArray[-2] ]

#get element in postion n of the list
def fib2(n):
    if n ==1 or n == 2: return 1
    #list start at 1 
    return fib2(n-1) + fib2(n-2)
    
print(fib(6))
print(fib2(6))