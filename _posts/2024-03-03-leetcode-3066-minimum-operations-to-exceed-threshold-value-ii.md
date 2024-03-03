---
layout      : single
title       : LeetCode 3066. Minimum Operations to Exceed Threshold Value II
tags        : LeetCode Medium Array Heap Simulation
---
雙周賽125。

## 題目

輸入整數陣列 nums，以及整數 k。  

每次操作，你可以：  

- 選擇 nums 中，最小的兩個元素 x 和 y  
- 從 nums 中刪除 x 和 y  
- 將 min(x, y) * 2 + max(x, y) 插入陣列中的任意位置  

求**最少**需要幾次操作，才能使得 nums 中所有元素都**大於等於** k。  

## 解法

要取**最小值**，又要**加入**元素，選擇 min heap 正合適。  

維護 min heap，將原本的 nums 全部加入，之後按照題意模擬。  
注意某些語言可能會溢位。  

時間複雜度 O(N log N)。  
空間複雜度 O(N)。  

```python
class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        # h = nums
        # heapify(h)
        h = []
        for x in nums:
            heappush(h, x)
        
        ans = 0
        while len(h) >= 2 and h[0] < k:
            x = heappop(h)
            y = heappop(h)
            t = min(x, y) * 2 + max(x, y)
            heappush(h, t)
            ans += 1
            
        return ans
```
