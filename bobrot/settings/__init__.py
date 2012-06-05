from base import *
from app import *
try:
    from local import *
except ImportError:
    raise Exception('Create local.py from sample_local.py')

