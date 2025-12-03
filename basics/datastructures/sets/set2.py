set1 = { 2,4,6,8,10,12,14}
set2 = {1,2,3,4,5,6,7,8,9,10}

#union ->all unique elements from both sets
print(f"Union of set1 and set2 is {set1.union(set2)}")

#intersection -> common elements from both sets
print(f"Intersection of set1 and set2 is:{set1.intersection(set2)}")

#difference -> elements in set1 but not in set2
print(f"Difference of set1 and set2 is:{set1.difference(set2)}")

#difference -> elements in set2 but not in set1
print(f"Difference of set2 and set1 is:{set2.difference(set1)}")

#symmetric difference -> elements in set1 and set2 but not in both
print(f"Symmetric difference of set1 and set2 is:{set1.symmetric_difference(set2)}")