#def prime (num):
  #  i=2
#    l=num/2
#    while i<=l:
#     if num%2==0:
#          print("it is not prime number")
#          break
#     i=i+1
#    else:
  #       print("it is a prime number")
# a=int(input("enter a number")
# prime(a)











def prime(num):
    l=int(num/2)
    for i in range(2,l+1):
        if num%i==0:
            print("it is not a prime number")
            break
    else:
        print("it is a prime number")
a=int(input("enter a number"))
prime(a)














