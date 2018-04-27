# coding=utf-8
# author: Xiguang Liu<g10guang@foxmail.com>
# 2018-04-27 13:32
# 题目描述：https://www.nowcoder.com/practice/beb5aa231adc45b2a5dcc5b62c93f593?tpId=13&tqId=11166&tPage=1&rp=1&ru=%2Fta%2Fcoding-interviews&qru=%2Fta%2Fcoding-interviews%2Fquestion-ranking


class Solution:
    def reOrderArray(self, array):
        """
        调整整形数组中元素的位置，而且不能改变元素的相对位置
        思路二：
        将奇数偶数分别放到队列中，然后分别从队列中取出元素
        """
        odd = []
        even = []
        for x in array:
            if x % 2 == 0:
                even.append(x)
            else:
                odd.append(x)
        i = 0
        for x in odd:
            array[i] = x
            i += 1
        for x in even:
            array[i] = x
            i += 1
        return array

    def reOrderArray2(self, array):
        """
        思路一：
        将问题转化为排序问题，使用稳定排序
        """
        # sorted 排序是保证稳定的 https://stackoverflow.com/questions/1915376/is-pythons-sorted-function-guaranteed-to-be-stable
        return sorted(array, key=lambda x: 1 - (x % 2))
