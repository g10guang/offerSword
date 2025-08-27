package main

import (
	"fmt"
	"sync"
)

func printLoop(target int, recv <-chan int, send chan<- int) {
	cnt := 0
	for {
		n, ok := <-recv
		if !ok {
			break
		}
		fmt.Printf("n=%d\n", n)
		y := (n + 1) % 3
		send <- y

		cnt++
		if cnt >= target {
			break
		}
	}
}

func main() {
	c1 := make(chan int, 1)
	c2 := make(chan int, 1)
	c3 := make(chan int, 1)

	var group sync.WaitGroup
	group.Add(3)

	go func() {
		defer group.Done()
		printLoop(10, c1, c2)
	}()

	go func() {
		defer group.Done()
		printLoop(10, c2, c3)
	}()

	go func() {
		defer group.Done()
		printLoop(10, c3, c1)
	}()

	c1 <- 0

	group.Wait()
}
