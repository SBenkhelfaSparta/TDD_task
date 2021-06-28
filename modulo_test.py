import unittest
import pytest

from modulo import Modulo

class ModuloTest(unittest.TestCase):
    modu = Modulo()

    def test_mod(self):
        self.assertEqual(self.modu.mod(10, 2), 0)

    def test_positive(self):
        self.assertEqual(self.modu.positive(-21, 9), False)
