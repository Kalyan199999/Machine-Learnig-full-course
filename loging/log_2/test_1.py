from logger import logging

def add(a,b):
    try:
        logging.debug('Trying to add the two values')
        logging.debug(f'The sum of values {a} and {b} is {a+b}')
        return a+b
    except Exception as e:
        logging.error(e)

def divide(a,b):
    try:
        logging.debug('Trying to divide the two values')
        logging.debug(f'The division of values {a} and {b} is {a/b}')
        return a/b
    except Exception as e:
        logging.error(e)

if __name__ == '__main__':
    print( add(4,3) )
    print( divide(4,0) )
    print( divide(4,2) )
    