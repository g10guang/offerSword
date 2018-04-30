# coding=utf-8
# author: Xiguang Liu<g10guang@foxmail.com>
# 2018-04-30 13:38
# 题目描述：https://www.nowcoder.com/practice/6a296eb82cf844ca8539b57c23e6e9bf?tpId=13&tqId=11182&rp=1&ru=/ta/coding-interviews&qru=/ta/coding-interviews/question-ranking


class Solution:
    def GetLeastNumbers_Solution(self, tinput, k):
        """
        使用快排
        """
        if k > len(tinput) or k == 0:
            return []
        self.qsort(tinput, 0, len(tinput) - 1, k)
        return sorted(tinput[:k])

    def qsort(self, tinput, lo, hi, k):
        if lo == hi:
            return
        head = lo
        i, tail = head + 1, hi
        elem = tinput[head]
        while i <= tail:
            if tinput[i] > elem:
                tinput[i], tinput[tail] = tinput[tail], tinput[i]
                tail -= 1
            else:
                tinput[i], tinput[head] = tinput[head], tinput[i]
                i += 1
                head += 1
        tinput[head] = elem
        if head == k - 1:
            return
        elif head > k - 1:
            self.qsort(tinput, lo, head - 1, k)
        else:
            # head < k - 1
            self.qsort(tinput, head + 1, hi, k)


from heapq import heappop, heappush


class Solution2:
    def GetLeastNumbers_Solution(self, tinput, k):
        """
        使用堆排序
        因为 python 原生使用的是小顶堆，而我们这题目中需要用到大顶堆，所以本题目中将 tinput 中的数字转化为负数处理
        """
        if k == 0 or k > len(tinput):
            return []
        h = []
        index = 0
        while len(h) < k:
            heappush(h, -tinput[index])
            index += 1
        for x in range(index, len(tinput)):
            t = -tinput[x]
            if t > h[0]:
                heappop(h)
                heappush(h, t)
        ret = [0] * k
        index = k - 1
        while h:
            ret[index] = -heappop(h)
            index -= 1
        return ret


import unittest


class TestCase(unittest.TestCase):
    def setUp(self):
        self.s = Solution()
        self.s2 = Solution2()

    def test_1(self):
        arr = [4, 5, 1, 6, 2, 7, 3, 8]
        k = 4
        r = self.s.GetLeastNumbers_Solution(arr, k)
        self.assertEqual([1, 2, 3, 4], r)

    def test_2(self):
        arr = [4, 5, 1, 6, 2, 7, 3, 8]
        k = 8
        r = self.s.GetLeastNumbers_Solution(arr, k)
        self.assertEqual([1, 2, 3, 4, 5, 6, 7, 8], r)

    def test_3(self):
        arr = [4, 5, 1, 6, 2, 7, 3, 8]
        k = 10

    def test_4(self):
        arr = [4, 5, 1, 6, 2, 7, 3, 8]
        k = 4
        r = self.s2.GetLeastNumbers_Solution(arr, k)
        self.assertEqual([1, 2, 3, 4], r)

    def test_5(self):
        arr = [4, 5, 1, 6, 2, 7, 3, 8]
        k = 8
        r = self.s2.GetLeastNumbers_Solution(arr, k)
        self.assertEqual([1, 2, 3, 4, 5, 6, 7, 8], r)

