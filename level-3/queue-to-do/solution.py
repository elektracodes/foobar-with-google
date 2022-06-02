import unittest

###
# Pattern
# n % 4 = 0, xor of range = n;
# n % 4 = 1, xor of range = 1;
# n % 4 = 2, xor of range = n+1;
# n % 4 = 3, xor of range = 0;
###

def xor(n):
    val = n % 4
    if val == 0:
        return n
    if val == 1:
        return 1
    if val == 2:
        return n + 1
    return 0

def solution(start, length):
    res = 0
    st = start - 1
    
    for i in range(length):
        check = st + length - i
        res ^= xor(st) ^ xor(check)
        st = check + i

    return res


class TestSolution(unittest.TestCase):
    def test1(self):
        self.assertEqual(2, solution(0, 3))
    def test2(self):
        self.assertEqual(14, solution(17,4))
    def test3(self):
        self.assertEqual(159001697058816, solution(0,20000000))

# Ran 3 tests in 9.790s                                                     
unittest.main()