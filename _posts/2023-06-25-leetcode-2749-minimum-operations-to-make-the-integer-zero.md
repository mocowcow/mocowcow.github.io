--- 
layout      : single
title       : LeetCode 2749. Minimum Operations to Make the Integer Zero
tags        : LeetCode Medium BitManipulation
---
周賽351。這鬼東西比Q4還難想，最周的單雙周賽Q4都不夠力。  

# 題目
輸入兩個整數num1和num2。  

每次操作，你可以從[0, 60]選擇一個整數i，並將num1減掉2<sup>i</sup> + num2。  

求**最少**需要幾次操作才可以使num1變成0。若無法使num1變成0則回傳-1。  

# 解法
操作x次，要從num1中扣掉x個num2和2<sup>i</sup>。因為num2的是固定的，直接扣掉之後再考慮2<sup>i</sup>怎麼分配。  
把num1-x\*num2記做remain。2<sup>i</sup>至少為1，如果remain不足x個，那就不可能有答案了，直接回傳-1。  

說到2<sup>i</sup>就會想到他是二進位中某一個位置的1 bit。  
可以將問題轉換成：x次操作，我們需要把num1扣掉x個num2後，remain擁有的1 bit個數就是最少需要扣掉幾次2<sup>i</sup>。  
那如果remain的1 bit不足x個怎辦？看看例題1：  
> num1 = 3, num2 = -2  
> 一次操作 remain = 5 = 0b101  
> 需要刪兩次，但是只能刪一次，不合法  
> 二次操作 remain = 7 = 0b111  
> 需要刪三次，但是只能刪兩次，不合法  
> 三次操作 remain = 9 = 0b1001  
> 需要刪兩次，但是應該要刪三次  
> 可以刪掉4+4+1  

更準確的說，remain能最多能夠以remain個2<sup>i</sup>(全部都是1)，最少數量等於1 bit的數量。  
所以只要操作次數ops滿足1 bits <= ops <= remain就可以順利變成0。  

但num2可能是負數，會讓remain越來越多，那最多到底需要幾次操作？  
num1最大值是10^9，num2最小值是-10^9，轉成二進位大概是30個位元。  
而我們每次可以刪的數高達2<sup>60</sup>，remain的每個位元都可以刪到。也就是說，在remain不斷增長的情況下，就算最差情況使得每個位元都是1，大概需要30幾次操作就可以全部刪掉。  

時間複雜度O(log remain)。  
空間複雜度O(1)。  

```python
class Solution:
    def makeTheIntegerZero(self, num1: int, num2: int) -> int:
        remain=num1
        ops=0
        
        while True:
            ops+=1
            remain-=num2
            
            if remain<ops: # ensure that remain >= ops
                return -1
        
            min_ops=remain.bit_count()
            max_ops=remain
            if min_ops<=ops: 
                return ops
```
