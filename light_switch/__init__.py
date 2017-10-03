import logging
import os


logging.basicConfig(level=int(os.environ.get('LOG_LEVEL', logging.INFO)))
log = logging.getLogger(os.environ.get('LOGGER_NAME', __name__))
