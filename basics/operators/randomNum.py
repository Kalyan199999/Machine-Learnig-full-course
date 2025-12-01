import random

print(random.randint(1, 10))
print(  random.random() )
print( random.randrange(1, 10) )

l = [50,10,90,100,20,80,30]
print( random.choice( l ) )

print( random.sample( l, 3 ) )

print( random.uniform(2,4) )

print(l)
random.shuffle( l )
print( l )