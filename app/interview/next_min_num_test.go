package main

import (
	"testing"

	"github.com/stretchr/testify/assert"
)

func Test_minNum(t *testing.T) {
	t.Run("case1", func(t *testing.T) {
		got := minNum([]int{2, 4, 9}, 23121)
		assert.Equal(t, 22999, got)
	})

	t.Run("case2", func(t *testing.T) {
		got := minNum([]int{7, 8, 9}, 3456)
		assert.Equal(t, 999, got)
	})

	t.Run("case3", func(t *testing.T) {
		got := minNum([]int{1, 2, 3}, 321)
		assert.Equal(t, 313, got)
	})

	t.Run("case4", func(t *testing.T) {
		got := minNum([]int{9}, 1)
		assert.Equal(t, -1, got)
	})

}
