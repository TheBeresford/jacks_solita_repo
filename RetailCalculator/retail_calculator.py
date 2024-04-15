import math

print("Retail calculator started.")

num_of_goods = int(input("Input the number of goods: "))
assert isinstance(num_of_goods, int)
print(f"Selling {num_of_goods} goods.")

value_of_good = float(input("Input the value of one good: "))
assert isinstance(value_of_good, float)
print(f"Selling goods with price {value_of_good}.")

total_price = num_of_goods * value_of_good
print(f"Total price of transaction: {round(total_price)}")


def requirements_for_next_discount(total_price, value_of_good, discount_rate_ceiling):
    diff_to_next_discount = discount_rate_ceiling - total_price
    print(f"Amount needed for next discount rate: {round(diff_to_next_discount)}.")
    num_of_items_needed = math.ceil(diff_to_next_discount / value_of_good)
    print(f"Number of items needed for next discount rate: {num_of_items_needed}")


# Discounts
if total_price < 1000:
    discount_percentage = 0
    requirements_for_next_discount(total_price, value_of_good, 1000)
elif total_price >= 1000 and total_price < 5000:
    discount_percentage = 0.03
    requirements_for_next_discount(total_price, value_of_good, 5000)
elif total_price >= 5000 and total_price < 7000:
    discount_percentage = 0.05
    requirements_for_next_discount(total_price, value_of_good, 7000)
elif total_price >= 7000 and total_price < 10000:
    discount_percentage = 0.07
    requirements_for_next_discount(total_price, value_of_good, 10000)
elif total_price >= 10000 and total_price < 50000:
    discount_percentage = 0.10
    requirements_for_next_discount(total_price, value_of_good, 50000)
else:
    discount_percentage = 0.15

print(f"Discount percentage: {discount_percentage}")
discount_amount = total_price * discount_percentage
print(f"Discount amount: {discount_amount}")

price_after_discount = total_price - discount_amount

# Taxes
tax_dictionary = {"UT": 0.0685, "NV": 0.08, "TX": 0.0625, "AL": 0.04, "CA": 0.0825}

state_code = input("Input state code (UT, NV, TX, AL, CA): ")
print(f"Working in state: {state_code}")

utah_tax_rate = tax_dictionary[state_code]
tax_amount = price_after_discount * utah_tax_rate
print(f"Tax amount: {round(tax_amount)}")

price_after_tax = price_after_discount + tax_amount
print(f"Total price after tax: {round(price_after_tax, 2)}")
