# -*- coding: UTF-8 -*-
__author__ = 'sakim'

import unittest
import picnic


class PicnicTest(unittest.TestCase):
    def test_solve(self):
        self.assertEqual(1, picnic.solve(2, [0, 1]))
        self.assertEqual(3, picnic.solve(4, [0, 1, 1, 2, 2, 3, 3, 0, 0, 2, 1, 3]))
        self.assertEqual(4, picnic.solve(6, [0, 1, 0, 2, 1, 2, 1, 3, 1, 4, 2, 3, 2, 4, 3, 4, 3, 5, 4, 5]))
        self.assertEqual(945, picnic.solve(10,
                                           [0, 1,
                                            0, 2,
                                            0, 3,
                                            0, 4,
                                            0, 5,
                                            0, 6,
                                            0, 7,
                                            0, 8,
                                            0, 9,
                                            1, 2,
                                            1, 3,
                                            1, 4,
                                            1, 5,
                                            1, 6,
                                            1, 7,
                                            1, 8,
                                            1, 9,
                                            2, 3,
                                            2, 4,
                                            2, 5,
                                            2, 6,
                                            2, 7,
                                            2, 8,
                                            2, 9,
                                            3, 4,
                                            3, 5,
                                            3, 6,
                                            3, 7,
                                            3, 8,
                                            3, 9,
                                            4, 5,
                                            4, 6,
                                            4, 7,
                                            4, 8,
                                            4, 9,
                                            5, 6,
                                            5, 7,
                                            5, 8,
                                            5, 9,
                                            6, 7,
                                            6, 8,
                                            6, 9,
                                            7, 8,
                                            7, 9,
                                            8, 9]))


if __name__ == '__main__':
    unittest.main()
