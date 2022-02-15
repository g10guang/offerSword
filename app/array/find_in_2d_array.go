package main

// https://www.nowcoder.com/practice/abc3fe2ce8e146608e868a70efebf62e?tpId=13&tqId=11154&tPage=1&rp=1&ru=/ta/coding-interviews&qru=/ta/coding-interviews/question-ranking
func Find(target int, array [][]int) bool {
	lenr := len(array)
	if lenr == 0 {
		return false
	}
	lenc := len(array[0])
	if lenc == 0 {
		return false
	}
	x, y := 0, lenc-1
	for x < lenr && y >= 0 {
		v := array[x][y]
		if v > target {
			y--
		} else if v < target {
			x++
		} else {
			return true
		}
	}
	return false
}
