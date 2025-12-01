# List maintains the insertion order and can have duplicates
number = [1,3,4,2,7,6,2,4,4]

print(number)
print(type(number))

# element accessing
for num in number:
    print(num , end=' ')

print()

# index accessing
for i in range(0,len(number)):
    print( number[i], end=' ')

print()

# ascending order
number.sort()
print(number)


# descending order
number.sort( reverse=True )
print(number)

# add an element
number.append(10)
number.append(15)
print(number)

# insert an element
number.insert(0, 100)
print(number)

# remove an element
number.remove(10)
print(number)
number.pop() # removes last element
print(number)

print(  number.count(4) )

# slice the list
print(number[1:4])

print( number[2:10:2] )

# reverse the list
print(number[::-1])

print( min(number) )
print( max(number) )

number.extend( [200,300,400,500] )
print(number)

# alter the list
number[4] = 12
print(number) 

number[ 5:7 ] = [ 20, 30 ]
print(number)

number.clear()
print(number)