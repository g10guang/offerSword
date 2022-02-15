package main

/**
 *
 * @param number int整型
 * @return int整型
 */
// https://www.nowcoder.com/practice/8c82a5b80378478f9484d87d1c5f12a4?tpId=13&tqId=11161&tPage=1&rp=1&ru=%2Fta%2Fcoding-interviews&qru=%2Fta%2Fcoding-interviews%2Fquestion-ranking
func jumpFloor(number int) int {
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
