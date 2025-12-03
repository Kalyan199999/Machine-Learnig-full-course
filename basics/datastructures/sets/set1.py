# sets doesn't stores the duplicates and it is unordered
set1 = {1,2,3,"Pavan",2.0,3.0,3.1}
print(set1)
print(type(set1))

set2 = {1,1,1,1,1,17,2,6,2,8,0,2,7,2,6}
print(set2)

set3 = set([1,3,3,4,5,2,7,6,8,9,10,2,2,2,1,3,4,2,1,1])
print(set3)

# Methods in sets

# check element in set
ele = 5
print(f"Checking {ele} in set3: {ele in set3}")

print(f"length of set3: {len(set3)}")

# add element
set3.add(11)
print(f"Set3 after adding 11: {set3}")

# remove element
try:
    set3.remove(100)
    print(f"Set3 after removing 100: {set3}")
except Exception as e:
    print(f"Exception occured: {e}")

set3.discard(10)
print(f"Set3 after discarding 10: {set3}")

set3.discard(100)
print(f"Set3 after discarding 100: {set3}")

poped = set3.pop()
print(f"Set3 after poping: {set3}")