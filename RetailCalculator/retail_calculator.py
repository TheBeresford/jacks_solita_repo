print("Retail calculator started.")

num_of_goods = int(input("Input the number of goods: "))
assert isinstance(num_of_goods, int)
print(f"Selling {num_of_goods} goods.")

value_of_good = float(input("Input the value of one good: "))
assert isinstance(value_of_good, float)
print(f"Selling goods with price {value_of_good}.")

total_price = num_of_goods * value_of_good
print(f"Total price of transaction: {total_price}")

utah_tax_rate = 0.0685
tax_amount = total_price * utah_tax_rate
print(f"Tax amount: {tax_amount}")

price_after_tax = total_price + tax_amount
print(f"Total price after tax: {price_after_tax}")
