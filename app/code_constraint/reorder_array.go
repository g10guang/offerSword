package main

// import "sort"

// /**
//  *
//  * @param array int整型一维数组
//  * @return int整型一维数组
//  */
// // https://www.nowcoder.com/practice/beb5aa231adc45b2a5dcc5b62c93f593?tpId=13&tqId=11166&tPage=1&rp=1&ru=%2Fta%2Fcoding-interviews&qru=%2Fta%2Fcoding-interviews%2Fquestion-ranking
// func reOrderArray(array []int) []int {
//	// 将问题看成是一道排序题
// 	sort.SliceStable(array, func(i, j int) bool {
// 		iodd := array[i]%2 == 1
// 		jodd := array[j]%2 == 1
// 		if iodd {
// 			if jodd {
// 				return i < j
// 			} else {
// 				return true
// 			}
// 		} else {
// 			if jodd {
// 				return false
// 			} else {
// 				return false
// 			}
// 		}
// 	})
// 	return array
// }

func reOrderArray(array []int) []int {
	// 用空间换时间
	odd := make([]int, 0, len(array))
	even := make([]int, 0, len(array))
	for _, v := range array {
		if v%2 == 1 {
			odd = append(odd, v)
		} else {
			even = append(even, v)
		}
	}

	result := make([]int, 0, len(array))
	for _, v := range odd {
		result = append(result, v)
	}
	for _, v := range even {
		result = append(result, v)
	}
	return result
}
