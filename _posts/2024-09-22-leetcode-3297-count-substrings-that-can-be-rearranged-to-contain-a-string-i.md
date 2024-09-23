---
layout      : single
title       : LeetCode 3297. Count Substrings That Can Be Rearranged to Contain a String I
tags        : LeetCode Medium
---
weekly contest 416。  

## 題目

輸入兩個字串 word1, word2。  

若字串 x 重排後，word2 是其**前綴**，則稱 x 是**合法的**。  

求 word1 有多少個**合法子字串**。  

## 解法

相似題 [76. Minimum Window Substring](https://leetcode.com/problems/minimum-window-substring/)。  
因為可以**重排**，所以不需要在乎出現順序，只要確保子字串完整覆蓋 word2 裡出現的字元。  

**子字串**問題通常可用**滑動窗口**解決。  
我們可以枚舉右邊界，並且在窗口內的子字串**合法時收縮左邊界**，保證 [0, left-1] 區間內都可以搭配 right 成為合法的子字串。  

時間複雜度 O(26N)。  
空間複雜度 O(26)。  

```python
class Solution:
    def validSubstringCount(self, word1: str, word2: str) -> int:
        d1 = Counter()
        d2 = Counter(word2)

        def ok():
            return all(d1[k] >= d2[k] for k in d2)

        ans = 0
        left = 0
        for right, c in enumerate(word1):
            d1[c] += 1
            while ok():
                d1[word1[left]] -= 1
                left += 1

            # update answer
            # [0, left-1] are valid leftbound
            ans += left 

        return ans
```
