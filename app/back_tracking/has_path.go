package main

/**
 * 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
 *
 * @param matrix string字符串
 * @param rows int整型
 * @param cols int整型
 * @param path string字符串
 * @return bool布尔型
 */
func hasPath(matrix string, rows int, cols int, path string) bool {
	// https://www.nowcoder.com/share/jump/14730551684078698139
	var walk func(a, b, j int) bool
	var mark []bool
	walk = func(a, b, j int) bool {
		if j == len(path) {
			return true
		}

		if a < 0 || a >= rows || b < 0 || b >= cols {
			return false
		}

		idx := a*cols + b
		if mark[idx] {
			return false
		}
		if matrix[idx] != path[j] {
			return false
		}

		mark[idx] = true
		if walk(a-1, b, j+1) || walk(a+1, b, j+1) || walk(a, b-1, j+1) || walk(a, b+1, j+1) {
			return true
		}

		mark[idx] = false
		return false
	}

	for r := 0; r < rows; r++ {
		for c := 0; c < cols; c++ {
			mark = make([]bool, rows*cols)
			if walk(r, c, 0) {
				return true
			}
		}
	}

	return false
}
