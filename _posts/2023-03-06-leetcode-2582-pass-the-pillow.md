--- 
layout      : single
title       : LeetCode 2582. Pass the Pillow
tags        : LeetCode Easy Simulation Math
---
周賽335。

# 題目
有n個人排成一線，編號分別為1\~n。最初，第一個人拿著枕頭。  
之後每一秒鐘，拿著枕頭的人會將枕頭傳給下一個人。如果傳到底了，則改變方向傳回去。  
- 例如：第n個人拿到枕頭後，傳回去給第n-1個人，再來是第n-2個人，以此類推  

輸入整數n和time，求經過n秒後是哪個人拿著枕頭。  

# 解法
暴力模擬，初始方向為向右走，如果走到底則改變方向；同理，走回出發點也要改變方向。  

時間複雜度O(time)。空間複雜度O(1)。  

```python
class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        move=1
        i=1
        for _ in range(time):
            i+=move
            if i in [1,n]:
                move=-move
        
        return i
```

對於n個人來說，需要n-1次可以從頭傳到尾，再n-1次從尾傳回起點，完整一趟共需要2\*(n-1)次。先以2\*(n-1)對time求餘數。    
如果剩餘步數step不超過n-1，則代表不須回頭，直接走到1+step處；否則會先花n-1步走到n，然後往回走step-(n+1)步。  

時間複雜度O(1)。空間複雜度O(1)。  

```python
class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        trip=2*(n-1)
        step=time%trip

        if step>n-1:
            step-=n-1
            return n-step
        
        return 1+step
```

從1移動step步後有三種情況：  
1. 小於n-1步，停在n左方  
2. 正好n-1步，停在n  
3. 大於n-1步，停在n右方  

對於第三種情況，將n作為對稱軸，把n扣掉**1+step與n的絕對距離**就會是往回走的位置。甚至可以簡化成一行。  

```python
class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        trip=2*(n-1)
        step=time%trip
        distance_to_n=abs(1+step-n)
        
        # return n-abs(1+time%(2*(n-1))-n)
        return n-distance_to_n
```