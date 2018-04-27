# coding=utf-8
# author: Xiguang Liu<g10guang@gmail.com>
# 2018-04-27 10:48
# 题目描述：https://www.nowcoder.com/practice/c6c7742f5ba7442aada113136ddea0c3?tpId=13&tqId=11160&tPage=1&rp=1&ru=%2Fta%2Fcoding-interviews&qru=%2Fta%2Fcoding-interviews%2Fquestion-ranking


class Solution:
    def __init__(self):
        # 动态规划中保存之前的计算结果
        self.dp = {0: 0, 1: 1, 2: 1}

    def Fibonacci(self, n):
        """
        寻找 Fibonacci 的第 n 项目
        :param n:
        :return:
        """
        if n in self.dp:
            return self.dp[n]
        f = self.Fibonacci(n - 1) + self.Fibonacci(n - 2)
        self.dp[n] = f
        return f
