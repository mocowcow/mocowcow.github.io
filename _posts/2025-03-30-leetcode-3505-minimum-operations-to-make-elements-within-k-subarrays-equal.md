---
layout      : single
title       : LeetCode 3505. Minimum Operations to Make Elements Within K Subarrays Equal
tags        : LeetCode Hard DP Greedy SlidingWindow SortedList
---
weekly contest 443。  
考點滿多的，劃分型 dp、中位數貪心、滑動窗口、對頂堆。  

## 題目

<https://leetcode.com/problems/minimum-operations-to-make-elements-within-k-subarrays-equal/description/>

## 解法

從 nums 中劃分出 k 個大小為 x 的不重疊子陣列。  
對於每個 nums[i] 可**選或不選**：  

- 選 num[i..i+x-1] 劃分出子陣列，然後從 nums[i+x..] 繼續找 k-1 個子陣列。  
- 跳過 nums[i]，從 num[i+1..] 繼續找 k 個子陣列。  

不同的選法會剩下相同的元素和需求子陣列數量，有**重疊的子問題**，考慮 dp。  
定義 dp(i, rem)：從 nums[i..] 分割出 rem 個大小 x 的子陣列的**最小成本**。  
本題 k 至多 15，可看做常數。  

---

再來討論分割子陣列的成本。  
要把子陣列中所有元素改成一樣的，改成哪個修改次數最少？  
答案是**中位數**。  

透過**滑窗窗口**找出枚舉所有大小 x 子陣列的中位數。  
知道要改成中位數之後，怎麼快速求出絕對差總和？  
在窗口大小變化的同時，也要順便維護左右**半邊的元素和**。  
相似題 [480. sliding window median]({% post_url 2023-04-28-leetcode-480-sliding-window-median %})。  

使用兩個 sorted list 維護中位數。  
設左邊的 L 維護前 l_cnt = (x+1) / 2 小的數；右邊的 R 維護剩餘 r_cnt = x - l_cnt 個數。  
取左中位數 median = L[-1]：  

- L 中的所有數改成 median 的成本為 (l_cnt \* median) - sum(L)  
- R 中的所有數改成 median 的成本為 sum(R) - (l_cnt \* median)  

---

先預處理所有子陣列劃分成本 cost[i] 後，答案即 dp(0, k)。  

時間複雜度 O(N log N + Nk)。  
空間複雜度 O(Nk)。  

```python
from sortedcontainers import SortedList as SL

class Solution:
    def minOperations(self, nums: List[int], x: int, k: int) -> int:
        N = len(nums)
        cost = get_median_cost(nums, x)

        @cache
        def dp(i, rem):
            if rem == 0:
                return 0
            if i == N:
                return inf
            res = dp(i+1, rem) # skip
            if i + x <= N: # take
                res = min(res, dp(i+x, rem-1) + cost[i])
            return res

        ans = dp(0, k)
        dp.cache_clear() # prevent MLE
        
        return ans


def get_median_cost(nums, sz):
    N = len(nums)
    l_sz = (sz+1) // 2
    r_sz = sz - l_sz
    l_sm = r_sm = 0
    L = SL()
    R = SL()

    def adjust():
        nonlocal l_sm, r_sm
        while len(L) > l_sz:
            t = L.pop()
            l_sm -= t
            R.add(t)
            r_sm += t
        while len(L) < l_sz and R:
            t = R.pop(0)
            r_sm -= t
            L.add(t)
            l_sm += t

    cost = [inf] * N
    for i in reversed(range(N)):
        x = nums[i]
        L.add(x)
        l_sm += x
        adjust()
        if len(L) + len(R) == sz:
            # median greedy
            median = L[-1]
            l_cost = (l_sz * median) - l_sm
            r_cost = r_sm - (r_sz * median)
            cost[i] = l_cost + r_cost

            t = nums[i+sz-1]
            if t in L:
                L.remove(t)
                l_sm -= t
            else:
                R.remove(t)
                r_sm -= t
            adjust()
    return cost
```
