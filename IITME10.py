#ways of formatting in python to make code for effective and easy 

num = int(input("Enter the number: "))

for i in range(1,11):
    print(num,'X',i,"=",num*i)
    print(f'{num} X {i} = {num*i}')
    print('%d X %d = %d'% (num,i,num*i))
    print('{0} X {1} = {2}'.format(num,i,num*i))
    