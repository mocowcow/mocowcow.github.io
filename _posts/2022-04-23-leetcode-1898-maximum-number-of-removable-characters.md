---
layout      : single
title       : LeetCode 1898. Maximum Number of Removable Characters
tags 		: LeetCode Medium Array Stinrg BinarySearch 
---
二分搜學習計畫。好像第一次碰到這種函數型有搭配字串，還算是挺新鮮。

# 題目
輸入字串s和p，且p為s的子序列。  
另有整數陣列removable，代表刪除s中的第幾removable[i]個位置中的字元。  
求s在移除removable前k個位置的字元之後，依然使p為s的子序列的狀況下，k最大可以為多少。

# 解法
雖然題目說是**刪除**，絕對不能真的對字串去做刪減，否則高機率TLE。正確方法是**跳過**定義位置的字元。  
先定義一個函數canDo(k)，用來判斷能不能刪除removable中前k個位置，先不管實作，回到二分搜框架。  
最差狀況是不能刪除任何字元，所以下界是0。最佳狀況是removable全部都可以刪，上界是removable大小，開始二分搜。  
如果可以刪除mid個位置，則更新下界為mid；否則更新上界為mid-1。  

重點是canDo函數的細節。  
因為removable中的刪除字元並不是有序出現，在字串比對上會有點問題，所以直接要刪除的部分裝進set中，降低查詢成本。  
剩下就是普通的子序列比對：遍歷p中的每個字元，從s[0]開始往後找，如果s[i]和p[j]不同或i遭到刪除，則繼續將i後移。若找完p之前s就已經用盡，代表p不是s的子序列，回傳false；成功完成則回傳true。

```python
class Solution:
    def maximumRemovals(self, s: str, p: str, removable: List[int]) -> int:
        M=len(s)
        N=len(p)
        
        def canDo(k):
            skip=set(removable[:k])
            i=0
            for c in p:
                while i<M and s[i]!=c or i in skip:
                    i+=1
                if i==M:
                    return False
                i+=1
            return True
        
        lo=0
        hi=len(removable)
        while lo<hi:
            mid=(lo+hi+1)//2
            if not canDo(mid):
                hi=mid-1
            else:
                lo=mid
            
        return lo
```

