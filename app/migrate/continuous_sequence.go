package main

/**
 * 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
 *
 * @param sum int整型
 * @return int整型二维数组
 */
// https://www.nowcoder.com/practice/c451a3fd84b64cb19485dad758a55ebe?tpId=13&tqId=11194&rp=1&ru=%2Fta%2Fcoding-interviews&qru=%2Fta%2Fcoding-interviews%2Fquestion-ranking
func FindContinuousSequence(sum int) [][]int {
	var result [][]int
	for i := sum/2 + 1; i >= 2; i-- {
		n := sum / i
		start := n - i/2 + 1
		if i%2 == 1 {
			start = n - i/2
		}
		if start <= 0 {
			continue
		}
		acc := (start + start + i - 1) * i / 2
		if acc == sum {
			var t []int
			for k := start; k < start+i; k++ {
				t = append(t, k)
			}
			result = append(result, t)
		}
	}
	return result
}
