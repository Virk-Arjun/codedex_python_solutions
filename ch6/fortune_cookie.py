import random 

def fortune (): 
  fortunes = ["Don't pursue happiness – create it", "All things are difficult before they are easy", "The early bird gets the worm, ut the second mouse gets the cheese", "Someone in your life needs a letter from you", "Don't just think. Act!", "Your heart will skep a beat", "The fortume yhou search for is in another cookie", "Help! I'm ebing held prisoner in a Chinese bakery"]
  fortune_number = random.randint(1, 8)
  if fortune_number == 1: 
    print (fortunes[0])
  elif fortune_number == 2: 
    print (fortunes[1])
  elif fortune_number == 3: 
    print (fortunes[2])
  elif fortune_number == 4: 
    print (fortunes[3])
  elif fortune_number == 5: 
    print (fortunes[4])
  elif fortune_number == 6: 
    print (fortunes[5])
  elif fortune_number == 7: 
    print (fortunes[6])
  elif fortune_number == 8: 
    print (fortunes[7])
  else: 
    print ("Invalid entry")

fortune() 
