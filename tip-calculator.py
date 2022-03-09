total = input("How much are you paying for your meal?: $ ")
float_total = float(total)
twenty_percent = (round (float_total * .20, 2))
fifteen_percent = (round (float_total * .15, 2))
ten_percent = (round (float_total * .10,2))
five_percent = (round (float_total * .05,2))

print(f"Your 20% tip amount is: ${twenty_percent}")
print(f"Your 15% tip amount is: ${fifteen_percent}")
print(f"Your 10% tip amount is: ${ten_percent}")
print(f"Your 5% tip amount is: ${five_percent}")

print("Please tip your server!")