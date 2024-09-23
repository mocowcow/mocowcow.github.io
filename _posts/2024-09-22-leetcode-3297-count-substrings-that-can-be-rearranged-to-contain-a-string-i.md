---
layout      : single
title       : LeetCode 3297. Count Substrings That Can Be Rearranged to Contain a String I
tags        : LeetCode Medium
---
weekly contest 416。  
吐槽點實在太多了，可能比正文還多。  

---

本次 Q3, Q4 幾乎相同，差別在 Q4 多了一句話：  
> Note that the memory limits in this problem are smaller than usual, so you must implement a solution with a linear runtime complexity.  

因為空間限制更小，所以答案必須是線性複雜度。  
當時 Q3 寫了 O(26N)，忽略常數應該算是線性吧？直接貼去 Q4，拿到 TLE。  
我也沒多想，以為是日常 python3 被卡常數，索性換成 golang 就過了。  
後來才想到有嚴格的 O(N) 解法，不愧是尊貴的 golang，竟然能 26N 通過。  

---

先不管 26N 算不算線性，但是**空間小所以耗時要更少**這句話好像沒什麼邏輯。感覺像是打錯字。
反正 26N 在 Q4 是拿到 TLE 而非 MLE，感覺空間限制也沒變小。  

但是 C# 選手就非常有感了，空間限制小到不可思議，就算直接 return 0 都會 MLE。  

## 題目

輸入兩個字串 word1, word2。  

若字串 x 重排後，word2 是其**前綴**，則稱 x 是**合法的**。  

求 word1 有多少個**合法子字串**。  

## 解法

相似題 [76. Minimum Window Substring](https://leetcode.com/problems/minimum-window-substring/)。  
因為可以**重排**，所以不需要在乎出現順序，只要確保子字串**完整覆蓋** word2 裡出現的字元。  

**子字串**問題通常可用**滑動窗口**解決。  
我們可以枚舉右邊界，並且在窗口內的子字串**合法時收縮左邊界**，保證 [0, left-1] 區間內都可以搭配 right 成為合法的子字串。  

為判斷窗口內子字串是否覆蓋 word2，需要枚舉 26 種字元並檢查出現次數，若全部都大於等於 word2 中出現次數即為覆蓋。  

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
