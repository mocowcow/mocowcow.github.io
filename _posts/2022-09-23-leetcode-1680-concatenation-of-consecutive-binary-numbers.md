--- 
layout      : single
title       : LeetCode 1680. Concatenation of Consecutive Binary Numbers
tags        : LeetCode Medium Math BitManipulation Simulation
---
每日題。看到10^9+7還以為是dp，又被騙了。  

# 題目
輸入整數n，將1\~n的數字轉成二進位後全部串接起來，最後轉回十進位，對10^9+7取餘數後回傳。  

# 解法
每次在末端新的數字，需要將原本的數字向左移。  
例如：0b110要接上0b11，事實上是先將0b110向左移動兩位變成0b11000，加上0b11變成0b11011。  

因此每次接上新數字x之前需要先計算出其位元數size，將原本數字ans向左移，加上x後模10^9+7。  
內建的bin函數會將十進位數字轉成二進位字串0bxxx，扣掉前面兩個字元0b即為正確位元數。  

bin函數的時間複雜度為O(log n)，共執行n次，整體時間複雜度O(n log n)，空間複雜度O(1)。  

```python
class Solution:
    def concatenatedBinary(self, n: int) -> int:
        MOD=10**9+7
        ans=0
        
        for x in range(1,n+1):
            # shift
            size=len(bin(x))-2
            ans<<=size
            # append
            ans=(ans+x)%MOD
        
        return ans
```

利用位元運算的小技巧，透過x&(x-1)==0，可以檢查x是否為2的冪。  
位元數size初始為0，若新的數字x為2的冪，這時候會使用到一個新的位元數，使size+1。  

把bin函數替換掉後，時間複雜度降到O(n)。  

```python
class Solution:
    def concatenatedBinary(self, n: int) -> int:
        MOD=10**9+7
        ans=0
        size=0
        
        for x in range(1,n+1):
            # shift
            if x&(x-1)==0:
                size+=1
            ans<<=size
            # append    
            ans=(ans+x)%MOD
        
        return ans
```