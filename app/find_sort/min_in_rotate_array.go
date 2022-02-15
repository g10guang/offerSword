package main

/**
 *
 * @param rotateArray int整型一维数组
 * @return int整型
 */
// https://www.nowcoder.com/practice/9f3231a991af4f55b95579b44b7a01ba?tpId=13&tqId=11159&tPage=1&rp=1&ru=%2Fta%2Fcoding-interviews&qru=%2Fta%2Fcoding-interviews%2Fquestion-ranking
func minNumberInRotateArray(rotateArray []int) int {
	length := len(rotateArray)
	low := 0
	high := length - 1
	for low < high {
		if rotateArray[low] < rotateArray[high] {
			return rotateArray[low]
		}
		mid := (low + high) / 2
		if rotateArray[high] < rotateArray[mid] {
			low = mid + 1
		} else if rotateArray[high] > rotateArray[mid] {
			high = mid
		} else {
			high--
		}
	}
	return rotateArray[low]
}
