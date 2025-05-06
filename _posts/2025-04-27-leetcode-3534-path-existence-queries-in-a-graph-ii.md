---
layout      : single
title       : LeetCode 3534. Path Existence Queries in a Graph II
tags        : LeetCode Hard HashTable Sorting BinarySearch BinaryLifting
---
weekly contest 447。  
花了點時間整理倍增模板，以後可以節省不少時間。  

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

時間複雜度 O((n log n) + (Q log n log n))。  
空間複雜度 O(n log n)。  

```python
class Solution:
    def pathExistenceQueries(self, n: int, nums: List[int], maxDiff: int, queries: List[List[int]]) -> List[bool]:
        pos = sorted(range(n), key=lambda x: nums[x])
        mp = [0] * n
        for i, old_idx in enumerate(pos):
            mp[old_idx] = i

        N = n
        MX = N.bit_length()

        # f[i][jump]: 從 i 跳 2^jump 次的位置
        f = [[-1]*MX for _ in range(N)]

        # 初始化每個位置跳一次
        j = 0
        for i in range(N):
            while j+1 < N and nums[pos[j+1]] - nums[pos[i]] <= maxDiff:
                j += 1
            f[i][0] = j

        # 倍增遞推
        for jump in range(1, MX):
            for i in range(N):
                temp = f[i][jump-1]
                if temp != -1:  # 必須存在中繼點
                    f[i][jump] = f[temp][jump-1]

        # x 跳 step 次可否抵達 y
        def ok(x, y, step):
            for jump in range(MX):
                if step & (1 << jump):
                    x = f[x][jump]
            return x >= y

        def solve(x, y):
            if x == y:
                return 0

            if x > y:
                x, y = y, x

            lo, hi = 1, n+1
            while lo < hi:
                mid = (lo + hi) // 2
                if not ok(x, y, mid):
                    lo = mid + 1
                else:
                    hi = mid

            if lo <= n:
                return lo
            return -1

        return [solve(mp[x], mp[y]) for x, y in queries]
```

可能有同學會問：為什麼大神的做法不需要二分搜？  
沒錯，上述做法可以繼續優化，把二分和倍增合併同時做。  

---

二分找最小值，實際上是找**第一個滿足條件**的 step。  
假設存在合法的答案 step 存在，理論上可以由若干個 f[i][jump] 組成。  

但有個小問題，f[i][jump] 的定義是從 i 跳 2^jump 次後的位置。  
如果後面沒有其他可達的位置，則不管跳幾次都會停在同一點，無法得到正確的 step。  
例如：  
> nums = [.., 99, 100], maxDiff = 1  

不管從 99 跳幾次都會停在 100。沒辦法得到正確 step。  

---

所以我們需要小小的修改，改找**最後一個不滿足條件** 的位置，即保證 x 跳躍後依然小於 y。  
如果某個 f[x][jump] >= y，則代表更大的 jump 肯定也至少會到 y，都不滿足限制，需要找更小的 jump。  

如果由大到小枚舉 jump，一旦 f[x][jump] >= y，則代表他可能超過 step，不跳；  
否則從 x 跳到 f[x][jump]，並記錄跳了 2^jump 次。  

按照上述二分邏輯，x 會停在**最後一個**小於 y 的點。  
若存在合法的答案 step，按照定義，**從 x 再跳一次**肯定能到 y 上 (有可能超過 y)。  

注意：最後判斷 x >= y，而非 x == y。  

時間複雜度 O((n + Q) log n)。  
空間複雜度 O(n log n)。  

```python
class Solution:
    def pathExistenceQueries(self, n: int, nums: List[int], maxDiff: int, queries: List[List[int]]) -> List[bool]:
        pos = sorted(range(n), key=lambda x: nums[x])
        mp = [0] * n
        for i, old_idx in enumerate(pos):
            mp[old_idx] = i

        N = n
        MX = N.bit_length()

        # f[i][jump]: 從 i 跳 2^jump 次的位置
        f = [[-1]*MX for _ in range(N)]

        # 初始化每個位置跳一次
        j = 0
        for i in range(N):
            while j+1 < N and nums[pos[j+1]] - nums[pos[i]] <= maxDiff:
                j += 1
            f[i][0] = j

        # 倍增遞推
        for jump in range(1, MX):
            for i in range(N):
                temp = f[i][jump-1]
                if temp != -1:  # 必須存在中繼點
                    f[i][jump] = f[temp][jump-1]

        # x >= y 最少要跳幾次
        # -1 表示跳不到
        def min_jump(x, y):
            if x == y:
                return 0

            if x > y:
                x, y = y, x

            # 最多先跳到 y-1
            step = 0
            for jump in reversed(range(MX)):
                temp = f[x][jump]
                if temp < y:
                    x = temp
                    step += 1 << jump

            # 再跳一次
            step += 1
            x = f[x][0]

            if x >= y:
                return step
            return -1

        return [min_jump(mp[x], mp[y]) for x, y in queries]
```
