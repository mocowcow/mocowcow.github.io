---
layout      : single
title       : LeetCode 1007. Minimum Domino Rotations For Equal Row
tags 		: LeetCode Medium Array Greedy
---
每日題。題目雖然一直強調骨牌，但跟骨牌沒有半點關係。

# 題目
兩個陣列tops和bottoms，裡面只會出現1~6的數字。  
可以讓tops[i]和bottoms[i]交換，求最少幾次交換可以讓其中一個陣列元素完全相同。若不能達成則回傳-1。

# 解法
要讓整個陣列值相同，有兩個選擇：  
> tops = [2,1,2,4,2,2], bottoms = [5,2,6,2,3,2]  
1. 試著全部換成tops的第一個元素=2  
2. 試著全部換成bottoms的第一個元素=5，不可能達成  

但是完成的連續陣列又可以選在任一個，所以又有兩種換法：  
1. tops = [2,2,2,2,2,2], bottoms = [5,1,6,4,3,2]  
2. tops = [5,1,6,4,3,2], bottoms = [2,2,2,2,2,2]  

所以總共有2*2=4總換法。  
寫一個函數match(a1,a2,t)，表示數字為t，以a1為主，試將a2的t換過來。若不可能達成則回傳最大數。  
對四個可能性取最小者即可。

```python
class Solution:
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        
        def match(a1,a2,t):
            cnt=0
            for a,b in zip(a1,a2):
                if a==t:
                    continue
                elif b==t:
                    cnt+=1
                else:
                    return math.inf
            return cnt
        
        ans=min(match(tops,bottoms,tops[0]),
                match(bottoms,tops,tops[0]),
                match(tops,bottoms,bottoms[0]),
                match(bottoms,tops,bottoms[0])
                )
        
        return ans if ans!=math.inf else -1
```

