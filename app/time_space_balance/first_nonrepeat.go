package main

/**
 * 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
 *
 * @param str string字符串
 * @return int整型
 */
func FirstNotRepeatingChar(str string) int {
	mark := make(map[rune]int)
	for _, c := range str {
		mark[c]++
	}
	for i, c := range str {
		if mark[c] == 1 {
			return i
		}
	}
	return -1
}
