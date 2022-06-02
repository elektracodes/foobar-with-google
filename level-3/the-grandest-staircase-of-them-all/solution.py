import unittest

###
#    In order to solve this challenge we need to undestand Partition theories and specifically
#    how to partition numbers with distrinct parts. (src https://en.wikipedia.org/wiki/Partition_(number_theory)#Odd_parts_and_distinct_parts)
#
#    Definition: A partition of a nonnegative integer n is a nonincreasing sequence
#    of positive integers with sum n.
#
#    For example 4 can be divide to these partitions 3+1 | 2+2 | 2+1+1 | 1+1+1+1 
#    but not to 5-1 | 6-2 | 6-3+1 etc.
# 
#    By using this formula we can manually calculate these test cases
#
#    solution(3) = 1, {2, 1}  
#    solution(4) = 1, {3, 1}
#    solution(5) = 2, {4, 1}, {3, 2}
#    solution(6) = 3, {5, 1}, {4, 2}, {3, (3) -> {2, 1}}
#    solution(7) = 4, {6, 1}, {5, 2}, {4, 3}, {4, (3) -> {2, 1}}
#    solution(8) = 5, {7, 1}, {6, 2}, {5, 3}, {5, (3) -> {2, 1}}, {4, (4) -> {3, 1}}
#    solution(9) = 7, {8, 1}, {7, 2}, {6, 3}, {5, 4}, {5, (4) -> {3, 1}}, {4, (5) -> {3, 2}}
###

def cached_staircases(n):
    cache = [[None]*(n+2) for i in range(n+1)]
   
    def calc_num_staircases(n,height):
      if cache[n][height]!=None:
        return cache[n][height]
      if n==0:
        return 1
      elif n<height:
        return 0
      else:
        remaining=calc_num_staircases(n-height,height+1)+calc_num_staircases(n,height+1)
        cache[n][height] = remaining
        return remaining
    
    # We need to subtrack 1 from the total because of this statement of the challenge
    # >Each type of staircase should consist of 2 or more steps. No two steps are allowed to be at the same height - each step must be lower than the previous one    
    return calc_num_staircases(n,1)-1

def solution(n):
      return cached_staircases(n)


class TestSolution(unittest.TestCase):
    def test1(self):
        self.assertEqual(487067745, solution(200))
    def test2(self):
        self.assertEqual(1, solution(3))
    def test3(self):
        self.assertEqual(1, solution(4))
    def test4(self):
        self.assertEqual(2, solution(5))
    def test4(self):
        self.assertEqual(3, solution(6))
    def test5(self):
        self.assertEqual(4, solution(7))
    def test6(self):
        self.assertEqual(5, solution(8))
    def test7(self):
        self.assertEqual(7, solution(9))                                                                             
unittest.main()