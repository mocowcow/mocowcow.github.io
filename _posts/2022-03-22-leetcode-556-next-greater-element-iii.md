---
layout      : single
title       : LeetCode 556. Next Greater Element III
tags 		: LeetCode Medium String Math 
---
學習計畫碰到的。用了一個超級爛的方法竟然還能過，笑死了。

# 題目
輸入正整數n，求大於n且和n的數字組成一樣的最小數字。若不存在則回傳-1。整數最大只能到2^32-1。

# 解法
把n轉成字串拿去用內建函數求出所有排列，再用set去重複，就是所有可能的重組數nums了。  
nums排序好，二分搜找第一個大於n的數，如果不存在或是該數超過2^32-1，則回傳-1，否則回傳該數。  

因為n最大可以到2147483647，長度N=10，求排列時間為O(N!)，勉強壓線過去，在大一點可能就不會過了。

```python
class Solution:
    def nextGreaterElement(self, n: int) -> int:
        permu = set(permutations(list(str(n))))
        nums = sorted([int(''.join(x)) for x in permu])
        idx = bisect_right(nums,n)
        
        if idx < len(nums) and nums[idx] <= 2147483647:
            return nums[idx]
        else:
            return -1
```

