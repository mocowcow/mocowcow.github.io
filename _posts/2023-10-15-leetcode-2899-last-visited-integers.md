---
layout      : single
title       : LeetCode 2899. Last Visited Integers
tags        : LeetCode Easy Array String Simulation
---
雙周賽115。題目太臭長直接看範例亂寫，太粗心吃一個WA，好慘。  

## 題目

輸入字串陣列words，其中words[i]是某個整數字串，或是"prev"。  

從頭遍歷words，如果碰到"prev"，則找到在words**上次訪問**的整數：  

- 令k為"prev"連續出現次的次數，nums為目前訪問過的整數陣列，而nums_reverse是nums的反轉陣列  
- 位於nums_reverse[k-1]的元素就是當前"prev"所指的**上次訪問**的整數  
- 如果k**大於**訪問過的整數數量，則回傳-1  

回傳包含這些上次訪問整數的陣列。  

## 解法

按照題意模擬，直接維護一個反轉的整數陣列nums，根據words[i]的內容做決定。  

時間複雜度O(N)。  
空間複雜度O(N)。  

```python
class Solution:
    def lastVisitedIntegers(self, words: List[str]) -> List[int]:
        nums=deque()
        k=0
        ans=[]
        for w in words:
            if w=="prev":
                k+=1
                if k>len(nums):
                    ans.append(-1)
                else:
                    ans.append(nums[k-1])
            else:
                k=0
                nums.appendleft(int(w))
        
        return ans
```
