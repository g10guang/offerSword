package main

// https://www.nowcoder.com/practice/4060ac7e3e404ad1a894ef3e17650423?tpId=13&tqId=11155&tPage=1&rp=1&ru=%2Fta%2Fcoding-interviews&qru=%2Fta%2Fcoding-interviews%2Fquestion-ranking
func ReplaceSpace(s string) string {
	spCount := 0
	for _, c := range s {
		if c == ' ' {
			spCount++
		}
	}
	newLen := len(s) + spCount*2
	buf := make([]byte, newLen)
	for i := 0; i < len(s); i++ {
		buf[i] = s[i]
	}

	// 从后往前拷贝
	k := newLen - 1
	for i := len(s) - 1; i >= 0; i-- {
		c := s[i]
		if c == ' ' {
			buf[k] = '0'
			buf[k-1] = '2'
			buf[k-2] = '%'
			k -= 3
		} else {
			buf[k] = c
			k--
		}
	}
	return string(buf)
}
