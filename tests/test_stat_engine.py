import unittest
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))
from src.stat_engine import StatEngine

class TestStatEngine(unittest.TestCase):

    def test_mean(self):
        engine = StatEngine([1,2,3])
        self.assertEqual(engine.get_mean(), 2)

    def test_median(self):
        engine = StatEngine([1,2,3,4])
        self.assertEqual(engine.get_median(), 2.5)

    def test_mode(self):
        engine = StatEngine([1,1,2,2])
        self.assertEqual(engine.get_mode(), [1,2])

if __name__ == "__main__":
    unittest.main()