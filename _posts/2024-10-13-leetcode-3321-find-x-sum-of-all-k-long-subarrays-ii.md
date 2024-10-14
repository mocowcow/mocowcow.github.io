---
layout      : single
title       : LeetCode 3321. Find X-Sum of All K-Long Subarrays II
tags        : LeetCode Hard SortedList Simulation TwoPointers SlidingWindow
---
weekly contest 419。  
這題又是 sorted list 專場，難度大降。  
可惜我寫出來的時後比賽已經結束了。  

## 題目

輸入長度 n 的整數陣列 nums，還有兩個整數 k 和 x。  

陣列的 x-sum 計算方式如下：  

- 統計陣列中所有元素的出現頻率。  
- 只保留頻率最高的前 x 種元素。若兩元素頻率相同，則保留**數值較大**者。  
- 求結果陣列的和。  

注意：若陣列中不同的元素少於 x 種，則 x-sum 等於陣列元素和。  

回傳長度為 n - k + 1 的陣列 answer，其中 answer[i] 代表子陣列 nums[i..i+k-1] 的 x-sum。  

## 解法

枚舉子陣列很容易想到**滑動窗口**優化，只保留大小 k 窗口內的所有元素。  
難點在於：如何動態維護前 x 大頻率的元素，並計算其總和？  

---

我們可以透過有序容器 sorted list 來維護各元素的出現頻率次序。  
元素頻率的排序是先比較頻率降序，然後比較元素數值降序，因此需要保存數對 (freq[val], val)。  
並以變數 tot 紀錄前 x 大元素和。  

擴展窗口右端點，增加一個元素 val 時，會使得 freq[val] 加 1。  
這時需從容器刪除 (freq[val], val)，並加入 (freq[val]+1, val)。  
分類討論對 tot 造成的影響：  

- 若修改後 val 不為前 x 大，沒有影響。  
- 若修改後 val 為前 x 大：  
  - 修改前 val 就是前 x 大，則使 tot 加 val。  
  - 修改前 val 並非前 x 大，則使 tot 加 freq[val] \* val。  
    並且會將修改前第 x 大的元素 t 踢掉，變成第 x+1 大的元素。因此 tot 要扣除 t 的貢獻。  

同理，收縮窗口左端點，刪減一個元素 val 時，會使得 freq[val] 減 1。  
這時需從容器刪除 (freq[val], val)，並加入 (freq[val]-1, val)。  
分類討論對 tot 造成的影響：  

- 若修改前 val 不為前 x 大，沒有影響。  
- 若修改前 val 為前 x 大：  
  - 修改後 val 還是前 x 大，則使 tot 減 val。  
  - 修改後 val 並非前 x 大，則使 tot 減 freq[val] \* val (注意此為修改前的 freq[val])。  
    並且會將修改前第 x+1 大的元素 t 變成第 x 大。因此 tot 要加上 t 的貢獻。  

---

將以上邏輯封裝成函數，套用滑動窗口即可。  

時間複雜度 O(N log k)。  
空間複雜度 O(N)。  

```python
from sortedcontainers import SortedList as SL
class Solution:
    def findXSum(self, nums: List[int], k: int, x: int) -> List[int]:
        freq = Counter()
        tot = 0
        sl = SL(key=lambda x:(-x[0], -x[1])) # most freq, big val
        for val in set(nums):
            sl.add([0, val])

        def add(val):
            nonlocal tot
            # remove old
            old_pos = sl.bisect_left([freq[val], val])
            sl.pop(old_pos)
            # add new
            freq[val] += 1
            sl.add([freq[val], val])
            new_pos = sl.bisect_left([freq[val], val])
            # compare position
            if new_pos < x:
                if old_pos < x:
                    tot += val
                else: # old sl[x-1] become sl[x]
                    tot += freq[val] * val
                    t = sl[x]
                    tot -= t[0] * t[1]

        def rmv(val):
            nonlocal tot
            # remove old
            old_pos = sl.bisect_left([freq[val], val])
            sl.pop(old_pos)
            # add new
            freq[val] -= 1
            sl.add([freq[val], val])
            new_pos = sl.bisect_left([freq[val], val])
            # compare position
            if old_pos < x:
                if new_pos < x:
                    tot -= val
                else: # old sl[x] become sl[x-1]
                    tot -= freq[val] * val + val # freq[val] before remove
                    t = sl[x-1]
                    tot += t[0] * t[1]

        ans = []
        left = 0
        for right, val in enumerate(nums):
            add(val)
            if right - left + 1 == k:
                ans.append(tot)
                rmv(nums[left])
                left += 1

        return ans
```
