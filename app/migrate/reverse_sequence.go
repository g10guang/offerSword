package main

import "strings"

/**
 * 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
 *
 *
 * @param str string字符串
 * @return string字符串
 */
// https://www.nowcoder.com/practice/3194a4f4cf814f63919d0790578d51f3?tpId=13&tqId=11197&rp=1&ru=%2Fta%2Fcoding-interviews&qru=%2Fta%2Fcoding-interviews%2Fquestion-ranking
func ReverseSentence(str string) string {
	parts := strings.Split(str, " ")
	l := len(parts)
	for i := 0; i < l/2; i++ {
		parts[i], parts[l-i-1] = parts[l-i-1], parts[i]
	}
	return strings.Join(parts, " ")
}
