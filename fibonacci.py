count= int(input("How many fibonacci numbers you want to generate : "))

def fibonacci_series(n):
    i =1
    if count == 0:
        fib = []
    elif count == 1:
        fib = [1]
    elif count ==2 :
        fib =[1,1]
    elif count>2:
        fib=[1,1]
        while i < (count-1):
            fib.append(fib[i]+fib[i-1])
            i+=1
    return fib



print(fibonacci_series(count))