---
layout      : single
title       : LeetCode 1986. Minimum Number of Work Sessions to Finish the Tasks
tags 		: LeetCode Medium Backtracking Array DP BitManipulation
---
以前某次周賽沒解完的，看討論區才知道有也可以用bit，搞不好會成為今後的趨勢。

# 題目
輸入長度N的整數陣列tasks，代表每項工作耗時需多久，整數sessionTime代表最大連續工作時間。  
每個工作階段可以做任意個工作，但是連續時間不可以超過sessionTime。求完成所有工作最少需幾個工作階段。

# 解法
看測資不大就想說用回溯法了。  
維護串列ses，代表現有的工作階段的可用時間，回溯函數bt(i)代表處理第i項任務，從bt(0)開始遞迴。  
對每個task[i]可以選擇加到任一現有的工作階段，或是重新開啟一個新的階段，當i=N時表示處理完整個tasks，以ses大小更新答案。  
剪枝發揮重要的加速作用：若當前ses若不小於ans則可以直接放棄計算，反正後面工作階段數量也不可能減少。

```python
class Solution:
    def minSessions(self, tasks: List[int], sessionTime: int) -> int:
        N = len(tasks)
        ans = math.inf
        ses = []

        def bt(i):
            nonlocal ans
            if len(ses) >= ans:
                return
            if i >= N:
                ans = len(ses)
            else:
                for j in range(len(ses)):
                    if ses[j] >= tasks[i]:
                        ses[j] -= tasks[i]
                        bt(i+1)
                        ses[j] += tasks[i]
                ses.append(sessionTime-tasks[i])
                bt(i+1)
                ses.pop()

        bt(0)

        return ans

```
