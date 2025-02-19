---
layout      : single
title       : LeetCode 3455. Shortest Matching Substring
tags        : LeetCode Hard String BinarySearch
---
biweekly contest 150。  
好消息，我比賽時寫出了 O(N) 的滑窗解法。  
壞消息，過的時候晚了 2 分鐘。  

下次還是寫簡單的好。  

## 題目

<https://leetcode.com/problems/shortest-matching-substring/description/>

## 解法

以 "*" 號把 p 分割成三個模式串，找到 p1, p2, p3 在 s 中的所有出現位置。  
為了快速匹配字串，此處選 kmp。  

---

枚舉中間 p2 的所有出現索引 i2，然後用二分搜在左右兩邊找 p1 和 p2 的索引。  
p1 越靠右越好，最多 i2 - len(p1)，找最後一個小於等於的。  
p3 越靠左越好，最小 i2 + len(p2)，找第一個大於等於的。  

如果兩個都有找到，則整個子字串的左端點就是 p1 的起點 i1；右端點是 p3 的結尾 j3 = i3 + len(p3) - 1。  

---

最麻煩的是模式串可能為空。  
我當時是寫一堆特判處理所有情形，但是很多大神都用上巧妙的方式解決：  
> 模式串為空，直接認定**每個索引都匹配成功**。  

這樣就可以當作一般情況處理了。  

注意以下測資：  
> s = "aa",  p = "aa**"  
> 答案 i1 = 0  
> i2 = i3 = 2  
> 長度 = 2  

所以在模式串為空時，要回傳的是 N+1 個索引，而非只有 N 個。  

時間複雜度 O(N log N)。  
空間複雜度 O(N)。  

```python
class Solution:
    def shortestMatchingSubstring(self, s: str, p: str) -> int:
        p1, p2, p3 = p.split("*")
        a1, a2, a3 = KMP_all(s, p1), KMP_all(s, p2), KMP_all(s, p3)

        ans = inf
        for i2 in a2:
            lim1 = i2 - len(p1)
            lim3 = i2 + len(p2)

            idx1 = bisect_right(a1, lim1) - 1
            idx3 = bisect_left(a3, lim3)

            if idx1 >= 0 and idx1 < len(a1):
                if idx3 < len(a3):
                    i1 = a1[idx1]
                    j3 = a3[idx3] + len(p3)
                    ans = min(ans, j3 - i1)

        if ans == inf:
            return -1

        return ans


# PMT optimized version
def prefix_function(s):
    N = len(s)
    pmt = [0]*N
    for i in range(1, N):
        j = pmt[i - 1]
        while j > 0 and s[i] != s[j]:
            j = pmt[j - 1]
        if s[i] == s[j]:
            j += 1
        pmt[i] = j
    return pmt


# search p in s, return every starting idnex of p
def KMP_all(s, p):
    if p == "":
        return list(range(len(s)+1))
    M, N = len(s), len(p)
    pmt = prefix_function(p)
    j = 0
    res = []
    for i in range(M):
        while j > 0 and s[i] != p[j]:
            j = pmt[j - 1]
        if s[i] == p[j]:
            j += 1
        if j == N:
            res.append(i - j + 1)
            j = pmt[j - 1]
    return res
```
