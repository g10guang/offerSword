package main

/**
 * 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
 *
 * @param n int整型
 * @return int整型
 */
// https://www.nowcoder.com/practice/7a0da8fc483247ff8800059e12d7caf1?tpId=13&tqId=11200&rp=1&ru=/ta/coding-interviews&qru=/ta/coding-interviews/question-ranking
func Sum_Solution(n int) int {
	var result int
	var fn func(x int) bool
	fn = func(x int) bool {
		result += x
		return x > 0 && fn(x-1)
	}
	fn(n)
	return result
}
