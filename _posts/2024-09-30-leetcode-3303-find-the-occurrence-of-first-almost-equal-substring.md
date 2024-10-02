---
layout      : single
title       : LeetCode 3303. Find the Occurrence of First Almost Equal Substring
tags        : LeetCode Hard String
---
biweekly contest 140。  
我搞了半天的 rolling hash 竟然被卡常數，真搞不懂時間限制的標準。  

## 題目

輸入兩個字串 s 和 pattern。  

若一個字串 x 在修改**至多一個**字元後等同於字串 y，則稱 x 和 y **幾乎相等**。  

回傳**最小**的 s 的子字串起始索引，其子字串與 pattern **幾乎相等**。  
若不存在則回傳 -1。  

## 解法

修改 pattern **至多一個**字元，可能的結果有 pattern 本身，或是任意 pattern[i] 修改成任意字母。  
總共 26 \* N = 2e6 種可能。  

透過 rolling hash 將所有可能的子字串加入集合中，最後再枚舉 s 中的子字串，第一個找到的就是答案。  
可惜會超時，只能想想別的辦法。  

---

Q3 的時候是求**子序列**，我們利用了**前後綴分解**的技巧找到分割點，使得左右兩邊的匹配長度至少等於 N-1。  
雖然本題 Q4 是求**子字串**，但同樣也適用**前後綴分解**的思維。  

設一個子字串 sub = s[i..j] 幾乎相等於 pattern。  
那麼兩者肯定具有**公用前綴** pref = sub[i..] 還有**公共後綴** suff = sub[..j]，並有 len(pref) + len(suff) >= N-1。  

---

問題轉換成：找 sub 和 pattern 的**公共前綴**與**公共後綴**。  
以前周賽中也碰過不少次，正是 z-function。  

但是原始的 z-function 是在字串 s 本身找子字串 s[i..] 的**最長公共前綴**。  
此處是要在 s 裡找 pattern，所以需要將兩者串接為 pattern + "#" +s。  
其中 "#" 號是只是分隔習慣，不加也可以。  

至於後綴，只需把 s 和 pattern 都反轉後，另外套一次 z-function 即可。  
注意：z[i] 指的是 text = pattern + "#" + s，取 z[i] 值記得加上 len(pattern) + 1 的偏移量。  
注意：z[i] 是從左向右數，所以後綴 z-array 的索引也要反轉，然後再加上偏移量。  

時間複雜度 O(N)。  
空間複雜度 O(N)。  

```python
class Solution:
    def minStartingIndex(self, s: str, pattern: str) -> int:
        M, N = len(s), len(pattern)
        pre_z = z_function(pattern + "#" + s)
        suf_z = z_function(pattern[::-1] + "#" + s[::-1])

        # check substring s[i..j]
        # where pre[i] + suf[j] >= N-1
        for i in range(M - N + 1):
            j = i + N - 1
            rev_j = M - 1 - j  # reverse j
            pre_i = i + N + 1  # offset len(pattern + "#")
            suf_j = rev_j + N + 1  # offset len(pattern + "#")
            if pre_z[pre_i] + suf_z[suf_j] >= N - 1:
                return i

        return -1


def z_function(s):
    N = len(s)
    z = [0]*N
    L = R = 0
    for i in range(1, N):
        if R < i:  # not covered by previous z-box
            # z[i] = 0
            pass
        else:  # partially or fully covered
            j = i-L
            if j+z[j] < z[L]:  # fully covered
                z[i] = z[j]
            else:
                z[i] = R-i+1

        while i+z[i] < N and s[i+z[i]] == s[z[i]]:  # remaining substring
            z[i] += 1
        if i+z[i]-1 > R:  # R out of prev z-box, update R
            L = i
            R = i+z[i]-1
    return z
```
