# coding=utf-8
# author: Xiguang Liu<g10guang@gmail.com>
# 2018-04-26 17:27
# 题目描述：https://www.nowcoder.com/practice/4060ac7e3e404ad1a894ef3e17650423?tpId=13&tqId=11155&tPage=1&rp=1&ru=%2Fta%2Fcoding-interviews&qru=%2Fta%2Fcoding-interviews%2Fquestion-ranking


class Solution:
    # s 源字符串
    def replaceSpace(self, s):
        return s.replace(' ', "%20")
