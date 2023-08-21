---
layout      : single
title       : LeetCode 2826. Sorting Three Groups
tags        : LeetCode Medium Array DP BinarySearch
---
雙周賽111。這題描述有夠繞，而且測資範圍很詭異的小，不知道出題者在想什麼。  

## 題目

輸入長度n的整數陣列nums。  

將0到n-1的數字分別編入組別1\~3之中，其中nums[i]代表數字i的組別。某些組別可能不包含任何數。  

你可以執行以下操作任意次：  

- 選擇數字x，並改變其組別。也就是將nums[x]改成1\~3的任意數  

一個新的陣列res是透過以下程序建構而成：  

- 將各組中的數字排序  
- 依照組別1,2,3的順序將數字加入res  

若nums能夠構造出一個**非遞減**排序的陣列res，則稱nums為**美麗的**。  

求**最少**需要幾次操作才能使得nums變成**美麗的**。  

## 解法

其實res的建構方式簡單講就是：從左到右掃3次，第i次只把第i組的數字加入res。  
而且nums中沒有重複數字，與其說非遞減，不如說是**遞增**。  
為了使res遞增，則須要確保各組別的數字都是相連的，不可以交錯出現，nums必須呈現[1..2..3..]這種狀態。  

我們不知道nums[i]分配到哪組才是最佳解，並且nums[i]可選的組別受限於nums[i-1]的組別。  
假設我們給nums[i]分配到2組，則nums[i+1, N-1]則形成一個規模更小的子問題。  

定義dp(i,prev)：nums[i, N-1]只能選prev\~3的組別時，使得res遞增的最小操作次數。  
轉移方程式：dp(i,prev)=min( dp(i+1, j)+cost FOR ALL prev<=j<=3 )，若j=nums[i]則cost為0，否則為1。  
base base：當i=N時，沒有剩餘數字，回傳0。  

prev只會有3種，每個狀態最多也只要轉移3次，可以視作常數。  
時間複雜度O(N)。  
空間複雜度O(N)。  

```python
class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        N=len(nums)
        
        @cache
        def dp(i,prev):
            if i==N:
                return 0
            res=inf
            for j in range(prev,4):
                cost=int(j!=nums[i])
                res=min(res,dp(i+1,j)+cost)
            return res
        
        return dp(0,1)
```

既然是要使得nums非遞減，只要找到有幾個不符合非遞減的元素，修改他們就行。  
可以先求nums的最長遞增子序列(LIS)長度，注意是**不嚴格遞增**，總長度N扣掉LIS長度就是答案。  

時間複雜度O(N log N)。  
空間複雜度O(N)。  

```python
class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        N=len(nums)
        dp=[] # LIS
        for x in nums:
            idx=bisect_right(dp,x)
            if len(dp)==idx:
                dp.append(x)
            else:
                dp[idx]=x
            
        return N-len(dp)
```
