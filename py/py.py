import warnings
import gc
import time
warnings.filterwarnings("ignore")

import logging
from os.path import join
logger = logging.getLogger(__name__)
formatter = logging.Formatter('%(asctime)s:%(levelname)s:%(message)s')
file_handler = logging.FileHandler(join('py', 'logging', 'Python_log.log'))
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)
logger.setLevel(logging.INFO)


class PyCUMSUM:

    def __init__(self, seq):
        gc.collect()

        start = time.time()
        self.cumsum = cumsum(seq)
        self.duration = time.time() - start


def cumsum(seq):
    """
    Return cumsum

    INPUT:
    seq: the sequence

    OUTPUT:
    cumsum of seq
    """

    cseq = []
    csum = 0
    for i, x in enumerate(seq):
        csum += x
        cseq.append(csum)
        logger.debug('At ' + str(i) + ' x=' + str(x) + ' with csum=' + str(csum))

    return cseq


if __name__ == '__main__':
    logger.setLevel(logging.DEBUG)
    cumsum([1, 2, 3, 4, 5])
