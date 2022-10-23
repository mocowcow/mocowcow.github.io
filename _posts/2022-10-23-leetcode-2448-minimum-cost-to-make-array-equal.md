--- 
layout      : single
title       : LeetCode 2448. Minimum Cost to Make Array Equal
tags        : LeetCode Hard Array TwoPointers Greedy
---
周賽316。又感受到python的弱點，好險最近有學go來彌補計算太慢的問題，不然真的要吃土。  

# 題目
輸入兩個長度為n的陣列nums和cost。  

你可以執行以下操作**任意**次：  
- 將nums中的任何元素增加或減少1  

對第i個元素執行一次操作的成本為cost[i]。  

求使nums中所有元素相等的**最小總成本**。  

# 解法
陣列中的元素很多，而且相同元素的操作成本可能不同，單獨計算肯定是不現實的。  
問題在於要怎麼找到要把所有元素變成目標元素x，這個x要怎麼找？  

因為每次操作一定是把**最大元素縮減**，或是把**最小元素增加**，所以可以使用雙指針來處理。  
先統計各元素的操作成本，選擇成本較小者邊界縮減後，先把成本加入答案，再把成本更新到新元素中。  

例：  
> total_cost = [2,1,4], lo = 1, hi = 3
> 縮減lo，此次成本為2  
> total_cost = [_,3,4], lo = 2, hi = 3  
> 縮減lo，此次成本為3  
> 總成本為2+3 = 5  

時空間複雜度都是O(N)，其中N為cost的長度10^6。  
然而python跑太慢，拿到TLE。  

```python
class Solution:
    def minCost(self, nums: List[int], cost: List[int]) -> int:
        cnt=[0]*1000005
        lo=1
        hi=1000000
        ans=0
        
        for n,c in zip(nums,cost):
            cnt[n]+=c
            
        while lo<hi:
            if cnt[lo]<cnt[hi]:
                ans+=cnt[lo]
                cnt[lo+1]+=cnt[lo]
                lo+=1
            else:
                ans+=cnt[hi]
                cnt[hi-1]+=cnt[hi]
                hi-=1
        
        return ans
```

python拿到TLE我也懶得去修改細節，果斷換go來做，兩者執行速度真的是天壤之別。  

```go
func minCost(nums []int, cost []int) int64 {
    cnt:=make([]int,1000005)
    ans:=0
    lo:=1
    hi:=1000000
    
    for i,n:=range nums{
        cnt[n]+=cost[i]
    }
    
    for lo<hi{
        if cnt[lo]<cnt[hi]{
            ans+=cnt[lo]
            cnt[lo+1]+=cnt[lo]
            lo++
        }else{
            ans+=cnt[hi]
            cnt[hi-1]+=cnt[hi]
            hi--
        }
    }
    
    return int64(ans)
}
```