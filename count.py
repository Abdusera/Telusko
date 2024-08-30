def count (lst) :
    even = [0]
    odd = [0]
    for i in lst :
        if i %2 == 0 :
             even.append(i)
        else:
            odd.append(i)
    return even,odd
#lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10,11,12,13,14,15,16,17,18,19,20]
nums= input("Please enter the values you want : ")
lst =list(map(int,nums.split()))
even,odd = count(lst)
print('even :{} and odd {}'.format(even,odd))



