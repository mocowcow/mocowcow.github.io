--- 
layout      : single
title       : LeetCode 1562. Find Latest Group of Size M
tags        : LeetCode Medium Array BinarySearch Simulation SortedList
---
二分搜學習計畫。竟然有誇張的O(N)解，到底是什麼腦子才能想出這種可怕的解法。

# 題目
輸入長度N陣列arr，裡面有1~N的數字各出現一次。  
你有一個長度N的二進位字串，索引以1開始計，剛開始都為0。在第i次動作時，你會將第arr[i]的位元設為1。  
另外輸入整數m，代表要找長度為m的1群體。**1群組**指的是由連續的1所組成，且左右方不可以是1。  
求最後一次使字串中出現長度為m的1群組的動作，若不存在則回傳-1。

> arr = [3,5,1,2,4], m = 1  
> step1 : "00100" 1群組:["1"]  
> step2 : "00101" 1群組:["1","1"]  
> step3 : "10101" 1群組:["1","1","1"]   
> step4 : "11101" 1群組:["111","1"]  
> step5 : "11111" 1群組:["11111"]  

# 解法
剛開始看半天誤會題目，理解完全錯誤還通過79/114測資，有夠好笑。  
題目要求最後一次出現的動作，乾脆反其道而行，從全為1的字串開始回推，每次動作把對應位置的1改回0，看哪次動作完出現長度m的群組就可以馬上回傳答案。  

使用左閉右開的區間數對[start,end)模擬1群體，起點為start，終點為end-1，初始為長度n的全1字串。  
從arr的後方往前遍歷，對於arr[i]對應到的第idx個位元，使用二分搜找到對應的群組sl[j]，將其刪除，並加入新產生的子群組。若新子群組長度為m則直接回傳i，直到i=0處理完還沒找到，代表不會出現m大小的群組，回傳-1。

```python
from sortedcontainers import SortedList

class Solution:
    def findLatestStep(self, arr: List[int], m: int) -> int:
        N=len(arr)
        if N==m:
            return N
        ctr=Counter([N])
        sl=SortedList([(1,N+1)])
        for i in range(N-1,-1,-1):
            idx=arr[i]
            # find corresponding group
            j=sl.bisect_right((idx,math.inf))-1
            s,e=sl[j]
            sl.remove(sl[j])
            ctr[e-s]-=1
            # split
            if s!=idx:
                sl.add((s,idx))
                ctr[idx-s]+=1
            if idx+1!=e:
                sl.add((idx+1,e))
                ctr[e-(idx+1)]+=1
            if ctr[m]:
                return i

        return -1
```

O(N)解法真的是神奇，簡短而且不難理解，就是很難憑空想出來。  
看這二進位字串的索引是從1開始計，不禁開始懷疑出題者是不是一開始就有想到這個解法，簡直巧妙到不行。  

先列出每次將位置mid設為1時，所可能出現的狀況：  
1. 左右都是0，群組長度1  
2. 左右其中一個不是0，使該群組長度+1  
3. 左右都是1，使左右兩群組合併，且總長度+1  

有沒有發現其實我們只會存取到各群組的左、右邊界？如此一來，我們只需將群組大小記錄在最左、最右格子，每次更新位元時，複雜度只要O(1)。  
遍歷arr，對其更新的位置mid，往左找一格，mid-1的值即為左方群組的大小，右邊同理。因為是檢查上一次修改，所以先看看左右群組是否有長度等於m，若是則更新答案。最後計算新群組長度=左+右群組長度+1，將新長度標記到新群組的最左右格子。

```python
class Solution:
    def findLatestStep(self, arr: List[int], m: int) -> int:
        N=len(arr)
        if m==N:
            return m
        size=[0]*(N+2)
        last=-1
        
        for i,mid in enumerate(arr):
            left=size[mid-1]
            right=size[mid+1]
            if left==m or right==m:
                last=i
            size[mid-left]=size[mid+right]=left+right+1
   
        return last
```
