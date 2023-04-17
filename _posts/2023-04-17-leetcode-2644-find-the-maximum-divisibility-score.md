--- 
layout      : single
title       : LeetCode 2644. Find the Maximum Divisibility Score
tags        : LeetCode Easy Array Simulation
---
周賽341。前一題初始值設錯，這題就記得了。  
好像是第一次看到周賽中有兩題Easy？  

# 題目
輸入整數陣列nums和divisors。  

divisors[i]的**可除性分數**定義為索引j的數量，其中nums[j]可被divisors[i]整除。  

回傳可除性分數**最高**的diviros[i]。若有多個分數相同，則選擇最小者。  

# 解法
測資不大，直接暴力計算。  

遍歷divisors中每個除數div，看看把nums中多少個數整除。  
如果大於之前的次數，或是次數相同但**除數更小**時更新答案。  

時間複雜度O(MN)，其中M為nums長度，N為divisors長度。空間複雜度O(1)。  

```python
class Solution:
    def maxDivScore(self, nums: List[int], divisors: List[int]) -> int:
        
        def f(div):
            cnt=0
            for n in nums:
                if n%div==0:
                    cnt+=1
            return cnt
        
        ans=0
        mx=-1
        for div in divisors:
            cnt=f(div)
            if cnt>mx or (cnt==mx and div<ans):
                ans=div
                mx=cnt
                
        return ans
```
