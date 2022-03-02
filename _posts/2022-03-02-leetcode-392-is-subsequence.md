---
layout      : single
title       : LeetCode 392. Is Subsequence
tags 		: LeetCode Easy String TwoPointers BinarySearch
---
每日題。今天才注意這題有follow up。

# 題目
輸入字串s和t，檢查s是不是t的子序列。

# 解法
使用雙指標，i紀錄s字串的位置，j紀錄t字串的位置。  
每次將j+1，若s[i]=t[j]則表示配對成功，則也i+1。最後若i=s長度則代表整個子序列配對成功。  
時間複雜度O(M+N)。

```python
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        M = len(s)
        N = len(t)
        i = j = 0
        while i < M and j < N:
            if s[i] == t[j]:
                i += 1
            j += 1
        return M == i
```

利用python內建的疊代器解法。  
建立t的疊代器it，對目標字串s中每個字元c檢查是否在it中，若全部都找到就代表是子序列。  
因為內建的in語法會一直疊代查找目標直到找到為止，每次都會對it使用next()函數，所以每個字元最多使用一次。

```python
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        it = iter(t)
        return all(c in it for c in s)
```

follow up說如果字串s的長度k<=10^9怎麼辦，有沒有辦法加速？使用二分搜。  
維護雜湊表d，先遍歷來源字串t的字元，將index保存至d[字元]裡，例如t='aba'，d['a']=[0,2]，d['b']=[1]。  
變數start代表字串t可以使用的範圍，初始值為0，表示整個字串都沒用過。  
對s中的每個字串c，在d[c]裡面找到第一個大於等於start的值，並回傳其位置idx。若idx=d[c]大小則代表沒有可用的，直接回傳false，否則更新start為idx+1。  
假設d[c]平均長度為M，整個時間複雜度會是O(k*M log N)。

```python
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        N = len(t)
        d = defaultdict(list)
        for i in range(N):
            d[t[i]].append(i)

        start = 0
        for c in s:
            idx = bisect_left(d[c], start)
            if idx == len(d[c]):
                return False
            start = d[c][idx]+1

        return True
```


