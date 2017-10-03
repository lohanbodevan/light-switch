import logging
import os


#dotenv_path = os.path.join(os.getcwd(), '.env')
#if os.path.isfile(dotenv_path):
#    from dotenv import load_dotenv
#    load_dotenv(dotenv_path)

logging.basicConfig(level=int(os.environ.get('LOG_LEVEL', logging.INFO)))
log = logging.getLogger(os.environ.get('LOGGER_NAME', __name__))
