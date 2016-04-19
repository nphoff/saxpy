import numpy as np
import random
import math
import unittest
from saxpy import SAX

class test(unittest.TestCase):

    def setUp(self):
        self.sax = SAX()
        self.delta = 1.0e-10

    def testNormalization(self):
        x = [random.random() for x in range(0, 1000)]
        normalizedX = self.sax.normalize(x, self.delta)
        assert abs(np.mean(normalizedX)) < self.delta
