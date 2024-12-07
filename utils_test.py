import unittest
from utils import *

class TestGrid(unittest.TestCase):
    def setUp(self):
        self.lines = readlines('testdata/grid.txt')
        self.G = Grid(self.lines, '^', 3)
        self.assertEqual(self.G.X, (4,6))

    def test_print(self):
        self.assertEqual(
            self.G.__str__(),
"""....#.....
.........#
..........
..#.......
.......#..
..........
.#..^.....
........#.
#.........
......#...""")

    def test_get(self):
        self.assertEqual(self.G[4,0], '#')

    def test_isupper(self):
        print()
        self.assertFalse('FOO'.isupper())

    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)

if __name__ == '__main__':
    unittest.main()