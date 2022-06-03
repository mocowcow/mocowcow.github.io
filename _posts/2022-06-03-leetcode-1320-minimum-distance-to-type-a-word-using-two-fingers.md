--- 
layout      : single
title       : LeetCode 1320. Minimum Distance to Type a Word Using Two Fingers
tags        : LeetCode Hard String DP
---
隨便抽的，思路跑歪，不小心卡了一點時間。

# 題目
![示意圖](https://assets.leetcode.com/uploads/2020/01/02/leetcode_keyboard.png)
你有一個附圖的鍵盤，每個案件有各自的X-Y座標。  

而兩個按鍵之間的**距離**，定義為abs(x1-x2)+abs(y1-y2)。  
輸入字串word，計算只用兩根手指打字，所需要的**最小移動距離總和**。  

注意，兩根手指的初始位置是自由的，所以不必計入距離。且兩根手指也不一定要在第一和第二個字元上。  

# 解法
雖然說兩根手指自由放，但是第一根手指一定是放在word[0]對應的按鍵上。  
那麼第二根就很隨意了，從word[0]\~word[N-1]對應的任何按鍵都可以，但是一定有較佳的選擇。之後每個字母分別嘗試用兩根手指選一根按。    
雖然一看就知道是DP，不過我一直糾結要怎麼表示還沒放下去的手指，想半天才發現設成-1就好。  

定義dp(i,f1,f2)：現在要決定word[i]用哪隻手指按，而目前兩根手指分別在f1, f2上方。  
轉移方程式：dp(i,f1,f2)=min(dp(i+1,word[i],f2)+(word[i]和f1距離), dp(i+1,f1,word[i])+(word[i]和f2距離))  
base case：當i超出word邊界時，代表所有字母都打完了，不需要再移動，回傳0。  

因為要考慮到剛開始手指還沒下放，距離計算的部分比較麻煩，拉出來寫成一個函數dist，若其中有位置是-1，代表手指未下放，直接回傳0；否則計算兩按鍵位置後回傳。  

一開始兩根手指都是自由的，所以都是-1，直接回傳dp(0,-1,-1)就是答案。  

```python
class Solution:
    def minimumDistance(self, word: str) -> int:
        N=len(word)
        
        def dist(c1,c2):
            if c1==-1 or c2==-1:
                return 0
            return abs(c1//6-c2//6)+abs(c1%6-c2%6)
        
        @cache
        def dp(i,f1,f2):
            if i==N:
                return 0
            c=ord(word[i])-65
            move1=dp(i+1,c,f2)+dist(f1,c)
            move2=dp(i+1,f1,c)+dist(f2,c)
            return min(move1,move2)
            
        return dp(0,-1,-1)
```

後來想想好像不需要特別處理未下放的手指，反正第一個手指一定是按word[0]，那麼我們直接在i=1窮舉所有位置作為手指二的出發點，求其中最小的結果就是答案。

```python
class Solution:
    def minimumDistance(self, word: str) -> int:
        N=len(word)
        
        def dist(c1,c2):
            return abs(c1//6-c2//6)+abs(c1%6-c2%6)
        
        @cache
        def dp(i,f1,f2):
            if i==N:
                return 0
            c=ord(word[i])-65
            move1=dp(i+1,c,f2)+dist(f1,c)
            move2=dp(i+1,f1,c)+dist(f2,c)
            return min(move1,move2)
        
        ans=inf
        f1=ord(word[0])-65
        for i in range(N):
            f2=ord(word[i])-65
            ans=min(ans,dp(1,f1,f2))
        return ans
```