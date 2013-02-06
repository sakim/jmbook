# -*- coding: UTF-8 -*-
import festival
import unittest

class TestFestival(unittest.TestCase):
  def test_calculate(self):
    r = festival.calculate([1, 2, 3, 1, 2, 3], 3)
    self.assertEqual(r, 1.75000000000)
    r = festival.calculate([1, 2, 3, 1, 2, 3], 2)
    self.assertEqual(r, 1.50000000000)
    r = festival.calculate([3, 2, 3, 1, 2, 1], 3)
    self.assertEqual(r, 4/float(3))

if __name__ == '__main__':
  unittest.main( )