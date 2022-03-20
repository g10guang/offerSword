package main

/**
 * 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
 *
 * @param str string字符串
 * @return string字符串一维数组
 */
// https://www.nowcoder.com/practice/fe6b651b66ae47d7acce78ffdd9a96c7?tpId=13&tqId=11180&tPage=1&rp=1&ru=%2Fta%2Fcoding-interviews&qru=%2Fta%2Fcoding-interviews%2Fquestion-ranking
func Permutation(str string) []string {
	set := make(map[string]bool)
	var bs []byte
	for _, ch := range str {
		bs = append(bs, byte(ch))
	}
	swap := func(i, j int) {
		bs[i], bs[j] = bs[j], bs[i]
	}
	var perm func(pos int)
	perm = func(pos int) {
		if pos+1 == len(str) {
			solution := string(bs)
			set[solution] = true
			return
		}
		for i := pos; i < len(str); i++ {
			swap(pos, i)
			perm(pos + 1)
			swap(pos, i)
		}
	}
	perm(0)
	result := make([]string, 0, len(set))
	for solution := range set {
		result = append(result, solution)
	}
	return result
}
