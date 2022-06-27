--- 
layout      : single
title       : LeetCode 2317. Maximum XOR After Operations
tags        : LeetCode Medium Array BitManipulation
---
雙周賽81。超級腦筋急轉彎，想了一陣子才做出來，但終究是走了遠路。

# 題目
輸入正整數陣列nums，在更新每次動作中，你可以選擇任意的非負整數x和nums[i]，將nums[i]的值更新為nums[i] AND (nums[i] XOR x)。  
求做完**任意次更新**後，將nums中所有元素做XOR運算，最大結果為多少。

# 解法
先看看那一長串的更新是在幹什麼。  
nums[i]可以和任意非負數做XOR，其實就是可以生成任何數字的意思。
而nums[i]和某數做AND運算，會把非兩者共通的1位元全部清除，換句話說，不管怎樣都不可能超過nums[i]。  
兩者加起來，就是可以把nums[i]中的任何1位元變成0。  

再來是所有元素做XOR運算，兩個0合成一個1，兩個1合成一個0，要保持特定組成使結果為1。  
但我們可以操作nums[i]中不超過自身大小的任何位元，所以一定可以讓結果為0。  

結論：在nums[i]中所有出現過1位元的地方，都可以讓他在答案中出現。  

nums[i]最大值是10^8，真要說的話最多是27個bit，當時粗略計算用30綽綽有餘。  
檢查nums中每個數字n，若對應位元1，則加入set中。最後查看那些地方出現過1位元，更新到答案中。  

```python
class Solution:
    def maximumXOR(self, nums: List[int]) -> int:
        s=set()
        for n in nums:
            for i in range(30):
                if n&(1<<i):
                    s.add(i)
                    
        ans=0
        for i in range(30):
            if i in s:
                ans|=(1<<i)
                
        return ans
```

其實檢查1位元的同時就可以更新答案了，而且也沒有必要繼續處理剩下的數字，直接快進到下一個位元。  
時間從上面的1800ms減半到900ms，加速不少。  

```python
class Solution:
    def maximumXOR(self, nums: List[int]) -> int:
        ans=0
        for i in range(30):
            for n in nums:
                if n&(1<<i):
                    ans|=(1<<i)
                    break
        
        return ans
```

然而最佳答案只要把全部的數字做OR運算就好，甚至可以壓縮成一行，難怪一堆人氣到不行。  

```python
class Solution:
    def maximumXOR(self, nums: List[int]) -> int:
        ans=0
        for n in nums:
            ans|=n
        return ans
```