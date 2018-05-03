# coding=utf-8
# author: Xiguang Liu<g10guang@foxmail.com>
# 2018-05-03 11:51
# 题目描述：https://www.nowcoder.com/practice/390da4f7a00f44bea7c2f3d19491311b?tpId=13&tqId=11195&rp=1&ru=%2Fta%2Fcoding-interviews&qru=%2Fta%2Fcoding-interviews%2Fquestion-ranking


class Solution:
    def FindNumbersWithSum(self, array, tsum):
        result = None
        p, q = 0, len(array) - 1
        while p < q:
            if array[p] + array[q] == tsum:
                if result:
                    if result[0] * result[1] > array[p] * array[q]:
                        result = [array[p], array[q]]
                else:
                    result = [array[p], array[q]]
                p += 1
                q -= 1
            elif array[p] + array[q] > tsum:
                q -= 1
            else:
                p += 1
        return result if result else []


