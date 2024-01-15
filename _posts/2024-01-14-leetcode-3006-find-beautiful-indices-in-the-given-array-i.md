---
layout      : single
title       : LeetCode 3006. Find Beautiful Indices in the Given Array I
tags        : LeetCode Medium String BinarySearch
---
周賽380。這題目有點難讀，如果自己算索引會吐血，直接看範例比較快。  

## 題目

輸入陣列 s, a, b 還有整數 k。  

一個**美麗的**索引 i 滿足：  

- 0 <= i <= s.length - a.length  
- s[i..(i + a.length - 1)] == a  
- 存在索引 j 使得：  
  - 0 <= j <= s.length - b.length
  - s[j..(j + b.length - 1)] == b
  - |j - i| <= k  

回傳所有**美麗的**索引，並由小到大排序。  

## 解法

簡而言之，就是從索引 i 開頭找到等於 a 的子字串，然後又在距離 k 以內的索引 j 找到等於 b 的子字串，那就是**美麗的**。  

首先要判斷 s 中那些索引可以做為字串 a, b 的開頭，分別記做 i_indexes, j_indexes。  
直接枚舉每個索引 i 作為起點，如果找到子字串就記錄下來。需要重複相同邏輯兩次，可以封裝成函數。  

那對於合法的索引 i 來說，他要找到介於 [lo, hi] 之間的索引 j，其中 lo = i - k, hi = i + k。  
直接在合法的 j 裡面找第一個**大於等於** lo 的位置 pos。  
有可能所有 j 都小於 lo，先檢查 pos 是否超出邊界；若存在 j_indexes[pos]，再檢查是否小於 i + k。  
成功找到範圍內的 j，就把 i 加入答案。  

時間複雜度 O(MN + N log N)，其中 N = len(s)，M = max(len(a), len(b))。  
空間複雜度 O(N)。  

```python
def get_indexes(s, t):
    indexes = []
    for i in range(len(s)):
        if s[i:i+len(t)] == t:
            indexes.append(i)
    return indexes

class Solution:
    def beautifulIndices(self, s: str, a: str, b: str, k: int) -> List[int]:
        i_indexes = get_indexes(s, a)
        j_indexes = get_indexes(s, b)
                
        ans = []
        for i in i_indexes:
            lo = i-k
            hi = i+k
            j_pos = bisect_left(j_indexes, lo)
            
            if j_pos < len(j_indexes) and lo <= j_indexes[j_pos] <= hi:
                ans.append(i)
        
        return ans
```

上面方法找子字串開頭的複雜度是 O(MN)，在 Q2 的時候子字串長度最多才 10，完全沒問題。  
但是到 Q4 直接上升到 10^5，肯定要想其他方法。  

隨便找一種能夠 O(N) 匹配子字串的演算法換掉就行，例如 KMP 或是 rolling hash 之類的。  
這邊直接拿準備好的 KMP 模板貼上去就結束了。  

時間複雜度 O(N log N)。  
空間複雜度 O(N)。  

```python
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

def KMP(s, p):  
    M, N = len(s), len(p)
    pmt = prefix_function(p)
    j = 0
    res = []
    for i in range(M):
        while j > 0 and s[i] != p[j]:
            j = pmt[j-1]
        if s[i] == p[j]:
            j += 1
        if j == N:
            res.append(i - j + 1)
            j = pmt[j-1]
    return res

class Solution:
    def beautifulIndices(self, s: str, a: str, b: str, k: int) -> List[int]:
        i_indexes = KMP(s, a)
        j_indexes = KMP(s, b)
                
        ans = []
        for i in i_indexes:
            lo = i-k
            hi = i+k
            j_pos = bisect_left(j_indexes, lo)
            
            if j_pos < len(j_indexes) and lo <= j_indexes[j_pos] <= hi:
                ans.append(i)
        
        return ans
```

其實也不需要二分，這些合法開頭索引都是有序的。  
維護滑動窗口，枚舉 i 的過程中將小於 lo 的 j 移出窗口，最後檢查窗口內第一個 j 是否界於 [lo, hi] 內。  

時間複雜度 O(N)。  
空間複雜度 O(N)。  

```python
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

def KMP(s, p):  
    M, N = len(s), len(p)
    pmt = prefix_function(p)
    j = 0
    res = []
    for i in range(M):
        while j > 0 and s[i] != p[j]:
            j = pmt[j-1]
        if s[i] == p[j]:
            j += 1
        if j == N:
            res.append(i-j+1)
            j = pmt[j-1]
    return res

class Solution:
    def beautifulIndices(self, s: str, a: str, b: str, k: int) -> List[int]:
        i_indexes = KMP(s, a)
        j_indexes = KMP(s, b)
                
        ans = []
        j_pos = 0
        for i in i_indexes:
            lo = i-k
            hi = i+k
            while j_pos < len(j_indexes) and j_indexes[j_pos] < lo:
                j_pos += 1
            
            if j_pos < len(j_indexes) and lo <= j_indexes[j_pos] <= hi:
                ans.append(i)
        
        return ans
```
