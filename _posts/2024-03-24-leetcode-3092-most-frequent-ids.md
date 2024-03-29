---
layout      : single
title       : LeetCode 3092. Most Frequent IDs
tags        : LeetCode Medium Array HashTable SortedList Simulation Heap
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

如果其他語言沒有方便的有序集合，那只能用 max heap 來做了。  

heap 沒辦法隨機刪除，只能另外紀錄哪些元素**應該被刪除**，等晚一點他跑出來的時候才刪掉，這叫做**懶刪除 (lazy deletion)** 。  

時間複雜度 O(N log N)。  
空間複雜度 O(N)。  

```python
class Solution:
    def mostFrequentIDs(self, nums: List[int], freq: List[int]) -> List[int]:
        N = len(nums)
        d = Counter()
        h = [0] * N # max heap
        lazy_del = Counter()
        
        ans = []
        for id, delta in zip(nums, freq):
            # mark old freq as "to be delete"
            lazy_del[d[id]] += 1
            
            # add new freq
            d[id] += delta
            heappush(h, -d[id])
            
            # check if top element marked
            while h and lazy_del[-h[0]] > 0:
                lazy_del[-h[0]] -= 1
                heappop(h)
                
            # find max freq
            ans.append(-h[0])
            
        return ans
```

懶刪除的另一種實現方式，是在 heap 裡面同時記錄 ID。  
如果出現在頂端的 ID 與實際出現次數不符，代表他是過期的，可以刪掉。  

與上面兩種方式稍微不太相同，每次更新後必定會往 heap 加入新的元素，heap 必定不為空，所以不需要加入哨兵或是特判。  

時間複雜度 O(N log N)。  
空間複雜度 O(N)。  

```python
class Solution:
    def mostFrequentIDs(self, nums: List[int], freq: List[int]) -> List[int]:
        N = len(nums)
        d = Counter()
        h = [] # max heap
        
        ans = []
        for id, delta in zip(nums, freq):
            # add new freq
            d[id] += delta
            heappush(h, [-d[id], id])
            
            # check if top element marked
            while -h[0][0] != d[h[0][1]]:
                heappop(h)
                
            # find max freq
            ans.append(-h[0][0])
            
        return ans
```
