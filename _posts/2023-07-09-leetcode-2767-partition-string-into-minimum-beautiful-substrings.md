--- 
layout      : single
title       : LeetCode 2767. Partition String Into Minimum Beautiful Substrings
tags        : LeetCode Medium Array Backtracking HashTable
---
雙周賽108。把5的次方看成5的倍數，被騙個WA。  

# 題目
輸入二進位字串s，將其分割成一個或多個**美麗的**子字串。  

一個**美麗的**子字串必須滿足：  
- 沒有前導零  
- 其二進位的值是5的次方數  

求最少可以分割出幾個**美麗的**子字串。若不可能則回傳-1。  

# 解法
對於從索引i開始的子字串，可以選擇i\~N-1之間的索引j作為分割點。若s[i,j]這個子字串是**美麗的**，則繼續遞迴處理j+1\~N的子問題。  

先預處理範圍內所有可能出現的**5的次方數**，裝到集合中，之後將二進位值解析後可用O(1)時間判斷。  

維護回溯函數bt(i,cnt)，代表子字串s[i,N-1]尚未分割，且已經分割出cnt個子字串的情形。  
從索引0開始，枚舉分割點，直到整個字串都分割完畢。  

因為不可有前導零，若s[i]是0的話可以直接剪枝。
而當前分割的子字串數量cnt若已經等於當前答案最小值，也可以直接跳出。  
雖然理論上高達15!，但實際上沒幾個子陣列是5的次方，搭配剪枝，執行時間其實非常快。  

時間複雜度O(N!)。  
空間複雜度O(N)。  

```python
power_of_5=set()
x=1
while x<(2<<15):
    power_of_5.add(x)
    x*=5

class Solution:
    def minimumBeautifulSubstrings(self, s: str) -> int:
        ans=inf
        N=len(s)
        
        def ok(i,j):
            val=0
            for c in range(i,j+1):
                val=val*2+int(s[c])
            return val in power_of_5
        
        def bt(i,cnt):
            nonlocal ans
            if cnt>=ans:
                return
            if i==N:
                ans=cnt
                return 
            if s[i]=="0":
                return False
            for j in range(i,N):
                if ok(i,j):
                    bt(j+1,cnt+1)
        
        bt(0,0)
        
        if ans==inf:
            return -1
        
        return ans
```
