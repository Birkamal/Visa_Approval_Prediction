from Visa_Prediction.logger import logging
from Visa_Prediction.exception import USvisaException
import sys


'''Demo for logger'''
#logging.info("Welcome to our custom log")

'''Demo for exception'''
try:
    a=1/"12"
except Exception as e:
    logging.info(e) # to get error message in logger, helps during production
    raise USvisaException(e, sys) from e # we trace the issue with the help of sys


