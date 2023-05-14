package main

/**
 * 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
 *
 * @param threshold int整型
 * @param rows int整型
 * @param cols int整型
 * @return int整型
 */
func movingCount(threshold int, rows int, cols int) int {
	// https://www.nowcoder.com/share/jump/14730551684079854734
	mark := make([]bool, rows*cols)
	idxFn := func(a, b int) int {
		return a*cols + b
	}

	scoreFn := func(v int) int {
		score := 0
		for v > 0 {
			r := v % 10
			score += r
			v /= 10
		}

		return score
	}

	var walk func(a, b int) int
	walk = func(a, b int) int {
		if a < 0 || a >= rows || b < 0 || b >= cols {
			return 0
		}

		idx := idxFn(a, b)
		if mark[idx] {
			return 0
		}

		mark[idx] = true
		if scoreFn(a)+scoreFn(b) > threshold {
			return 0
		}

		left := walk(a, b-1)
		right := walk(a, b+1)
		up := walk(a-1, b)
		down := walk(a+1, b)

		return left + right + up + down + 1
	}

	return walk(0, 0)
}
