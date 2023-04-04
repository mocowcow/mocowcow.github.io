--- 
layout      : single
title       : LeetCode 2610. Convert an Array Into a 2D Array With Conditions
tags        : LeetCode Medium Array Matrix HashTable
---
周賽339。滿普通的題，如果測資範圍大一點就只能用雜湊表做。  

# 題目
輸入整數陣列nums。你必須透過nums構造一個符合下列需求的二維陣列：  
- 二維陣列中**只**包含nums中出現過的元素  
- 每列的元素**不可重複**  
- 列數**越小越好**  

回傳構造出的二維陣列。若有多種答案，則選擇任意一種。  

注意：每列的元素數量可以不相同。  

# 解法
先統計每個元素的出現次數，並不斷遍歷這些獨特的元素。把還有剩餘次數的元素加進新的列中，直到全部使用過為止。  

時間複雜度O(N^2)。空間複雜度O(N)。  

```python
class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        d=Counter(nums)
        remain=len(nums)
        ans=[]
        
        while remain:
            ans.append([])
            for k in d:
                if d[k]>0:
                    d[k]-=1
                    ans[-1].append(k)
                    remain-=1
                    
        return ans
```

如果測資大一點，上面方法可能會超時，必須及時刪除掉剩餘0次的鍵值。  

時間複雜度O(N)。空間複雜度O(N)。  

```python
class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        d=Counter(nums)
        ans=[]
        
        while d:
            ans.append(list(d.keys()))
            for k in ans[-1]:
                d[k]-=1
                if d[k]==0:
                    del d[k]
                    
        return ans
```