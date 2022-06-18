--- 
layout      : single
title       : LeetCode 745. Prefix and Suffix Search
tags        : LeetCode Hard String Design Hashtable 
---
每日題。好像是想考字典樹吧，結果被我偷雞偷過了。字典樹的解法很多種，但沒一種我覺得容易理解的。

# 題目
設計包含一些單詞的特殊字典，可以依特定前綴和後綴搜尋符合的單字。  

實作WordFilter類別：  
- WordFilter(string[] words)：以words建立字典。  
- f(string prefix, string suffix)：在words中到前綴為prefix且後綴為suffix的單字。若有多個，則回傳索引最大者；若不存在則回傳-1。  
   
# 解法
每個word長度最多才10，最多15000個word，最多15000次查詢，總覺得測資不大，應該不需要太多技巧。  

建構子很簡單，維護雜湊表pref及suff，以前、後綴為鍵值保存對應到的單字索引位置。  
遍歷words中所有所有單字w，枚舉其產生的所有前、後綴，分別加入pref及suff中。  
查詢函數f只要拿前、後綴到pref和suff中取得對應的集合，做AND運算後回傳最大索引即可；若無交集則回傳-1。  

但我還真沒想到竟然會TLE，只好對查詢函數做快取，才能順利通過。  

```python
class WordFilter:

    def __init__(self, words: List[str]):
        self.pref=defaultdict(set)      
        self.suff=defaultdict(set)        
        for i,w in enumerate(words):
            for size in range(len(w)+1):
                self.pref[w[:size]].add(i)
                self.suff[w[size:]].add(i)
                
    @cache           
    def f(self, prefix: str, suffix: str) -> int:
        union=self.pref[prefix]&self.suff[suffix]
        if union:
            return max(union)
        return -1
```

另外看見一種更聰明的方法，在建構子的時候每個單字w所可能產生的前、後綴組合，並以不可能出現的符號作為分隔符號，紀錄對應的索引，時間複雜度為O(N*k^2)，這裡N指的是words長度，k為words[i]長度。  
而查詢函數f只需要將查詢的前、後綴串接，回到雜湊表裡面取值，複雜度為O(1)。  

```python
class WordFilter:

    def __init__(self, words: List[str]):
        self.d={}
        for i,w in enumerate(words):
            for j in range(len(w)+1):
                for k in range(len(w)+1):
                    pat=w[:j]+'#'+w[k:]
                    self.d[pat]=i
                
    def f(self, prefix: str, suffix: str) -> int:
        pat=prefix+'#'+suffix
        if pat in self.d:
            return self.d[pat]
        return -1
```