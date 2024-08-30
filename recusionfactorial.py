def fala (n):
    if n<=0 :
        return 1
    return   n * fala(n-1)
result = fala(5)
print(result)