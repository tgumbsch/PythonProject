import numpy as np
import unittest
from py.py import PyCUMSUM, cumsum
from cpp.cpp import CppCUMSUM
from R.R import RCUMSUM
#"""


class TestPyCUMSUM(unittest.TestCase):
    def test_intsample(self):
        seq = [1, 2, 3, 4, 5]
        ex = [1, 3, 6, 10, 15]
        PyC = PyCUMSUM(seq)
        self.assertEqual(ex, PyC.cumsum)
        self.assertEqual(ex, cumsum(seq))

    def test_np(self):
        r = np.random.RandomState(0)
        cases = 10
        length = 100
        for dummy_iterator in range(cases):
            seq = r.randn(length)
            PyC = PyCUMSUM(seq)
            NpC = np.cumsum(seq)
            pyc = cumsum(seq)
            for Py, py, Np in zip(PyC.cumsum, pyc, NpC):
                self.assertAlmostEqual(Np, Py, places=10)
                self.assertAlmostEqual(Np, py, places=10)

    def test_cpp(self):
        r = np.random.RandomState(0)
        cases = 10
        length = 100
        for dummy_iterator in range(cases):
            seq = r.randn(length)
            PyC = PyCUMSUM(seq)
            CppC = CppCUMSUM(seq)
            pyc = cumsum(seq)
            for Py, py, Cpp in zip(PyC.cumsum, pyc, CppC.cumsum):
                self.assertAlmostEqual(Cpp, Py, places=10)
                self.assertAlmostEqual(Cpp, py, places=10)

    def test_R(self):
        r = np.random.RandomState(0)
        cases = 10
        length = 100
        for dummy_iterator in range(cases):
            seq = r.randn(length)
            PyC = PyCUMSUM(seq)
            RC = RCUMSUM(seq)
            pyc = cumsum(seq)
            for Py, py, R in zip(PyC.cumsum, pyc, RC.cumsum):
                self.assertAlmostEqual(R, Py, places=10)
                self.assertAlmostEqual(R, py, places=10)


class TestCppCUMSUM(unittest.TestCase):
    def test_intsample(self):
        seq = [1, 2, 3, 4, 5]
        ex = [1, 3, 6, 10, 15]
        CppC = CppCUMSUM(seq)
        self.assertEqual(ex, CppC.cumsum)

    def test_npcumsum(self):
        cases = 10
        length = 100
        r = np.random.RandomState(0)
        for dummy_iterator in range(cases):
            seq = r.randn(length)
            CppC = PyCUMSUM(seq)
            NpC = np.cumsum(seq)
            for Cpp, Np in zip(CppC.cumsum, NpC):
                self.assertAlmostEqual(Np, Cpp, places=10)


class TestRCUMSUM(unittest.TestCase):
    def test_intsample(self):
        seq = [1, 2, 3, 4, 5]
        ex = [1, 3, 6, 10, 15]
        RC = RCUMSUM(seq)
        self.assertEqual(ex, RC.cumsum)

    def test_npcumsum(self):
        cases = 10
        length = 100
        r = np.random.RandomState(0)
        for dummy_iterator in range(cases):
            seq = r.randn(length)
            RC = RCUMSUM(seq)
            NpC = np.cumsum(seq)
            for R, Np in zip(RC.cumsum, NpC):
                self.assertAlmostEqual(Np, R, places=10)


if __name__ == '__main__':
    unittest.main()
