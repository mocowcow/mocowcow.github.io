--- 
layout      : single
title       : LeetCode 2549. Count Distinct Numbers on Board
tags        : LeetCode Easy Array Simulation
---
周賽330。挺爛的題目描述，沒事寫什麼10^9，花一段時間才搞懂想問什麼。  

# 題目
輸入正整數n，初始時n放在桌面上。接下來的10^9天，你必須執行以下動作：  
- 對於每個放在桌上的數字x，找到符合1 <= i <= n且滿足x % i ==1 的所有數字i   
- 然後將這些數字i放到桌面上  

求經過10^9天之後，桌面上有多少**不同**的整數。  

注意：  
- 一旦某個數字被放到桌面上，他會一直保留到結束  
- %代表取餘運算，例如14 % 3等於2  

# 解法
正整數取餘數之後只會變小，而且不會是負數，因此可以從n\~1逐一處理。  

維護陣列長度n+1的陣列table，分別代表各數字x是否存在於桌面上，並初始n為true。  
從n往下遍歷到1之間的每個數字x，若x存在於桌面上，則再分別對x以1\~n的取餘數，並將所有餘數為1的i擺放到桌面上。  

最後遍歷一次table，統計出現在桌面上的數字個數。  

時間複雜度O(n^2)。空間複雜度O(n)。  

```python
class Solution:
    def distinctIntegers(self, n: int) -> int:
        table=[False]*(n+1)
        table[n]=True
        
        for x in reversed(range(1,n+1)):
            if table[x]:
                for i in range(1,n+1):
                    if x%i==1:
                        table[i]=True
                        
        return sum(table)
```
