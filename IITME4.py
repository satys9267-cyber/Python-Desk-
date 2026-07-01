#Question converting the complex flowchart into python code 

print("Travel from A to B")
Time=int(input("Enter the Time: "))
Longer = int(input("Longer time"))

if (Time>= Longer):
  price = int(input("Enter the price: "))
  Higher = int(input("Higher price: "))
  
  if(price>=Higher):{
      print("train")
  }
  else:
    {print("coach")}
  
else:
  price = int(input("Enter the price: "))
  Higher = int(input("Higher price: "))
  if(price>=Higher):{
      print("day time flight ")
  }
  else:
    {print("red time flight")}

