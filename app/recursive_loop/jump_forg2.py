# coding=utf-8
# author: Xiguang Liu<g10guang@gmail.com>
# 2018-04-27 11:15
# 题目描述：https://www.nowcoder.com/practice/22243d016f6b47f2a6928b4313c85387?tpId=13&tqId=11162&tPage=1&rp=1&ru=%2Fta%2Fcoding-interviews&qru=%2Fta%2Fcoding-interviews%2Fquestion-ranking


class Solution:
    def jumpFloorII(self, number):
        """
        因为青蛙可以跳到任意一级，所以在青蛙本次跳跃中每个台阶都有可能跳上去，也有可能不跳上去。
        抽象：从大小为 n 的集和中所有元素的组合方式有：2**n 种
        :param number:
        :return:
        """
        return 2 ** (number-1)

