import unittest

def solution(s):
    if (not s):
        return 0
    if (len(s) == 1):
        return 1

    for str_len in range(1, len(s) + 1):
        # if length is not divisible then skip
        if len(s) % str_len:
            continue

        # Generate all possible linear combinations
        comb_seq = s + s[:str_len - 1]
        combs = set()
        for start_index in range(len(s)):
            combs.add(comb_seq[start_index:start_index + str_len])
        
        # The number of occurances for every combo
        for comb in combs:
            count = comb_seq.count(comb)
            # Check if the count of combinations and the string are the same length
            if str_len * count == len(s):
                return count

class TestSolution(unittest.TestCase):
    def test1(self):
        self.assertEqual(2, solution("abccbaabccba"))

    def test2(self):
        self.assertEqual(4, solution("abcabcabcabc"))

    def test3(self):
        self.assertEqual(8, solution("aaaaaaaa"))

    def test4(self):
        self.assertEqual(1, solution("abcdefg"))

    def test5(self):
        self.assertEqual(1, solution("abccb8aabccba"))

    def test6(self):
        self.assertEqual(5, solution("abcabcabcabcabc"))

    def test7(self):
        self.assertEqual(3, solution("abcabcabc"))

    def test8(self):
        self.assertEqual(1, solution("ababc"))
    
    def test9(self):
        self.assertEqual(0, solution(""))

    def test10(self):
        self.assertEqual(1, solution("a"))    
         
unittest.main()