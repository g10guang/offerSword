package main

/**
 * 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
 *
 * @param str string字符串
 * @param n int整型
 * @return string字符串
 */
// https://www.nowcoder.com/practice/12d959b108cb42b1ab72cef4d36af5ec?tpId=13&tqId=11196&rp=1&ru=%2Fta%2Fcoding-interviews&qru=%2Fta%2Fcoding-interviews%2Fquestion-ranking
func LeftRotateString(str string, n int) string {
	l := len(str)
	if l <= 1 {
		return str
	}
	d := n % l
	return str[d:] + str[:d]
}
