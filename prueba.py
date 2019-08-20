from numeroscomplejos import *
import unittest

class PruebasFunciones(unittest.TestCase):
    def test(self):
        self.assertEqual(suma((2,1),(1,3)),(3,4))
        self.assertEqual(producto((3, -2), (1, 2)), (7, 4))
        self.assertEqual(producto((0, 1), (0, 1)), (-1, 0))
        self.assertEqual(resta((2, -3), (4, -1)), (-2, -2))
        self.assertEqual(resta((3, -2), (4, -6)), (-1, 4))
        self.assertEqual(division((-2, 1), (1, 2)), (0, 1))

        self.assertEqual(modulo((3,9)),9.486832980505138)
        self.assertEqual(conjugado((7, 10)), (7, -10))
        self.assertEqual(polar((3,2)), (3.605551275463989,0.5880026035475675))
        self.assertEqual(fase((2, 89)), 1.548328198209071)


if __name__ == '__main__':
    unittest.main()
