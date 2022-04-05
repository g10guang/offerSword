package main

/**
 * 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
 *
 * @param str string字符串
 * @return int整型
 */
// https://www.nowcoder.com/practice/1277c681251b4372bdef344468e4f26e?tpId=13&tqId=11202&rp=1&ru=/ta/coding-interviews&qru=/ta/coding-interviews/question-ranking
func StrToInt(str string) int {
	if len(str) == 0 {
		return 0
	}
	var result int
	isNegative := false
	if str[0] == '+' {
		str = str[1:]
	} else if str[0] == '-' {
		isNegative = true
		str = str[1:]
	}
	for _, c := range str {
		d := rune(c) - '0'
		if d > 9 || d < 0 {
			return 0
		}
		result = result*10 + int(d)
	}
	if isNegative {
		result = -result
	}
	return result
}
