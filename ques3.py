import random
x=1
while x<=10:
    num1=random.randint(0,10)
    num2=random.randint(0,10)
    answer=num1*num2
    print(num1,"X",num2,"=",end='')
    response=int(input())
    if response==answer:
        print("Right")
    if response!=answer:
        print("Wrong.The answer is",answer)
    x=x+1
print("Thank you!!")