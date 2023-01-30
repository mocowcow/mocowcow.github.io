--- 
layout      : single
title       : LeetCode 2551. Put Marbles in Bags
tags        : LeetCode Hard Array Sorting Greedy Heap
---
周賽330。只想得到dp解，沒想到是腦筋急轉彎。  

# 題目
你有k個背包。輸入一個整數陣列weights，其中weights[i]代表第i顆彈珠的重量。另外還有整數k。  

你必須按照以下規則，將彈珠分裝到k個背包中：  
- 背包不可以為空  
- 如果第i和第j顆彈珠都在同一個背包中，則介於i和j的所有彈珠都必須在同一個背包中  
- 如果一個背包裝了i\~j的彈珠，則成本為weights[i] + weights[j]  

一個分配方案的**分數**為個背包的成本總和。  

求所有方案中**最大分數**和**最小分數**的差值。  

# 解法
看到子陣列切割馬上想到dp(i,k)代表從i點切出k個背包的解法，但是weights長度N和k都高達10^5，怎麼看都不可能過。  

看看例題2：  
> weights = [1, 3], k = 2  
> 切成兩個部分[1]和[3]  
> 成本分別為1+1和3+3  

分成k個背包，中間有k-1個分割點。對於每個分割點來說，其左邊的元素會作為**左方背包的右端點**，而右邊的元素會做為**右方背包的左端點**。然後第一個元素必定是第一個背包的左端點、最後一個元素必定是最後一個背包的右端點。  
> weights = [1, 3], k = 2  
> 唯一切割點介於[1,3]之間。成本為1+3  
> 1作為第一個背包左端，3作為最後一個背包右邊。成本再加上1+3  
> 分數為4+4=8  

因此我們只要窮舉出所有的切割點，分別找出成本最大/最小的k-1個，便可求得分數。  
然而第一個和最後一個元素一定會包含在最大/最小分數的切割方案中，必定相減為0，所以不用特別處理。  

時間複雜度O(N log N)。空間複雜度O(N)。  

```python
class Solution:
    def putMarbles(self, weights: List[int], k: int) -> int:
        cut=[a+b for a,b in pairwise(weights)]
        cut.sort(reverse=True)
        
        ans=0
        for i in range(k-1):
            ans+=cut[i]-cut[-1-i]
            
        return ans
```

也可以用heap來做，在k比較小的情況下可以有效降低複雜度。  
維護min heap保存最大的成本，max heap保存最小的成本，最後求和相減。  

時間複雜度O(N log k)。空間複雜度O(k)。  

```python
class Solution:
    def putMarbles(self, weights: List[int], k: int) -> int:
        N=len(weights)
        min_heap=[]
        max_heap=[]
        for i in range(1,N):
            cost=weights[i]+weights[i-1]
            heappush(min_heap,cost)
            heappush(max_heap,-cost)
            if len(min_heap)>=k:
                heappop(min_heap)
                heappop(max_heap) 
                
        return sum(min_heap)+sum(max_heap)
```