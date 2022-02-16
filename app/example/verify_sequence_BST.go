package main

/**
 * 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
 *
 * @param sequence int整型一维数组
 * @return bool布尔型
 */
// https://www.nowcoder.com/practice/a861533d45854474ac791d90e447bafd?tpId=13&tqId=11176&tPage=1&rp=1&ru=%2Fta%2Fcoding-interviews&qru=%2Fta%2Fcoding-interviews%2Fquestion-ranking
func VerifySquenceOfBST(sequence []int) bool {
	if len(sequence) == 0 {
		return false
	}
	if len(sequence) == 1 {
		return true
	}
	rightStartIdx := -1
	root := sequence[len(sequence)-1]
	for i := 0; i < len(sequence)-1; i++ {
		v := sequence[i]
		if root < v {
			rightStartIdx = i
			break
		}
	}
	if rightStartIdx != -1 {
		for i := rightStartIdx + 1; i < len(sequence)-1; i++ {
			v := sequence[i]
			if root > v {
				return false
			}
		}

		left := sequence[:rightStartIdx]
		if len(left) > 0 {
			if !VerifySquenceOfBST(left) {
				return false
			}
		}
		right := sequence[rightStartIdx : len(sequence)-1]
		if len(right) > 0 {
			if !VerifySquenceOfBST(right) {
				return false
			}
		}
		return true
	}

	left := sequence[:len(sequence)-1]
	if len(left) > 0 {
		return VerifySquenceOfBST(left)
	}
	return true
}
