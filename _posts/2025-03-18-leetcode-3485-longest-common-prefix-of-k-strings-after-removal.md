---
layout      : single
title       : LeetCode 3485. Longest Common Prefix of K Strings After Removal
tags        : LeetCode Hard String SortedList
---
biweekly contest 152。

## 題目

<https://leetcode.com/problems/longest-common-prefix-of-k-strings-after-removal/description/>

## 解法

先考慮不刪除 words[i] 的做法。  

我們會枚舉每個 w 的前綴 pre，並且統計 pre 的出現次數。  
只要 pre 出現滿足 k 次，那麼 len(pre) 就是答案的候選之一。  
最後找出候選長度中的最大值。  

---

再來考慮刪除 words[i]。  

先枚舉要刪除的 words[i]，刪除其所有前綴後，再找候選中的最大值。  
但 w 的 pre 刪除後，出現次數可能會低於 k 次，這時必須從答案候選中**刪除**。  

維護答案候選長度的資料結構需要有效率的**新增**、**刪除**，還有求**最大值**。  
故選用 sorted list。  

---

最後還有一個問題。  

測資保證 sum(len(words[i])) <= 10^5。  
但在最差情況下只有一個長度 N = 10^5 的，同樣有需要枚舉 N 個子陣列，每次 O(N)。  
O(N^2) 高達 10^5，理論上是會超時的 (但不知道為啥 python 能過)。  

我們還需要優化子陣列的枚舉方式，例如**字典樹**或是 **rolling hash**，將每次枚舉的複雜度降低到 O(1)。  
此處選用 rolling hash。  

時間複雜度 O()。  
空間複雜度 O()。  

```python
MOD = 10 ** 9 + 7
base = 87


class Solution:
    def longestCommonPrefix(self, words: List[str], k: int) -> List[int]:
        d = Counter()
        sl = SL()
        sl.add(0)

        def add(w):
            ps = 0
            for i, c in enumerate(w):
                ps = (ps * base + ord(c)) % MOD
                # ps = w[:i+1]
                d[ps] += 1
                if d[ps] == k:
                    sl.add(i + 1)

        def remove(w):
            ps = 0
            for i, c in enumerate(w):
                ps = (ps * base + ord(c)) % MOD
                # ps = w[:i+1]
                if d[ps] == k:
                    sl.remove(i + 1)
                d[ps] -= 1

        for w in words:
            add(w)

        ans = []
        for i, w in enumerate(words):
            remove(w)
            ans.append(sl[-1])
            add(w)

        return ans
```
