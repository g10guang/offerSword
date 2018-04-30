# coding=utf-8
# author: Xiguang Liu<g10guang@foxmail.com>
# 2018-04-30 14:24
# 题目描述：https://www.nowcoder.com/practice/459bd355da1549fa8a49e350bf3df484?tpId=13&tqId=11183&rp=1&ru=%2Fta%2Fcoding-interviews&qru=%2Fta%2Fcoding-interviews%2Fquestion-ranking


class Solution:
    def FindGreatestSumOfSubArray(self, array):
        """
        维护：历史最大和，当前扫描的和
        """
        curSum, maxSum = array[0], array[0]
        index = 1
        while index < len(array):
            if curSum < 0:
                curSum = 0
            curSum += array[index]
            if curSum > maxSum:
                maxSum = curSum
            index += 1
        return maxSum

