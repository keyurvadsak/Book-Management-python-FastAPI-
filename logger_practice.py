import logging 
from logging.handlers import RotatingFileHandler

logger = logging.getLogger("first-logger")

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(levelname)s - %(message)s',
                    handlers=[
                        logging.FileHandler("first_app.log"),
                        logging.StreamHandler()
                    ])
logger.debug("logger debug message")
logger.info("logger info message")
logger.critical("logger critical message")
logger.warning("logger warning message")
logger.error("logger error message")


logger.setLevel(logging.DEBUG)
console_handler = logging.StreamHandler()
console_formater = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s',datefmt='%m/%d/%Y %I:%M:%S %p')
console_handler.setFormatter(console_formater)
logger.addHandler(console_handler)


file_handler = RotatingFileHandler("abc.log")
file_handler.setFormatter(console_formater)
logger.addHandler(file_handler)

logger.debug("logger RotatingFileHandlerdebug message")
logger.info("logger RotatingFileHandler info message")
logger.critical("logger RotatingFileHandler critical message")
logger.warning("logger RotatingFileHandler warning message")
logger.error("logger RotatingFileHandler error message")






