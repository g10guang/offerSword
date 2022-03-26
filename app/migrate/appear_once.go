package main

import "fmt"

// https://www.nowcoder.com/practice/e02fdb54d7524710a7d664d082bb7811?tpId=13&tqId=11193&rp=1&ru=%2Fta%2Fcoding-interviews&qru=%2Fta%2Fcoding-interviews%2Fquestion-ranking&u_atoken=edc34eac-192a-440f-af8b-c9c26db61107&u_asession=01SGB6Zkp_3l4ZHj7K0ZeT72p7eM8Xu9x5CWfiZ2ATobcnTSldhG4-tgajp3MfR5xTX0KNBwm7Lovlpxjd_P_q4JsKWYrT3W_NKPr8w6oU7K-qazal7642iIqO6q4s1I6dMcQByPPnliJkG2x7ZcOtkmBkFo3NEHBv0PZUm6pbxQU&u_asig=058un4ynxXv3LVdcU4rcDeWFg5afu9wHc3g7lM8x4LGsT2RK0MSBiFDoRtWEoRePvXzetU28h6ITsLPoiiWeDVoq32hz6rw2whLuxCg6H_QkIdaq6QjA_64fRLZ7JhUs_KFvt-I6_BmBDHvhxHs0nL70fMz4XKQ2_PdJkyD_Yf3gv9JS7q8ZD7Xtz2Ly-b0kmuyAKRFSVJkkdwVUnyHAIJzZKdNqEhSIS1WKK-4Br5U_yGAj5fYlP2JnTJ828VlY_X0mfvgokSjlkXJtJJt_itu-3h9VXwMyh6PgyDIVSG1W9H71K98Mxzvq0RmqLsYQS8Ua23l0f3L1wibGI-E2ARH-y4mQZkdbr5rNIvqGjP04lNkh9AHnrBJdr_RisuSFxpmWspDxyAEEo4kbsryBKb9Q&u_aref=3NYZm7hxG%2FviuWQ6TXpaya6Zb4k%3D
func FindNumsAppearOnce(nums []int) []int {
	//返回[a,b] 其中ab是出现一次的两个数字
	mark := make(map[int]int, len(nums)/2+1)
	for _, v := range nums {
		mark[v]++
	}
	var result []int
	for _, v := range nums {
		if mark[v] == 1 {
			result = append(result, v)
		}
		if len(result) == 2 {
			break
		}
	}
	return result
}
