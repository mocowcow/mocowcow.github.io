--- 
layout      : single
title       : LeetCode 2335. Minimum Amount of Time to Fill Cups
tags        : LeetCode Easy Array Sorting Greedy
---
周賽301。總感覺Q1變質了，以前幾乎都是不用動腦子的水題，這題我竟然卡住十分鐘。  

# 題目
有一台飲水機，可以提供冷、溫、熱水。每一秒可以裝2杯不同溫度的水，或是1杯任意溫度的水。  

輸入長度為3的整數陣列amount，分別代表三種溫度的所需杯數。求最少需要幾秒才能全部裝完。  

# 解法
想半天才想通，每次要挑出剩餘數量最多的兩種來裝水，裝到只剩下最後一種之後才單獨裝。  

將amount排序，如果最大的數字x於等於其餘兩種，則只需要x次。  
否則判斷次大的種類，逐次-1，使得其餘兩種平均。最後則需要兩種中較大者作為剩餘的裝水次數。  

```python
class Solution:
    def fillCups(self, amount: List[int]) -> int:
        amount.sort()
        
        if amount[2]>=amount[0]+amount[1]:
            return amount[2]
        
        for _ in range(amount[2]):
            if amount[0]>amount[1]:
                amount[0]-=1
            else:
                amount[1]-=1
                
        return amount[2]+max(amount[0],amount[1])
```

結果最佳解非常的簡短，可以把答案分成兩種情況：  
1. 有一種水非常多，答案就是他的數量  
2. 否則一次取最多的兩種，答案為總數/2，但因有可能為奇數，故向上取整  

```python
class Solution:
    def fillCups(self, amount: List[int]) -> int:
        return max(max(amount),(sum(amount)+1)//2)
```
