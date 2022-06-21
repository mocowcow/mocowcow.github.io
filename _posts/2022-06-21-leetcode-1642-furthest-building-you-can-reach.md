--- 
layout      : single
title       : LeetCode 1642. Furthest Building You Can Reach
tags        : LeetCode Medium Array BinarySearch Sorting Greedy Heap
---
每日題。今天去拜訪朋友，可愛小貓的活力真的能讓人開心一整天。 
然後這題目的範例GIF畫風驟變，不知道從哪裡開始吐槽。   

# 題目
輸入整數陣列heights代表每一棟大樓的高度，還有整數bricks和ladders。  
你從第0棟建築開始出發，往右移動：  
- 如果當前建築比下一棟還高，可以直接移動  
- 否則你可以使用**一個梯子**或是兩建築**高度差**個**磚塊**往上爬  

假設所有磚塊和梯子都依最有效率的方法使用，求最遠可以抵達到第幾棟建築。  

# 解法
第一眼感覺要回溯法暴力搜尋，一看測資範圍超級大，絕對不可能。  
測資這麼大，而且答案又具有二分性質，那就可以使用函數型二分搜。  

撰寫一個輔助函數canDo(target)，用來判斷能否順利抵達第target棟建築。  
因為我們從0出發，下界永遠為0，而最佳情況是全部走完，上界為最後一棟建築N-1。  
開始二分搜：如果我們能無法成功抵達第mid棟建築，那麼從mid開始之後的一定也不可能抵達，更新上界為mid-1；否則mid以前的都能成功抵達，更新下界為mid。  

重點是canDo函數的實作，我們要先找出從0移動到target過程中有多少**向上**移動，而最理想的的狀況，就是有足夠的梯子用來應付所有**向上**。否則只能選擇最大的幾個使用梯子，剩餘的乖乖用磚塊。最後依照磚塊的需求數needBrick是否小於bricks個，若是則回傳true，否則false。  

最差情況會執行log N次二分搜，而canDo函數的複雜度主要為排序的O(N log N)，整體複雜度為O(N(log N)^2)，耗時1035ms。

```python
class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        N=len(heights)
        
        def canDo(target):
            up=[]
            for i in range(target):
                if heights[i+1]>heights[i]:
                    up.append(heights[i+1]-heights[i])
            noLadder=len(up)-ladders
            if noLadder<=0:
                return True
            useBrick=sorted(up)[:noLadder]
            needBrick=sum(useBrick)
            return bricks>=needBrick
            
        lo=0
        hi=N-1
        while lo<hi:
            mid=(lo+hi+1)//2
            if not canDo(mid):
                hi=mid-1
            else:
                lo=mid
                
        return lo
```

後來看到有個heap標籤，我才想到這個更好的解法。  
維護一個最小堆積h，最多只保存ladders個使用樓梯的元素，依序遍歷heights，如果有**向上**，則加入h中。  
若h大小超出ladders，則彈出最小元素，改成使用磚塊，將其加入needBrick中，若超過限制的bricks則代表只能到上一棟建築為止，回傳答案。 

雖然有點醜，但是複雜度降到O(N log N)，執行時間只要588ms，勝過98.16%。

```python
class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        N=len(heights)
        h=[]
        needBrick=0
        
        for i in range(1,N):
            diff=heights[i]-heights[i-1]
            if diff>0:
                heappush(h,diff)
                if len(h)>ladders:
                    needBrick+=heappop(h)
                    if needBrick>bricks:
                        return i-1

        return N-1
```