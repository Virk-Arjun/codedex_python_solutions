order = 0 

def get_item(x): 
  if x == 1: 
    print("Cheeseburger") 
  elif x == 2: 
    print("Fries") 
  elif x == 3: 
    print("Soda") 
  elif x == 4: 
    print("Ice Cream") 
  elif x == 5: 
    print("Cookie") 
  else: 
    print("Invalid") 

def welcome (): 
  print ("Hello welcome to McD's. Please place an order.")
  print ("1: Cheeseburger 2: Fires 3: Soda 4: IC 5: Cookie")

welcome () 
order = int(input("What would you like to oder")) 
print(get_item(order))
