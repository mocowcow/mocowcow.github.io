---
layout      : single
title       : LeetCode 2966. Divide Array Into Arrays With Max Difference
tags        : LeetCode Medium Array Sorting
---
周賽376。應該是近幾次最簡單的Q2。  

## 題目

輸入長度n的整數陣列nums，還有正整數k。  

試將nums分割成一個或多個長度為3，且滿足以下條件的陣列：  

- nums中每個元素正好屬於一個陣列  
- 陣列任一兩個元素的差小於等於k  
  
回傳二維陣列，其中包含所有分割出的陣列。  
如果沒有合法分割方式，則回傳空陣列；若有多個答案，則回傳任一。  

## 解法

既然要將數值較近的元素分組，就先排序。  

題目保證nums長度一定是3的倍數，直接枚舉長度為3的子陣列，判斷差值是否超過k即可。  

時間複雜度O(N log N)。  
空間複雜度O(1)，答案空間不計入。  

```python
class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        N=len(nums)
        nums.sort()
        
        ans=[]
        for i in range(0,N,3):
            a,b,c=nums[i],nums[i+1],nums[i+2]
            ans.append([a,b,c])
            if c-a>k:
                return []
            
        return ans
```
