---
layout      : single
title       : LeetCode 2934. Minimum Operations to Maximize Last Elements in Arrays
tags        : LeetCode Medium Array Greedy
---
周賽371。複製貼上漏了一個字沒改到，免費WA一次。  

## 題目

輸入整數陣列nums1和nums2，長度都是n。  

你可以執行以下操作任意次：  

- 選擇索引i，將nums1[i]和nums2[i]的值交換  

你的目標是以**最小操作次數**滿足以下條件：  

- nums1[n-1]是nums1中的最大值  
- nums2[n-1]是nums2中的最大值  

回傳滿足兩條件所需的**最小操作次數**。若無法達成，則回傳-1。  

## 解法

操作只能交換同一個索引的值，也就是只有兩種可能：  

1. nums1[n-1]和nums2[n-1]維持不變  
2. nums1[n-1]和nums2[n-1]交換  

看滿足哪個條件所需的交換次數較小。  

維護函數f(e1,e2)：代表以e1為nums1最大值，以e2為nums2最大值，所需最小交換次數。  
枚舉索引i，只要nums1[i]或nums2[i]不滿足條件，則試著交換。能換就計數+1；不能換直接回傳inf，代表不合法。  

時間複雜度O(N)。  
時間複雜度O(1)。  

```python
class Solution:
    def minOperations(self, nums1: List[int], nums2: List[int]) -> int:
        N=len(nums1)
        
        def f(e1,e2):
            cnt=0
            for i in range(N):
                if nums1[i]<=e1 and nums2[i]<=e2:
                    continue
                elif nums2[i]<=e1 and nums1[i]<=e2:
                    cnt+=1
                else:
                    return inf
            return cnt

        e1=nums1[-1]
        e2=nums2[-1]
        ans=min(f(e1,e2),f(e2,e1))
        
        if ans==inf:
            return -1
        return ans
```
