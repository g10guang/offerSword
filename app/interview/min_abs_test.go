package main

import "testing"

func Test_minAbs(t *testing.T) {
	t.Run("case 1", func(t *testing.T) {
		r := minAbs([]int{1, 3, 2, 10}, []int{7, 13, 9, 13})
		t.Logf("r=%d", r)
	})
}
