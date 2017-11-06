import subprocess  # rpy2 problematic for some os
import numpy as np
import matplotlib.pyplot as plt
import csv
import gc
import time


class RCUMSUM:

    def __init__(self, seq):
        gc.collect()

        start = time.time()

        with open('./R/SEQ.csv', "w") as file_:
            writer = csv.writer(file_, delimiter='\n')
            writer.writerow(seq)

        command = 'Rscript'
        path2script = './R/_main.Rd'
        cmd = [command, path2script]

        x = subprocess.check_output(cmd, universal_newlines=True, stderr=subprocess.STDOUT)

        self.cumsum = []
        with open('./R/CUMSUM.csv', "r") as file_c:
            reader = csv.reader(file_c, delimiter=' ')
            i = 0
            for row in reader:
                if i != 0:
                    self.cumsum.append(float(row[0]))
                i = i + 1

        self.duration = time.time() - start
