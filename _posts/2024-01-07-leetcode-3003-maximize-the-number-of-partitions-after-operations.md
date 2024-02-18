---
layout      : single
title       : LeetCode 3003. Maximize the Number of Partitions After Operations
tags        : LeetCode Hard String DP BitManipulation Bitmask
---
周賽379。又一次根本不知道怎麼做的題，最近 Q4 難度真是越來越誇張。  

## 題目

輸入字串 s，以及整數 k。  

你必須執行以下分割操作，直到 s 變成**空字串**為止：  

- 找到 s 的**最長前綴**，且前綴中最多擁有 k 種**不同**字元  
- 從 s 中**刪除**此前綴，並將分割計數加 1。若有剩餘的字元則維持原本的順序  

在執行操作之前，你可以將 s 中的任一字元修改成其他字元，**最多**一次。  

求最多一次修改的情況下，能夠得到的**最大**分割次數。  

## 解法

看了滿多篇題解，最後選了個最簡單的作法，其他都太過複雜。  

一眼看來，根本不知道要修改哪裡好，乾脆試著搞 dp，枚舉**所有索引**的所有修改結果。  
而且最多只能修改一次，枚舉 N 個修改點、各 26 種修改結果，目前為止是 O(N \* 26)。  

---

接下來要處理前綴中不同字元，使用 bitmask 來記錄出現過的字元。  
乍看之下有 2^26 種 mask。但前綴是**連續**的，一直到出現超過 k 種字元才會進行分割。  
因此在不進行任何改變的情況下，每個索引只會對應到一種 mask。  
這時候可以枚舉 s[i] 修改成 26 種字元的情形。  

那如果索引 i 的前方某個字元修改過，就可能使得 i 所屬的前綴的字元改變。  
可能會少掉 26 種原本擁有的字元之一，然後出現另外 25 種之一，大約是 26^2 種組合。也就是說，修改過的情況下，索引 i 最多會對應到 26^2 種 mask。  
但最多只能修改一次，修改過的後只能按照規則延長前綴或是分割，因此轉移的來源狀態會只有一種。  

---

比起分析時間複雜度，實作的部分相對簡單。  

定義 dp(i,mask,changed)：當前前綴延伸到 i，包含的字元以 mask 表示，且修改紀錄為 changed。  
從 i 之後的部分所能提供的最大分割數。  
轉移：

- 不修改 s[i]：  
  - 加入 s[i] 後超過 k 個字元，只能以 s[i] 做新的前綴起點。轉移 dp(i+1, mask(s[i]), changed)  
  - 否則直接加入 s[i]，轉移 dp(i+1, mask(s[i]) \| mask, changed)  

- 若可以修改，則枚舉修改的目標字元 char：  
  - 加入 char 後超過 k 個字元，只能以 s[i] 做新的前綴起點。轉移 dp(i+1, mask(char), true)  
  - 否則直接加入 char，轉移 dp(i+1, mask(char) \| mask, true)  

從以上的可用狀態中取最大者就是答案。  

邊界：當 i = N 時，字串分割完畢，只有 1 種答案。  

---

dp(i, mask, False) 共有 N 種狀態，每個狀態轉移 26 次，共 O(N \* 26)。  
dp(i, mask, True) 共有 N \* 26^2 種狀態，每個狀態轉移 1 次，共 O(N \* 26^2)。  

時間複雜度 O(N \* 26^2)。  
空間複雜度 O(N \* 26^2)。  

```python
class Solution:
    def maxPartitionsAfterOperations(self, s: str, k: int) -> int:
        N = len(s)
        
        @cache
        def dp(i,mask,changed):
            if i == N:
                return 1
            
            c = ord(s[i]) - 97
            char_mask = 1 << c
            new_mask = mask | char_mask
            if new_mask.bit_count() > k: # over k chars, must split
                res = dp(i + 1, char_mask, changed) + 1
            else: # no split
                res = dp(i + 1, new_mask, changed)
                
            if not changed: # can chande s[i]
                for c in range(26): # enumerate 26 chars change to
                    char_mask = 1 << c
                    new_mask = mask | char_mask
                    if new_mask.bit_count() > k: # over k chars, must split
                        res = max(res, dp(i + 1, char_mask, True) + 1)
                    else: # no split
                        res = max(res, dp(i + 1, new_mask, True))
            return res
        
        return dp(0, 0, False)
```
