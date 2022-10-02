--- 
layout      : single
title       : LeetCode 2423. Remove Letter To Equalize Frequency
tags        : LeetCode Easy String HashTable Simulation
---
雙周賽88。非常變態的題目，幾乎每個人都會吃到BUG，我非常尊敬那些一次通過的神人。  

# 題目
輸入由小寫英文字母組成的字串word。你必須刪除某一索引上的字母，使得所有字母的出現頻率相同。  
如果刪除某一個字母後可以使word中所有字母的出現頻率相等，則回傳true，否則回傳false。  

注意：  
- 出現頻率指的是其在word中的出現次數  
- 你一定要刪除一個字母，不可不刪除  

# 解法
如果用公式解會卡到很多很多很多edge cases，而測資本身不大，透過模擬來找到刪除的字母會是比較好的選擇。  
先計算每個字母出現頻率，列舉word中每個字元c，先刪掉一個c，若剩下的頻率完全相同則回傳true；否則把c加回去，嘗試下一個位置。  

時間複雜度O(N\*26)，空間複雜度O(26)。  

```python
class Solution:
    def equalFrequency(self, word: str) -> bool:
        d=Counter(word)
        
        for c in word:
            d[c]-=1
            ks=set()
            for x in ascii_lowercase:
                if d[x]:
                    ks.add(d[x])
            if len(ks)==1:
                return True
            d[c]+=1
            
        return False
```
