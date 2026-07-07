#find no of digits in number

num= abs(int(input("Enter the number: ")))
digit =1

while(num>9):
    num = num//10
    digit = digit+1
print(digit)

