import unittest

def solution(x, y):
    return str((x + y - 1) * (x + y - 2) // 2 + x)

class TestSolution(unittest.TestCase):
    def test1(self):
        self.assertEqual("96", solution(5, 10))
    def test2(self):
        self.assertEqual("9", solution(3, 2))
    def test3(self):
        self.assertEqual("1", solution(1, 1))    
    def test4(self):
        self.assertEqual("4", solution(1, 3))
    def test5(self):
        self.assertEqual("1", solution(0, 0))  
                         
unittest.main()