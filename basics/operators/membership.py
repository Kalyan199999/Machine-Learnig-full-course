# Member ship operator
# in, not in

name = "  Pavan KAlyan "

name = name.lower().split()

name = " ".join(name)

print(name)

print( "an" in name )
print( "an" not in name )

print( "xy" in name )
print( "xy" not in name )


fruits = [ 'apple' , 'banana' , 'mango','graps' ]

print( 'apple' in fruits )

for ele in fruits:
    print( ele ,end=" ")