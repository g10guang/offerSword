package main

import "container/list"

// https://www.nowcoder.com/practice/00de97733b8e4f97a3fb5c680ee10720?tpId=13&tqId=11207&rp=1&ru=%2Fta%2Fcoding-interviews&qru=%2Fta%2Fcoding-interviews%2Fquestion-ranking
var mark = make(map[byte]*list.Element)
var l list.List

func Insert(ch byte) {
	e, ok := mark[ch]
	if ok {
		l.Remove(e)
		return
	}
	e = l.PushBack(ch)
	mark[ch] = e
}

func FirstAppearingOnce() byte {
	if l.Len() > 0 {
		return l.Front().Value.(byte)
	}
	return '#'
}
