import warnings
warnings.filterwarnings("ignore")
import gc
import time
import pandas as pd
import argparse
import os
import logging
logger = logging.getLogger(__name__)
formatter = logging.Formatter('%(asctime)s:%(levelname)s:%(message)s')
if not os.path.exists(os.path.join('py', 'logging')):
    os.makedirs(os.path.join('py', 'logging'))
file_handler = logging.FileHandler(os.path.join('py', 'logging', 'Python_log.log'))
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
    # Set up the parsing of command-line arguments
    parser = argparse.ArgumentParser(description="Compute distance functions on time-series")
    parser.add_argument("--datadir", required=True,
                        help="Path to input directory containing seq.csv")
    parser.add_argument("--outdir", required=True,
                        help="Path to the output directory where cumsum.csv will be created")
    args = parser.parse_args()

    # Set the paths
    data_dir = args.datadir
    out_dir = args.outdir

    # Create the output directory if it does not exist
    if not os.path.exists(args.outdir):
        os.makedirs(args.outdir)

    # Read the file
    seq = pd.read_csv("%s/%s" % (args.datadir, 'seq.csv'), parse_dates=[0], usecols=[0, 1])  # , index_col=0)

    # Set logging level to debug
    logger.setLevel(logging.DEBUG)

    # Computation
    cseq = pd.DataFrame(cumsum(seq.values[:, 1].tolist()), index=seq.values[:, 0])

    # Write to file
    cseq.to_csv("%s/%s" % (args.outdir, 'out.csv'), header=False)
