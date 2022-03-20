package main

/**
 *
 * @param array int整型一维数组
 * @return int整型
 */
func FindGreatestSumOfSubArray(array []int) int {
	max := array[0]
	acc := max
	for _, v := range array[1:] {
		if acc > max {
			max = acc
		}
		if acc < 0 {
			acc = v
			continue
		}
		if acc+v > 0 {
			acc += v
		} else {
			acc = 0
		}
	}
	if acc > max {
		max = acc
	}
	return max
}
