--- 
layout      : single
title       : LeetCode 2543. Check if Point Is Reachable
tags        : LeetCode Hard Math
---
雙周賽96。想破頭好不容易想通，交出去AC後發現比賽結束10秒了。比想不出來還難受許多。  

# 題目
有個無限大的網格，你一開始位於(1, 1)，而你的目標是(targetX, targetY)，不限制移動步數。  

每**一步**，你可以從(x, y)移動到以下任一點：  
- (x, y - x)  
- (x - y, y)  
- (2 * x, y)  
- (x, 2 * y)  

輸入兩個整數targetX和targetY，代表目標位置。若可以成功抵達則回傳true，否則回傳false。  

# 解法
一開始想說從起點開始bfs，抵達目標回傳步數，結果座標上限高達10^9，空間一定不夠紀錄。必須從目標點逐漸逆推回起點。  

因為是反著走，所以四種移動方式變成：  
- (x, y + x)  
- (x + y, y)  
- (x / 2, y)  
- (x, y / 2)  

為了快速縮減座標大小，不斷將X和Y除2，直到兩個都是質數為止。  
最理想的狀況下當然是X=Y=1，直接抵達終點。  

可惜大多數情況下沒有這麼順利，試著以範例1的X=6, Y=9來想想看：  
> 不斷除2，最後X=3, Y=9  
> 兩個質數相加變偶數，X=3, Y=12  
> 新的偶數再不斷除2，X=3, Y=3  

這時候兩個數無論怎樣操作，最終都會等於3，沒辦法繼續減少。  

回去看一開始的X-Y和Y-X，這不就是求gcd的輾轉相除法嗎？在X和Y都為奇數時，若gcd為1，則代表成功回到起點。  

時間複雜度為gcd的O(log max(targetX, targetY))。空間複雜度O(1)。  

```python
class Solution:
    def isReachable(self, a: int, b: int) -> bool:
        while a%2==0:
            a//=2
        while b%2==0:
            b//=2
            
        return gcd(a,b)==1
```
