--- 
layout      : single
title       : LeetCode 2357. Make Array Zero by Subtracting Equal Amounts
tags        : LeetCode Easy Array HashTable Simulation
---
周賽304。這題還不錯，雖然我用得是暴法解，但是還能透過觀察看到更好的解法。

# 題目
輸入非負整數陣列nums。在每次動作中，你必須：  
1. 選擇一個正整數x，且x小於等於nums中最小的非零元素  
2. 將nums中所有正數扣掉x  

求最少需要幾次動作才能使nums所有元素成為0。  

# 解法
題目要求將nums變成全0的陣列，我們稍微修改，將變成0的元素從陣列中刪出，最後得到空陣列，這樣比較好處理。  

先過濾掉所有0，若陣列不為空則執行迴圈：  
- 動作次數+1  
- 找出陣列中最小值mn，將所有元素扣掉mn，若等於0則從陣列中移除  

最後回傳動作次數ans。  

```python
class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        ans=0
        ns=[x for x in nums if x>0]
        
        while ns:
            ans+=1
            mn=min(ns)
            ns=[x-mn for x in ns if x>mn]
            
        return ans
```

仔細想想，例如[1,2,3]這種狀況，刪除完第一次變成[0,1,2]，第二次變[0,0,1]，第三次才變成[0,0,0]，原來只要計算nums中有幾種非0的正整數就好。  

將nums裝入集合中，如果包含0，則將0移除，這時集合的大小正是需要的動作次數。  

```python
class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        s=set(nums)
        if 0 in s:
            s.remove(0)
            
        return len(s)
```
