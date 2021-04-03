print("Welcome to the Bar!")
Age = int(input("How old are you? "))
bill = 10
Veteran = ("Are you a veteran? Y or N")
ID = ()

if Age >= 21 and Age <= 60:
  print("You can Enter the bar")
  bill -= 3 
  print(f"Your final bill is ${bill}")
if Age >= 65:
    Veteran = input("Are you a veteran? Y or N. ")
    if Veteran == 'Y':
      if Veteran == 'N':
        bill -= 10
    print("Your entry fee is on the house! Thank you for your service")

elif Age >= 18 and Age <= 21:
  print("Go to Canada, you can have a drink there legally")

else:
  print("Go to sleep")  


