---
layout      : single
title       : LeetCode 3081. Replace Question Marks in String to Minimize Its Value
tags        : LeetCode Medium String Array Greedy HashTable Sorting
---
雙周賽 126。不得不說，這題沒有設置隱藏測資真的是佛心來著，不然通過人數肯定剩一半。  

## 題目

輸入由小寫字母或 '?' 組成的字串 s。  

對於一個只由小寫字母組成、長度為 m 的字串 t，定義函數 cost(i) 代表在 [0, i - 1] 的區間內，有多少個字元**等於** t[i]。  
也就是 t[i] 在 t[0..(i - 1)] 的出現次數。  

t 的價值等於所有索引 i 的 cost(i) 總和。  

例如 t = "aab"：  

- cost(0) = 0
- cost(1) = 1
- cost(2) = 0
- 因此 "aab" 的價值為 0 + 1 + 0 = 1  

你必須將**所有** '?' **替換**成任意小寫字母，並使得**價值最小化**。  

回傳替換所有 '?' 後的字串。如果有多個答案，則回傳字典序最小者。  

## 解法

同一個字元出現越多次，之後的 cost(i) 會產生更大的價值。  
而且字典順序要盡可能小，因此填 '?' 的時候，優先選填出現次數最少、且順序最小的字元。  

首先遍歷一次 s，計算個字元的出現次數。  
再對每個 '?' 分別找出 26 字母中的最佳字元填入。  

然後提交答案，就錯了。  

---

試想以下例子：  
> "abcdefghijklmnopqrstuvwxy??"  

a\~y 各出現一次，後面跟著兩個問號。  
如果照著剛才的找法，會填入 "za"，但正確答案是 "az"。  
發現找到的東西是對的，但是填入順序不對。  

為避免這種情況，需要把填入的字元先排序一次，再填入就行。  

時間複雜度 O(N log N)。  
空間複雜度 O(N)。  

```python
class Solution:
    def minimizeStringValue(self, s: str) -> str:
        d = Counter(s)
        use = []
        for _ in range(d["?"]):
            cand = "a"
            for c in ascii_lowercase:
                if d[c] < d[cand]:
                    cand = c
            d[cand] += 1
            use.append(cand)
        
        use.sort(reverse=True)
        a = list(s)
        for i, c in enumerate(a):
            if c == "?":
                a[i] = use.pop()
                
        return "".join(a)
```
