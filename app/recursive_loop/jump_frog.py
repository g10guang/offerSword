# coding=utf-8
# author: Xiguang Liu<g10guang@gmail.com>
# 2018-04-27 11:04
# 题目描述：https://www.nowcoder.com/practice/8c82a5b80378478f9484d87d1c5f12a4?tpId=13&tqId=11161&tPage=1&rp=1&ru=%2Fta%2Fcoding-interviews&qru=%2Fta%2Fcoding-interviews%2Fquestion-ranking


class Solution:
    def __init__(self):
        self.dp = {0: 1, 1: 1, 2: 2}

    def jumpFloor(self, number):
        """
        动态规划
        :param number:
        :return:
        """
        if number in self.dp:
            return self.dp[number]
        f = self.jumpFloor(number-1) + self.jumpFloor(number-2)
        self.dp[number] = f
        return f
