import logging
from datetime import datetime
import os
import os,sys

# log file name
LOG_FILE_NAME = f"{datetime.now().strftime('%m%d%Y__%H%M%S')}.log"

# log directory
LOG_DIR = os.path.join(os.getcwd(), "logs")
# create dir if not exists
os.makedirs(LOG_DIR,exist_ok = True)

# log file path
LOG_FILE_PATH = os.path.join(LOG_DIR,LOG_FILE_NAME)

# log configure
logging.basicConfig(
    filename = LOG_FILE_PATH,
    format = "[ %(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level = logging.INFO
)