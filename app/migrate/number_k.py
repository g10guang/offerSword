# coding=utf-8
# author: Xiguang Liu<g10guang@foxmail.com>
# 2018-05-02 13:23
# 题目描述：https://www.nowcoder.com/practice/70610bf967994b22bb1c26f9ae901fa2?tpId=13&tqId=11190&rp=1&ru=/ta/coding-interviews&qru=/ta/coding-interviews/question-ranking


class Solution:
    def GetNumberOfK(self, data, k):
        """
        二分搜索
        1) 先找到 k 出现的位置
        2) 从 [lo..ki] 中寻找 k 出现的最左位置
        3) 从 [ki+1..hi] 中寻找 k 出现的最右位置
        """
        lo, hi = 0, len(data) - 1
        ki = 0
        while lo <= hi:
            mid = (hi + lo) // 2
            if data[mid] > k:
                hi = mid - 1
            elif data[mid] < k:
                lo = mid + 1
            else:
                ki = mid
                break
        else:
            # 数字 k 没有在 data 中出现
            return 0
        # 保证 data[k_down+1] == data[k_up-1] == k
        k_down, k_up = ki-1, ki+1
        while lo <= k_down:
            mid = (lo + k_down) // 2
            if data[mid] < k:
                lo = mid + 1
            else:
                # data[mid] == k
                k_down = mid - 1
        while k_up <= hi:
            mid = (k_up + hi) // 2
            if data[mid] > k:
                hi = mid - 1
            else:
                # data[mid] == k
                k_up = mid + 1
        # data[k_down, k_up] 区间内都是 k
        return k_up - k_down - 1


import unittest


class TestCase(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def test_1(self):
        data = [1, 1, 1, 1, 1, 2, 2, 3, 4, 5, 7, 9, 9]
        r = self.s.GetNumberOfK(data, 1)
        self.assertEqual(5, r)
        r = self.s.GetNumberOfK(data, 2)
        self.assertEqual(2, r)
        r = self.s.GetNumberOfK(data, 8)
        self.assertEqual(0, r)
        r = self.s.GetNumberOfK(data, 9)
        self.assertEqual(2, r)

