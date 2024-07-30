from signLanguage.logger import logging
from signLanguage.exception import SignException
import sys

#logging.info("Welcome to python logging")

try:

    a= 7/6
    print(a)


except Exception as e:
    raise SignException(e, sys) from e