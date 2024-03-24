---
layout      : single
title       : LeetCode 3092. Most Frequent IDs
tags        : LeetCode Medium Array HashTable SortedList Simulation
---
周賽 390。

## 題目

有一個 ID 的集合，各 ID 的出現次數會隨著時間改變。  

輸入兩個長度 n 的整數陣列 nums 和 freq。  
nums 中的每個元素都代表一個 ID，而對應的 freq 代表 ID 在每步驟的變化量：  

- 如果 freq[i] 是正數，則 ID = nums[i] 會增加 freq[i] 次  
- 如果 freq[i] 是負數，則 ID = nums[i] 會減少 freq[i] 次  

回傳長度同為 n 的陣列 ans，其中 ans[i] 代表在第 i 步驟後，集合中**出現最多次的 ID** 的**出現次數**。  
若集合為空，則 ans[i] = 0。  

## 解法

除了要維護各 ID 的出現次數，同時還要維護各 ID 的出現次數。  
每次 ID 的出現次數改變後，要從容器中刪除舊的次數，然後加入新的次數。而且還要能快速查詢最大次數。  
因此選用 sorted list。  

一開始所有的 ID 次數都是 0，全部加入 sorted list 裡面初始化。  
之後按照上述流程模擬即可。  

時間複雜度 O(N log N)。  
空間複雜度 O(N)。  

```python
from sortedcontainers import SortedList as SL

class Solution:
    def mostFrequentIDs(self, nums: List[int], freq: List[int]) -> List[int]:
        N = len(nums)
        d = Counter()
        sl = SL([0] * N)

        ans = []
        for id, delta in zip(nums, freq):
            # del old freq
            sl.remove(d[id])
            # add new freq
            d[id] += delta
            sl.add(d[id])
            # find max freq
            ans.append(sl[-1])
            
        return ans
```
