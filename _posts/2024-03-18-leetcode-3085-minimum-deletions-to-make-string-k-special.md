---
layout      : single
title       : LeetCode 3085. Minimum Deletions to Make String K-Special
tags        : LeetCode Medium String HashTable
---
周賽 389。

## 題目

輸入字串 word 和整數 k。  

如果 word 中的所有索引都滿足 \|freq(word[i]) - freq(word[j])\| <= k，則稱為 **k 特殊**。  
freq(x) 指的是字元 x 在 word 中的出現次數，而 \|y\| 是 y 的絕對值。  

求**最少**要刪除多少個字元，才能使得 word 成為**k 特殊**。  

## 解法

刪除字元會讓出現次數下降，有兩種情況可以使得上下界絕對差變小：  

1. 出現次數**最多**的字元，各刪除一次  
2. 出現次數**最少**的字元，**全部刪除**  

如果某字元 c 是出現次數最少的字元，只刪除幾個、不全部刪乾淨的話，反而會使得絕對差變大。  

---

字串中最多只有 26 個字元，乾脆枚舉所有字元的出現次數 lo 作為下界，而上界就是 lo + k。  
對於其他字元來說，如果他們的出現次數高於 lo + k，則調整至 lo + k；若小於 lo，則調整至 0。  

時間複雜度 O(N + 26^2)。  
空間複雜度 O(26)。  

```python
class Solution:
    def minimumDeletions(self, word: str, k: int) -> int:
        d = Counter(word)
        ans = inf
        for lo in d.values():
            cnt = 0
            for v in d.values():
                if v < lo: # under lower bound, delete all
                    cnt += v
                    continue
                else: # set to upper bound 
                    cnt += max(0, v - (lo + k))
            ans = min(ans, cnt)
                
        return ans
```

逆向思維也很有趣：與其找要刪的，不如找**留著的**有多少。  
同樣枚舉下界 lo，看看在 [lo, lo + k] 區間能夠留下多少字元。  
字串長度 N 扣掉最大保留字元 mx_keep 就是要刪掉的數量。

```python
class Solution:
    def minimumDeletions(self, word: str, k: int) -> int:
        d = Counter(word)
        mx_keep = 0
        for lo in d.values():
            keep = 0
            for v in d.values():
                if v >= lo: # keep freq in [lo, lo + k]
                    keep += min(v, lo + k)
            mx_keep = max(mx_keep, keep)
                
        return len(word) - mx_keep
```
