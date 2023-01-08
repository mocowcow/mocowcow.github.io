--- 
layout      : single
title       : LeetCode 2531. Make Number of Distinct Characters Equal
tags        : LeetCode Medium String HashTable
---
周賽327。這題通過率3441/23732，有點可怕。  

# 題目
輸入兩個字串word1和word2。  

一次**移動**指的是選擇兩個索引i和j，其中0 <= i < word1.length and 0 <= j < word2.length。然後將word1[i]和word2[j]交換。  

如果可以透過**正好一次移動**使得word1和word2中的**不同的字元**數量相同，則回傳true；否則回傳false。  

# 解法
如果一個字串word="abcc"，選擇哪個c來交換都是一樣的，所以可以窮舉兩字串中出現過的字元種類。  

word1選擇字元k1，word2選擇字元k2，進行分類討論：  
1. 若k1等於k2，交換後，雙方的出現頻率不會改變，獨特的字元數保持不變  
2. 否則根據k1和k2的出現頻率，來對字元數調整  

設原本的word1共有cnt1種字元，而word2有cnt2種字元：    
- 如果k1只出現一次，則交換後使得d1減少一種字元  
- 如果k2只出現一次，則交換後使得d2減少一種字元  
- 如果d1中不存在k2，則交換後d1會增加一種字元  
- 如果d2中不存在k1，則交換後d2會增加一種字元  

調整後，若字元種類相同，則直接回傳true；所有組合都不同的話，最後回傳false。  

時間複雜度O(N + M + 26 \* 26)，可以視為O(N + M)。空間複雜度O(26)，可以視為O(1)。

```python
class Solution:
    def isItPossible(self, word1: str, word2: str) -> bool:
        d1=Counter(word1)
        d2=Counter(word2)
        
        for k1 in d1.keys():
            for k2 in d2.keys():
                cnt1=len(d1)
                cnt2=len(d2)
                if k1!=k2:
                    if d1[k1]==1: # d1 lose a key
                        cnt1-=1
                    if d2[k1]==0: # d2 get a new key
                        cnt2+=1
                    if d2[k2]==1: # d2 lose a key
                        cnt2-=1
                    if d1[k2]==0: # d1 get a new key
                        cnt1+=1
                        
                if cnt1==cnt2:return True

        return False
```
