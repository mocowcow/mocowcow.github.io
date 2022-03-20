---
layout      : single
title       : LeetCode 2208. Minimum Operations to Halve Array Sum
ㄒtags 		: LeetCode Medium Array Heap Greedy
---
雙周賽74。第三題比第二題簡單，其實我先秒殺這題才回去搞上一題的。

# 題目
輸入整數陣列nums，每次動作可以挑其中一個數減半，求最少要幾次動作才能將數列總和**減少最少一半**。

# 解法
簡單明瞭，每次動作一定是挑剩餘最大的來減半，一看就知道是用max heap。  
減少至少一半，也就是不大於原來的一半時停止。每次挑最大的數出來減半，再將總量扣掉，行動次數+1。

```python
class Solution:
    def halveArray(self, nums: List[int]) -> int:
        total=sum(nums)
        curr=total
        half=total/2
        h=[]
        for n in nums:
            heappush(h,-n)
            
        move=0
        while curr>half:
            n=-heappop(h)/2
            curr-=n
            heappush(h,-n)
            move+=1
            
        return move
```

