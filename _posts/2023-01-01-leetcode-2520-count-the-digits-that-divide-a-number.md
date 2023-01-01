--- 
layout      : single
title       : LeetCode 2520. Count the Digits That Divide a Number
tags        : LeetCode Easy String
---
周賽326。元旦一大早就在打比賽，真是美好的新年。  

# 題目
輸入整數num，求num中有幾個數字能夠整除num。  

# 解法
最直觀的方法，把num轉成字串後逐一拆出數字，判斷能不能整除num。  

時間複雜度O(log N)。空間複雜度O(log N)。  

```python
class Solution:
    def countDigits(self, num: int) -> int:
        ans=0
        for c in str(num):
            n=int(c)
            if num%n==0:
                ans+=1

        return ans
```

也可以寫成一行。  

```python
class Solution:
    def countDigits(self, num: int) -> int:
        return sum(num%int(c)==0 for c in str(num))
```

轉成字串需要額外的空間，也可以直接在num上面操作，透過取餘數的方式拆出每個數字。  

時間複雜度O(log N)。空間複雜度O(1)。  

```python
class Solution:
    def countDigits(self, num: int) -> int:
        ans=0
        x=num
        while x>0:
            digit=x%10
            if num%digit==0:
                ans+=1
            x//=10
                
        return ans
```