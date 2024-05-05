---
layout      : single
title       : LeetCode 3138. Minimum Length of Anagram Concatenation
tags        : LeetCode Medium String Simulation Sorting
---
周賽 396。又是超級爛的題目描述，不管 LCUS 原文或是 LCCN 的翻譯都很爛，不知道在搞什麼。  
描述偷改過了，原本好像是講：  
> typically using all the original letters exactly once  

結果一堆人用 GCD 去做 (包括我)。  
而已近 600 個測資都沒有攔截到，某方面來講也是很厲害，明明簡單的 "aabb" 就可以擋下。  

中文翻譯也很厲害：  
> 给你一个字符串 s ，它由某个字符串 t 和**它**的 同位字符串 连接而成  

真是夢回當年國文課，猜第二個**它**是指誰？  

## 題目

輸入字串 s，且 s 是由 t 的**易位構詞**依序連接而成。  

求字串 t 可能的**最小長度**。  

**易位構詞**是將一個字串的字元重新排列而成。例如："aab" 的易位構詞有 "aab", "aba" 和 "baa"。  

## 解法

其實跟上一題有點相似，只是要找到某個長度為 size 的字串 t，且每個長度為 t 的子字串都是**易位構詞**。  

判斷易位構詞方法很多。  
對於 python 來說，最快的方式就是把兩個字串排序、或是丟到字典裡比對。  
冷知識：排序複雜度高，但執行起來反而快。  

題目要找最小值，因此從 1 開始枚舉 size，若每個大小為 size 的子字串都滿足易位構詞，則回傳 size。  

---

每次枚舉一個長度 size，需要遍歷字串一次，是 O(N)。  
只有在 size 能夠整除 s 的情況下才有可能是答案。而 size 最多只會有 sqrt(size) \* 2 個因數。  

時間複雜度 O(sqrt(N) \* N)。  
空間複雜度 O(1)。  

```python
class Solution:
    def minAnagramLength(self, s: str) -> int:
        N = len(s)
        
        for size in range(1, N):
            if N % size != 0:
                continue
            target = Counter(s[:size])
            for i in range(0, N, size):
                if target != Counter(s[i:i + size]):
                    break
            else:
                return size
            
        return N
```
