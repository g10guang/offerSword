package main

/**
 * 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
 *
 * @param base double浮点型
 * @param exponent int整型
 * @return double浮点型
 */
// https://www.nowcoder.com/practice/1a834e5e3e1a4b7ba251417554e07c00?tpId=13&tqId=11165&tPage=1&rp=1&ru=%2Fta%2Fcoding-interviews&qru=%2Fta%2Fcoding-interviews%2Fquestion-ranking
func Power(base float64, exponent int) float64 {
	result := float64(1)
	div := exponent < 0
	if exponent < 0 {
		exponent = -exponent
	}
	for i := 0; i < exponent; i++ {
		result = result * base
	}
	if div {
		result = 1 / result
	}
	return result
}
