import logging
import sys

format_string = "%(asctime)s [%(levelname)s] - %(filename)s: %(message)s"

# logging.basicConfig(
#     filemode='w',
#     filename='example.log',
#     level=logging.DEBUG,
#     format= format_string
# )

logger = logging.getLogger()

formatter = logging.Formatter(format_string) 

file_handler = logging.FileHandler(filename='example.log',mode='w')
file_handler.setFormatter(formatter)
stdout_handler = logging.StreamHandler(sys.stdout)

logger.addHandler(file_handler)
logger.addHandler(stdout_handler)
logger.setLevel(logging.DEBUG)

msg = 'example'

logging.debug(msg)
logging.info(msg)
logging.warning(msg)
logging.error(msg)
logging.critical(msg)

print("hello")