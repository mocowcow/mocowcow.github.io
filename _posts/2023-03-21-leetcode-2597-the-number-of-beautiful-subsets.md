--- 
layout      : single
title       : LeetCode 2597. The Number of Beautiful Subsets
tags        : LeetCode Medium Array Backtracking Sorting HashTable
---
周賽337。好像有一段時間沒出過回溯法。如果測資大一些就是Hard題了。  

# 題目
輸入正整數陣列nums和正整數k。  

如果一個子集中沒有任意兩數絕對差為k，則稱為**美麗的**。  

求nums有幾個**非空美麗子集**。  

# 解法
N不大，最多才20，可以用回溯法暴力窮舉每個元素拿或不拿，最多2^20，差不多是10^6，還可接受。  

原本nums是無序的，選擇一個元素x時要檢查x+k和x-k有沒有拿過。把nums遞增排序後就只要檢查x-k。  
維護一個雜湊表d，記錄各元素的出現次數。而回溯函數bt(i)計算nums[i]拿或不拿，到i等於N時，所有元素都處理完畢。  
如果x-k沒有拿過，則可以選擇拿x，將d[x]加1後遞迴，然後恢復原狀。  

注意題目求的是非空子集，所以最後答案要扣掉空集合的1。  

時間複雜度O(2^N)。空間複雜度O(N)。  

```python
class Solution:
    def beautifulSubsets(self, nums: List[int], k: int) -> int:
        N=len(nums)
        nums.sort()
        ans=0
        d=Counter()
        
        def bt(i):
            nonlocal ans
            if i==N:
                ans+=1
                return
            bt(i+1)
            x=nums[i]
            if d[x-k]==0:
                d[x]+=1
                bt(i+1)
                d[x]-=1
        
        bt(0)
        
        return ans-1
```
