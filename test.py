
""" with open("requirements.txt","r") as file:
    lines=file.readlines()
    l=[line.split("\n")[0] for line in lines]
    print(l)
"""

from src.logger import logging
import sys
from src.exception import CustomException

try:
    1/0
except Exception as e:
    logging.info(e)
    raise CustomException(e,sys)
