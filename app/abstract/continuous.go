package main

import (
	"sort"
)

/**
 *
 * @param numbers int整型一维数组
 * @return bool布尔型
 */
// https://www.nowcoder.com/practice/762836f4d43d43ca9deb273b3de8e1f4?tpId=13&tqId=11198&rp=1&ru=%2Fta%2Fcoding-interviews&qru=%2Fta%2Fcoding-interviews%2Fquestion-ranking
func IsContinuous2(numbers []int) bool {
	sort.Slice(numbers, func(i, j int) bool {
		return numbers[i] < numbers[j]
	})
	joker := 0
	notJokerIndex := 0
	for i, v := range numbers {
		if v == 0 {
			joker++
			notJokerIndex = i + 1
		} else {
			break
		}
	}
	diff := 0
	for j := notJokerIndex + 1; j < len(numbers); j++ {
		if numbers[j] == numbers[j-1] {
			return false
		}
		diff += numbers[j] - numbers[j-1]
	}
	return diff < 5
}

func IsContinuous(numbers []int) bool {
	var mark uint16
	min := 100
	max := 0
	for _, n := range numbers {
		if n == 0 {
			continue
		}
		if (mark & (1 << (n - 1))) > 0 {
			return false
		}
		mark |= 1 << (n - 1)
		if min > n {
			min = n
		}
		if min == 100 {
			min = n
		}
		if max < n {
			max = n
		}
	}
	return max-min < 5
}
