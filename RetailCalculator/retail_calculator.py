print("Retail calculator started.")

num_of_goods = int(input("Input the number of goods: "))
assert isinstance(num_of_goods, int)
print(f"Selling {num_of_goods} goods.")

value_of_good = float(input("Input the value of one good: "))
assert isinstance(value_of_good, float)
print(f"Selling goods with price {value_of_good}.")

total_price = num_of_goods * value_of_good
print(f"Total price of transaction: {total_price}")
