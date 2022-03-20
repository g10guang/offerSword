package main

/**
 *
 * @param index int整型
 * @return int整型
 */
func GetUglyNumber_Solution(index int) int {
	if index == 0 {
		return 0
	}
	uglyNums := make([]int, 0, index)
	uglyNums = append(uglyNums, 1)
	p2, p3, p5 := 0, 0, 0
	for len(uglyNums) <= index {
		n2, n3, n5 := uglyNums[p2]*2, uglyNums[p3]*3, uglyNums[p5]*5
		min := min3(n2, n3, n5)
		uglyNums = append(uglyNums, min)
		if min == n2 {
			p2++
		}
		if min == n3 {
			p3++
		}
		if min == n5 {
			p5++
		}
	}
	return uglyNums[index-1]
}

func min3(a, b, c int) int {
	return min2(min2(a, b), c)
}

func min2(x, y int) int {
	if x < y {
		return x
	}
	return y
}
