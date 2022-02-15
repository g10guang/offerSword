package main

/**
 * 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
 *
 * @param n int整型
 * @return int整型
 */
// https://www.nowcoder.com/practice/8ee967e43c2c4ec193b040ea7fbb10b8?tpId=13&tqId=11164&tPage=1&rp=1&ru=%2Fta%2Fcoding-interviews&qru=%2Fta%2Fcoding-interviews%2Fquestion-ranking
func NumberOf1(n int) int {
	count := 0
	ph := 1
	for i := 0; i < 32; i++ {
		if ph&n == ph {
			count++
		}
		ph >>= 1
	}
	return count
}
