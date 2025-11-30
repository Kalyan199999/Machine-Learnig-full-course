sent = "This is#pavan kalyan#and I'm a computer science#student!"

# split the string into list of words
arr = sent.split()

print(sent)
print(arr)

arr = sent.split(sep="#")

print(arr)

# join the list of words into a string
fruits = ['apple','banana','mango']
fruitNames = ' '.join(fruits)
print(fruitNames)