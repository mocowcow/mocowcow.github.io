--- 
layout      : single
title       : LeetCode 2765. Longest Alternating Subarray
tags        : LeetCode Easy Array TwoPointers SlidingWindow
---
雙周賽108。連續兩次雙周賽都網站炸掉，這種網站還想賣系統設計課程給誰。  

而且題目描述真的很爛，寫一堆囉嗦的公式搞得很麻煩，簡單一句**由兩個元素交替組成子陣列**可以扯好大串，真是服了。  
然後例題1的nums = [2,3,4,3,4]，他只提出了[3,4],[3,4,3],[3,4,3,4]三種，漏掉了[2,3]沒講，害我懷疑半天為什麼[2,3]不滿足條件？？？  

# 題目
輸入整數陣列nums。一個長度為m的**交替的**子陣列s滿足：  
- m大於1  
- s1 = s0 + 1  
- 子陣列由s0和s1兩個元素交替組成，如[s0, s1 ,s0 ...]  

求最長的**交替的**子陣列長度。若不存在則回傳-1。  

# 解法
跟上週的[2760. longest even odd subarray with threshold]({% post_url 2023-07-02-leetcode-2760-longest-even-odd-subarray-with-threshold %}) 有八成相似。  

枚舉所有索引i作為左邊界，若nums[i]+1 = nums[i+1]，找到長度為2的**交替子陣列**，嘗試將右邊界擴展。  
擴展結束後以當前區間大小更新答案。  

時間複雜度O(N^2)。  
空間複雜度O(N)。  

```python
class Solution:
    def alternatingSubarray(self, nums: List[int]) -> int:
        ans=0
        N=len(nums)
        
        for i in range(N-1):
            if nums[i]+1==nums[i+1]:
                j=i+1
                while j+1<N and nums[j+1]==nums[j-1]:
                    j+=1
                ans=max(ans,j-i+1)
        
        if ans==0:
            return -1
        
        return ans
```
