# Reflection
# 1. The thing that was the most surprising to me is that list methods like sort()
# edit the original list and don't return a new list that is sorted.
# I would have expected to assign the return value to a new list, but if I
# want a new list I should use sorted(inventory)
# 2. A Python list can be used in a statistics class to look at a sample of
# daily sales data from a store rather than doing all the math in Excel.
# The same list could be used to compute the mean, range and number of
# data points above the mean. If the sample changes, simply re-running the
# code would provide updated values rather than having to recreate the
# spreadsheet.

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
