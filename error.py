a = 5
b = 2

try:
    print("Resource open ")
    print(a/b)
    k = int(input("Please enter the value"))
    print(k)
except ZeroDivisionError as e:
  print("sorry the values can not be devided")

except ValueError as e :
    print("The value you entered is not integer")
finally:
  print("Resource closed")
