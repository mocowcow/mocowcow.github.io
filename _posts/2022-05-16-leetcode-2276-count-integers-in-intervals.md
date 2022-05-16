--- 
layout      : single
title       : LeetCode 2276. Count Integers in Intervals
tags        : LeetCode Hard Array SortedList BinarySearch
---
周賽293。邊界條件調整了半天總算才正確，但是忘記把除錯的print拿掉，搞成Output Limit Exceeded，太丟臉了。

# 題目
輸入一個**空的**區間集合，實作一個資料結構，他可以：  
- **加入**新的區間到集合  
- **計算**有多少整數出現在**至少一個**區間中  

將間隔添加到間隔集。
計算至少在一個區間中出現的整數個數。

實作CountIntervals類別：
- 無參數建構子，初始化空的區間集合  
- void add(int left, int right)，將區間[left, right]加入集合  
- int count()，回傳有幾個整數出現在**至少一個**區間中  

請注意，區間[left, right]表示left <= x <= right的所有整數x。

# 解法
找多少整數出現在至少一個區間中，其實等價於**有多少區間出現過**。  
測資N<=10^9超級大，而且又有10^5次查詢，感覺可用動態開點線段樹，但是沒信心在半小時內刻出來，最後選則比較熟悉的sorted list來做區間合併。  

當天的程式碼超級醜，今天重新寫一次，真的有點懷疑當初怎麼寫出來的。  

初始化size=0，大小可以在區間合併的時候順便處理，才不需要每次呼叫count都重新計算。  
每次插入新的區間[left,right]時，先以二分搜找到第一個大於等於left的位置i。
有時候前一個區間的右邊界會和left重疊，例如：  
> sl=[[1,7],[10,13]] add=[4,8]  
> 第一個大於4的區間為[10,13]  
> left包含在[1,7]中，需要更新left為1  

第二種情形：  
> sl=[[1,9],[10,13]] add=[4,8]  
> 第一個大於4的區間為[10,13]  
> [4,8]整個都包含在[1,9]中，不用合併了

第一種情形要先往左邊更新left，並把i-1區間加入toRmv；第二種就直接return。
再來試著往右邊合併，若區間i的左邊界小於等於right，則重複以下動作：  
1. 以右邊界更新right
2. 將此區間加入至toRmv，待合併結束後一次刪除  
3. i右移一格

合併完後，遍歷toRmv，從sl中一一刪除，並扣掉其大小。最後加入新的區間[left,right]，並加上其大小。

```python
from sortedcontainers import SortedList
class CountIntervals:

    def __init__(self):
        self.sl=SortedList()
        self.size=0

    def add(self, left: int, right: int) -> None:
        N=len(self.sl)
        i=self.sl.bisect_left([left,left])
        toRev=[]
        if i!=0 and self.sl[i-1][1]>=left:
            if self.sl[i-1][1]>=right: # full coverd
                return
            left=self.sl[i-1][0]
            toRev.append(self.sl[i-1])
        # merge side
        while i<N and right>=self.sl[i][0]:
            right=max(right,self.sl[i][1])
            toRev.append(self.sl[i])
            i+=1
        # remove merged intervals
        for x in toRev:
            self.size-=x[1]-x[0]+1
            self.sl.remove(x)
        # insert new interval
        self.size+=right-left+1
        self.sl.add([left,right])

    def count(self) -> int:
        return self.size
```
