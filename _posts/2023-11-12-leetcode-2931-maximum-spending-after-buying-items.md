---
layout      : single
title       : LeetCode 2931. Maximum Spending After Buying Items
tags        : LeetCode Hard Array Matrix Greedy Heap
---
雙周賽117。本次比賽第二個吐槽點，Q4比Q3甚至Q2還簡單。  
若不是Q2有洩題嫌移，搞不好過得人還比Q4少。  

## 題目

輸入m\*n的矩陣values，代表m個不同的商店，各店販售n種不同的商品。  
其中values[i][j]代表商店i的第j個商品的價錢。  
而且商店中的價格是以非遞減呈現。也就是說，對於所有0 <= j < n - 1，滿足values[i][j]>=values[i][j+1]。  

每一天你可以從任一商店購買一個物品。具體來說，在d天：  

- 選擇商店i  
- 以values[i][j]\*d購買最靠右的可用商品j。也就是在該商店沒有被購買過的商品j  

注意：每個商店中的物品都是獨立的。若你從商店1購買物品0，之後還是可以在其他商店買物品0。  

求買完全部m\*n個商品，**最多可以花多少錢**。  

## 解法

講得很複雜，反正就是每個商品各買一次，看怎樣順序能把總價最大化。  

最初，每個商店的n-1個物品都能買。  
天數d越小，得到的乘積也越小。應該貪心地先購買價格較小的商品。  
先買最小的values[i][j]，然後values[i][j-1]解鎖。  

因為values[i]是非遞減，所以新解鎖的商品只會更貴，不會更便宜。  
重複買最便宜的，直到買完為止。  

維護最便宜的商品，使用min heap正合適。  

最多只會同時存在m個商店的一個商品，總共需要加入mn個。  
時間複雜度O(mn log m)。  
空間複雜度O(m)。  

```python
class Solution:
    def maxSpending(self, values: List[List[int]]) -> int:
        M,N=len(values),len(values[0])
        h=[]
        for r in range(M):
            heappush(h,[values[r][N-1],r,N-1])
            
        ans=0
        for day in range(1,M*N+1):
            val,r,c=heappop(h)
            ans+=val*day
            if c>0:
                heappush(h,[values[r][c-1],r,c-1])
                
        return ans
```
