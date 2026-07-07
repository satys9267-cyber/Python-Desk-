#factorial of number 
num = int(input("Enter the number: "))

i=1
answer = 1
while(i<=num):
    answer = answer*i
    i=i+1
    
print(answer)

num1 = int(input("Enter the number: "))
fact=1

while(0<num1):
    fact= fact*num1
    num1 = num1-1
    
print("factorial of number","is",fact)


