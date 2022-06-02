import unittest

def solution(l):
    return sorted(l, key=lambda j: [int(i) for i in j.split('.')])

class TestSolution(unittest.TestCase):
    def test1(self):
        self.assertEqual(["0.1","1.1.1","1.2","1.2.1","1.11","2","2.0","2.0.0"], solution(["1.11", "2.0.0", "1.2", "2", "0.1", "1.2.1", "1.1.1", "2.0"]))
    def test2(self):
        self.assertEqual(["1.0","1.0.2","1.0.12","1.1.2","1.3.3"], solution(["1.1.2", "1.0", "1.3.3", "1.0.12", "1.0.2"]))
    def test3(self):
        self.assertEqual([], solution([]))
    def test4(self):
        self.assertEqual(["1.0","1.0.20","10.0.12","10.1.2","12.3.3"], solution(["12.3.3","1.0.20","1.0","10.0.12","10.1.2",]))
unittest.main()