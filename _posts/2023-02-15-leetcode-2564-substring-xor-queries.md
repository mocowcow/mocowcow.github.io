--- 
layout      : single
title       : LeetCode 2564. Substring XOR Queries
tags        : LeetCode Medium Array String BitManipulation SlidingWindow HashTable
---
周賽332。一樣走了遠路，還寫錯邊界吃兩次蟲，好歹是過了。  

# 題目
輸入**二進位**字串s，以及二維整數陣列qeuries，其中queries[i] = [first<sub>i</sub>, second<sub>i</sub>]。  

對於第i個查詢，你必須找到s的最短子字串，其對應的**十進位值**val和first<sub>i</sub>做XOR運算後等於second<sub>i</sub>。也就是val ^ first<sub>i</sub> = second<sub>i</sub>。

第i個查詢的答案是子字串[left<sub>i</sub>, right<sub>i</sub>]的兩個端點，如不存在合法的子字串，則答案為[-1, -1]。如果有多個符合的子字串，則選擇left<sub>i</sub>**最小**者。  

回傳陣列ans，其中ans[i] = [left<sub>i</sub>, right<sub>i</sub>]為第i個查詢的答案。  

# 解法
首先有個很重要的轉換：val ^ first = sencond，而XOR特性是相消，再XOR一次first後變成val = first ^ second，問題就簡化成找十進位值等於first ^ second的子字串。  

而first和second上限10^9正好是30個位元，所以只要使用滑動窗口，窮舉長度為1\~30的所有子字串就可以找到所有對應的值。又因為題目要求**最短**且**最靠左**的子字串，所以從長度由小漸增，窗口由左至右，這樣每個值配對到的第一個子字串就會是答案。  

預處理完所有子陣列值之後，對於每個查詢分別至雜湊表內取值，若查詢值不存在則為[-1, -1]。  

需要遍歷s共30次，常數可忽略。查詢每次O(1)，共O(M)。時間複雜度O(N + M)，其中N為s長度，M為qeuries長度。空間複雜度O(MX)，其中MX為所有first^second中的最大值，在此處為(10^10)-1。  

```python
class Solution:
    def substringXorQueries(self, s: str, queries: List[List[int]]) -> List[List[int]]:
        seen={}
        
        for size in range(1,31):
            val=0
            left=0
            mask=1<<(size)
            for right,c in enumerate(s):
                val=(val<<1)+(c=="1")
                if val&mask:
                    val-=mask
                if right-left+1==size:
                    if val not in seen:
                        seen[val]=[left,right]
                    left+=1
                    
        ans=[]  
        for a,b in queries:
            t=a^b
            if t in seen:
                ans.append(seen[t])
            else:
                ans.append([-1,-1])
                
        return ans
```
