--- 
layout      : single
title       : LeetCode 2528. Maximize the Minimum Powered City
tags        : LeetCode
---
雙周賽95。用線段樹寫半天一直TLE，比賽結束後洗完澡才恍然大悟，根本不需要線段樹。  

# 題目
輸入長度為n的整數陣列nums，其中stations[i]代表第i個城市的發電廠廠量。  

每個發電廠的供電範圍都是固定的。如果供電範圍為r，則城市i的發電廠可以為所有城市j供電，其中|i - j| <= r 且 0 <= i, j <= n - 1。  

而城市的**電量**等於為其供電的發電廠總數。  

你現在要新建k個發電廠，可以蓋在任何城市中，且供電範圍和原有的其他發電廠一致。  

輸入整數r和k，求最佳的新建策略下，所有**城市中電量最小**者的**最大可能電量**為多少。  

注意：k個發電廠可以蓋在不同城市中。  

# 解法
看到**最小值最大化**應當想到二分答案。若目標電量越大，則達成難度越大；目標電量越小，則達成難度越小。  

先對原本的發電廠計算差分，之後每次判斷的時候只要複製一份就好。  

電量最低為0，下界設為0。極端情況下每個城市都有10^5個電廠，且可以覆蓋到其他所有10^5個城市，初始電量皆為10^10。而最多可以新建10^9個電廠，電量上限為10^10 + 10^9，方便起見直接設上界為10^11。  
如果可以讓所有城市電量至少為mid，則更新下界為mid；否則mid以上的都不可能達成，更新上界為mid-1。  

那麼如何判斷新建k個電廠是否能夠使每個城市達到最低電量low？  
我們是從左到右遍歷各城市，對差分做前綴和求當前城市電量，因此左方的城市一定都已經滿足low電量。當前遍歷到的城市i應當為發電廠最左方的城市，而最右方的城市應該是i+(2\*r)，因此再做一次差分，讓i\~i+2\*r這個範圍補上不足的電量。  
如果建造的發電廠不超過k座，則代表可行，回傳true；否則回傳false。  

時間複雜度O(N log MX)，其中MX為最大可能電量，即二分上界。空間複雜度O(N)。  

```python
class Solution:
    def maxPower(self, stations: List[int], r: int, k: int) -> int:
        N=len(stations)
        rr=r*2
        
        # difference array
        power=[0]*(N+1)
        for i,n in enumerate(stations):
            lb=max(0,i-r)
            rb=min(N-1,i+r)
            power[lb]+=n
            power[rb+1]-=n
            
        def ok(low):
            diff=power[:]
            cnt=0
            # prefix sum
            for i in range(N):
                if i>0:
                    diff[i]+=diff[i-1]
                if diff[i]<low:
                    need=low-diff[i]
                    cnt+=need
                    if cnt>k:return False
                    diff[i]+=need
                    diff[min(N-1,i+rr)+1]-=need
            return True
        
        lo=0
        hi=10**11
        while lo<hi:
            mid=(lo+hi+1)//2
            if not ok(mid):
                hi=mid-1
            else:
                lo=mid
                
        return lo
```
