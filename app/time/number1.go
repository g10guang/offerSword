package main

/**
 * 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
 *
 * @param n int整型
 * @return int整型
 */
func NumberOf1Between1AndN_Solution(n int) int {
	var result int
	for i := 0; i <= n; i++ {
		for x := i; x > 0; x /= 10 {
			if x%10 == 1 {
				result++
			}
		}
	}
	return result
}
