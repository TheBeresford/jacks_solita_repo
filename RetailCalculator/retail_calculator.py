import math

print("Retail calculator started.")

product_names_and_prices = {
    "bike": 100,
    "quadbike": 500,
    "car": 15000,
    "helicopter": 1000000,
    "airplane": 3000000,
    "kissa": 5000000,
}

while True:
    name_of_good = input("Input the name of the good: ")
    if name_of_good in product_names_and_prices.keys:
        break
    else:
        print("Invalid product name.")
print(f"Selling {name_of_good}.")

while True:
    num_of_goods = int(input("Input the number of goods: "))
    if isinstance(num_of_goods, int):
        break
    else:
        print("Invalid number of goods.")
print(f"Selling {num_of_goods} goods.")

total_price = num_of_goods * name_of_good
print(f"Total price of transaction: {round(total_price)}")


def requirements_for_next_discount(total_price, value_of_good, discount_rate_ceiling):
    diff_to_next_discount = discount_rate_ceiling - total_price
    print(f"Amount needed for next discount rate: {round(diff_to_next_discount)}.")
    num_of_items_needed = math.ceil(diff_to_next_discount / value_of_good)
    print(f"Number of items needed for next discount rate: {num_of_items_needed}")


# Discounts
if total_price < 1000:
    discount_percentage = 0
    requirements_for_next_discount(total_price, name_of_good, 1000)
elif total_price >= 1000 and total_price < 5000:
    discount_percentage = 0.03
    requirements_for_next_discount(total_price, name_of_good, 5000)
elif total_price >= 5000 and total_price < 7000:
    discount_percentage = 0.05
    requirements_for_next_discount(total_price, name_of_good, 7000)
elif total_price >= 7000 and total_price < 10000:
    discount_percentage = 0.07
    requirements_for_next_discount(total_price, name_of_good, 10000)
elif total_price >= 10000 and total_price < 50000:
    discount_percentage = 0.10
    requirements_for_next_discount(total_price, name_of_good, 50000)
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
print(f"Total price after tax: {round(price_after_tax, 2)}\n")

# writing the reciept
kuitti = "-" * 16

kuitti = kuitti + f"\nNumber of items...{num_of_goods}"
kuitti = kuitti + f"\nValue of individual items...{name_of_good}"
kuitti = kuitti + f"\nTotal price.......{total_price}"
kuitti = kuitti + f"\n\nDiscount...{discount_amount}"
kuitti = kuitti + f"\nPrice after discount...{price_after_discount}"
kuitti = kuitti + f"\nTax amount added...{tax_amount}"
kuitti = kuitti + f"\n\nTotal...{price_after_tax}\n"

kuitti = kuitti + "-" * 16

print(kuitti)
