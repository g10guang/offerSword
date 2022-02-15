package main

/**
 * 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
 *
 * @param number int整型
 * @return int整型
 */
// https://www.nowcoder.com/practice/22243d016f6b47f2a6928b4313c85387?tpId=13&tqId=11162&tPage=1&rp=1&ru=%2Fta%2Fcoding-interviews&qru=%2Fta%2Fcoding-interviews%2Fquestion-ranking
func jumpFloorII(number int) int {
	// dp := make([]int, number+1)
	// dp[1] = 1
	// for i := 2; i <= number; i++ {
	// 	dp[i] = dp[i-1] * 2
	// }
	// return dp[number]

	return 1 << (number - 1)
}
