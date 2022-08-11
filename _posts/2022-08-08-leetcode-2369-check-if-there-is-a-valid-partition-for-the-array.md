--- 
layout      : single
title       : LeetCode 2369. Check if There is a Valid Partition For The Array
tags        : LeetCode Medium Array DP
---
周賽305。完蛋，花了半天在想怎麼用stack來做，比賽結束才聽說是DP，馬上就用top down寫出來。

# 題目
輸入整數陣列nums。你必須將陣列分割為一個或多個連續的子陣列。  
若每個子陣列都符合以下其中一項條件，則稱此分割有效：  
- 子陣列正好由2個相等的元素組成。例如[2,2]  
- 子陣列正好由3個相等的元素組成。例如[4,4,4]  
- 子陣列正好由3個連續遞增的元素組成，且相鄰元素的差為1。例如[3,4,5]；但[1,3,5]不是  

如果陣列至少有一種有效分割方式，則回傳true；否則回傳false。  

# 解法
果然top down還是比較好思考，只要處理自己管轄的部分，剩下的就交給遞迴去處理吧！  

定義dp(i)：由nums[i]開始至末端的子陣列是否能有效的被分割。  
轉移方程式：符合三種條件中的任一即可：  
1. nums[i]等於nums[i+1]，且nums[i+2]開始的子陣列能被分割  
2. nums[i]等於nums[i+1]等於nums[i+2]，且nums[i+3]開始的子陣列能被分割  
3. nums[i]等於nums[i+1]-1等於nums[i+2]-2，且nums[i+3]開始的子陣列能被分割  

base case：當i等於nums長度N時，空陣列代表已經成功分割完，直接回傳true。  
而dp(0)表示由nums[0]開始的子陣列是否能被分割，和完整陣列相同，直接回傳dp(0)就是答案。  

```python
class Solution:
    def validPartition(self, nums: List[int]) -> bool:
        N=len(nums)
        
        @cache
        def dp(i):
            if i==N:
                return True
            if i+1<N and nums[i]==nums[i+1] and dp(i+2):
                return True
            if i+2<N and nums[i]==nums[i+1]==nums[i+2] and dp(i+3):
                return True
            if i+2<N and nums[i]==nums[i+1]-1==nums[i+2]-2 and dp(i+3):
                return True
            return False
        
        return dp(0)
```

試著改成bottom up的寫法，這邊索引太多加加減減，頭腦不夠清晰真的很難一次寫對，只好先用沒效率的方法處理base case，之後再來改進。  
對比賽中直接寫出bottom up的大神表達尊重。  

```python
class Solution:
    def validPartition(self, nums: List[int]) -> bool:
        N=len(nums)
        dp=[False]*(N)
        
        for i in range(1,N):
            if (i-2<0 or dp[i-2]) and nums[i]==nums[i-1]:dp[i]=True
            if i>1 and (i-3<0 or dp[i-3]) and nums[i]==nums[i-1]==nums[i-2]:dp[i]=True
            if i>1 and (i-3<0 or dp[i-3]) and nums[i]==nums[i-1]+1==nums[i-2]+2:dp[i]=True
            
        return dp[-1]
```

把dp陣列長度加上1，讓dp[0]表示base case，所以狀態轉移中的每個dp索引都要遞增1。  

```python
class Solution:
    def validPartition(self, nums: List[int]) -> bool:
        N=len(nums)
        dp=[False]*(N+1)
        dp[0]=True
        
        for i in range(1,N):
            if dp[i-1] and nums[i]==nums[i-1]:dp[i+1]=True
            if i>1 and dp[i-2] and nums[i]==nums[i-1]==nums[i-2]:dp[i+1]=True
            if i>1 and dp[i-2] and nums[i]==nums[i-1]+1==nums[i-2]+2:dp[i+1]=True
            
        return dp[-1]
```