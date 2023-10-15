---
layout      : single
title       : LeetCode 2901. Longest Unequal Adjacent Groups Subsequence II
tags        : LeetCode Medium Array String DP
---
雙周賽115。最近好幾次都是題目內容完全一樣，只改測資範圍就當成兩題，所以有人都做第二題然後去前面貼一樣的code。  
結果這次好了，內容有差異，答案邏輯還完全不一樣，騙到不少人。  

## 題目

輸入整數n，以及字串陣列words[i]還有整數陣列groups，兩者長度皆為n。  

**漢明距離**指的是兩個等長等長字串中，對應字元**不同**的位置數。  

你必須從索引陣列[0, 1, ..., n - 1]中選擇一個**最長子序列**，記為[i0, i1, ..., ik - 1]，子序列長度記為k。  
對於所有介於0 < j + 1 < k的j，必須滿足：  

- groups[i<sub>j</sub>] != groups[i<sub>j+1</sub>]  
- words[i<sub>j</sub>]和[i<sub>j+1</sub>]**等長**，且**漢明距離**為1  

回傳一個陣列字串，**依序**由該子序列中的索引對應words中的字串而成。若有多個答案，則回傳任意一個。  

注意：words中的字串長度可能**不同**。  

## 解法

題目真的超長超囉嗦，但其實就是變化版的LIS。  
只是銜接條件不是元素遞增，而是**不同組**+**漢明距離1**。  
先寫一個函數ok(i,j)來判斷兩索引能不能銜接。  

定義dp(i)：由words[i]結尾的最長子序列。  
轉移方程式：max(dp(j) FOR ALL 0<=j<i) + words[i]  
base case：dp(i)只有一個選擇，就是words[i]。  

注意：dp保存的是**字串子序列**本身，而不是長度。更新最大值要取子序列長度。  

時間複雜度O(n^2)。  
空間複雜度O(n^2)。  

```python
class Solution:
    def getWordsInLongestSubsequence(self, n: int, words: List[str], groups: List[int]) -> List[str]:
        
        def ok(i,j):
            if groups[i]==groups[j]:
                return False
            if len(words[i])!=len(words[j]):
                return False
            return sum(c1!=c2 for c1,c2 in zip(words[i],words[j]))==1
        
        @cache
        def dp(i):
            longest=[]
            for j in range(i):
                if ok(i,j):
                    t=dp(j)
                    if len(t)>len(longest):
                        longest=t
            return longest+[words[i]]
        
        ans=[]
        for i in range(n):
            t=dp(i)
            if len(t)>len(ans):
                ans=t
                
        return ans
```
