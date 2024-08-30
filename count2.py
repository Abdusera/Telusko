def count(n):
    a =0
    b =1
    sum = 0
    print(a)
    sum += a
    while sum + b < n :
        print(b)
        sum += b

        c = a+b
        a = b
        b = c

count(100)