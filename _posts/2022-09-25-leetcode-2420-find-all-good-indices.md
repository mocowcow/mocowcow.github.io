--- 
layout      : single
title       : LeetCode 2420. Find All Good Indices
tags        : LeetCode Medium Array Greedy DP
---
周賽312。差點以為是單調堆疊之類的東西，結果應該是貪心，要說是dp也可以。  

# 題目
輸入大小為n的整數陣列nums和一個正整數k。  

若滿足以下條件，我們將索引i稱為**好的**：  
-  k <= i < n - k  
- 索引i左方k個連續元素為**非遞增**順序  
- 索引i右方k個連續元素為**非遞減**順序  

將所有**好的**索引依照遞增順序回傳。  

# 解法
一下子遞增遞減有點混淆，不如說要找到索引i為中心，各往左右找k個元素都要是遞增的。  
先從左往右掃一次，找到每個位置i左邊有幾個連續遞增元素；再從右往左掃，找到i右邊有幾個遞增元素。  
再來遍歷第三次，入果i的左右各有k個以上的遞增元素，則加入答案。  

時間複雜度O(N)，空間複雜度O(N)。  

```python
class Solution:
    def goodIndices(self, nums: List[int], k: int) -> List[int]:
        N=len(nums)
        lb=[0]*N
        rb=[0]*N
        ans=[]
        
        last=-inf
        cnt=0
        for i,n in enumerate(nums):
            lb[i]=cnt
            if n>last:
                cnt=1
            else:
                cnt+=1
            last=n
        
        last=-inf
        cnt=0
        for i in range(N-1,-1,-1):
            n=nums[i]
            rb[i]=cnt
            if n>last:
                cnt=1
            else:
                cnt+=1
            last=n
            
        for i in range(N):
            if lb[i]>=k and rb[i]>=k:
                ans.append(i)
                
        return ans
```
