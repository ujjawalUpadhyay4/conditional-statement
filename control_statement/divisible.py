#number to be divisible by 11 or 5 or not

num = int(input("Enter the number"))
if(num%5 == 0 and num%11 ==0):
    print("number is divisible by 5 and 11")
else:
    print("number is not divisible by 5 or 11")
    