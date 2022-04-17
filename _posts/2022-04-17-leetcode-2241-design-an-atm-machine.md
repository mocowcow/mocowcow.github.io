---
layout      : single
title       : LeetCode 2241. Design an ATM Machine
tags 		: LeetCode Medium Design Array Greedy
---
雙周賽76。有點強迫症的提款機，題目很長一串而已，做起來沒什麼難度。

# 題目
有一台ATM可以存20, 50, 100, 200和500面額的紙鈔。一開始ATM都是空的，用戶可以存入或提取任意金額的錢。  
但是提款的時候，機器會優先選擇給你可用的較大面額鈔票，且不考慮之後有沒有辦法湊滿金額：  
- 假設機器中有2張50、1張100和1張200，你要提取300元，機器會選擇200+100  
- 假設機器中有3張200和1張500，你要提取600元，機器會選擇500，但是剩下的100塊湊不出來，所以擺爛不讓你提款

實作類別ATM：  
- 無參數建構子  
- void deposit(int[] banknotesCount)，按照幣值由小到大存入鈔票張數  
- int[] withdraw(int amount)，提款amount金額，若提款成功則回傳五種鈔票各幾張；否則回傳[-1]

# 解法
初始化長度為5個陣列D，代表各面額數量。陣列T紀錄面額，供後續計算查表使用。  
存款函數不會出錯，直接照著數量加進去就好。  
提款時建立長度為5的陣列W，紀錄提款時要使用的各面額數量。  
依題目要求，從最大面額開始，如果要湊的金額amount可以使用多少張T[i]的紙鈔，加入W中，扣除所佔額度，往下一個較小的額度找。  
所有面額都算過一遍後，如果amount不為0，代表沒辦法成功湊數，回傳[-1]；否則，從原本各面額存量D扣除提出數W，然後回傳W。

```python
class ATM:
    #$20, $50, $100, $200, and $500.
    def __init__(self):
        self.D=[0]*5
        self.T=[20,50,100,200,500]

    def deposit(self, banknotesCount: List[int]) -> None:
        for i in range(5):
            self.D[i]+=banknotesCount[i]

    def withdraw(self, amount: int) -> List[int]:
        W=[0]*5
        for i in range(4,-1,-1):
            if self.D[i]==0:
                continue
            use=min(amount//self.T[i],self.D[i])
            W[i]=use
            amount-=use*self.T[i]
                
        if amount==0:
            for i in range(5):
                self.D[i]-=W[i]
            return W
        else:
            return [-1]
        
```

