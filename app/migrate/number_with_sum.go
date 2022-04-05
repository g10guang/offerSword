package main

/**
 * 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
 *
 * @param array int整型一维数组
 * @param sum int整型
 * @return int整型一维数组
 */
// https://www.nowcoder.com/practice/390da4f7a00f44bea7c2f3d19491311b?tpId=13&tqId=11195&rp=1&ru=%2Fta%2Fcoding-interviews&qru=%2Fta%2Fcoding-interviews%2Fquestion-ranking
func FindNumbersWithSum(array []int, sum int) []int {
	if len(array) < 2 {
		return nil
	}
	left := 0
	right := len(array) - 1
	for left < right {
		n := array[left] + array[right]
		if n == sum {
			return []int{array[left], array[right]}
		} else if n > sum {
			right--
		} else {
			left++
		}
	}
	return nil
}
