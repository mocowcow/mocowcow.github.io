--- 
layout      : single
title       : LeetCode 2729. Check if The Number is Fascinating
tags        : LeetCode Easy String Simulation bitmask BitManipulation HashTable
---
雙周賽106。

# 題目
輸入由三位數的整數n。  

如果n符合以下條件，則稱為**迷人的**：  
- 將n和n\*2和n\*3**連接**在一起，其中數字1\~9各出現一次，且沒有0  

若n是**迷人的**則回傳true，否則回傳false。  

**連接**指的是直接加在後方。例如121和371連接為121371。  

# 解法
直接照字面意思操作，轉成字串後檢查出現次數。  

輸入的n固定為三位數，所以轉成字串只需要三或四次運算，可以視為常數。時間複雜度O(1)。  
出現數字也只有10種，空間複雜度O(1)。  

```python
class Solution:
    def isFascinating(self, n: int) -> bool:
        s=str(n)+str(n*2)+str(n*3)
        d=Counter(s)
            
        return "0" not in d and len(s)==len(d)==9 
```

也可以使用bitmask維護出現狀態，因為不允許0，初始值可以直接將第0位的bit設置成已出現。  

其實還有一個小小的剪枝，如果n*3達到1000必定為false。  
因為9個數字各出現一次，必定是9個位元，若2n或是3n有四個位數，根據鴿巢原理，至少有某個數字會出現兩次以上。  

時間複雜度O(1)。  
空間複雜度O(1)。    

```python
class Solution:
    def isFascinating(self, n: int) -> bool:
        if n*3>=1000:
            return False

        mask=1
        for i in range(1,4):
            x=n*i
            while x>0:
                r=x%10
                x//=10
                if mask&(1<<r):
                    return False
                mask|=(1<<r)
        
        return True
```