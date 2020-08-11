# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# PROBLEM 1                                                                                             #
#   Given a list of numbers and a number k, return whether any two numbers from the list add up to k.   #
#   For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.                      #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
import unittest


def solution(l, k):
    l.sort()

    for i, elem in enumerate(l):
        if elem <= k and l[i+1::].count(k - elem) >= 1:
            return True

    return False


class Test(unittest.TestCase):

    def test_true_values(self):
        self.assertTrue(solution([10, 15, 3, 7], 17))
        self.assertTrue(solution([3, 1, 7, 10, 2, 13, 5], 5))
        self.assertTrue(solution([0, 0, 1, 5, 10], 0))
        self.assertTrue(solution([0, 1, 5, 8, 3, 10], 8))

    def test_false_values(self):
        self.assertFalse(solution([7, 3, 5, 1, 2], 2))
        self.assertFalse(solution([10, 1, 2, 3, 4, 5], 10))
        self.assertFalse(solution([0, 1, 2, 3], 0))
        self.assertFalse(solution([9, 1, 4, 2, 5], 12))


if __name__ == '__main__':
    unittest.main()
