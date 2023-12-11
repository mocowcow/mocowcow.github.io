---
layout      : single
title       : LeetCode 2960. Count Tested Devices After Test Operations
tags        : LeetCode Easy Array Simulation
---
周賽375。

## 題目

輸入長度n的整數陣列batteryPercentages，代表各機器的電池電量。  

你的目標是依序測試第0\~n-1台機器：  

- 若第i台機器的電量大於0：  
  - 受測機器數量**增加**1  
  - 對於[i+1, n-1]之間的索引j，將第j台機器的電量**減少**1%。電量最低只能到0 %  
  - 移動到下一台機器  
- 電量不足則跳過不管  

求有多少機器會被測試。  

## 解法

題目寫了一串沒用的東西，說是電量不可低於0，實際上變成負數也不會怎樣。  
直接按照題意模擬。  

時間複雜度O(N^2)。  
空間複雜度O(1)。  

```python
class Solution:
    def countTestedDevices(self, batteryPercentages: List[int]) -> int:
        N=len(batteryPercentages)
        ans=0
        for i,x in enumerate(batteryPercentages):
            if x>0:
                ans+=1
                for j in range(i+1,N):
                    if batteryPercentages[j]>0: # no need 
                        batteryPercentages[j]-=1
                    
        return ans
```
