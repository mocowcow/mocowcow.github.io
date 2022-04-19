---
layout      : single
title       : LeetCode 300. Longest Increasing Subsequence
tags 		: LeetCode Medium DP Array BinarySearch
---
二分搜學習計畫。只記得DP版本怎麼搞，二分搜解法已經忘記了。

# 題目
輸入整數陣列nums，求最長遞增子序列(Longest Increasing Subsequence)長度。  
遞增子序列指的是原陣列所有元素出現或不出現組成，不改變元素的相對出現順序。例如[3,6,2,7]是陣列[0,3,1,6,2,2,7]的子序列。

# 解法
先講講原本的dp解法。  
定義dp(i)為以nums[i]結尾的遞增子序列長度。  
轉移方程式：dp(i)=max(dp[j]+1 FOR ALL j<i 且 nums[j]<nums[i])。  
i=0時，前方沒有其他元素，為base case，長度直接設為1。  

這題用bottom up的方式比較好理解，每個以i為結尾的位置，可以是由另一個小於i的位置j結尾的子序列生成而來。  
LIS不一定會是在最後尾出現，必須檢查每個dp[i]來找到最大值。

```python
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        N=len(nums)
        dp=[1]*N
        for i in range(1,N):
            for j in range(i):
                if nums[i]>nums[j]:
                    dp[i]=max(dp[i],dp[j]+1)
                    
        return max(dp)
```

試試看top down寫法，其實寫起來好像也沒說比較麻煩。

```python
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        @lru_cache(None)
        def dp(i):
            if i==0:
                return 1
            best=1
            for j in range(i):
                if nums[j]<nums[i]:
                    best=max(best,dp(j)+1)
            return best
                    
        return max(dp(i) for i in range(len(nums)))
```

二分搜解法，這個就比較玄學一點，要我自己想八成是想不太到。  
自己感覺這有點像是貪心法的概念，舉個例子：  
> [1,3,2,4]  
> i=0, LIS=[1] base case   
> i=1, LIS=[1,3] 沒有比3更大的數，加到尾端  
> i=2, LIS=[1,2] 因為所有由[1,3]所生成的遞增序列，一定也能由[1,2]生成  
> i=3, LIS=[1,2,4] 沒有比4更大的數，加到尾端  

講起來就是每次考慮新數字n時，找找看有沒有大於等於的n元素在序列中，有的話將其替換；否則直接加入序列最尾端。  
特別注意的是，這個**序列本身並等於實際上的LIS**。  

```python
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp=[]
        for n in nums:
            idx=bisect_left(dp,n)
            if idx==len(dp):
                dp.append(n)
            else:
                dp[idx]=n
                
        return len(dp)
```

