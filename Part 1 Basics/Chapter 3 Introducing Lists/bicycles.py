bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles)

# Accessing Elements in a List
print(bicycles[0])
print(bicycles[0].title())

# Index Positions Start at 0, Not 1
print(bicycles[1])
print(bicycles[3])

# Access last item of the list by asking for the item at index -1
print(bicycles[-1])

# Using Individual Values from a List
message = f"My first bicycle was a {bicycles[0].title()}."
print(message)