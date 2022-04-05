package main

/**
 * 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
 *
 * @param n int整型
 * @param m int整型
 * @return int整型
 */
// https://www.nowcoder.com/practice/f78a359491e64a50bce2d89cff857eb6?tpId=13&tqId=11199&rp=1&ru=%2Fta%2Fcoding-interviews&qru=%2Fta%2Fcoding-interviews%2Fquestion-ranking
func LastRemaining_Solution(n int, m int) int {
	var fn func(x int) int
	fn = func(x int) int {
		if x == 1 {
			return 0
		}
		d := fn(x - 1)
		return ((m % x) + d) % x
	}
	if n <= 0 {
		return -1
	}
	return fn(n)
}
