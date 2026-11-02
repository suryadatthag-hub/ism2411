# Reflection
# 1. The most surprising feature to me is that list methods such as sort()
#    change the original list instead of returning a new sorted list.
#    I would have expected to assign the result to another variable, but
#    sorted(inventory) is the appropriate choice when I want a separate copy.
#
# 2. In a statistics class, a Python list could help analyze a sample of daily
#    sales figures for a business instead of calculating the results manually
#    in Excel. I could use the same list to calculate the mean, find the range,
#    and count observations above the mean. If the sample changed, rerunning
#    the code would update these results without repeating the spreadsheet steps.

# Exercise 1: Build the list
print("Exercise 1: Build the list")
inventory = ["pen", "notebook", "stapler", "tape", "marker"]
print(inventory)
print(len(inventory))

# Exercise 2: Positive and negative indices
print("\nExercise 2: Index practice")
middle_index = len(inventory) // 2
print(inventory[0])
print(inventory[-1])
print(inventory[middle_index])

# Exercise 3: Slicing
print("\nExercise 3: Slicing")
print(inventory[:3])
print(inventory[-2:])
print(inventory[::2])

# Exercise 4: Modify the list and print each change
print("\nExercise 4: Modify")
inventory.append("envelope")
print(inventory)
inventory.remove("tape")
print(inventory)
inventory.sort()
print(inventory)

# Exercise 5: Tuples cannot be modified in place
print("\nExercise 5: Tuple comparison")
coords = (40.7128, -74.0060)
try:
    coords[0] = 99
except TypeError:
    print("TypeError caught: tuples are immutable. They are useful for fixed")
    print("coordinates because individual values cannot be changed accidentally.")
print(coords)

# Exercise 6: Summarize daily sales
print("\nExercise 6: Average of a list of sales")
sales = [100, 250, 75, 480, 200]
total = sum(sales)
count = len(sales)
average = total / count
print(f"Total: {total}")
print(f"Count: {count}")
print(f"Average: {average}")
print(f"Best: {max(sales)}")
print(f"Worst: {min(sales)}")

# Exercise 7: Build a separate discounted list with append()
print("\nExercise 7: Accumulator pattern")
prices = [9.99, 14.99, 4.99, 24.99, 1.99]
discounted = []
for price in prices:
    discounted.append(round(price * 0.90, 2))
print(f"Original: {prices}")
print(f"Discounted: {discounted}")

# Exercise 8: Filter sales strictly above 300
print("\nExercise 8: Filter above threshold")
sales = [340, 127, 589, 204, 467, 88, 731, 315, 62, 490]
high_sales = []
for sale in sales:
    if sale > 300:
        high_sales.append(sale)
print(high_sales)
print(f"Count: {len(high_sales)}")
print(f"Average: {sum(high_sales) / len(high_sales):.2f}")
