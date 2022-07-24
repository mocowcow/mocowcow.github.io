--- 
layout      : single
title       : LeetCode 2350. Shortest Impossible Sequence of Rolls
tags        : LeetCode Hard Array Greedy
---
雙周賽83。超級腦筋急轉彎，總覺得有O(N)解法，但就是想不出來。  
說起來leetcode官方也是誇張，有人直播洩題4次都沒被懲處，所謂的**作弊零容忍**根本是笑話，看看就好。  

# 題目
輸入長度n的整數陣列rolls，和整數k。你有一個k面骰，值為1\~k，共擲n次，rolls[i]代表第i次的結果。  
求**不為rolls子序列**的最短長度。  

例：  
> rolls = [4,2,1,2,3,3,2,4,1], k = 4  
> [1,4,2]不為rolls子序列，故答案為3  

# 解法
當晚我用了dp+二分搜，只通過不到一半的測資，可憐。  
看到有人只花不到2分鐘就做出這題，這程式邏輯一定很簡單，果真是簡單的不行。  

換個角度思考，只要找滿k個數，就會使**能找到全部排列組合的子序列**長度+1。而答案需要找不到的子序列，故需要比該長度多1。 
維護集合s，保存目前找到的數。   
遍歷rolls中所有數字r，將其加到集合中。若找滿k個數字，則使答案遞增1，並清空集合。  

```python
class Solution:
    def shortestSequence(self, rolls: List[int], k: int) -> int:
        ans=0
        s=set()
        
        for r in rolls:
            s.add(r)
            if len(s)==k:
                ans+=1
                s.clear()
                
        return ans+1
```
