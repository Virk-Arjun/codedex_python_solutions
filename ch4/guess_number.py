guess = 0

tries = 0 

while guess != 6:
  guess = int(input("Guess the number:  "))
  tries += 1
  if tries > 10: 
    print ("You lost") 
    exit
  else: 
    print ("Try again!")

print("You got it! in " + str(tries) + " tries")
