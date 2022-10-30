--- 
layout      : single
title       : LeetCode 2453. Destroy Sequential Targets
tags        : LeetCode Medium Array HashTable Greedy
---
雙周賽90。之前看人家寫貪心題都可以壓成one loop，感覺很帥就試試看，結果寫錯拿一個WA。我看以後還是乖乖拆成多個步驟。  

# 題目
輸入由正整數組成的陣列nums，表示數列上的目標。還有一個整數space。  

你有一台可以摧毀目標的機器。將nums[i]**輸入**機器，則會破壞所有等同nums[i] + (c \* space)的目標，其中c非負整數。你要盡可能破壞較多的目標。  

求**可破壞目標數最多**的選擇之中，nums[i]的**最小值**。  

# 解法
看到nums[i] + (c \* space)愣住一下，其實就是模space做分組。若兩個數字a,b同餘space，則他們是同一個組別，可以互相被消除。  

先以space取餘數把所有數字分組。找到單組最多個人數mx_target，過濾出人數正好為mx_target的組別中所有成員，其值最小者就是答案。  

最差情況下nums的元素都不相同，需要遍歷三次，時空間複雜度都是O(N)。  

```python
class Solution:
    def destroyTargets(self, nums: List[int], space: int) -> int:
        d=defaultdict(list)
        for n in nums:
            r=n%space
            d[r].append(n)
            
        mx_target=max(len(v) for v in d.values())
        ans=min(min(v) for v in d.values() if len(v)==mx_target)
        
        return ans
```

一個迴圈同時找到最大目標數+最小值。  

```python
class Solution:
    def destroyTargets(self, nums: List[int], space: int) -> int:
        d=defaultdict(list)
        for n in nums:
            r=n%space
            d[r].append(n)
            
        mn=inf
        mx_grp=0
        for v in d.values():
            if len(v)>mx_grp:
                mx_grp=len(v)
                mn=min(v)
            elif len(v)==mx_grp:
                mn=min(mn,min(v)) 
        
        return mn
```