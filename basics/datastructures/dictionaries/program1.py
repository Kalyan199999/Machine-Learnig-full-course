# Dictionaries

nums = [1,2,3,1,2,2,2,3,4,8,10,2,1,3,4,6,10]

freq = {}

print(f"Type of freq is:{type(freq)}")

for num in nums:

    if num in freq:
        freq[num] += 1
    else:
        freq[num] = 1

print(freq)

for key,val in freq.items():
    print(f"{key} occurs {val} times")

print()
# Methods

# get
print( f"Frequency of 1 is:{freq.get(1)}" )
# if key not found
print( f"frequency of 100 is:{freq.get(100,-1)}\n")

# deleting
print( f"Deleting the key 1 and its frequency is:{freq.pop(1)}" )
print(freq)
# if key not found
print( f"Deleting the key 100 and its frequency is:{freq.pop(100,-1)}\n")

# contains
print( f"Does the key 2 exist in the dictionary? {2 in freq}" )
print( f"Does the key 100 exist in the dictionary? {100 in freq}\n")


del freq[2]
print(freq)

print(f"\n Keys:{freq.keys()}")
print(f"Values:{freq.values()}\n")
print(f"Items:{freq.items()}\n")
print(f"Length of the dictionary is:{len(freq)}")