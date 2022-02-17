---
layout      : single
title       : LeetCode 39. Combination Sum
tags 		: LeetCode Medium Array Backtracking
---
每日題。回溯回溯的一天。

# 題目
輸入不重複的整數陣列candidates及整數target，求所有用candidates內元素達到target的組合。每個數字可以重複使用無限次。

# 解法
看到輸入範圍不大就會想用回溯法。  
先把candidates依降冪排序。函數bt(i,curr,cnt)，i表示當前輪到第幾個數字，cnt表示距離目標還缺多少，curr保存使用的數。  
對每個可用數字嘗試加入，如果cnt<0就回頭；cnt=0就將curr加入答案；cnt>0則繼續加入其他數字。  
如果要選擇加入第i數字，因可以重複使用，下次還是i；不加的話下次就輪到i+1。

```python
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        N = len(candidates)
        candidates.sort(reverse=1)

        def bt(i, curr, cnt):
            if cnt == 0:
                ans.append(curr[:])
                return
            if i == N or cnt < 0:
                return
            else:
                curr.append(candidates[i])
                bt(i, curr, cnt-candidates[i])
                curr.pop()
                bt(i+1, curr, cnt)

        bt(0, [], target)
        return ans
```

上面的方法會讓堆疊很深，效率不佳，改寫成這樣會比較快。  
超過所需值的數字就不嘗試了，直接跳下一個。

```python
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        N = len(candidates)
        candidates.sort(reverse=1)

        def bt(i, curr, cnt):
            if cnt == 0:
                ans.append(curr[:])
            else:
                for j in range(i, N):
                    if candidates[j] <= cnt:
                        curr.append(candidates[j])
                        bt(j, curr, cnt-candidates[j])
                        curr.pop()

        bt(0, [], target)
        return ans
```