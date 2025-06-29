height = int(input("How tall are you in cm"))
credits = int(input("How many credits do ou have")) 

if height >= 137 and credits >= 10: 
  print ("Enjoy the ride mf") 
elif height < 137 and credits >=10: 
  print ("You are not tall enought to take the ride") 
elif height >= 137 and credits < 10: 
  print ("You do not have enough credits to ride loser") 
else: 
  print ("You do not meet any requirements") 
