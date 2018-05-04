# -*- coding: utf-8 -*-
# author: Xiguang Liu<g10guang@foxmail.com>
# 2018-05-04 14:05
# 题目描述：https://www.nowcoder.com/practice/94a4d381a68b47b7a8bed86f2975db46?tpId=13&tqId=11204&rp=1&ru=%2Fta%2Fcoding-interviews&qru=%2Fta%2Fcoding-interviews%2Fquestion-ranking


class Solution:
    def multiply(self, A):
        """
        累乘，时间复杂度 = O(n^2)
        :param A:
        :return:
        """
        l = len(A)
        B = [1] * l
        for i in range(l):
            for j in range(l):
                if i != j:
                    B[i] *= A[j]
        return B


class Solution2:
    def multiply(self, A):
        """
        B[i] = A[0] * A[1] * ... * A[i-1] * A[i+1] * ... * A[n-1]
        思路：
        B[i] 分为两半运算 A[0] * A[1] * ... * A[i-1] 和 A[i+1] * ... * A[n-1]
        时间复杂度 = O(n)
        """
        B = [0] * len(A)
        i = 0
        t = 1
        while i < len(A):
            # 保证：t = A[0] * A[1] * ... * A[i-1]
            B[i] = t
            t *= A[i]
            i += 1
        i = len(A) - 1
        t = 1
        while i >= 0:
            # 保证 t = A[n-1] * A[n-1] * ... * A[i+1]
            B[i] *= t
            t *= A[i]
            i -= 1
        return B
