import logging
from tecnoteca.googlemap.config import PROJECTNAME

def log(msg):
    logger = logging.getLogger(PROJECTNAME)
    logger.debug(msg)