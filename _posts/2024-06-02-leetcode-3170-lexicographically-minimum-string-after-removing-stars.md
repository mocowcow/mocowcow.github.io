---
layout      : single
title       : LeetCode 3170. Lexicographically Minimum String After Removing Stars
tags        : LeetCode Medium String Heap Simulation Stack
---
周賽 400。

## 題目

輸入字串 s。其中可能包含數個 '\*' 字元。你必須將所有 '\*' 號移除。  

若字串中存在 '\*'，執行以下操作：  

- 刪除**最左**的 '\*'，以及其左方**最小**非的 '\*' 字元。  
    若存在多個最小字元，可以刪除任意一個。  

求刪除所有 '\*' 後，滿足**最小字典序**的字串結果。  

## 解法

直接舉幾個例子，看看怎樣刪最划算。先從最簡單的來：  
> s = "aaa\*"  

刪哪個都一樣。繼續看其他例子：  

> s = "aba\*"  
> 刪第一個 a，會變成 "ba"  
> 刪第二個 a，會變成 "ab"  
> s = "baa\*"  
> 刪哪個都一樣  
> s = "aab\*"  
> 刪哪個都一樣  

因為刪除的是最小的字元 c，其補位的字元肯定是**大於等於** c。若右方存在較大的字元，會使字典序變大。  
而字典順序是由左向右比較，因此刪除靠右的 c，更有可能避免字典序變大。  

---

維護左方剩餘的字元，並按照字典序、索引位置排序。  
這裡使用 min heap，先以字典序遞增排序、再以索引遞減排序。  

遍歷 s 中的每個字元 c，如果是 '\*' 則找出左方字典序最小、且索引最大的字元，並將其標記為刪除；  
否則將 c 及其索引加入 heap 中。  

時間複雜度 O(N log N)。  
空間複雜度 O(N)。  

```python
class Solution:
    def clearStars(self, s: str) -> str:
        a = list(s)
        h = [] # min char, max idx
        
        for i, c in enumerate(s):
            if c == "*":
                _, j = heappop(h)
                a[-j] = ""
                a[i] = ""
            else:
                heappush(h, [c, -i])
                
        return "".join(a)
```

其實只有 26 種字元，每次要刪除時，直接從最小的 "a" 遍歷到 "z"，先找到誰就刪誰。  
刪除要找最大的索引，是一種**後進先出**的規則，正好就是 stack。  

時間複雜度 O(N)。  
空間複雜度 O(N)。  

```python
class Solution:
    def clearStars(self, s: str) -> str:
        a = list(s)
        st = [[] for _ in range(26)]
        
        for i, c in enumerate(s):
            if c == "*":
                a[i] = ""
                for x in range(26):
                    if st[x]:
                        j = st[x].pop()
                        a[j] = ""
                        break
            else:
                st[ord(c) - 97].append(i)
                
        return "".join(a)
```
