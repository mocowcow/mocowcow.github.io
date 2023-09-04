---
layout      : single
title       : LeetCode 2844. Minimum Operations to Make a Special Number
tags        : LeetCode Medium String
---
周賽361。卡了快半小時才想通。  

## 題目

輸入字串num，代表一個非負整數。  

每次操作，你可以選擇num中的一個數位刪除。如果所有數位都被刪除，則num會變成0。  

如果一個整數x能被25整除，則稱為**特殊的**。  

求最少需要多少操作才能使num變得**特殊**。  

## 解法

能被25整除的數，後兩位數只有00,25,50,75四種。分別檢查哪種結尾操作最少。  

維護函數find(t)，代表以t結尾的最少操作次數。  
有時候num只有一位，避免麻煩可以先加一個前導0。  
從後往前遍歷num，配對結尾t，字元不同則需要刪除，操作次數cnt加1，直到t匹配完成。  

時間複雜度O(N)。  
空間複雜度O(N)。  

```python
class Solution:
    def minimumOperations(self, num: str) -> int:
        num="0"+num
        N=len(num)
        
        def find(t):
            j=1
            cnt=0
            for i in reversed(range(N)):
                if num[i]!=t[j]:
                    cnt+=1
                    continue
                else:
                    j-=1
                    if j<0:break
            return cnt            
        
        return min(
            find("00"),
            find("25"),
            find("50"),
            find("75"),
        )
```
