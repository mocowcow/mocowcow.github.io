---
layout      : single
title       : LeetCode 2848. Points That Intersect With Cars
tags        : LeetCode Easy Array Simulation PrefixSum HashTable
---
周賽362。

## 題目

輸入二維整數陣列nums，代表數軸上停放的車子。  
對於所有索引i，其中nums[i] = [start<sub>i</sub>, end<sub>i</sub>]，代表車子在數軸上所佔據的範圍。  

求數軸上有多少個整數點被**任意車體**覆蓋。  

## 解法

其實我看不太懂題目描述在講什麼，不過可以把i當作y軸，車子是x軸。  
而第i車身覆蓋y=i上x=(start, end)的範圍，然後求x軸上有多少點上有車身。  
反正就是好幾條橫線，最後看x軸上有幾個點上面有線。  

只要x軸上的點有車身出現過就行，不管他幾次。  
直接遍歷所有車，將車身範圍加入集合中，最後回傳集合大小。  

時間複雜度O(N \* MX)，其中N為nums長度，MX為最大車身長度。  
空間複雜度O(MX)。  

```python
class Solution:
    def numberOfPoints(self, nums: List[List[int]]) -> int:
        s=set()
        for a,b in nums:
            for i in range(a,b+1):
                s.add(i)
                
        return len(s)
```

如果測資範圍比較大，可以使用差分標記車身範圍，最後對差分做前綴和，找出有身車的點。  

時間複雜度O(N+MX)，其中N為nums長度，MX為最大車身長度。  
空間複雜度O(M)。  

```python
class Solution:
    def numberOfPoints(self, nums: List[List[int]]) -> int:
        MX=101
        diff=[0]*101
        
        for a,b in nums:
            diff[a]+=1
            if b+1<MX:
                diff[b+1]-=1
                
        ans=0
        ps=0
        for x in diff:
            ps+=x
            if ps>0:
                ans+=1
                
        return ans
```
