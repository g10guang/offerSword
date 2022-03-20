package main

/**
 *
 * @param numbers int整型一维数组
 * @return int整型
 */
// https://www.nowcoder.com/practice/e8a1b01a2df14cb2b228b30ee6a92163?tpId=13&tqId=11181&rp=1&ru=%2Fta%2Fcoding-interviews&qru=%2Fta%2Fcoding-interviews%2Fquestion-ranking&u_atoken=3f0e983d-873d-4b98-9df5-de18d62882db&u_asession=01SwNcgXDR85M4w1hFv3XVrmSJo5JPZ9RdSVkOyCz6cBr--G1Xc3Osz56n_jN6YHOeX0KNBwm7Lovlpxjd_P_q4JsKWYrT3W_NKPr8w6oU7K-W7R09UmE3peUOuqPzJ-i4csbyNNxFL2cMC-C6PyRxA2BkFo3NEHBv0PZUm6pbxQU&u_asig=05ZzWZXByCBXe3TS4C2roTfqSmYJVq5VcFPrR7nV-HN-9aRijFXRgy5r8HxNa7Csw5RIGYXL1G4JUZKTZIOFbfFcBg5ZNSa5ZZ3rIa-4dZqI-hubU3Rxeu56Xz6vF6uf9ZQRHbPOETTg4314gcPOQqaMdokX6nrhAMjrYp1XcRhI_9JS7q8ZD7Xtz2Ly-b0kmuyAKRFSVJkkdwVUnyHAIJzbSGsy8L8TJIgrn3ji_BA9WqN1KDPXGC53LRrJZdNhT_NmRfc2Xc7etamoD1SdQYLu3h9VXwMyh6PgyDIVSG1W9wgpRtcOF-huY91_7drkzq3tQKZkwTf6EpRSsJY3Qx5eYZAdjqZvQMz7RWYUY3MfG08ZY-pOXHY9FW3Il_3VmpmWspDxyAEEo4kbsryBKb9Q&u_aref=ygdBL%2Fkzl1kGj%2F7x4pukTg4%2FIBc%3D
func MoreThanHalfNum_Solution(numbers []int) int {
	var n int
	var cnt int
	for _, v := range numbers {
		if cnt == 0 {
			cnt = 1
			n = v
		} else if v == n {
			cnt++
		} else {
			cnt--
		}
	}
	return n
}
