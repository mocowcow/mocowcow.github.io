--- 
layout      : single
title       : LeetCode 2389. Longest Subsequence With Limited Sum
tags        : LeetCode Easy Array PrefixSum BinarySearch Sorting
---
周賽308。滿不錯的題，測資加大一點可以變成medium。  

# 題目
輸入長度n的整數陣列nums，以及長度m的整數陣列queries。  

回傳長度為m的陣列answer，其中answer[i]代表可以從nums中組成的最長子序列長度，且其總和不超過queires[i]。  

# 解法
看到子序列求總和，就知道元素的順序不影響答案，直接排序再說。  

既然希望子序列長度盡可能大，那麼可以從最小的元素依序取用，直到總和快要超過限制大小為止。  
n和m最大都是1000，暴力法O(N^2)剛好可以通過。  

```python
class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        nums.sort()
        
        def f(limit):
            size=0
            for n in nums:
                if n>limit:break
                limit-=n
                size+=1
            return size
        
        return [f(x) for x in queries]
```

如果測資大小增加，上述暴力法肯定是沒辦法通過的，這時候要想想別的辦法。  

可以對排序好的nums做前綴和，在透過二分搜找到最適當的長度。  
因為我們要找的是最後一個小於等於queries[i]的位置，所以先找到第一個大於queries[i]的索引，將其減一後求得。  

每次查詢O(log N)，共M次，整體時間複雜度O(M log N)。題外話，第一名只用了51秒寫出這個答案，真的有夠變態。  

```python
class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        nums.sort()
        N=len(nums)
        psum=[0]*(N+1)
        for i,n in enumerate(nums):
            psum[i+1]=psum[i]+n
            
        return [bisect_right(psum,x)-1 for x in queries]
```