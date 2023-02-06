--- 
layout      : single
title       : LeetCode 2553. Separate the Digits in an Array
tags        : LeetCode Easy Array Stack
---
雙周賽97。

# 題目
輸入正整數陣列nums，將nums中所有整數分別拆成數字，裝進answer陣列中，且要保持原本的順序。  

> 例如10921，拆開變成[1,0,9,2,1]  

# 解法
懶一點的方法還是直接將整數轉成字串，遍歷其中每個字元在轉回數字，加到答案中。  

時間複雜度O(N log M)，其中N為nums長度，M為nums[i]大小。空間複雜度O(N log M)。  

```python
class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        return [int(c) for n in nums for c in str(n)]
```

使用求餘運算拆分數字時，因為會先從最右邊的數字先拆出來，可以利用stack後進先出的特性，將數字反轉後加回答案中。  

```python
class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        ans=[]
        st=[]
        for n in nums:
            while n>0:
                st.append(n%10)
                n//=10
            while st:
                ans.append(st.pop())
                
        return ans
```