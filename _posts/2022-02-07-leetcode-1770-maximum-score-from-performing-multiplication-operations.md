---
layout      : single
title       : LeetCode 1770. Maximum Score from Performing Multiplication Operations
tags 		: LeetCode Medium DP Array
---
DP教學系列。被python內建的cache坑了好幾次TLE，連MLE都出現，不斷調整cache大小才過，太噁心了。

# 題目
輸入長度N的陣列nums，及長度M的陣列multipliers，N>=M。  
你必須執行M次乘法動作，可以選擇nums中最前或是最後的數和multipliers[i]相乘，並獲得分數。nums中使用過的頭或尾必須丟掉，求最多可獲得多少分數。

# 解法
>步驟1：定義狀態  

直覺想用top-down方式，一開始我以dp(i,left,right)表示第i次動作，left、right表示nums可用的最左右方元素位置。  

>步驟2：找出狀態轉移方程式  

對於第i,left,right狀態，要先查看動左邊還是右邊之後造成的影響，何者能夠獲得更大利潤空間，並加上當回合選擇的得分。  
所以dp(i,left,right)=max(左數乘積+dp(i+1, left+1, right),右數乘積+dp(i+1, left, right+1))。

>步驟3：處理base cases  

當i=M-1時，表示處理到最後一個數字了，不必再考慮未來收入，直接回傳max(左數乘積,右數乘積)即可。

後來想到right可以通過計算得到，有點類似之前的[撿櫻桃](https://leetcode.com/problems/cherry-pickup/)，可以節省一個變數，進而將空間從M^3降到M^2。最後變成dp(i,left)。  
程式碼如下，因為懶得手動刻記憶化，結果吃了一堆紅字，得不償失。晚點再更新其他版本。


```python
class Solution:
    def maximumScore(self, nums: List[int], multipliers: List[int]) -> int:
        N = len(nums)
        M = len(multipliers)

        @lru_cache(2000)
        def dp(i, left):
            right = N-1-(i-left)
            if i == M-1:
                return max(nums[left]*multipliers[i], nums[right]*multipliers[i])
            else:
                return max(nums[left]*multipliers[i]+dp(i+1, left+1),
                           nums[right]*multipliers[i]+dp(i+1, left))

        return dp(0, 0)
```
