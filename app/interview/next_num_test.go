package main

import (
	"testing"

	"github.com/stretchr/testify/assert"
)

func Test_nextNum(t *testing.T) {
	t.Run("case1", func(t *testing.T) {
		got := nextNum(1234)
		assert.Equal(t, 1243, got)
	})

	t.Run("case2", func(t *testing.T) {
		got := nextNum(1243)
		assert.Equal(t, 1324, got)
	})

	t.Run("case3", func(t *testing.T) {
		got := nextNum(4321)
		assert.Equal(t, 4321, got)
	})

	t.Run("case4", func(t *testing.T) {
		got := nextNum(1239876)
		assert.Equal(t, 1263789, got)
	})
}
