name = "paVaN kaLYan"

# get the length
length = len(name)

print(f"The length of '{name}' is {length}")

# change to uppercase
nameUpper = name.upper()
print(f'Upper case: {nameUpper}')

# capitalize
cap = name.capitalize()
print(f'Capatilize:{cap}')

# change to lower
nameLower = name.lower()
print(f'Lower case:{nameLower}')

# Title-case words
titleName = name.title() 
print(f'Title case {titleName}')

# Swap letter cases
swap = name.swapcase()
print(f'Swap case:{swap}')

# printing each chars
for i in range(len(name)):
    print( name[i], end='')