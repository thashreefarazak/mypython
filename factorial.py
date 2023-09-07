def factorial(num):
    fact=1
    for i in range(1,num+1):
        fact=fact*i
    print("factorial",fact)
a=int(input("enter a number"))
factorial(a)






def factorial(num):
    fact=1
    i=1
    while i<=num:
        fact=fact*i
        i=i+1
    print("it is factorial",fact)
a=int(input("enter a number"))
factorial(a)

