package main

import (
	"fmt"
	"math/rand"
)

// 已知rand5()提供[0,4]随机散列，实现rand16()实现[0,16]随机散列
func rand5() int {
	return rand.Intn(5)
}

func rand16() int {
	// 0, 5, 10, 15
	// 0, 1, 2, 3, 4
	for {
		a := rand5()
		b := rand5()

		// [0, 19]
		t := a*5 + b
		if t < 16 {
			return t
		}
	}
}

func rand71() int {
	for {
		// 0, 16, 32, 48, 64
		// 0, 1, ..., 16
		a := rand16()
		b := rand16()
		t := a * 16 + b
		if t < 71 {
			return t
		}
	}
}

func main() {
	counter := make(map[int]int)
	total := 1000 * 1000
	for i := 0; i < total; i++ {
		v := rand71()
		counter[v]++
	}

	for n, cnt := range counter {
		fmt.Printf("n=%d cnt=%d p=%f\n", n, cnt, float64(cnt) / float64(total))
	}
}