# coding=utf-8
# author: Xiguang Liu<g10guang@foxmail.com>
# 2018-05-02 12:08
# 题目描述：https://www.nowcoder.com/practice/96bd6684e04a44eb80e6a68efc0ec6c5?tpId=13&tqId=11188&rp=1&ru=/ta/coding-interviews&qru=/ta/coding-interviews/question-ranking


import copy


class Solution3:
    def __init__(self):
        self.tmp = None
        self.data = None
        self.cnt = 0

    def InversePairs(self, data):
        """
        前两种方法都超时
        选用更加快速的排序方法：归并排序
        归并排序也无法 AC.....Python 还是慢
        """
        self.data = data
        self.tmp = copy.copy(data)
        self.mergeSort(0, len(self.data) - 1)
        return self.cnt

    def mergeSort(self, lo, hi):
        if lo >= hi:
            return
        mid = (lo + hi) // 2
        self.mergeSort(lo, mid)
        self.mergeSort(mid + 1, hi)
        self.merge(lo, mid, hi)

    def merge(self, lo, mid, hi):
        i, k = lo, mid + 1
        ti = lo
        while i <= mid and k <= hi:
            if self.data[i] < self.data[k]:
                self.tmp[ti] = self.data[i]
                i += 1
            else:
                self.tmp[ti] = self.data[k]
                # 只有后面往前插入时才需要更新 self.cnt
                # [i..mid] 中的数字与 data[k] 组成 mid-i+1 对逆序对
                self.cnt += mid - i + 1
                k += 1
            ti += 1
        while i <= mid:
            self.tmp[ti] = self.data[i]
            ti += 1
            i += 1
        while k <= hi:
            self.tmp[ti] = self.data[k]
            ti += 1
            k += 1
        for x in range(lo, hi + 1):
            self.data[x] = self.tmp[x]


class Solution:
    def InversePairs(self, data):
        cnt = 0
        for i in range(0, len(data) - 1):
            for j in range(i + 1, len(data)):
                if data[i] > data[j]:
                    cnt += 1
        return cnt


class Solution2:
    def InversePairs(self, data):
        """
        使用稳定的排序方法，然后统计元素移动的位置距离，就可以判断逆袭对有多少
        这里简单地使用插入排序
        """
        cnt = 0
        for i in range(1, len(data)):
            k = i
            t = data[i]
            while k > 0 and t < data[k - 1]:
                data[k] = data[k - 1]
                cnt += 1
                k -= 1
            data[k] = t
        return cnt


import unittest


class TestCase(unittest.TestCase):
    def setUp(self):
        self.s = Solution3()

    def test_1(self):
        data = [1, 2, 3, 4, 5, 6, 7, 0]
        r = self.s.InversePairs(data)
        self.assertEqual(7, r)

    def test_2(self):
        data = [364, 637, 341, 406, 747, 995, 234, 971, 571, 219, 993, 407, 416, 366, 315, 301, 601, 650, 418, 355, 460,
                505, 360, 965, 516, 648, 727, 667, 465, 849, 455, 181, 486, 149, 588, 233, 144, 174, 557, 67, 746, 550,
                474, 162, 268, 142, 463, 221, 882, 576, 604, 739, 288, 569, 256, 936, 275, 401, 497, 82, 935, 983, 583,
                523, 697, 478, 147, 795, 380, 973, 958, 115, 773, 870, 259, 655, 446, 863, 735, 784, 3, 671, 433, 630,
                425, 930, 64, 266, 235, 187, 284, 665, 874, 80, 45, 848, 38, 811, 267, 575]
        r = self.s.InversePairs(data)
        self.assertEqual(2519, r)
