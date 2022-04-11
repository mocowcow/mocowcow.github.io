---
layout      : single
title       : LeetCode 2234. Maximum Total Beauty of the Gardens
tags 		: LeetCode Hard PrefixSum BinarySearch
---
周賽288。大多數人都是二分搜解法，我雖然也有嘗試二分搜，不過是搜所有花園最低值上限，之後從上限開始往下爆搜，效率太差。  
想了兩天總算稍微理解別人的答案。

# 題目
flowers陣列代表每個花園的花數，你可以再加種newFlowers朵花。整數target, full, partial分別用於計算花園美麗度。  
美麗度由以下公式計算：  
> 擁有至少target朵花的花園數\*full + 剩下花園的最少花數\*partial  

原先種好的花不能移動，求加種完newFlowers朵花時的最大可能美麗度為多少。

# 解法
為了後續方便計算，先把超過target的花園減至target，然後排序。  
先講講兩個edge cases，不管用什麼解法都可以先過濾掉。  
1. 初始的flowers全部都達到target，再怎樣都改變不了美麗度，直接回傳N*target  
2. newFlowers可以把所有的花園都塞到達標，但有時候不塞滿才是最佳解，所以回傳max(塞滿,留一個將近滿)

再來是比較難搞懂的部分。  
先利用前綴和計算出cost陣列，cost[i]代表使左方所有花園達到和flower[i]同樣花量所需的用量。  
例如：  
> flowers = [2,3,4,6]  
> cost[0]=0，因為flowers[0]左方沒有東西  
> cost[1]=1，要讓[2]成為3，用量1  
> cost[2]=3，要讓[2,3]成為4，用量2+1=3  
> cost[3]=9，要讓[2,3,4]成為6，用量4+3+2=9  

如此可以透過二分搜快速的找到最佳的花數下限。  

從最接近target的花園開始種起，最節省種植次數。  
維護指針j指向下一個要加種的目標，先調整到倒數第一個未達標的花園。  
重複以下計算直到new用光為止：  
1. 先二分搜，在cost中找到最後一個大於等於new值的位置idx，確定剩餘new次至少可以讓所有花園達到flower[idx]一樣多花  
2. 全部塞到和flower[idx]一樣多，有可能還有多的次數，即剩下new-cost[idx]次。將其除以idx+1，平均分給全部花園。  
3. 更新ans，把flower[j]塞到達標，j往左移，並從new中扣除使用的次數  

```python
class Solution:
    def maximumBeauty(self, flowers: List[int], newFlowers: int, target: int, full: int, partial: int) -> int:
        N = len(flowers)
        fl = sorted(min(x, target) for x in flowers)

        if fl[0] == target:  # 已經都達標了
            return N*full
        if newFlowers >= N*target-sum(fl):  # 可以全部達標
            return max(N*full, (N-1)*full+(target-1)*partial)

        cost = [0]  # cost[i] = 讓花園0~i全部和花園i一樣多 所需要的用量
        for i in range(1, N):
            cost.append(cost[-1]+(fl[i]-fl[i-1])*i)

        j = N-1  # j=倒數第一座未達標的花園
        while fl[j] == target:
            j -= 1

        ans = 0
        while newFlowers >= 0:
            idx = min(j, bisect_right(cost, newFlowers)-1)
            lowest = fl[idx] + (newFlowers-cost[idx])//(idx+1)
            ans = max(ans, (N-j-1)*full+lowest*partial)
            newFlowers -= target-fl[j]
            j -= 1

        return ans
```

