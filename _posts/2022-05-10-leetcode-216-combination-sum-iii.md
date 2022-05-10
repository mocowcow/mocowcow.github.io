--- 
layout      : single
title       : LeetCode 216. Combination Sum III
tags        : LeetCode Medium Array Backtracking
---
每日題。第二天回溯題，看來這周可能是回溯周。

# 題目
求由k個數總和為n的所有組合，且符合以下規則：  
- 只使用數字1到9  
- 每個數字最多使用一次  

回傳所有可能的組合，且同樣的組合只能出現一次，也可以以任意順序輸出。  

# 解法
一樣沒什麼好辦法，只能用回溯暴力搜尋可能的組合。  
從數字1開始搜尋，對1\~9的數字j分別嘗試加入，並繼續從j\~9中選數字。直到所有無法繼續加入數字後，判斷是否只用了k個數且總和為n，若是則將組合加入答案。

```python
class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        ans=[]
        
        def bt(i,curr,val):
            if len(curr)==k:
                if val==n:
                    ans.append(curr[:])
            else:
                for j in range(i,10):
                    curr.append(j)
                    bt(j+1,curr,val+j)
                    curr.pop()
                    
        bt(1,[],0)
        
        return ans
```
