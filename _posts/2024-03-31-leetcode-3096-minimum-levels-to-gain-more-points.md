---
layout      : single
title       : LeetCode 3096. Minimum Levels to Gain More Points
tags        : LeetCode Medium Array Greedy PrefixSum
---
雙周賽 127。

## 題目

輸入長度 n 的二進位陣列 possible。  

Alice 和 Bob 在玩一個總共 n 關卡的遊戲。  
possible[i] == 0 代表第 i 關可以通關，反之，possible[i] == 1 代表不可能通關。  
玩家如果通過一個關卡可以**獲得** 1 分，沒通過則**失去** 1 分。  

最初由 Alice 從關卡 0 開始，可以**依序**挑戰任意個關卡。剩餘的關卡都會由 Bob 挑戰。  
Alice 想知道他**最少**要挑戰幾關，才能獲得比 Bob 更高的分數。若不可能則回傳 -1。  

注意：每個玩家至少要挑戰一關。  

## 解法

Alice 多玩一關，Bob 就少一關。  

先求出 Bob 玩全部關卡的分數 B；而 Alice 沒玩任何關，分數 A = 0。  
之後依序枚舉前 N - 1 個關卡給 Alice 玩。如果 Alice 得分，Bob 同時也會扣分；反之亦然。  
途中當 A > B 時，直接回傳當前關卡數。  

時間複雜度 O(N)。  
空間複雜度 O(1)。  

```python
class Solution:
    def minimumLevels(self, possible: List[int]) -> int:
        N = len(possible)
        A = B = 0
        for x in possible:
            if x == 1:
                B += 1
            else:
                B -= 1
        
        for i in range(N - 1):
            if possible[i] == 1:
                A += 1
                B -= 1
            else:
                A -= 1
                B += 1
            
            if A > B:
                return i + 1
            
        return -1
```

如果把 possible 轉換成由 1, -1 構成的陣列，發現根本就是**前綴和**。  
如果 Alice 做了前面 i 題，得分為 sum(nums[0..i])，即 ps[i + 1]；  
Bob 得分為 sum(nums[(i+1)..(N-1)])，即 ps[N] - ps[i + 1]。  

```python
class Solution:
    def minimumLevels(self, possible: List[int]) -> int:
        N = len(possible)
        a = [1 if x == 1 else -1 for x in possible]
        ps = list(accumulate(a, initial=0))
        
        for i in range(N - 1):
            if ps[i + 1] > ps[N] - ps[i + 1]:
                return i + 1
        
        return -1
```

時間複雜度 O(N)。  
空間複雜度 O(N)。
