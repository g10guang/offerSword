# coding=utf-8
# author: Xiguang Liu<g10guang@foxmail.com>
# 2018-04-30 11:28
# 题目描述：https://www.nowcoder.com/practice/e8a1b01a2df14cb2b228b30ee6a92163?tpId=13&tqId=11181&tPage=1&rp=1&ru=%2Fta%2Fcoding-interviews&qru=%2Fta%2Fcoding-interviews%2Fquestion-ranking
from builtins import map


class Solution:
    def MoreThanHalfNum_Solution(self, numbers):
        """
        使用字典进行统计计数
        """
        map = {}
        for x in numbers:
            map[x] = map[x] + 1 if x in map else 1
        ret = 0
        half = len(numbers) // 2
        for k, v in map.items():
            if v > half:
                ret = k
        return ret


class Solution2:
    def MoreThanHalfNum_Solution(self, numbers):
        """
        排序
        """
        sn = sorted(numbers)
        mid = len(sn) // 2
        midElem = numbers[mid]
        cnt = 1
        # 向左探索
        for i in range(mid + 1, len(sn)):
            if midElem == sn[i]:
                cnt += 1
        for i in range(mid - 1, -1, -1):
            if midElem == sn[i]:
                cnt += 1
        return midElem if cnt > len(numbers) // 2 else 0


class Solution3:
    def MoreThanHalfNum_Solution(self, numbers):
        """
        使用 O(1) 空间进行统计计数
        以下统计 majotiry 方法只能够使用在 majority 出现次数超过数组长度一半的情况下，不适用于普通数组
        """
        majority = numbers[0]
        cnt = 1
        for i in range(1, len(numbers)):
            cnt = cnt + 1 if numbers[i] == majority else cnt - 1
            if cnt == 0:
                # majority 不可能出现在 [0..i] 之间
                majority = numbers[i]
                cnt = 1
        cnt = 0
        for x in numbers:
            if x == majority:
                cnt += 1
        return majority if cnt > len(numbers) // 2 else 0


import unittest


class TestCase(unittest.TestCase):
    def setUp(self):
        self.s = Solution2()

    def test_1(self):
        numbers = [1, 2, 3, 2, 2, 2, 5, 4, 2]
        r = self.s.MoreThanHalfNum_Solution(numbers)
        self.assertEqual(2, r)


def majority(nums):
    m, cnt = nums[0], 1
    for i in range(1, len(nums)):
        cnt = cnt + 1 if m == nums[i] else cnt - 1
        if cnt == 0:
            m = nums[i]
    return m


def majority2(nums):
    for i in nums:
        nums[i] += 100
    print(nums)
