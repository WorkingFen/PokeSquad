import logging
import os
import sys
import traceback


def exception_handler(type, value, tb: traceback):
    logger.exception("Uncaught exception: {0}".format(str(value)))
    for entry in traceback.format_tb(tb):
        logger.exception(str(entry))


if not os.path.exists('../log'):
    os.makedirs('../log')


logging.basicConfig(format='%(asctime)s - %(message)s', level=os.environ.get("LOGLEVEL", "INFO"))
logger = logging.getLogger('pokesquad')
logger.addHandler(logging.FileHandler('../log/pokesquad.log'))
sys.excepthook = exception_handler

