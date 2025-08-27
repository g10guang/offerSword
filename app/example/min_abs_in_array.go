package main

import (
	"sort"
	"testing"
)

// 给定两个自然数数组A和B，从A中任取一个元素a，从B中任取一个元素b。d=绝对值(a-b)求d的最小值。
// A和B的长度都不为0举例: A=[ 1,3,2,10]，B = [7,13，9,13]，输出1 (即10-9)给出时间复杂度和空间复杂度
func minAbsInArray(a, b []int) int {
	sort.Slice(a, func(i, j int) bool {
		return a[i] < a[j]
	})

	sort.Slice(b, func(i, j int) bool {
		return b[i] < b[j]
	})

	pa := 0
	pb := 0
	minAbs := -1
	for pa < len(a) && pb < len(b) {
		va := a[pa]
		vb := b[pb]

		diff := va - vb
		if diff < 0 {
			diff = -diff
		}
		if diff == 0 {
			return 0
		}

		if minAbs == -1 || diff < minAbs {
			minAbs = diff
		}

		if va < vb {
			pa++
		} else {
			pb++
		}
	}

	return minAbs
}

func Test_minAbsInArray(t *testing.T) {
	type args struct {
		a      []int
		b      []int
		expect int
	}
	cases := []args{
		{
			a:      []int{1, 3, 2, 10},
			b:      []int{7, 13, 9, 13},
			expect: 1,
		},

		{
			a:      []int{1, 3, 2, 10},
			b:      []int{10, 13, 9, 13},
			expect: 0,
		},
	}

	for _, c := range cases {
		real := minAbsInArray(c.a, c.b)
		t.Logf("a=%d b=%d expect=%d real=%d", c.a, c.b, c.expect, real)
	}
}
