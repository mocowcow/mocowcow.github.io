---
layout      : single
title       : LeetCode 739. Daily Temperatures
tags 		: LeetCode Medium Stack MonotonicStack
---
剛好出現在學習計畫，真的是睜眼都會看到stack。 

# 題目
整數陣列temperatures代表每天的溫度，對每一天計算要過幾天才會碰到更高溫度。如果不會遇到更高溫，則保持0。

# 解法
仔細回想一下，似乎只要是在某個時間點可能一次處理多個先前數值的情況，幾乎都很適合stack？  
題目要求找不到更高溫的話就保持0，作為陣列初始值。  
單調遞減堆疊st實質上保存的值是溫度，但需要計算日期差，所以改為紀錄天數，反正可以透過天數取溫度。  
遍歷每天i的溫度，若比st頂端j的溫度還高，就持續將st中的日期差更新為i-j，直到st為空或是遇到更高溫為止。  

```python
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        N=len(temperatures)
        ans=[0]*N
        st=[]
        
        for i,t in enumerate(temperatures):
            while st and t>temperatures[st[-1]]:
                day=st.pop()
                ans[day]=i-day
            st.append(i)
            
        return ans
```

