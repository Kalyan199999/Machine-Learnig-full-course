# Multiple loggers with different log levels
import logging

# custom logger
logger1 = logging.getLogger('module1')
logger1.setLevel(logging.DEBUG)

logger2 = logging.getLogger('module2')
logger2.setLevel(logging.INFO)

logger3 = logging.getLogger('module3')
logger3.setLevel(logging.WARNING)

logger4 = logging.getLogger('mathematical operation')
logger4.setLevel(logging.ERROR)

logging.basicConfig(
    filename='app.log',
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    # filemode='w',
    datefmt='%Y-%m-%d %H:%M:%S'
)