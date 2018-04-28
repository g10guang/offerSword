# coding=utf-8
# author: Xiguang Liu<g10guang@foxmail.com>
# 2018-04-28 20:19
# 题目描述：https://www.nowcoder.com/practice/d77d11405cc7470d82554cb392585106?tpId=13&tqId=11174&tPage=1&rp=1&ru=%2Fta%2Fcoding-interviews&qru=%2Fta%2Fcoding-interviews%2Fquestion-ranking


class Solution:

    def IsPopOrder(self, pushV, popV):
        """
        解决思路，模拟入栈和出栈的过程，如果能够模拟，那么 PopV 是 PushV 的一种可能；否则不是
        """
        stack = []
        pushIndex = 0
        popIndex = 0
        while popIndex < len(popV):
            if not stack:
                stack.append(pushV[pushIndex])
                pushIndex += 1
            else:
                if popV[popIndex] == stack[-1]:
                    popIndex += 1
                    stack.pop()
                else:
                    # 判断是否还有更多元素可以入栈
                    if pushIndex == len(pushV):
                        return False
                    # 尝试入栈
                    stack.append(pushV[pushIndex])
                    pushIndex += 1
        return True
