



# --- Exercise 1 ---
def calculate_tax(price, rate):
    return price * rate


print(f"Tax on $100 at 7%: ${calculate_tax(100, 0.07):.2f}")
print(f"Tax on $250 at 8%: ${calculate_tax(250, 0.08):.2f}")


# --- Exercise 2 ---
def apply_discount(price, tier):
    if tier == "gold":
        return price * 0.85
    elif tier == "silver":
        return price * 0.90
    elif tier == "bronze":
        return price * 0.95
    else:
        return price


print()
for tier in ["gold", "silver", "bronze", "none"]:
    print(f"{tier}: ${apply_discount(200, tier):.2f}")


# --- Exercise 3 ---
discounted_price = apply_discount(200, "gold")
total_price = discounted_price + calculate_tax(discounted_price, 0.07)

print()
print(f"After gold discount: ${discounted_price:.2f}")
print(f"After tax: ${total_price:.2f}")


def final_price(price, tier, tax_rate):
    discounted = apply_discount(price, tier)
    tax = calculate_tax(discounted, tax_rate)
    return discounted + tax


print(
    f'final_price(200, "gold", 0.07) = '
    f'${final_price(200, "gold", 0.07):.2f}'
)


# --- Exercise 4 ---
orders = [
    (200, "gold"),
    (150, "silver"),
    (80, "bronze"),
    (500, "none"),
]

print()
for price, tier in orders:
    total = final_price(price, tier, 0.07)
    print(f"Price: ${price} | Tier: {tier} | Final: ${total:.2f}")


# --- Exercise 5 ---
sales = [120, 80, 250, 175, 90]

# Fix: Indent the loop body and add each sale to the running total
# instead of replacing the total with the current sale.
total = 0
for sale in sales:
    total += sale

print()
print(f"Total: ${total}")

# Fix: Add the missing colon and indent the loop body so the count
# increases once for each sale.
count = 0
for sale in sales:
    count += 1

print(f"Count: {count}")

# Fix: Use < instead of <= because the last valid index is one less
# than the list's length. Indent both statements inside the loop.
i = 0
while i < len(sales):
    print(sales[i])
    i += 1


# --- Exercise 6 ---
# The x inside double_it() is local to that function.
# It is separate from the global x, so assigning 999 inside
# the function does not change the global value of 100.

x = 100


def double_it():
    x = 999
    return x * 2


print()
print(x)
print(double_it())
print(x)
