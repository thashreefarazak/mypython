def reverse(num):
    digit = 0
    renum = 0
    while num > 0:
        digit = num % 10
        renum = renum * 10 + digit
        num= num // 10
    print("it is renum", renum)
a=int(input("enter a numb"))
reverse(a)












def reverse(num):
    digit=0
    reminder=0
    i=0
    while i>=0:
    digit=num%10
    reminder=reminder*10+digit
    num=num//10
      print()
