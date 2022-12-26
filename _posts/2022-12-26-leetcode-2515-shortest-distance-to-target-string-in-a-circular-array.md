--- 
layout      : single
title       : LeetCode 2515. Shortest Distance to Target String in a Circular Array
tags        : LeetCode Easy Array String
---
周賽325。被例題2晃了一下，想說長度3的陣列怎麼會有索引3，原來指的是3%3=索引0。  

# 題目
輸入索引從0開始的**循環**字串陣列words和一個字串target。**循環陣列**代表陣列的頭尾是相連的。  

也就是說，words[i]的下一個元素是words[(i + 1) % n]，而words[i]的前一個元素是words[(i - 1 + n) % n]，其中n是words的長度。  

你從startIndex出發，每次移動1步，可以抵達上一個或是下一個單字。  

求抵達字串target所需的**最短距離**。如果字串target不存在於words中，則回傳-1。  

# 解法
題目說target有可能不存在，先特別處理一下，若不存在則直接回傳-1。  

然後target也有可能存在多個，遍歷words過程中，若碰到target則分別嘗試往兩個方向走回startIndex，以較小值更新答案。  
注意，某些不支持負數mod的的語言應該要先加上N再取餘數。  

時間複雜度O(N)。空間複雜度O(1)。  

```python
class Solution:
    def closetTarget(self, words: List[str], target: str, startIndex: int) -> int:
        if target not in words:return -1
        N=len(words)
        ans=inf
        for i,w in enumerate(words):
            if w==target:
                a=(i-startIndex)%N
                b=(startIndex-i)%N
                ans=min(ans,a,b)
        
        return ans
```

取餘數的方法不太直觀，看到別人有更容易理解的算法：先求target和startIndex的最短距離a，另一個方向距離則是N-a。  
也可以把inf留到最後才判斷，降低至一次遍歷。  

```python
class Solution:
    def closetTarget(self, words: List[str], target: str, startIndex: int) -> int:
        N=len(words)
        ans=inf
        for i,w in enumerate(words):
            if w==target:
                a=abs(i-startIndex)
                b=N-a
                ans=min(ans,a,b)
                
        return -1 if ans==inf else ans
```