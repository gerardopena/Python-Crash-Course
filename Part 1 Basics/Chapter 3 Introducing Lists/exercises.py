# 3-1 Names
names = ["John", "Joe", "Jose", "Jesus"]
print(names[0])
print(names[1])
print(names[2])
print(names[3])

# 3-2 Greetings
print(f'Hello {names[0]}, how are you')
print(f'Hello {names[1]}, how are you')
print(f'Hello {names[2]}, how are you')
print(f'Hello {names[3]}, how are you')

# 3-3 Your Own List
cars = ["Honda", "Toyota", "BMW", "Ford"]
print(f'I would like to own a {cars[0]} car')
print(f'I would like to own a {cars[1]} car')
print(f'I would like to own a {cars[2]} car')
print(f'I would like to own a {cars[3]} car')

# 3-4 Guest List
guests = ['Joe', 'John', 'Jane']
print(f"{guests[0].title()}, you are invited to a dinner I'm hosting")
print(f"{guests[1].title()}, you are invited to a dinner I'm hosting")
print(f"{guests[2].title()}, you are invited to a dinner I'm hosting")

# 3-5 Changing Guest List
print(f"{guests[2].title()} can not make it to the dinner I'm hosting")
guests[2] = 'Jake'
print(f"{guests[0].title()}, you are invited to a dinner I'm hosting")
print(f"{guests[1].title()}, you are invited to a dinner I'm hosting")
print(f"{guests[2].title()}, you are invited to a dinner I'm hosting")

# 3-6 More Guests
print('I have found a bigger dinner table')
guests.insert(0,'Jacob')
guests.insert(2,'Jack')
guests.append('Joel')
print(f"{guests[0].title()}, you are invited to a dinner I'm hosting")
print(f"{guests[1].title()}, you are invited to a dinner I'm hosting")
print(f"{guests[2].title()}, you are invited to a dinner I'm hosting")
print(f"{guests[3].title()}, you are invited to a dinner I'm hosting")
print(f"{guests[4].title()}, you are invited to a dinner I'm hosting")
print(f"{guests[5].title()}, you are invited to a dinner I'm hosting")

# 3-7 Shrinking Guest List
print('I can only invite two people for dinner')
print(f"I am sorry {guests.pop()}, but I can't invite you over to dinner")
print(f"I am sorry {guests.pop()}, but I can't invite you over to dinner")
print(f"I am sorry {guests.pop()}, but I can't invite you over to dinner")
print(f"I am sorry {guests.pop()}, but I can't invite you over to dinner")
print(f"{guests[0].title()}, you are still invited to a dinner I'm hosting")
print(f"{guests[1].title()}, you are still invited to a dinner I'm hosting")
del guests[0]
del guests[0]
print(guests)

# 3-8 Seeing the World
locations = ['Mexico', 'Australia', 'Korea', 'Japan', 'Canada']
print(locations)
print(sorted(locations))
print(locations)
print(sorted(locations, reverse=True))
print(locations)
locations.reverse()
print(locations)
locations.reverse()
print(locations)
locations.sort()
print(locations)
locations.sort(reverse=True)
print(locations)

# 3-9 Dinner Guests
guests = ['Joe', 'John', 'Jane']
print(f'I am inviting {len(guests)} guests over for dinner\n')

# 3-10 Every Function
languages = ['Spanish', 'Japanese']
print(languages)
languages.insert(1,'English')
print(languages[1].title())
language_popped = languages.pop()
print(language_popped)
del languages[0]
print(languages)

print("")
languages = ['Spanish', 'Japanese', 'English']
print(sorted(languages))
print(languages)

print("")
print(sorted(languages, reverse=True))
print(languages)

print("")
languages.reverse()
print(languages)
languages.reverse()
print(languages)

print("")
languages.sort()
print(languages)