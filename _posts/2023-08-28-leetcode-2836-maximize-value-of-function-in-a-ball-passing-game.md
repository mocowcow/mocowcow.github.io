---
layout      : single
title       : LeetCode 2836. Maximize Value of Function in a Ball Passing Game
tags        : LeetCode Hard Array Graph BitManipulation BinaryLifting
---
周賽360。這題在賽中也是標medium，結果考試的競賽的東西，確實是過分了。  
學到了一個新的知識點，叫做倍增(binary lifting)。  

## 題目

輸入長度n的整數陣列receiver，還有整數k。  

有n個玩家在玩傳球遊戲，編號分別為[0, n-1]，而receiver[i]代表第i個玩家將要傳球的下一個人。  
玩家可以傳球給自己，也就是receiver[i] = i。  

你必須選擇一個玩家開始傳球，一場遊戲需要正好傳球k次。  

假設你選擇玩家x開始，定義f(x)等於：x加上k個接球玩家的id總和。  
例如傳球順序為[1,1,1]，則f(1) = 1+1+1 = 3。  

你的目標是找到可以得到f(x)最大值的玩家x。  
求f(x)的最大值。  

注意：receiver可能出現重複值。  

## 解法

我們需要要知道n個點跑k次的分數總和，但光是k就高達10^10，直接慢慢跑肯定不行，要想個辦法快速計算。  

假設我們要從i0傳球k次，可以拆成兩個步驟：  

1. 從i0傳k/2次，抵達i1  
2. 再從i1傳k/2次，抵達i2

而這還可以繼續分解，拆成好幾個相同的子問題。我們要維護的是每個從位置i移動2^j次後的位置和成本。  
k可以被分解成log(k)個2的次方數，每次計算從i出發跳k步，只需要log(k)次傳球，

定義f[i][j]代表從玩家i開始傳球2^j次後的位置，而val[i][j]代表這2^j個接球人的id總和(不包含最開始發球的)。  
從小到大遍歷j，可以保證使用到的j-1一定被處理過。  

最後窮舉所有玩家做為出發點，若k的第j個位元為1，則傳球2^j次。傳完k次後更新答案。  

時間複雜度O(n log k)。  
空間複雜度O(n log k)。  

```python
class Solution:
    def getMaxFunctionValue(self, receiver: List[int], k: int) -> int:
        N = len(receiver)
        MX = k.bit_length()

        # f[i][jump]: 從 i 跳 2^jump 次的位置
        # -1 代表沒有下一個點
        f = [[-1]*MX for _ in range(N)]
        val = [[-1]*MX for _ in range(N)]

        # 初始化每個位置跳一次
        # 實作細節自行修改
        for i in range(N):
            f[i][0] = receiver[i]
            val[i][0] = receiver[i]

        # 倍增遞推
        for jump in range(1, MX):
            for i in range(N):
                temp = f[i][jump-1]
                if temp != -1:  # 必須存在中繼點
                    f[i][jump] = f[temp][jump-1]
                    val[i][jump] = val[i][jump-1] + val[temp][jump-1]

        # 從 x 跳 k 次
        # -1 表示不合法
        def k_jump(x, k):
            val_sm = x
            for jump in range(MX):
                if k & (1 << jump):
                    val_sm += val[x][jump]
                    x = f[x][jump]
            return val_sm

        return max(k_jump(i, k) for i in range(N))
```
