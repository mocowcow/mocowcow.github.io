---
layout      : single
title       : LeetCode 3534. Path Existence Queries in a Graph II
tags        : LeetCode Hard HashTable Sorting BinarySearch BinaryLifting
---
weekly contest 447。

## 題目

<https://leetcode.com/problems/path-existence-queries-in-a-graph-ii/description/>

## 解法

與 Q2 不同的地方有兩個：  

- nums 不保證有序  
- 不只判斷是否連通，還要求**最短距離**  

---

首先處理 nums 無序的問題。  
將所有索引 i 按照 nums[i] 的值遞增排序，記做 sorted_pos。  

可得 nums[sorted_pos[i]] <= nums[sorted_pos[i+1]]。  
sorted_pos[0] 即 nums 中最小的 nums[i]，以此類推。  

然後把原本的 i 映射至排序後的位置，記做 mp。  
之後查詢 x, y 時，取排序後的映射值 mp[x], mp[y] 即可。  

例如：  
> nums = [1,8,3,4,2]  
> sorted_pos = [0,4,2,3,1]  
> nums[0] = 1 是 sorted_pos[0]  
> nums[1] = 8 是 sorted_pos[4]  
> nums[2] = 3 是 sorted_pos[2]  
> nums[3] = 4 是 sorted_pos[3]  
> nums[4] = 2 是 sorted_pos[1]  

查詢 x, y = 2, 4：  
> sorted_pos[x] = nums[2] 排序後的位置 = 2  
> sorted_pos[y] = nums[4] 排序後的位置 = 1  

---

接下來的位置 i 指的是排序後的位置，並非指 nums[i]。  

排序後可用雙指針方法得出從 i 跳 1 次 (最遠 maxDiff) 可達最遠位置 j。  
有 n 個點，總不可能暴力一次次慢慢跳，要想辦法優化。  

既然知道 i 跳 1 次可到 j，那再從 j 跳 1 次到 k。等價於 i 跳 2 次會到 k。  
同理，從 i 跳 2 次到 t，再從 t 跳 2 次到 k。等價於 i 跳 4 次會到 k。  
更一般地說，從 i 跳 2^(jump) 次到達的點，可由跳兩次 2^(jump-1) 遞推得出。  
這種方法叫做**倍增**(binary lifting)。  

對於每個點 i，需要維護若干個跳 2^jump 次的位置，記做 f[i][jump]。  
共有 n 個點，jump 至多 O(log n) 就可以跳完所有點，複雜度 O(n log n)。  

---

就算知道 i 跳 2^jump 次的位置又能幹嘛？我們要的是準確的**所需最小次數**。  
所需次數有**單調性**，如果跳 step 次能到，則 step+1 肯定也能到；反之，step 不能，則 step-1 也不能。  
可以透過**二分答案**找到正確次數。  

維護函數 ok(x, y, step) 判斷從 x 跳 step 次是否能抵達 y。  
為方便起見約定 x <= y。  
step 可以由若干個二的冪所組成，選擇對應的 fa[x][jump] 進行跳躍，最後判斷 x >= y 即可。  

注意：若查詢 x == y 則不用跳，記得特判。  

時間複雜度 O(n log log n)。  
空間複雜度 O(n log n)。  

```python
class Solution:
    def pathExistenceQueries(self, n: int, nums: List[int], maxDiff: int, queries: List[List[int]]) -> List[bool]:
        MX = n.bit_length()

        sorted_pos = sorted(range(n), key=lambda x: nums[x])
        mp = [0] * n
        for i, old_idx in enumerate(sorted_pos):
            mp[old_idx] = i

        # find farest pos can reach by 1 jump
        f = [[-1]*MX for _ in range(n)]
        j = 0
        for i in range(n):
            while j+1 < n and nums[sorted_pos[j+1]] - nums[sorted_pos[i]] <= maxDiff:
                j += 1
            f[i][0] = j

        # binary lifting
        for jump in range(1, MX):
            for i in range(n):
                t = f[i][jump-1]
                f[i][jump] = f[t][jump-1]

        def ok(x, y, step):
            for jump in range(MX):
                if step & (1 << jump):
                    x = f[x][jump]
            return x >= y

        ans = []
        for x, y in queries:
            if x == y:  # no need to jump
                ans.append(0)
                continue

            x, y = mp[x], mp[y]
            if x > y:
                x, y = y, x

            lo, hi = 1, n + 1
            while lo < hi:
                mid = (lo + hi) // 2
                if not ok(x, y, mid):
                    lo = mid + 1
                else:
                    hi = mid

            if lo <= n:
                ans.append(lo)
            else:
                ans.append(-1)

        return ans
```
