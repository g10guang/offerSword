# coding=utf-8
# author: Xiguang Liu<g10guang@foxmail.com>
# 2018-05-02 14:07
# 题目描述：https://www.nowcoder.com/practice/e02fdb54d7524710a7d664d082bb7811?tpId=13&tqId=11193&rp=1&ru=%2Fta%2Fcoding-interviews&qru=%2Fta%2Fcoding-interviews%2Fquestion-ranking


class Solution:
    def __init__(self):
        self.arr = None
        self.result = []

    # 返回[a,b] 其中ab是出现一次的两个数字
    def FindNumsAppearOnce(self, array):
        """
        思路： 使用三向切分的快速排序
        因为数组中有且仅有一个数字出现了一个，其他数字都出现了两次，所以只出现一个的数字肯定出现在长度为奇数的那一边
        """
        self.arr = array
        self.qsort(0, len(array) - 1)
        return self.result

    def qsort(self, lo, hi):
        if lo == hi:
            self.result.append(self.arr[lo])
            return
        if lo >= hi:
            return
        lt, i, gt = lo, lo + 1, hi
        elem = self.arr[lo]
        while i <= gt:
            if self.arr[i] < elem:
                self.arr[i], self.arr[lt] = self.arr[lt], self.arr[i]
                lt += 1
                i += 1
            elif self.arr[i] > elem:
                self.arr[i], self.arr[gt] = self.arr[gt], self.arr[i]
                gt -= 1
            else:
                # self.arr[i] == elem
                i += 1
        # [lo..lt-1] < v
        # [lt..gt] == v
        # [gt+1..hi] > v
        if lt == gt:
            self.result.append(elem)
            if (lt - lo) % 2 == 1:
                self.qsort(lo, lt - 1)
            else:
                self.qsort(gt + 1, hi)
        else:
            self.qsort(lo, lt - 1)
            self.qsort(gt + 1, hi)


class Solution2:
    def FindNumsAppearOnce(self, array):
        """
        使用哈希表进行统计计数
        """
        map = {}
        for x in array:
            if x not in map:
                map[x] = 1
            else:
                map[x] += 1
        result = []
        for k, v in map.items():
            if v == 1:
                result.append(k)
                if len(result) == 2:
                    break
        return result


import unittest


class TestCase(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def test_1(self):
        arr = [1, 2, 3, 4, 3, 2, 1, 6]
        r = self.s.FindNumsAppearOnce(arr)
        self.assertEqual([4, 6], r)

    def test_2(self):
        arr = [1, 2, 3, 4, 1, 2, 3, 4, 0, 8]
        r = self.s.FindNumsAppearOnce(arr)
        self.assertEqual([0, 8], r)
