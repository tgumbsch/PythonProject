import numpy as np

from cpp.cpp import CppCUMSUM
from py.py import PyCUMSUM
from R.R import RCUMSUM
methods = [PyCUMSUM, RCUMSUM, CppCUMSUM]
names = ['Python', 'R', 'C++']

from matplotlib import pyplot as plt


plt.rc('text', usetex=True)
plt.rc('font', family='serif')

trials = 3
ranges = [int(k) for k in np.logspace(0, 10, 5, base=2)]


def Runtime(method):
    Rt = []
    for lengths in ranges:
        seq = np.random.randn(lengths)
        time = []
        for k in range(trials):
            m = method(seq)
            time.append(m.duration)
        Rt.append(time)
    return Rt


if __name__ == "__main__":
    for n, m in zip(names, methods):
        Tm = Runtime(m)
        plt.errorbar(ranges, [np.mean(k) for k in Tm], yerr=[np.std(k) for k in Tm], label=n)
    plt.xlabel('length', fontsize=14)
    plt.ylabel('s', fontsize=14)
    plt.legend(loc='best', fontsize=14)
    plt.semilogx()
    plt.semilogy()
    plt.savefig('Runtime.pdf')
