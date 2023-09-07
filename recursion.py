#def recursion(n):
 #   if n<=1:
#return n
#    else:
#        return n+recursion(n-1)
s=recursion(5)#
print(s)#



def factorial(num):
    if num<=1:
        return num
    else:
       num *factorial(num-1)
s=factorial(5)
print(s)
