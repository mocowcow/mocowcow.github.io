--- 
layout      : single
title       : LeetCode 2640. Find the Score of All Prefixes of an Array
tags        : LeetCode Medium Array Simulation PrefixSum
---
雙周賽102。

# 題目
conver是陣列arr的**轉換矩陣**，定義如下：  
- conver[i] = arr[i] + max(arr[0..i])，其中max(arr[0..i])為0 <= j <= i之中，所有arr[j]的最大值。  

而arr的**分數**對應轉換矩陣的總和。  

輸入長度n的整數陣列nums，回傳同為長度n的陣列ans，其中ans[i]代表nums[0..i]的分數。  

# 解法
方便起見，先建構出conver，之後再來求分數。  
conver[i]會用到0\~i中arr[i]的最大值，從最左開始遍歷arr，並維護最大值，逐一計算出conver[i]。  

而分數是子陣列conver[0,i]的總和，也就是前綴和，一邊累加一邊更新分數。  

```python
class Solution:
    def findPrefixScore(self, nums: List[int]) -> List[int]:
        conv=[]
        mx=0
        
        for n in nums:
            mx=max(mx,n)
            conv.append(n+mx)
            
        ps=0
        ans=[]
        
        for n in conv:
            ps+=n
            ans.append(ps)
            
        return ans
```
