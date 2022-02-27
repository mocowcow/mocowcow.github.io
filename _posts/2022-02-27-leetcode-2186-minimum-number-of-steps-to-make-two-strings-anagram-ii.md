---
layout      : single
title       : LeetCode 2186. Minimum Number of Steps to Make Two Strings Anagram II
tags 		: LeetCode Medium 
---
周賽282。大家的好朋友anagram又來了。

# 題目
輸入兩個字串s和t，每次動作可以對s或t加入任何一個字元，求最少需要幾次動作才能讓兩字串互為anagram。

# 解法
題目規定只能加不能刪，那就是把兩邊加到數量一樣就是了。  
維護一個雜湊表ctr，對s中每個字元計數+1，對t中每個字元計數-1，最後值若是正數代表s比t多出多少個字元；負數則是s比t少了多少。回傳雜湊表中所有元素的絕對值就是答案。

```python
class Solution:
    def minSteps(self, s: str, t: str) -> int:
        ctr = Counter(s)
        for c in t:
            ctr[c] -= 1

        ans = 0
        for _, v in ctr.items():
            ans += abs(v)

        return ans

```
