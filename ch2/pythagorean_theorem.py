import math 

value_a = int(input("Enter a value for the adjacent side"))
value_b = int(input("Enter a value for the opposite side"))

value_c = math.sqrt(value_a ** 2 + value_b **2)
print ("The value of the hypotenuese is " + str(value_c))
