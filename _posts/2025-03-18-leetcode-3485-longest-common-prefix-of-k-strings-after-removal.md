---
layout      : single
title       : LeetCode 3485. Longest Common Prefix of K Strings After Removal
tags        : LeetCode Hard String SortedList Trie Sorting String
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
並且為了對應沒有 k 共通前綴的情形，在 sorted list 內先加入一個 0 當作哨兵。  

---

最後還有一個問題。  

測資保證 sum(len(words[i])) <= 10^5。  
但在最差情況下只有一個長度 N = 10^5 的，同樣有需要枚舉 N 個子陣列，每次 O(N)。  
O(N^2) 高達 10^5，理論上是會超時的 (但不知道為啥 python 能過)。  

我們還需要優化子陣列的枚舉方式，例如**字典樹**或是 **rolling hash**，將每次枚舉的複雜度降低到 O(1)。  
此處選用 rolling hash。  

時間複雜度 O(L log L)，其中 L = sum(len(words[i]))。  
空間複雜度 O(L)。  

```python
from sortedcontainers import SortedList as SL

MOD = 10 ** 9 + 7
base = 87


class Solution:
    def longestCommonPrefix(self, words: List[str], k: int) -> List[int]:
        d = Counter()
        sl = SL([0])

        def add(w):
            ps = 0
            for i, c in enumerate(w):
                ps = (ps * base + ord(c)) % MOD
                # pre = w[:i+1]
                d[ps] += 1
                if d[ps] == k:
                    sl.add(i + 1)

        def remove(w):
            ps = 0
            for i, c in enumerate(w):
                ps = (ps * base + ord(c)) % MOD
                # pre = w[:i+1]
                if d[ps] == k:
                    sl.remove(i + 1)
                d[ps] -= 1

        for w in words:
            add(w)

        ans = []
        for w in words:
            remove(w)
            ans.append(sl[-1])
            add(w)

        return ans
```

字典樹做法。  

```python
from sortedcontainers import SortedList as SL


class Solution:
    def longestCommonPrefix(self, words: List[str], k: int) -> List[int]:
        trie = Trie(k)
        for w in words:
            trie.add(w)

        ans = []
        for w in words:
            trie.remove(w)
            ans.append(trie.sl[-1])
            trie.add(w)

        return ans


class TrieNode:
    def __init__(self) -> None:
        self.child = defaultdict(TrieNode)
        self.cnt = 0


class Trie:
    def __init__(self, k):
        self.root = TrieNode()
        self.k = k
        self.sl = SL([0])

    def add(self, w):
        curr = self.root
        for i, c in enumerate(w):
            curr = curr.child[c]
            curr.cnt += 1
            # pre = w[:i+1]
            if curr.cnt == self.k:
                self.sl.add(i + 1)

    def remove(self, w):
        curr = self.root
        for i, c in enumerate(w):
            curr = curr.child[c]
            # pre = w[:i+1]
            if curr.cnt == self.k:
                self.sl.remove(i + 1)
            curr.cnt -= 1
```

最後補充個[靈神的做法](https://leetcode.cn/problems/longest-common-prefix-of-k-strings-after-removal/solutions/3613732/pai-xu-lcp-xing-zhi-jian-ji-xie-fa-pytho-6p8e/)。  
這種方法看起來簡潔，背後思考量可不少。  
賽後自己練習，賽中趕時間可能還是用其他解法更快速。  

---

擁有**共通前綴**的字串，在根據字典序排序後都會聚集在一起。例如：  
> 有序的字串陣列 ss 內容如下：  
> ss[0] = "aa"  
> ss[1] = "aab"  
> ss[2] = "aac"  
> ss[3] = "aad"  

其中 lcp(ss[0..3]) == lcp(ss[0], ss[3]) = size。  
以反證法證明：  

- 設 lcp(ss[0..3]) > size：  
    愈多字串參與計算，lcp 只可能更小。  
    若前者大於 size，則後者也會大於 size。  
    與 lcp(ss[0], ss[3]) = size 的前提矛盾，假設不成立。  

- 設 lcp(ss[0..3]) < size：  
    ss[0] 和 ss[3] 有共通前綴 "aa"。  
    若 lcp(ss[0..3]) 小於 2，則 ss[1..2] 至少有一個前綴不為 "aa" 的字串。  
    與**已排序**的前提矛盾，假設不成立。  

因此對若干個字串求 lcp，只需將其排序，然後求**第一個**和**最後一個**字串的 lcp。

---

先不考慮刪除。  
如何在在 words 中求至少 k 個子字串的 lcp？  
將 words 排序，得到排序後的字串陣列 ss。  
枚舉所有長度 k 的子陣列 ss[i..i+k-1]，求 lcp(ss[i], ss[i+k-1])，並更新答案。  

---

再來考慮刪除一個字串的情形。  
設最長 lcp 長度為 mx，出自於子陣列 ss[mx_i..mx_i+k-1]。  
第二長的 lcp 長度 為 mx2。

分類討論刪除字串 r 的情形：  

- 若 r 不屬於 ss[mx_i..mx_i+k-1]，不影響，答案為 mx。  
- 若 r 屬於 ss[mx_i..mx_i+k-1]，則 mx 不可用，答案變為 mx2。  

舉例：  
> ss = ["aa","aa","b","cc","cc"], k = 2  
> mx = 2, mx_i = 0 ("aa")  
> mx2 = 2 ("cc")  

若刪除 r = "aa"，因 "aa" 屬於 ss[mx_i..mx_i+k-1]，區間內不足 k 個字串，故答案變成 mx2 = 2 ("cc")。  
若刪除 r = "b" 或 "cc"，兩者都不屬於 ss[mx_i..mx_i+k-1]，不影響答案，依然為 mx = 2 ("aa")。  

---

但上述範例中，mx 與 mx2 所屬子陣列沒有交集。如果兩者有交集呢？  
例如：  
> ss = ["aa","aab","ab"], k = 2  
> mx = 2, mx_i = 0 ("aa")  
> mx2 = 1 ("a")  

刪除 r = "aab"，同時屬於 mx 和 mx2 的子陣列。
mx1 與 mx2 有**交集**，代表 mx2 是 mx 的前綴 ("a" 是 "aa" 的前綴)。  
換句話說，[mx_i..mx_i-1] 中的任意字串都是 "aa" 開頭，所以隨便挑一個都滿足 mx2 的前綴 "a"。  
所以答案依然是 mx2。  

再舉另外一個例子，這次 mx 比 mx2 出現更晚：  
> ss = ["a","ab","abc"], k = 2  
> mx = 2, mx_i = 1 ("ab")  
> mx2 = 1 ("a")  

刪除 r = "ab"，同時屬於 mx 和 mx2 的子陣列。  
兩者有交集，故 mx2 是 mx 的前綴 ("a" 是 "ab" 的前綴)。  
刪除 "ab" 後，依然可以由 "abc" 與 "a" 滿足 mx2。  
答案是 mx2。  

---

按照此方法找出 mx, mx_i 以及 mx2。  
屬於 ss[mx_i..mx_i+k-1] 中的索引字串答案為 mx2；否則為 mx。  
之後遍歷 words 查表即可。  

時間複雜度 O(N log N)。  
空間複雜度 O(N)。  

```python
def lcp(s, t):
    if len(s) > len(t):
        s, t = t, s
    for i, c in enumerate(s):
        if c != t[i]:
            return i
    return len(s)


class Solution:
    def longestCommonPrefix(self, words: List[str], k: int) -> List[int]:
        N = len(words)

        if N-1 < k:
            return [0] * N

        ss = sorted(words)
        mx = mx2 = -1
        mx_i = -1
        for i in range(N-k+1):
            sz = lcp(ss[i], ss[i+k-1])
            if sz > mx:
                mx2 = mx
                mx, mx_i = sz, i
            elif sz > mx2:
                mx2 = sz
                
        mp = {}
        for i, w in enumerate(ss):
            if mx_i <= i <= mx_i + k-1:
                mp[w] = mx2
            else:
                mp[w] = mx

        return [mp[w] for w in words]
```
