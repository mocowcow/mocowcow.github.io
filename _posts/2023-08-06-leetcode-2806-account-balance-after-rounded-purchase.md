---
layout      : single
title       : LeetCode 2806. Account Balance After Rounded Purchase
tags        : LeetCode Easy Math Simulation
---
雙周賽110。有點小囉嗦，還差點忘記怎麼四捨五入。  

## 題目

起初你擁有100塊錢。  

輸入整數purchaseAmount，代表你接下來的消費額。  

你會在商店買東西，然後消費額會四捨五入到**最接近的**十的倍數。  
也就是說，你會支付一個**非負**的額度roundedAmount，且roundedAmount是十的倍數，並且abs(roundedAmount - purchaseAmount)被**最小化**。  

如果有多個最接近的十的倍數，則選擇較大者。  

求支付完消費額度後會剩下多少錢。  

注意：0也視作10的倍數。  

## 解法

一開始本來想說把amount除10後用內建函數round來處理，但總覺得哪裡怪怪的。後來改成暴力枚舉，成功躲過這個陷阱。  
沒錯，round(0.5)因為浮點數精度問題，結果竟然是0！  

還是乖乖手動判斷餘數吧，如果餘數大於等於5就進位，否則捨去。  
從初始的100塊中扣掉就是答案。  

時間複雜度O(1)。  
空間複雜度O(1)。  

```python
class Solution:
    def accountBalanceAfterPurchase(self, purchaseAmount: int) -> int:
        d,r=divmod(purchaseAmount,10)
        if r>=5:
            d+=1
            
        return 100-d*10
```

來自[votrubac](https://leetcode.com/problems/account-balance-after-rounded-purchase/discuss/3868120/One-Liner)大佬的一行版本，真的有夠簡潔。  

```python
class Solution:
    def accountBalanceAfterPurchase(self, purchaseAmount: int) -> int:
        return 100-(purchaseAmount+5)//10*10
```
