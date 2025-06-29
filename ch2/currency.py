pesos = int(input("How much in pesos is left?"))
soles = int(input("How much in soles is left?"))
reais = int(input("How much in reais is left?"))

total_in_usd = (pesos * 0.052) + (soles * 0.28) + (reais * 0.18) 

print ("Your total is $" + str(total_in_usd))
