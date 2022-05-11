--- 
layout      : single
title       : LeetCode 2178. Maximum Split of Positive Even Integers
tags        : LeetCode Medium Greedy Math
---
模擬雙周賽82。回想起來，當時練習的時候是5/7晚上10點左右，結果網站竟然炸掉快半小時！當時還想說：明天周賽最好不要給我出事，然後就真的出事了。

# 題目
輸入一個數字finalSum，盡可能將其分割成多個**不重複正偶數**。  
例：12可以拆成(2,4,6)，但不可以是(2,2,4,4)。

回傳一個整數串列，代表任一種合法的拆分方式。如果無法拆分，則回傳空串列。

# 解法
要把某個數n拆分成x個偶數，那n一定也得是偶數。  
一開始可以先把奇數過濾掉，直接回傳[]。  

仔細想想，既然要盡可能拆成多個數，那我就先從最小的數字2開始拆，每次拆完就遞增2。  
那麼迴圈的中止條件是什麼？本想要用set紀錄那些用過，但是若真碰到重複值，就很難處理。  
更保險的方法是：確保剩餘的finalSum扣除掉分割數lo之後，還能拆出一個比lo更大的數。

```python
class Solution:
    def maximumEvenSplit(self, finalSum: int) -> List[int]:
        if finalSum&1:
            return []
        ans=[]
        lo=2
        while finalSum>lo*2:
            ans.append(lo)
            finalSum-=lo
            lo+=2
            
        ans.append(finalSum)
        
        return ans
```

看看別人的作法，和我的思路剛好相反。  
我是從finalSum開始拆解，他是從2開始加入，直到總和即將超過finalSum之際停止。  
迴圈停止時總和不一定會等於finalSum，所以把差值塞回最後一個數字裡面。

```python
class Solution:
    def maximumEvenSplit(self, finalSum: int) -> List[int]:
        if finalSum&1:
            return []
        ans=[]
        curr=0
        lo=2
        while curr+lo<=finalSum:
            ans.append(lo)
            curr+=lo
            lo+=2
            
        ans[-1]+=finalSum-curr
            
        return ans
```