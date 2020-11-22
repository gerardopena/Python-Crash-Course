# Using Variables in Strings
first_name = "ada"
last_name = "lovelace"
full_name = f"{first_name} {last_name}"
print(full_name)

print(f"Hello, {full_name.title()}!")

message = f"Hello, {full_name.title()}!"
print(message)
print("")

# Adding Whitespace to stirngs with Tabs or Newlines
print("Python")
print("\tPython")
print("")

print("Languages:\nPython\nC\nJavascript")
print("")

print("Languages:\n\tPython\n\tC\n\tJavascript")
print("")

#Stripping Whitespace
favorite_language = "python "

# Temporarily remove right whitespace
print(favorite_language)
print(favorite_language.rstrip())
print(favorite_language)
print("")

# Permanently remove whitespace
favorite_language = favorite_language.rstrip()
print(favorite_language)
print("")

# Temporarily remove left whitespace
favorite_language = " python "
print(favorite_language.lstrip())
print("")

# Temporarily remove whitespace from both sides
print(favorite_language.strip())
