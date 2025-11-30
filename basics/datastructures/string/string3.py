sent = "This is pavan kalyan and I'm a computer science student!"

print(f'Original sentence: {sent}')

# get the index of substring from start
print(f'Index of van is:{sent.find("van")}')

print(f'Index of oxo is:{sent.find("oxo")}')

# get the index of substring from last
print(f'Last ndex of an is:{sent.rfind("an")}')

# get the occurances of substring
print(f'Frequency of an is:{sent.count("an")}')

# string startwith substring
print(f'Sentence starts with This:{sent.startswith("This")}')

# string ends with substring
print(f'Sentence ends with student!:{sent.endswith("student!")}')