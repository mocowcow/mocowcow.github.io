---
layout      : single
title       : LeetCode 2957. Remove Adjacent Almost-Equal Characters
tags        : LeetCode Medium String Greedy
---
雙周賽119。這題感覺有詐，不太敢直接交答案。  

## 題目

輸入陣列word。  

每次操作，你可以選擇任意一個索引i，並將word[i]變成任意小寫字母。

對於兩個字元a和b，滿足a == b，或者a和b在字母順序中相鄰，則稱為**幾乎相等**。  

求**最少**需要幾次操作，才能移除所有相鄰的**幾乎相等**字元。  

## 解法

**幾乎相等**，以下簡稱**相等**。  

考慮三個連續相等的字元aaa，如果修改第一或第三個字元，則需要修改兩次；若修改中間那個，則只需要一次。  
對於四個連續相等的字元aaaa，如果修改了第二個變成"a_aa"，第三四個字元還是會相等。得到規模較小的子問題，根據剛才的結論修改第四個字元。  

簡單來說，如果存在兩個相等的索引i,j，修改j可以保證i和j不相等，同時也可以保證j和j+1不相等(如果有的話)。  
所以修改完j，可以直接跳到j+2，接著判斷j+1和j+2是否相等。  

時間複雜度O(N)。  
空間複雜度O(1)。  

```python
class Solution:
    def removeAlmostEqualCharacters(self, word: str) -> int:
        N=len(word)
        
        ans=0
        i=1
        while i<N:
            if abs(ord(word[i-1])-ord(word[i]))<=1:
                ans+=1
                i+=2
            else:
                i+=1
        
        return ans
```
