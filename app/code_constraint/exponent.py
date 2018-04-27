# coding=utf-8
# author: Xiguang Liu<g10guang@foxmail.com>
# 2018-04-27 13:23
# 题目描述：https://www.nowcoder.com/practice/1a834e5e3e1a4b7ba251417554e07c00?tpId=13&tqId=11165&tPage=1&rp=1&ru=%2Fta%2Fcoding-interviews&qru=%2Fta%2Fcoding-interviews%2Fquestion-ranking


class Solution:

    def Power(self, base, exponent):
        return base ** exponent

    def Power2(self, base, exponent):
        if exponent == 0:
            return 1
        ret = 1
        if exponent > 0:
            for x in range(exponent):
                ret *= base
        # exponent < 0
        else:
            for x in range(exponent, 0):
                ret /= base
        return ret
