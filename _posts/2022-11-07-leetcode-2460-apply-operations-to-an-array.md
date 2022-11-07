--- 
layout      : single
title       : LeetCode 2460. Apply Operations to an Array
tags        : LeetCode Easy Array
---
周賽318。一直想著移動完0之後，若有兩個相鄰元素又相等，到底要不要再次操作？看來是我想太多。  

# 題目
輸入大小為n，由非負整數組成的陣列nums。  
你需要對該陣列執行n-1次操作，在第i次操作中：  
- 如果nums[i] == nums[i+1]，則將nums[i]乘以2，並將nums[i+1]設為0；否則跳過此次操作  

執行完**所有**操作後，將所有的移到陣列的末端。  
- 例如數組[1,0,2,0,0,1]變成[1,2,1,0,0,0]  

回傳操作後的陣列。注意，一次只能對一個索引i執行操作，而非同時對全部索引操作。  

# 解法
先照著題意，把相鄰且相同的數字合併到左邊，右邊歸零。最後初始化長度n的空陣列，依序把非零元素寫進去後回傳。  

時空間複雜度O(N)。  

```python
class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        N=len(nums)
        
        for i in range(N-1):
            if nums[i]==nums[i+1]:
                nums[i]*=2
                nums[i+1]=0
        
        ans=[0]*N
        write=0
        for n in nums:        
            if n!=0:
                ans[write]=n
                write+=1
        
        return ans
```

也可以不需要額外空間，直接在原陣列寫入新值。  

時間複雜度O(N)，空間複雜度O(1)。  

```python
class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        N=len(nums)
        
        write=0
        for i in range(N):
            if i+1<N and nums[i]==nums[i+1]:
                nums[i]*=2
                nums[i+1]=0
            if nums[i]:
                nums[write]=nums[i]
                write+=1
                
        while write<N:
            nums[write]=0
            write+=1
        
        return nums
```
