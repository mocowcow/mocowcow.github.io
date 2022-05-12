--- 
layout      : single
title       : LeetCode 90. Subsets II
tags        : LeetCode Medium Array Backtracking BitManipulation HashTable
---
複習回溯經典題，發現我以前竟然偷懶，全都用set去重複，沒有一次自己剪枝的。

# 題目
輸入可能有重複的陣列nums，回傳所有可能的子集合。  
答案中不應該包含重複的子集合，且可依任意順序排列。

# 解法
先來個用set去重複的解法，先排序把同樣的數字集中，保證順序不影響結果。

```python
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        N = len(nums)
        nums.sort()
        ans=set()
        
        def bt(i,curr):
            ans.add(tuple(curr))
            for j in range(i,N):
                curr.append(nums[j])
                bt(j+1,curr)
                curr.pop()
            
        bt(0,[])
        
        return ans
```

bit mask求子集之後再用set去重複。  
長度為N的集合共有2^N個子集，包含空集合。

```python
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        N = len(nums)
        nums.sort()
        ans=set()
        
        for mask in range(1<<N):
            sub=[]
            for i in range(N):
                if mask&(1<<i):
                    sub.append(nums[i])
            ans.add(tuple(sub))
        
        return ans
```


最後是自己剪枝的解法，一樣要先排序，如果當前數字i和i-1相同，則不加入。

```python
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        N = len(nums)
        nums.sort()
        ans = []

        def bt(i, curr):
            ans.append(curr[:])
            for j in range(i,N):
                if j>i and nums[j]==nums[j-1]:
                    continue
                curr.append(nums[j])
                bt(j+1,curr)
                curr.pop()

        bt(0, [])
        return ans
```