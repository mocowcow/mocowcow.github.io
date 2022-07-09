--- 
layout      : single
title       : LeetCode 1696. Jump Game VI
tags        : LeetCode Medium Array DP Heap
---
每日題。明明以前寫過，但是卻想不起來。看來我跟單調佇列還是不夠熟。

# 題目
輸入0索引的整數陣列nums和整數k。  
從索引0出發，每一次移動最多可往右跳k步，且不能超過陣列邊界。也就是可以從i跳到[i+1, min(n-1, i+k)] 之間任何位置。  
**分數**指的是經過的索引j上的nums[j]總和。求跳到最後一個位置(索引n-1)的**最大分數**。  

# 解法
起初只想到O(N*k)的解法，每個位置i可以由i-k\~i-1出發抵達，但是n和k上限高達10^5，沒意外的吃了TLE。  

後來看看提示，說只要找到可用範圍內最大者就好，所以我選擇用max heap來紀錄可用值。  
max heap以(dp值, 索引)為鍵，會將最佳的出發位置保持在頂端。  
因為索引0作為起點，所以dp[0]直接設為nums[0]的值，並將dp[0]加入heap中。  

遍歷剩下的索引，每次先替除掉超出k步範圍的之外的無效起點，之後才選擇heap頂端的索引做為起點，抵達至當前索引i，並將dp[i]押回heap。  
最後dp[N-1]就是答案。因為heap中最多存有k個元素，每次存取為O(log k)，共N次遍歷，整體複雜度為O(N log k)。  

```python
class Solution:
    def maxResult(self, nums: List[int], k: int) -> int:
        N=len(nums)
        dp=[0]*N
        dp[0]=nums[0]
        h=[[-nums[0],0]] # (val,idx)
        
        for i in range(1,N):
            while h[0][1]<i-k:
                heappop(h)
            dp[i]=nums[i]+-h[0][0]
            heappush(h,[-dp[i],i])
            
        return dp[-1]
```

核心思想一樣是保存可用的最大的出發點，使用單調遞減佇列代替max heap，可以將整體複雜度降低至O(N)。  

我曾看過一個關於單調佇列的比喻，十分傳神：如果新來的員工比能力等於/大於老員工，那麼老員工就可以被開除了。  
試想我們原本有以下dp[j]選擇作為dp[i]的參考索引：  
> q = [5,4,3,3]  
> nums[i] = -1  
> dp[i] = -1+5 = 4  
> 將4押入q中，這時前方[4,3,3]都不會比dp[i]得到更佳結果，故直接刪除  
> q = [5,~~4,3,3~~,4] = [5,4]

```python
class Solution:
    def maxResult(self, nums: List[int], k: int) -> int:
        N=len(nums)
        dp=[0]*N
        dp[0]=nums[0]
        q=deque([0])
        
        for i in range(1,N):
            while q[0]<i-k:
                q.popleft()
            dp[i]=nums[i]+dp[q[0]]
            while q and dp[i]>=dp[q[-1]]:
                q.pop()
            q.append(i)
            
        return dp[-1]
```