---
layout      : single
title       : LeetCode 3234. Count the Number of Substrings With Dominant Ones
tags        : LeetCode Medium
---
weekly contest 408。  
想了幾天才找到滿意的做法，以前似乎沒碰過這種題型，不得不說是真的難想。  
這題真的奇妙，不需要什麼特殊資料結構或是演算法，考察重點應該是觀察力，還有細節實作的細心程度。  

## 題目

輸入二進位字串 s。  

求有多少子字串是 **1 顯著**的。  

若一個字串中 1 的數量大於等於 0 的數量的**平方**，則稱為 **1 顯著**。  

## 解法

以下稱字串中 1 和 0 的數量為 cnt1 和 cnt2，並稱 **1 顯著** 為**合法**。  
子字串合法條件為：  
> cnt1 >= cnt0^2  

---

本來看到子字串問題就想要滑動窗口，但因為這個關係式比較難搞，合法的子字串不會連續出現。  
例如：  
> s = "010111"  
> 0 不合法  
> 01 合法  
> 010 不合法  
> 0101, 01011 還是不合法  
> 010111 突然又合法  

若在 010 不合法時縮減窗口左端點，之後就算不到 010111，所以**滑窗是錯的**。  

---

```python
class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        N = len(s)
        MX = isqrt(N)
        q = deque(i for i, c in enumerate(s) if c == "0")
        q.append(N) # sentinel
        ans = 0
        for i, c in enumerate(s):
            # substring s[i..j] only have "1"s
            if c == "1": 
                j = q[0] - 1
                ans += j - i + 1
            
            # substring s[i..j] have at least one "0"
            for zidx in range(len(q) - 1):
                j = q[zidx]
                # s[j+1..k] might have "1"s if required
                k = q[zidx + 1] - 1
                cnt0 = zidx + 1
                sz = j - i + 1
                cnt1 = sz - cnt0

                # at most MX 0s
                if cnt0 > MX:
                    break

                # case1: cnt1 >= cnt0^2
                # right bound can be [j..k]
                if cnt1 >= cnt0**2:
                    ans += k - j + 1
                
                # case2: cnt < cnt0^2
                # we need extra "1"s to make it dominant
                # right bound can be [j+extra..k]
                # cnt1 + extra >= cnt0^2
                # extra >= cnt0^2 - cnt
                else:
                    extra = cnt0**2 - cnt1
                    # ans += max(0, k - (j + extra) + 1)
                    res = k - (j + extra) + 1
                    if res > 0:
                        ans += res

            # discard expired "0"
            if c == "0":
                q.popleft()

        return ans
```
