package main

// https://www.nowcoder.com/practice/623a5ac0ea5b4e5f95552655361ae0a8?tpId=13&tqId=11203&rp=1&ru=%2Fta%2Fcoding-interviews&qru=%2Fta%2Fcoding-interviews%2Fquestion-ranking
func Duplicate2(numbers []int, duplication *[1]int) bool {
	initSize := 10000
	if len(numbers) < initSize {
		initSize = len(numbers)
	}
	mark := make(map[int]int, initSize)
	for _, v := range numbers {
		mark[v]++
	}
	for _, v := range numbers {
		if mark[v] > 1 {
			duplication[0] = v
			return true
		}
	}
	duplication[0] = -1
	return false
}

func Duplicate(numbers []int, duplication *[1]int) bool {
	// in-place解法，节省map空间
	for i := 0; i < len(numbers); i++ {
		n := numbers[i]
		if n == i {
			continue
		}
		if numbers[n] == numbers[i] {
			duplication[0] = n
			return true
		}
		numbers[n], numbers[i] = numbers[i], numbers[n]
	}
	duplication[0] = -1
	return false
}
