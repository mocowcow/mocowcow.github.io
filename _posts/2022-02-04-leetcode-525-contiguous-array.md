---
layout      : single
title       : LeetCode 525. Contiguous Array
tags 		: LeetCode Medium HashTalbe PrefixSum
---
買了個小遊戲[Vampire Survivors](https://store.steampowered.com/app/1794680/Vampire_Survivors/)，怎這會這麼好玩，尤其是開寶箱的音效歡樂到一個不行。

# 題目
輸入一個只有0和1的陣列，求0和1數量相同的子陣列最長長度。

# 解法
維護一個變數psum，當遇到1時psum+=1，否則psum-=1，代表1與0的數量差。  
再維護一個字典d，以psum為鍵，紀錄index。因為子陣列越長越好，所以只在鍵值不存在時才要更新d[psum]。  

當psum為正時，代表1的數量多了；反之代表0多了。假設當前i=10，psum=2(多了兩個1)，且存在d[psum]=j，可以藉由扣除左方子陣列[0:j]達到平衡，而長度就是當前索引i-d[sum]。  

範例[0,1]提醒我們要給字典d初始值，當讀取完整個陣列時：  
>psum=0，長度應為2  
長度 = i-d[psum] = 1-(-1) = 2  

所以要初始化d[0]=1。


```python
class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        ans = psum = 0
        d = {0: -1}

        for i, n in enumerate(nums):
            if n == 1:
                psum += 1
            else:
                psum -= 1

            if psum not in d:
                d[psum] = i
            else:
                ans = max(ans, i-d[psum])

        return ans
```
