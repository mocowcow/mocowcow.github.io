---
layout      : single
title       : LeetCode 740. Delete and Earn
tags 		: LeetCode Medium HashTalbe DP
---
趁著DP教學最近免費，把裡面的題目也刷一刷，也練習照著思考框架寫題解。

# 題目
輸入一個整數陣列nums，你可以選擇拿取任一個數字n，但是必須將所有的n+1及n-1拋棄。求最大能拿多少點數？

# 解法
首先用一個陣列table計算所有數字的出現次數，再來開始DP了。  

>步驟1：定義狀態  
測資內整數的範圍是0~10^4。
需要兩個長度10^4+1陣列，叫做take與ignore，take[i]及ignore[i]表示處理完數字i時，拿或不拿的最佳狀態。  

>步驟2：找出狀態轉移方程式  
對於每個take[i]的情況，必須選擇不拿前一個數，所以take[i]=ignore[i-1]+i*(i出現次數)；  
而ignore[i]則有可能是拿前一個，也有可能是不拿，取較大者，所以ignore[i]=max(take[i-1],ignore[i-1])。  
例如[1,1,1,1,1,1,1,2,3,4,4,4,4,4]這種情況，ignore[3]=ignore[2]=take[1]。  

>步驟3：處理base cases  
在這題的base cases很單純，在還沒處理任何數之前，拿或不拿的值都只能是0。  

因為我們只會用到前一次的DP狀態，其實可以節省空間，只要take和ignore兩個變數就可以完成。

```python
class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        table = [0]*10001

        for n in nums:
            table[n] += 1

        take = ignore = 0
        for i in range(10001):
            take, ignore = ignore+i*table[i], max(take, ignore)

        return max(take, ignore)
```
