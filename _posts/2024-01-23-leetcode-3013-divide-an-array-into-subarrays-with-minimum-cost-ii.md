---
layout      : single
title       : LeetCode 3013. Divide an Array Into Subarrays With Minimum Cost II
tags        : LeetCode Hard Array SlidingWindow TwoPointers SortedList
---
雙周賽122。資料結構題，本身並不是太難。但是前一題 Q3 太燒腦筋，根本沒時間寫了。  

## 題目

輸入長度 n 的整數陣列 nums，還有兩個正整數 k 和 dist。  

一個陣列的**成本**等於他的**第一個元素**。例如 [1,2,3] 的成本是 1。  

你要將 nums 分割成 k 個的獨立子陣列，且**第二個**子陣列的開頭索引和**第 k 個**子陣列的開頭索引的差值必須**小於等於** dist。  
也就是說，nums 分割成子陣列 nums[0..(i<sub>1</sub> - 1)], nums[i<sub>1</sub>..(i<sub>2</sub> - 1)], ..., nums[i<sub>k-1</sub>..(n - 1)]，滿足 i<sub>k-1</sub> - i<sub>1</sub> <= dist。  

求分割 k 個陣列的最小總成本。  

## 解法

和原題差不多，只是變成要分割成 k 個子陣列，所以要選 nums[0] 加上**額外自選** k-1 個最小的元素。  
以下所稱第_個元素都是**自選**的 k-1　個，並非必選的 nums[0]。  

除此之外，**第一個**元素索引和**最後一個**元素索引的差必須要在 dist 以內。其實就是一個滑動窗口的概念，在大小為 dist+1 的窗口中選擇 k-1 個最小值。  
也就是說，當第一個索引是 left 時，則最後一個索引 right 必須滿足 left < right <= min(left + dist, N-1)；  
或是當最後一個索引是 right 時，第一個索引 left 必須滿足 max(1, right - dist) < left < right，因為 nums[0] 不可以是自選的。  

---

綜上所述，我們需要枚舉窗口的右邊界 right，同時將 right 作為最後一個索引，然後在窗口內剩下的 dist 個元素中，選 k-2 個最小值。測資很好心的保證**k - 2 <= dist**，所以一定有答案。  
在 k 很大的情況下，每次暴力計算總和肯定會超時，需要其他技巧來維護前 k-2 小元素的和。  

我想到的是類似[480. sliding window median]({% post_url 2023-04-28-leetcode-480-sliding-window-median %})的作法，維護兩個有序容器 s1, s2，其中 s1 只裝 k-2 個最小值，並維護其總和 cost；其餘的丟到 s2 當候補，等到 s1 中的最小值過期、不足 k-2 個時，才從 s2 中挑最小的進去補。  

每次窗口右移，加入新值 x 時，總是先加入 s1：  

- 如果 s1 超過 k-2 個，則刪掉最大的值，丟到 s2 去，並從 cost 扣除  
- 不超過，則維持不變  

窗口右移，同時受到 dist 的限制的左邊界也會右移。需要刪掉出界的元素 out：  

- 如果 out 小於等於 s1 的**最大值**，則代表他一定在 s1 裡面。從 s1 刪除並從 cost 扣除  
    這時 s1 會不足 k-2 個：  
  - 如果 s2 有候補，就拉 s2 的最小值進去 s1，並增加 cost  
  - s2 是空的就算了，反正之後擴展邊界一樣會加到 s1  
- 否則一定在 s2 裡面，從 s2 中刪除  

---

雖然說是維護大小為 dist 的窗口，總共有 N 個，但還要分兩邊保持順序，有序容器每次操作O(log dist)。  

時間複雜度 O(N log dist)。  
空間複雜度 O(dist)。  

```python
from sortedcontainers import SortedList as SL

class Solution:
    def minimumCost(self, nums: List[int], k: int, dist: int) -> int:
        N = len(nums)
        ans = inf
        s1 = SL() # k-2 smallest 
        s2 = SL() # other candidates
        cost = nums[0]
        
        # we need k-1 smallest 
        # enumerate last(k-th) element
        # and keep k-2 other smallest
        for right in range(1, N):
            x = nums[right]
            # enough for total k-1 elements
            # update ans and pop expired element
            if len(s1) == k-2:
                ans = min(ans, cost + x)
                # pop expired
                left = right - dist
                if left >= 1:
                    out = nums[left]
                    if out <= s1[-1]: # in s1
                        s1.remove(out)
                        cost -= out
                        # add cand from s2
                        if s2:
                            cand = s2[0]
                            s2.remove(cand)
                            s1.add(cand)
                            cost += cand
                        
                    else: # in s2
                        s2.remove(out)
                    left += 1
            
            # expand right
            s1.add(x)
            cost += x
            if len(s1) > k-2:
                out = s1[-1]
                s1.remove(out)
                cost -= out
                s2.add(out)
            
        return ans
```
