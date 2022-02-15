package main

/**
 * 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
 *
 * @param number int整型
 * @return int整型
 */
// https://www.nowcoder.com/practice/72a5a919508a4251859fb2cfb987a0e6?tpId=13&tqId=11163&tPage=1&rp=1&ru=%2Fta%2Fcoding-interviews&qru=%2Fta%2Fcoding-interviews%2Fquestion-ranking
func rectCover(number int) int {
	n_1 := 2
	n_2 := 1
	result := 0
	for i := 3; i <= number; i++ {
		result = n_1 + n_2
		n_2 = n_1
		n_1 = result
	}
	if number == 1 {
		return 1
	}
	if number == 2 {
		return 2
	}
	return result
}
