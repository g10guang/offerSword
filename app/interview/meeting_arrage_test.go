package main

import (
	"testing"

	"github.com/stretchr/testify/assert"
)

func Test_meetingArrange(t *testing.T) {
	t.Run("case1", func(t *testing.T) {
		got := meetingArrange([][2]int{
			{10, 50}, {60, 120}, {140, 210},
		}, [][2]int{
			{0, 15}, {60, 70},
		}, 8)

		assert.Equal(t, [2]int{60, 68}, got)
	})
}
