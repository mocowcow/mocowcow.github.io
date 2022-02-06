---
layout      : single
title       : LeetCode 80. Remove Duplicates from Sorted Array II
tags 		: LeetCode Medium TwoPointers Array
---
# 題目
輸入一個有序遞增的陣列nums，同樣的數字最多只能出現2次，將多出來的數字去除掉。最後回傳去重複後的陣列長度。  
必須使用in-place演算法。

# 解法
很明顯要使用雙指標。read表讀取位置，write表寫入位置，再維護一個last變數保存上次讀入的數字。  
如果當前讀入與上次相同，則cnt+1，否則重置為1並更新last。如cnt小於等於2時，將last寫入write位置並遞增1。最後write會正好等於陣列長度，可以直接回傳。

```python
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        N = len(nums)
        read = write = 0
        last = None
        cnt = 0
        while read < N:
            if nums[read] != last:
                last = nums[read]
                cnt = 1
            else:
                cnt += 1
            if cnt <= 2:
                nums[write] = last
                write += 1
            read += 1

        return write
```

優化一下，其實不需要last變數，因為透過write就可以知道上次碰到什麼數字了。

```python
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        N = len(nums)
        read = write = 2
        while read < N:
            if nums[write-2] != nums[read]:
                nums[write] = nums[read]
                write += 1
            read += 1

        return write
```