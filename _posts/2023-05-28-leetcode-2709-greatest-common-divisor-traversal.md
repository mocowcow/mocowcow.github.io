--- 
layout      : single
title       : LeetCode 2709. Greatest Common Divisor Traversal
tags        : LeetCode Hard Array Math UnionFind HashTable
---
雙周賽105。看來我最擅長的題型就是並查集了，這次竟然打到100名內，真爽。  

# 題目
輸入整數陣列nums，某些情況下，你可以在索引之間**移動**。  
對於兩個不同的索引i和j，如果nums[i]和nums[j]的gcd不為1，則可以在兩者間自由移動。  

你的目標是檢查**所有**滿足i<j的索引數對(i, j)中，都**存在某條路徑**能夠從i移動到j。  

如果所有索引數對都可以移動則回傳true，否則回傳false。  

# 解法
雖說是要檢查所有(i,j)，但移動沒有方向限制，所以只要每個索引相互連通，一定可以任意移動。  

而1和任何數的gcd都是1，只要nums中存在1就不可能連通。但有個小陷阱：nums = [1]其實是連通的。  
所以只要N大於1，且nums存在1就可以過濾掉。  

只要gcd不為1就連通，也就是兩數間要有共通的因數。  
將每個數字做質因數分解，以所有質因數p為鍵值紀錄下索引位置i，然後將擁有共通因數的索引全部合併。  
最後檢查所有索引是否都屬於同一個連通塊。  

質因數分解需要O(sqrt(MX))，需要N次。合併N個節點需要O(N)。  
時間複雜度O(N sqrt(MX))，其中N為nums大小，MX為max(nums[i])。  
空間複雜度O(N sqrt(MX))。  

```python
class Solution:
    def canTraverseAllPairs(self, nums: List[int]) -> bool:
        N=len(nums)
        if N>1 and 1 in nums:
            return False
        
        def prime_fact(n):
            fact = set()
            p = 2
            while p*p <= n:
                if n%p==0:
                    fact.add(p)
                    while n % p == 0:
                        n //= p
                p += 1
            if n != 1:
                fact.add(n)
            return fact

        def find(x):
            if fa[x]!=x:
                fa[x]=find(fa[x])
            return fa[x]
        
        def union(a,b):
            f1=find(a)
            f2=find(b)
            if f1!=f2:
                fa[f1]=f2
        
        fa=list(range(N))
        d=defaultdict(list)
        
        for i,x in enumerate(nums):
            pf=prime_fact(x)
            for p in pf:
                d[p].append(i)
                
        for v in d.values():
            for i in range(1,len(v)):
                union(v[0],v[i])
        
        s=set()
        for i in range(N):
            s.add(find(i))
            
        return len(s)==1
```
