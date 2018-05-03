# coding=utf-8
# author: Xiguang Liu<g10guang@foxmail.com>
# 2018-05-03 13:25
# 题目描述：https://www.nowcoder.com/practice/762836f4d43d43ca9deb273b3de8e1f4?tpId=13&tqId=11198&rp=1&ru=%2Fta%2Fcoding-interviews&qru=%2Fta%2Fcoding-interviews%2Fquestion-ranking


class Solution:
    def IsContinuous(self, numbers):
        if not numbers:
            return False
        sortedNum = sorted(numbers)
        jokerCount = sum(1 for x in sortedNum if x == 0)
        for i in range(jokerCount + 1, len(sortedNum)):
            if sortedNum[i - 1] == sortedNum[i]:
                return False
            jokerCount -= sortedNum[i] - (sortedNum[i - 1] + 1)
            if jokerCount < 0:
                return False
        return True
