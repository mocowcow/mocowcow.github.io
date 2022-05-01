--- 
layout      : single
title       : LeetCode 2261. K Divisible Elements Subarrays
tags        : LeetCode Medium Array DFS HashTable
---
周賽291。把子陣列看成子序列，想半天才發現，浪費快半小時。  
雖然當初想的是回溯，結果沒有重複使用的要素，只是普通的dfs。

# 題目
輸入數列nums，還有整數k和p。  
nums的子陣列裡，可以被p所整除的元素最多只能有k個，求有多少種**不同的子陣列**。

# 解法
先預計算每個位置i的數字是否能被p整除，若是則設為1，用於之後扣減k的餘額。  
寫一個回溯函數dfs(i,remain,curr)，表示目前處理nums[i]是否能被加入子字串curr。
只有在remain不小於0的時候才是合法子字串，先將已經組成的子陣列加入set中去重複，再繼續往下一位置dfs。  

列舉每個位置進行dfs，因N<=200，就算最差狀況每個位置都不能被p整除，整體複雜度也只是O(N^2)而已，可以接受。  
注意dfs函數會將空字串也算進去，所以set大小要扣掉1才是正確答案。

```python
class Solution:
    def countDistinct(self, nums: List[int], k: int, p: int) -> int:
        N=len(nums)
        div=[0]*N
        ans=set()
        for i,n in enumerate(nums):
            if n%p==0:
                div[i]=1
        
        def dfs(i,remain,curr):
            if remain>=0:
                ans.add(tuple(curr))
                if i==N:
                    return
                curr.append(nums[i])
                dfs(i+1,remain-div[i],curr)
                    
        for i in range(N):
            dfs(i,k,[])
        
        return len(ans)-1
```

改回雙迴圈的普通暴力搜，改成這樣就覺得這題難度好像沒有達到Q3水準。

```python
class Solution:
    def countDistinct(self, nums: List[int], k: int, p: int) -> int:
        N=len(nums)
        div=[0]*N
        s=set()
        for i,n in enumerate(nums):
            if n%p==0:
                div[i]=1
                
        for i in range(N):
            sub=[]
            remain=k
            for j in range(i,N):
                if div[j]>remain:
                    break
                remain-=div[j]
                sub.append(nums[j])
                s.add(tuple(sub))
          
        return len(s)
```