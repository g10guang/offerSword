package main

import (
	"sort"
)

// 已知两个数组集合，a来自A，b来自B，求min(abs(a-b))
// 数组长度不为0
func minAbs(A, B []int) int {
	abs := func(n int) int {
		if n < 0 {
			return -n
		}
		return n
	}
	sort.Slice(A, func(i, j int) bool {
		return A[i] < A[j]
	})
	sort.Slice(B, func(i, j int) bool {
		return B[i] < B[j]
	})

	r := abs(A[0] - B[0])
	// [1,2,3,7,10]
	// [7,9,13,13]
	left := 0
	right := 0
	for left < len(A) && right < len(B) {
		diff := abs(A[left] - B[right])
		if diff < r {
			r = diff
		}

		if A[left] > B[right] {
			right++
		} else if A[left] < B[right] {
			left++
		} else {
			return 0
		}
	}

	return r
}
