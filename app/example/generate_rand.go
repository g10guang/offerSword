package main

import (
	"math/rand"
)

func rand5() int {
	return rand.Intn(5)
}

func rand16() int {
	// 0, 5, 10, 15, 20
	// rand5 * 5 + rand5
	for {
		n := rand5()*5 + rand5()
		if n < 16 {
			return n
		}
	}
}
