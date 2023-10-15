---
layout      : single
title       : LeetCode 2900. Longest Unequal Adjacent Groups Subsequence I
tags        : LeetCode Medium Array String Greedy
---
雙周賽115。

## 題目

輸入整數n，以及字串陣列words[i]還有**二進位**陣列groups，兩者長度皆為n。  

你必須從索引陣列[0, 1, ..., n - 1]中選擇一個**最長子序列**，記為[i0, i1, ..., ik - 1]，子序列長度記為k。  
對於所有介於0 < j + 1 < k的j都滿足groups[i<sub>j</sub>] != groups[i<sub>j+1</sub>]。  

回傳一個陣列字串，**依序**由該子序列中的索引對應words中的字串而成。若有多個答案，則回傳任意一個。  

注意：words中的字串長度可能**不同**。  

## 解法

反正就是索引子序列中，不可以有任意兩個相鄰的索引屬於**同一組**。  

遍歷索引i的過程中，假設groups[i]為1，且上一個索引組別為0，試想：  

- 選了i，長度加1，之後碰到組1就不能選；但組0可選  
- 不選i，之後碰到和1可選；但組0不可選  

如果不選i，還要等到下一個組1的索引出現才能選，不可能比選i得到更好的結果，所以組別交替時一定要選。  

時間複雜度O(n)。  
空間複雜度O(1)。  

```python
class Solution:
    def getWordsInLongestSubsequence(self, n: int, words: List[str], groups: List[int]) -> List[str]:
        ans=[]
        prev=None
        for i in range(n):
            if groups[i]!=prev:
                ans.append(words[i])
                prev=groups[i]
                
        return ans

```
