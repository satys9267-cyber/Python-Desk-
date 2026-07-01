#Question is if given input is number ends with 0 or 5 print 0or 5 otherwise print other 


num = int(input("Enter the number: "))

if (num%5 == 0):
  if (num%10 ==0):{
      print(0)
  }
  else:
    {print(5)}
else :
  {
      print('other')
  }

