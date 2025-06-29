for i in range(99, 0, -1): 
  print (f'{i} bottles of beer on the wall, ' 
         f'{i} bottles of beer, ' 
         f'Take one down, pass it around, ')
  next_i = i-1
  if next_i == 0:
        print("Take one down and pass it around, "
              "no more bottles of beer on the wall.")
  else:
      print(f"Take one down and pass it around, "
            f"{next_i} bottle{'s' if next_i != 1 else ''} of beer on the wall.")
