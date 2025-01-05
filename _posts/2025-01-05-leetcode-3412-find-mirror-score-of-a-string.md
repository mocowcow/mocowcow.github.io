---
layout      : single
title       : LeetCode 3412. Find Mirror Score of a String
tags        : LeetCode Medium Stack
---
weekly contest 431。  

## 題目

輸入字串 s。  

英文字母的**鏡像**定義為反轉字母表後對應的字母。  
例如：'a' 的鏡像是 'z'，'y' 的鏡像是 'b'。  

最初 s 中所有字元都是未標記的。  
你的起始分數為 0，執行以下操作：  

- 從左到右遍歷 s。  
- 對於每個索引 i，找到**最接近**的**未標記**索引 j，且滿足 j < i，且 s[j] 是 s[i] 的鏡像。  
    標記索引 i, j，然後將 i - j 加入分數。  
- 若對於 i 不存在滿足條件的索引 j，則什麼都不做。  

求操作結束後的分數。  

## 解法

字母表中有 26 個字母。  
若以 [0, 25] 表示，則 x 對應的鏡像為 y = 25-x。  

---

對於 x 來說，若有多個滿足 s[j] = y 的 j，最靠近的肯定是最後碰到的。  
鏡像是**後進先出**，所以用**堆疊**，每種鏡像各一個。  

時間複雜度 O(N)。  
空間複雜度 O(N)。  

```python
class Solution:
    def calculateScore(self, s: str) -> int:
        a = [ord(c)-97 for c in s]
        st = [deque() for _ in range(26)]
        ans = 0

        for i, x in enumerate(a):
            y = 25-x
            if st[y]:
                j = st[y].pop()
                ans += i-j
            else:
                st[x].append(i)

        return ans
```
