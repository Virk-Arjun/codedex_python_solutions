class Restaurant: 
  name = ''
  diner_type = ''
  rating = 0.0 
  open_or_closed = False 

bobs_burgers = Restaurant() 
bobs_burgers.name = 'Bobs Burgers'
bobs_burgers.diner_type = 'American Diner'
bobs_burgers.rating = 4.7 
bobs_burgers.open_or_closed = True 

print (vars(bobs_burgers)) 
