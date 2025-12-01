stack = []

print( type(stack) )

# push the element
stack.append(10)
stack.append(20)
stack.append(30)
stack.append(40)
stack.append(50)
stack.append(60)

print( stack )

# pop element
print( stack.pop() )

print( stack )

# remove all element from stack
while( len(stack) > 0 ):
    print( stack.pop() ,end=" " )