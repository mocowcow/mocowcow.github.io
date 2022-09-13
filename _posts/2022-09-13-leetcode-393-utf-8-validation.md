--- 
layout      : single
title       : LeetCode 393. UTF-8 Validation
tags        : LeetCode Medium Array BitManipulation
---
每日題。超多人點爛，可能是題目描述不太清楚的關係。雖然一開始我也覺得是垃圾題，但看到最佳解後覺得非常漂亮。  

# 題目
輸入整數陣列data，檢查它是否是有效的UTF-8編碼。  

UTF8中的每個字元長度可為1\~4個bytes，並符合以下規則：  
- 1 byte字元，其最左方的bit為0  
- 2\~4 bytes字元，其第一個byte最左方n個bit為1，且第n+1個bit為0。後方接續著n-1個由10開頭的byte  

# 解法
我們大致上需要兩種操作，先寫成獨立的函數：
- 檢查是否由01開頭  
- 計算前導1數量  

開始遍歷data中每個整數n，先檢查他有多少個前導1：  
- 0個，代表他1 byte，直接跳過不處理  
- 1個，不合法  
- 2\~4個，代表2\~3 bytes，接下來跟隨著n-1個10開頭的byte  
- 5個以上，不合法  

在檢查n-1個尾隨的10 byte時，假如輸入長度不足，或不符合10規則，則直接回傳false。  
時間複雜度O(N)，空間複雜度O(1)。  

不得不說這code真的是有夠醜，但我也沒想到什麼更好的方法。  

```python
class Solution:
    def validUtf8(self, data: List[int]) -> bool:
        
        def check01(n):
            return n&(1<<7) and not n&(1<<6)
        
        def count_leading_one(n):
            cnt=0
            for i in range(7,-1,-1):
                if n&(1<<i):
                    cnt+=1
                else:
                    break
            return cnt
        
        N=len(data)
        i=0
        while i<N:
            one=count_leading_one(data[i])
            if one==0:
                i+=1
                continue
            if one==1 or one>4 or i+one-1>=N:
                return False
            i+=1
            for _ in range(one-1):
                if not check01(data[i]):
                    return False
                i+=1
                    
        return True
```

看看別人做法才發現，與其計算前導1，不如直接將整數移位，檢查是否符合4種可能性，不僅可讀性上升，操作次數也降低許多。  
至於尾隨的10 byte則以變數來記錄欠缺個數，就不需要每次都檢查剩餘data長度是否足夠。  
時間複雜度O(N)，空間複雜度O(1)。

這似乎是我第一次用上0b來表示二進位整數，本來還以為這東西幾乎不會用上，算是意外收穫。  

```python
class Solution:
    def validUtf8(self, data: List[int]) -> bool:
        follow=0
        
        for n in data:
            if follow:
                if (n>>6)!=0b10:
                    break
                else:
                    follow-=1
            elif (n>>5)==0b110:
                follow=1
            elif (n>>4)==0b1110:
                follow=2
            elif (n>>3)==0b11110:
                follow=3
            elif (n>>7):
                return False

        return follow==0
```