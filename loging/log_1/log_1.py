import logging

logging.basicConfig(
    filename='log_1.log', 
    filemode='w',
    level=logging.DEBUG, 
    format='%(asctime)s:%(levelname)s:%(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
    )
logging.debug('---------------------New debug------------------------------------')
logging.debug('This is a debug message')
logging.info('This is an info message')
logging.warning('This is a warning message')
logging.error('This is an error message')
logging.critical('This is a critical message')
