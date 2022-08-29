--- 
layout      : single
title       : LeetCode 2391. Minimum Amount of Time to Collect Garbage
tags        : LeetCode Medium Array String Greedy HashTable PrefixSum
---
周賽308。題目超臭長的模擬題，花了超久才搞懂在問什麼，而且還很簡單。  

# 題目
輸入字串陣列garbage，其中garbage[i]表示第i個房子的垃圾。garbage[i]由字元"M","P"和"G"組成，分別代表一個金屬、紙或玻璃垃圾。回收一單位的垃圾皆須要1分鐘。  
還有一個整數陣列travel，其中travel[i]是從第i個房子到第i+1個房子所需的分鐘數。  

共有三輛垃圾車，每輛負責收一種垃圾。每輛垃圾車從0號房開始，按順序訪問各個房屋；但是**不需要**訪問所有房屋。  
同一個時間點只有一台垃圾車可以動作：當某台正在移動或是收垃圾時，另外兩台必須待機。  

求回收所有垃圾最少需要幾分鐘。  

# 解法
**不需要**訪問所有房屋指的是：若後方的房屋沒有出現某種垃圾，則對應的垃圾車不必繼續往後開。所以我們要維護三個變數，分別記錄三台垃圾車應該開到哪個位置。  
至於回收的垃圾，反正每一種都是要花費1分鐘，所以收垃圾的總時間其實就是所有字串的加總長度。  
最後是垃圾車的行車時間，因為垃圾車數量只有三台，沒有什麼太大的影響，可以直接暴力求和。  

遍歷所有垃圾的時間複雜度為O(N\*10\*3)，可以當作O(N)。而計算移動距離是O(N\*3)，一樣當作O(N)。整體複雜度O(N)。  

```python
class Solution:
    def garbageCollection(self, garbage: List[str], travel: List[int]) -> int:
        time=0
        mcar=pcar=gcar=0
        
        for i,s in enumerate(garbage):
            time+=len(s)
            if 'M' in s:
                mcar=i
            if 'P' in s:
                pcar=i
            if 'G' in s:
                gcar=i
        
        for i,n in enumerate(travel):
            i=i+1
            for car in [mcar,pcar,gcar]:
                if car>=i:
                    time+=n

        return time
```

如果垃圾車有很多台，上面求行車距離的部份會變成O(N\*M)，很有可能超時。  
可以先對房屋的距離做前綴和，以O(1)的成本得到每台車的移動距離，將整題複雜度保持在O(N)。  
紀錄垃圾車位置也要稍微修改一下，換成雜湊表，確保每個垃圾堆只需要遍歷一次。  

```python
class Solution:
    def garbageCollection(self, garbage: List[str], travel: List[int]) -> int:
        time=0
        cars={}
        psum=[0]*(len(travel)+1)
        for i,n in enumerate(travel):
            psum[i+1]=psum[i]+n
            
        for i,s in enumerate(garbage):
            time+=len(s)
            for car in s:
                cars[car]=i
            
        for i in cars.values():
            time+=psum[i]
        
        return time
```