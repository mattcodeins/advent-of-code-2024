import unittest
from utils import *

class TestGrid(unittest.TestCase):
    def setUp(self):
        grid = readlines('testdata/grid.txt', prnt=False)
        self.G = M(grid)

    def test_print(self):
        self.assertEqual(self.G.__str__(), gp)

    def test_get(self):
        self.assertEqual(self.G[2,0], 2)

    def test_set(self):
        self.G[2,0] = 'X'
        self.assertEqual(self.G[2,0], 'X')

    def test_rotate(self):
        self.G.rotate()
        self.assertEqual(self.G.__str__(), grot)

    def test_fliplr(self):
        self.G.fliplr()
        self.assertEqual(self.G.__str__(), gfh)

    def test_flipud(self):
        self.G.flipud()
        self.assertEqual(self.G.__str__(), gfv)

gp = """\
..2.
1...
...3
.4..\
"""

grot = """\
..1.
4...
...2
.3..\
"""

gfh = """\
.2..
...1
3...
..4.\
"""

gfv = """\
.4..
...3
1...
..2.\
"""

if __name__ == '__main__':
    unittest.main()