# Sorting a List Permanently with the sort() Method
cars = ['bmw', 'audi', 'toyota', 'suburu']
cars.sort()
print(cars)

# Sort a List Permenently in reverse alphabetical order
cars = ['bmw', 'audi', 'toyota', 'suburu']
cars.sort(reverse=True)
print(cars)

# Sorting a List Temporarily with the sorted() Function
cars = ['bmw', 'audi', 'toyota', 'suburu']
print("Here is the original list:")
print(cars)

print("\nHere is the sorted list:")
print(sorted(cars))

print("\nHere is the reverse sorted list;")
print(sorted(cars, reverse=True))

print("\nHere is the original list again:")
print(cars)

# Printing a List in Reverse Order
cars = ['bmw', 'audi', 'toyota', 'suburu']
print(f'\n{cars}')

cars.reverse()
print(cars)

# Finding the Length of a List
print(len(cars))