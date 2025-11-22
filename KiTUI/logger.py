import logging
from logging.handlers import RotatingFileHandler

# create rotating file handler
handler = RotatingFileHandler('dev.log', maxBytes=5*1024*1024, backupCount=3)
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)

logger = logging.getLogger('KiTUI')
logger.setLevel(logging.INFO)
logger.addHandler(handler)
