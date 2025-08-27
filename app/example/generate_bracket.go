package main

// GenerateBrackets 输入N代表扩展数量，返回所有合法的括号组合
// 例子：输入n=3，返回["((()))","(()())","(())()","()(())","()()()"]
func GenerateBrackets(n int) []string {
	var res []string
	var walkFn func(leftCnt, rightCnt int, prefix string)
	walkFn = func(leftCnt, rightCnt int, prefix string) {
		if rightCnt == n {
			res = append(res, prefix)
			return
		}

		if rightCnt < leftCnt {
			walkFn(leftCnt, rightCnt+1, prefix+")")
		}

		if leftCnt < n {
			walkFn(leftCnt+1, rightCnt, prefix+"(")
		}
	}

	walkFn(0, 0, "")

	return res
}
