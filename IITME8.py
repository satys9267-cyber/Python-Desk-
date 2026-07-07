#find whwether the no is palidrome or not 

#revers the number
num = int(input("Enter the number: "))
absNum = abs(num)
rev = absNum % 10
absNum = absNum //10
while(absNum>0):
    r = absNum %10
    absNum = absNum // 10
    rev = rev*10+r
if(num<0):
    rev= rev -2*rev
if(num == rev ):
    print("The number is palindrome: ")
else:
    print("The number is not palindrome")