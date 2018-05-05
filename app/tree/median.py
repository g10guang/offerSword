# -*- coding: utf-8 -*-
# author: Xiguang Liu<g10guang@foxmail.com>
# 2018-05-05 16:59
# 题目描述：https://www.nowcoder.com/practice/9be0172896bd43948f8a32fb954e1be1?tpId=13&tqId=11216&rp=1&ru=%2Fta%2Fcoding-interviews&qru=%2Fta%2Fcoding-interviews%2Fquestion-ranking


class Solution:
    """
    每次取中位数时候就重新排序
    """

    def __init__(self):
        self.container = []

    def Insert(self, num):
        self.container.append(num)

    def GetMedian(self):
        t = sorted(self.container)
        self.container = t
        if len(t) % 2 == 0:
            # python2 中 int / int == int
            # python3 中 int / int == float
            return (t[len(t) // 2] + t[len(t) // 2 - 1]) / float(2)
        return t[len(t) // 2]


from heapq import heappush, heappop


class Solution2:
    """
    维护两个堆，其中一个为 left 大根堆，另一个 right 最小根堆
    将小于中值的都插入到 left 中，将所有大于中值的都插入到 right 中
    这样就可以以最快的速度取到中值，以计算中位数

    因为所有元素都有可能成为中位数，因为后面的输入还不清楚，所以需要保存所有的元素

    由于 python 堆为小顶堆，而在本算法中需要用到大顶堆，借助一个小技巧，将大顶堆中的所有元素取相反数
    """

    def __init__(self):
        self.left = []
        self.right = []
        self.elemNum = 0

    def Insert(self, num):
        if len(self.right) == 0 or num > self.right[0]:
            heappush(self.right, num)
        else:
            # 取反 num
            heappush(self.left, -num)
        # 调整两个堆，目的 -1 <= len(self.left) - len(self.right) <= 1
        while len(self.left) - len(self.right) > 1:
            elem = -heappop(self.left)
            heappush(self.right, elem)
        while len(self.right) - len(self.left) > 1:
            elem = heappop(self.right)
            heappush(self.left, -elem)

    def GetMedian(self):
        if len(self.left) == len(self.right):
            if len(self.left) == 0:
                return 0
            return (-self.left[0] + self.right[0]) / 2.0
        elif len(self.left) > len(self.right):
            return -self.left[0]
        else:
            return self.right[0]


import unittest


class TestCase(unittest.TestCase):
    def setUp(self):
        self.s = Solution2()

    def test_1(self):
        data = [5, 2, 3, 4, 1, 6, 7, 0, 8]
        median = [5, 3.5, 3, 3.5, 3, 3.5, 4, 3.5, 4]
        for i, x in enumerate(data):
            self.s.Insert(x)
            r = self.s.GetMedian()
            self.assertEqual(median[i], r)
        # r = self.s.GetMedian()
        # self.assertEqual(4, r)
