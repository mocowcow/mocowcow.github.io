---
layout      : single
title       : LeetCode 881. Boats to Save People
tags 		: LeetCode Medium Greedy Sorting TwoPointers Array
---
每日題。今天是連續第五天greedy了，這周大概是greedy周跑不掉。

# 題目
陣列people代表每個人的重量，整數limit代表每艘船的最大負重。你有無限艘船，每艘船最多可承載2人，且兩人總重量不能超過limit。求最少需要幾掃船才能載運所有人。

# 解法
一開始以為船載重夠大可以裝一堆人，想說這下難算了，看清楚才發現最多只能載2人。  
這樣問題就變得很簡單，先從最重的人開始上船，每次看看剩餘空間夠不夠塞下最小的人，不能就算了。  
把people排序後，雙指標從前後端往中間夾，每次ans+1，全部人都處理完後回傳ans。

```python
class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        small=0
        big=len(people)-1
        ans=0
        
        while small<=big:
            if people[small]+people[big]<=limit:
                small+=1
            big-=1
            ans+=1
            
        return ans
```

