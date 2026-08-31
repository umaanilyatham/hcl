def arm_strong(num):
    sum=0
    digits=len(str(num))

    temp=num

    while temp>0:
        digit=temp%10
        sum+=digit**digits
        temp//=10
    return sum

num = int(input("Enter a number: "))
sum = arm_strong(num)
if sum == num:
    print(num, "is an armstrong number")
else:
    print(num, "is not an armstrong number")
