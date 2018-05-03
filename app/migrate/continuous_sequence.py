# coding=utf-8
# author: Xiguang Liu<g10guang@foxmail.com>
# 2018-05-03 11:12
# 题目描述：https://www.nowcoder.com/practice/c451a3fd84b64cb19485dad758a55ebe?tpId=13&tqId=11194&rp=1&ru=%2Fta%2Fcoding-interviews&qru=%2Fta%2Fcoding-interviews%2Fquestion-ranking


class Solution:
    def FindContinuousSequence(self, tsum):
        threshold = tsum // 2 + 1
        result = []
        start = 1
        sumtmp = 1
        index = 1
        while index <= threshold:
            if sumtmp == tsum:
                if index - start >= 1:
                    result.append(list(range(start, index + 1)))
                    sumtmp -= start
                    start += 1
            index += 1
            sumtmp += index
            while sumtmp > tsum:
                sumtmp -= start
                start += 1
        return result


import unittest


class TestCase(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def test_1(self):
        tsum = 11
        r = self.s.FindContinuousSequence(tsum)
        self.assertEqual([list(range(5, 7))], r)

    def test_2(self):
        tsum = 100
        r = self.s.FindContinuousSequence(tsum)
        self.assertEqual([list(range(9, 17)), list(range(18, 23))], r)

    def test_3(self):
        tsum = 1
        r = self.s.FindContinuousSequence(tsum)
        self.assertEqual([], r)

    def test_4(self):
        tsum = 3
        r = self.s.FindContinuousSequence(tsum)
        self.assertEqual([[1, 2]], r)
