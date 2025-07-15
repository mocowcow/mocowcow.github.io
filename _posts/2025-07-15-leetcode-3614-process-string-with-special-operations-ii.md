---
layout      : single
title       : LeetCode 3614. Process String with Special Operations II
tags        : LeetCode Hard Simulation
---
weekly contest 458。  

## 題目

<https://leetcode.com/problems/process-string-with-special-operations-ii/description/>

## 解法

最終字串長度高達 10^15，真要照著做肯定不行。  
但算算長度還是沒問題的，可以先排除 k 太大的情形。  

---

正難則反，試著從最終的長度反推出第 k 個是誰。  

先考慮最特殊的情況：只有字元。  
例如：  
> s = "abc", k = 1

很明顯答案是中間的 "b"。  
倒著操作：  
> s[2] 後，長度 sz = 3，不是答案  
> s[1] 後，長度 sz = 2，這個 "b" 是答案  

在後方**加入新字元**後，若新字元的索引正好是 k，代表他就是答案。  

不過有個小插曲，倒著處理操作的長度怎麼算？  
倒推的碰到 "\*" 的時候並不知道有沒有刪到東西，不太好處理。  

其實在最初計算階段的順便記錄下來就好，省事很多。  
也因此我們倒推時可以忽略 "\*"，因為長度已經計算好了，而且不可能影響答案。  

---

接下來看複製的 "#" 怎麼倒推？  
複製後的長度肯定是偶數，左半邊是原內容，右半邊是複製品。  
如果 k 位於左半邊，那沒有影響；如果 k 在右半邊，則直接刪除一半的長度，正好可以對應到左半的位置。  

---

最後剩下 "%" 號，反轉字串很麻煩。  

路不轉人轉；字串不轉 k 轉。  
在長度為 sz 的字串中，原本從左向右數第 k 個位置，翻轉後會變成第 sz-1-k 個位置。  
直接把 k 變成翻轉後的位置就好。  

時間複雜度 O(N)。  
空間複雜度 O(N)。  

```python
class Solution:
    def processStr(self, s: str, k: int) -> str:
        N = len(s)
        sz = 0
        sizes = [0] * N
        for i, c in enumerate(s):
            if c == "*":
                if sz:
                    sz -= 1
            elif c == "#":
                sz *= 2
            elif c == "%":
                pass
            else:
                sz += 1
            sizes[i] = sz

        if k >= sz:
            return "."

        for i in reversed(range(N)):
            c = s[i]
            sz = sizes[i]
            if c == "*":
                continue
            elif c == "#":
                # k 在右半邊
                if k >= sz // 2:
                    k -= sz // 2
            elif c == "%":
                # 對稱反轉
                k = sz-1-k
            elif k == sz-1:
                return c
```
