import logging.handlers
LOG_FILE = "system.log"

handler = logging.handlers.RotatingFileHandler(
    LOG_FILE, maxBytes=4 * 1024 * 1024, backupCount=5)
fmt = '%(asctime)s - %(process)d - %(lineno)s - %(name)s - %(message)s'

formatter = logging.Formatter(fmt)
handler.setFormatter(formatter)

logger = logging.getLogger('007')
logger.addHandler(handler)
logger.setLevel(logging.DEBUG)
