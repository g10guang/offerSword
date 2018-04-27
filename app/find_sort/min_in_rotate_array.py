# coding=utf-8
# author: Xiguang Liu<g10guang@gmail.com>
# 2018-04-27 10:19
# 题目描述：https://www.nowcoder.com/practice/9f3231a991af4f55b95579b44b7a01ba?tpId=13&tqId=11159&tPage=1&rp=1&ru=%2Fta%2Fcoding-interviews&qru=%2Fta%2Fcoding-interviews%2Fquestion-ranking


import unittest


class Solution:
    def minNumberInRotateArray(self, rotateArray):
        """
        在旋转数组中寻找最小值
        思路：
        使用二分查找
        :param rotateArray:
        :return:
        """
        lo, hi = 0, len(rotateArray) - 1
        while lo < hi:
            mid = (lo + hi) // 2
            elem = rotateArray[mid]
            if elem > rotateArray[hi]:
                lo = mid + 1
            elif elem < rotateArray[hi]:
                # 这里不能够是 hi = mid - 1 因为有可能 rotateArray[mid] 有可能是最小值
                hi = mid
            else:
                return elem
        return rotateArray[hi]


class TestCase(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def test_1(self):
        rotateArray = [6501, 6828, 6963, 7036, 7422, 7674, 8146, 8468, 8704, 8717, 9170, 9359, 9719, 9895, 9896, 9913,
                       9962, 154, 293, 334, 492, 1323, 1479, 1539, 1727, 1870, 1943, 2383, 2392, 2996, 3282, 3812, 3903,
                       4465, 4605, 4665, 4772, 4828, 5142, 5437, 5448, 5668, 5706, 5725, 6300, 6335]
        r = self.s.minNumberInRotateArray(rotateArray)
        self.assertEqual(154, r)
