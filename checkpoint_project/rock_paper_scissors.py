import random 

computer = random.randint(1, 3)

print ("===================") 
print ("Rock Paper Scissors") 
print ("===================")

print ("1) ✊")
print ("2) ✋")
print ("3) ✌️")

choice = int(input("Pick a number: "))

if choice == 1: 
    print ("You chose ✊")
elif choice == 2: 
    print ("You chose ✋")
elif choice == 3: 
    print ("You chose ✌️")
else: 
    print ("Invalid choice") 

if computer == 1: 
    print ("Computer chose ✊")
elif computer == 2: 
    print ("Computer chose ✋")
elif computer == 3: 
    print ("Computer chose ✌️")
else: 
    print ("Invalid choice")

if choice == computer: 
    print ("It's a tie!")
elif choice > computer: 
    print ("The player won!")
elif choice < computer: 
    print ("The computer won!")
else: 
    print ("Error. Try again :)")
