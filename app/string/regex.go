package main

/**
 * 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
 *
 * @param s string字符串
 * @param pattern string字符串
 * @return bool布尔型
 */
// https://www.nowcoder.com/practice/45327ae22b7b413ea21df13ee7d6429c?tpId=13&tqId=11205&rp=1&ru=%2Fta%2Fcoding-interviews&qru=%2Fta%2Fcoding-interviews%2Fquestion-ranking
func match(s string, pattern string) bool {
	var fn func(x string, p string) bool
	fn = func(x, p string) bool {
		lx := len(x)
		lp := len(p)
		if lx == 0 {
			if lp == 0 {
				return true
			}
			if lp > 1 {
				np := p[1]
				if np == '*' {
					return fn(x, p[2:])
				}
			}
			return false
		}
		if lp == 0 {
			return lx == 0
		}
		fp := p[0]
		fx := x[0]
		if fp == fx || fp == '.' {
			if lp > 1 {
				np := p[1]
				if np == '*' {
					return fn(x[1:], p[2:]) || fn(x[1:], p) || fn(x, p[2:])
				}
			}
			return fn(x[1:], p[1:])
		}
		if lp > 1 {
			np := p[1]
			if np == '*' {
				return fn(x, p[2:])
			}
		}
		return false
	}
	return fn(s, pattern)
}
