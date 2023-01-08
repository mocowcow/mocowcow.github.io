--- 
layout      : single
title       : LeetCode 2530. Maximal Score After Applying K Operations
tags        : LeetCode Medium Array Heap
---
周賽327。雖然不是很難，但是Q2需要heap好像對新人來說不太友善。  

# 題目
輸入整數陣列nums，還有整數k。你的初始分數為0。  

每次動作，你可以：  
1. 選擇一個索引i，其中0 <= i < nums.length  
2. 獲得nums[i]分數  
3. 將nums[i]替換成ceil(nums[i] / 3)  

求執行**正好k次動作**後，你可以達成的**最大分數**為多少。  

# 解法
維護max heap，每次取最大的數，得到分數後，將新的值塞回去，重複k次。  
向上取整套用公式，ceil(x / 3) = (x + 3 - 1) / 3 。  

時間複雜度O(k log N)。空間複雜度O(N)。  

```python
class Solution:
    def maxKelements(self, nums: List[int], k: int) -> int:
        h=[]
        for n in nums:
            heappush(h,-n)
            
        ans=0
        for _ in range(k):
            x=-heappop(h)
            ans+=x
            heappush(h,-((x+2)//3))
            
        return ans
```
