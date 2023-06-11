--- 
layout      : single
title       : LeetCode 2735. Collecting Chocolates
tags        : LeetCode Medium Array Simulation
---
周賽349。這題好像也很機車，更重要的是題目描述很爛，但不知道為何我電波對得上。

# 題目
輸入長度為n的整數陣列nums，代表收集每塊巧克力的成本。  
每個巧克力都對應不同的類型。最初，索引i的巧克力就對應到第i個類型。  

你可以花費成本x進行以下操作：  
- 將所有巧克力i的類型換成第i+1個的類型。如果i為n-1，則換成第0個的類型  

你可以執行任意次操作，求收集所有類型巧克力的**最小成本**。  

# 解法
個人感覺，與其說是交換類型，不如當作交換價格比較好理解。  
每次操作都可以把整個價格向右移一步，我們只要決定要在哪個價格買入就好。  

每次操作可以讓每個巧克力的價格改變。  
對於第i個巧克力來說：  
- 操作0次，只能用nums[i]的任意價格買  
- 操作1次，可以用nums[i-1, i]的任意價格買  
- 操作2次，可以用nums[i-2, i]的任意價格買  

以此類推，最多操作N-1次，就可以遍歷所有價格。  
維護陣列cost，代表每個巧克力的最低價。每次操作後更新完cost，其總和加上操作次數\*x就是總成本，以此更新答案。  

時間複雜度O(N^2)。  
空間複雜度O(N)。  

```python
class Solution:
    def minCost(self, nums: List[int], x: int) -> int:
        N=len(nums)
        cost=[inf]*N
        ans=inf
        
        for ops in range(N):
            for i in range(N):
                cost[i]=min(cost[i],nums[(i-ops)%N])
            tot=sum(cost)+x*ops
            ans=min(ans,tot)
            
        return ans
```
