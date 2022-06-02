import unittest

# Alternative way would be to use binary string (TODO)

def solution(n):
    # Cast n to int, initiate count
    n = int(n)
    cycle = 0 # The minimum number of operations it takes to get to 0
    # With n as binary, if cycle is even, divide
    while n != 1:
        if (n % 2) == 0:
            n /= 2
            cycle += 1
        else:
            if (n + 1)/2 == 1:
                n += 1
                cycle += 1
            elif (n - 1)/2 == 1:
                n -= 1
                cycle += 1
            elif ((n + 1)/2 % 2) == 0:
                n += 1
                cycle += 1
            elif ((n - 1)/2 % 2) == 0:
                n -= 1
                cycle += 1

    return cycle

class TestSolution(unittest.TestCase):
    def test1(self):
        self.assertEqual(2, solution("4"))
    def test2(self):
        self.assertEqual(5, solution("15"))
    def test3(self):
        self.assertEqual(1480, solution("999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999"))

# Ran 3 tests in 0.002s                                                  
unittest.main()