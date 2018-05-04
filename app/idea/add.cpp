// 题目描述：https://www.nowcoder.com/practice/59ac416b4b944300b617d4f7f111b215?tpId=13&tqId=11201&rp=1&ru=%2Fta%2Fcoding-interviews&qru=%2Fta%2Fcoding-interviews%2Fquestion-ranking

/*
通过十进制加法类比二进制加法
在二进制加法中，
t = num1 + num2 保存 num1+num2 还没有算进位时的值
num2 = (num1 & num2) << 1 计算需要进位的数值
num1 = t 做替换
重复执行以上操作，直到 num2 == 0 也就是两数相加没有进位为止。
这也是动态规划，将原来的问题转化为规模更小的子问题
*/
class Solution {
public:
    int Add(int num1, int num2)
    {
        while (num2) {
            int t = num1 ^ num2;
            num2 = (num1 & num2) << 1;
            num1 = t;
        }
        return num1;
    }
};
