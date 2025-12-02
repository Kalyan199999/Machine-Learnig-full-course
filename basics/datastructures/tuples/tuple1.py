tup1 = (1,2,3,"Pavan",'M',25.6,3,1,2.0,1,2,2,)
print(tup1)
print(type(tup1))

# accessing with index
for i in range(0,len(tup1)):
    print(tup1[i] , end=" ")

print()

print( f"count of 2 is:{tup1.count(2)}" )

# tuples are immutable
# tup1[0] = 10

print( tup1[2:5])
print( tup1[0:6:2])
print(tup1[::-1])
print(tup1.index(2))

# this is int not tuple,to make tuple use comma(,)
tup2 = (2)
print(tup2)
print(type(tup2))

tup3 = (2,)
print(tup3)
print(type(tup3))

# Nested tuples
tup4 = ( tup1 , tup3 )
print(tup4)

tup5 = ( (1,2,3,4) , (5,6,7,8) , (9,10,11,12),(13,14,15,16) )
print(tup5)
print(len(tup5))
print(tup5[0])

print(tup5[1][2])

print(tup5[2:4])

print(tup5[0:3:2])

print(tup5[::-1])

print(tup5.index((1,2,3,4)))

t6 = tuple([1,2,3,4,5,6,7,8,9,10])
print(t6)

t7 = tuple([(1,2,3),(4,5,6),(7,8,9),(10,11,12)])
print(t7)