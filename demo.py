from us_visa.logger import logging
from us_visa.exception import USvisaException
import sys

try:
    a = 1/"w"
except Exception as e:
    raise USvisaException(e,sys) from e
