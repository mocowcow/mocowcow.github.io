---
layout      : single
title       : LeetCode 3075. Maximize Happiness of Selected Children
tags        : LeetCode Medium Array Greedy Sorting
---
周賽388。

## 題目

輸入長度 n 的整數陣列 happiness，還有**正整數** k。  

有 n 個小孩在排隊，其中第 i 個小孩的**幸福度**為 happiness[i]。  

你必須在 k 個回合中，選擇 k 個小孩。  
每回合，你選擇一個小孩後，其餘**未被選擇過**的小孩的幸福度都會減少 1。  
注意：幸福度只有在正數時才會減少，也就是最低降到 0。  

求選擇 k 個小孩的**最大**幸福度總和。  

## 解法

在不考慮幸福度減少的前提下，選擇幸福度最高的 k 個小孩是最佳方案。  
但是考慮每回合遞減，要用怎樣的順序選擇比較好？  

舉個極端的例子：  
> happiness = [3,2,1], k = 3  
> 從大的開始選  
> 得到 3 + 1 + 0 = 4  
> 從小的開始選  
> 得到 1 + 1 + 1 = 3  

幸福度不為負，從大的開始選，如果幸福度小於減少量，就可以**少損失**一些；反之，從小的開始選，較晚選的幸福度就更有機會被扣好扣滿。  
因此選 k 個最大的幸福度，扣除減少量後，加入答案即可。  

時間複雜度 O(n log n)。  
空間複雜度 O(1)。  

```python
class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        happiness.sort()
        ans = 0
        for dec in range(k):
            x = happiness.pop()
            ans += max(0, x - dec)
            
        return ans
```
