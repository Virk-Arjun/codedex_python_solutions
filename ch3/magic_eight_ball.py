import random

question = input("Ask the 8-Ball a Question")

num = random.randint(1, 9) 

if num == 1: 
  print ("Yes - definetly")
elif num == 2: 
  print ("It is decidely so") 
elif num == 3: 
  print ("Without a doubt") 
elif num == 4: 
  print ("Reply hazy, try again") 
elif num == 5: 
  print ("Ask again later") 
elif num == 6: 
  print ("My sources say no") 
elif num == 7: 
  print ("Outlook not so good") 
else: 
  print ("Very doubtful") 
