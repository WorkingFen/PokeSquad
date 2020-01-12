import logging
import os


if not os.path.exists('../log'):
    os.makedirs('../log')


logging.basicConfig(format='%(asctime)s - %(message)s', level=os.environ.get("LOGLEVEL", "INFO"))
logger = logging.getLogger('pokesquad')
logger.addHandler(logging.FileHandler('../log/pokesquad.log'))


