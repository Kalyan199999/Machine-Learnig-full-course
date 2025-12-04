set1 = { 2,4,6,8,10,12,14}
set2 = {1,2,3,4,5,6,7,8,9,10,12,14}
set3 = {22,23,24,25,26}

print( f"Is the set1 and set2 are disjoint:{set1.isdisjoint(set2)}" )
print( f"Is the set1 and set3 are disjoint:{set1.isdisjoint(set3)}" )
print()

print(f"Is set1 is subset of set2:{set1.issubset(set2)}")
print(f"Is set2 is subset of set1:{set2.issubset(set1)}")
print()

print(f"Is set2 superset of set1:{set2.issuperset(set1)}")
print(f"Is set1  superset of set2:{set1.issuperset(set2)}")