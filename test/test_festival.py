# -*- coding: UTF-8 -*-
import unittest

import festival


class FestivalTest(unittest.TestCase):
    def test_solve(self):
        r = festival.solve([1, 2, 3, 1, 2, 3], 3)
        self.assertEqual(r, 1.75000000000)
        r = festival.solve([1, 2, 3, 1, 2, 3], 2)
        self.assertEqual(r, 1.50000000000)
        r = festival.solve([3, 2, 3, 1, 2, 1], 3)
        self.assertEqual(r, 4 / float(3))

if __name__ == '__main__':
    unittest.main()