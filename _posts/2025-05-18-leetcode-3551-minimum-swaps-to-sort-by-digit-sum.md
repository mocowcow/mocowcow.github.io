---
layout      : single
title       : LeetCode 3551. Minimum Swaps to Sort by Digit Sum
tags        : LeetCode Medium Simulation Sorting HashTable DFS UnionFind
---
weekly contest 450。  
本次寫起來最難受的一題，換來換去腦子差點打結。  

## 題目

<https://leetcode.com/problems/minimum-swaps-to-sort-by-digit-sum/description/>

## 解法

首先按題目要求排序 nums，將排序後的結果記做 target。  
逐一檢查每個位置 nums[i]，查看是否與 target[i] 相同：  

- 相同，不需操作  
- 不同，則找到 target[i] 當前位置 j，把 nums[i], nums[j] 交換  

需要快速查找某個元素 val 當前位於 nums 的位置。  
建立映射表 pos，其中 pos[val] = j，代表 pos 位於 nums[j]。  
每次換位 nums[j] 的值會改變，記得要更新映射表。  

時間複雜度 O((N log MX) + (N log MX))，其中 MX = max(nums)。  
空間複雜度 O(N)。  

```python
class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        N = len(nums)

        # expected pos of val after sorting
        target = [[sum(int(c) for c in str(val)), val] for val in nums]
        target = [x[1] for x in sorted(target)]

        # current pos of val
        pos = {}
        for i, val in enumerate(nums):
            pos[val] = i

        # swap val to target pos
        ans = 0
        for i in range(N):
            t = target[i]
            # swap
            if nums[i] != t:
                ans += 1
                # t at nums[j]
                j = pos[t]
                # swap i,j then update mapping
                nums[i], nums[j] = nums[j], nums[i]
                pos[nums[i]] = i
                pos[nums[j]] = j

        return ans
```

本題其實有個經典結論，不需要模擬交換過程。  
很多大神都是直接照結論算答案，而且出題者的提示也是如此。  

一個長度 N 的陣列 a，最差情況下需要交換幾次？
先來看看相對單純的案例：  
> a = [5,1,2,3,4]  
> target = [1,2,3,4,5]  
> a[0] 放錯了，正確值在 a[1]，交換 a[0], a[1]  
> a = [1,5,2,3,4]  
> a[1] 放錯了，正確值在 a[2]，交換 a[1], a[2]  
> a = [1,2,5,3,4]  
> a[2] 放錯了，正確值在 a[3]，交換 a[2], a[3]  
> a = [1,2,3,5,4]  
> a[3] 放錯了，正確值在 a[4]，交換 a[3], a[4]  
> a = [1,2,3,4,5]  
> a[4] 終於放對了  

交換 N-1 後，最後的值一定會被排擠到正確位置上。所以**至多換 N 次**。  

---

但有時候初始位置就正確，或是某些位置之間並無關連：  
> t = [1,2,3,4]  
> a = [1,2,3,4] 不需要換  
> a = [1,2,4,3] 需要換 1 次  
> a = [2,1,4,3] 需要換 2 次  
> a = [4,1,2,3] 需要換 3 次  

對於每個 val，其原本位置為 i，正確位置為 j。  
若把 j 畫一個箭頭指向 i，最後會得到若干個**環**。例如：  

![示意圖](/assets/img/3551.jpg)  

根據上述結論，每個大小為 sz 的環需交換 sz-1 次。  

---

t 是排序後的正確位置，而輸入陣列 a 可以透過換位變成 t。  
稱 a 是 t 的**置換**或是**排列** (permutation)。  
把每個元素指向排序後的正確位置，會生成若干個環，這些環稱做**置換環**。  

每個大小為 sz 的置換環需要 sz-1 次交換。  
若原陣列大小為 N，構成 cnt 個置換環，則需要 N - cnt 次交換。  

問題轉換成：  
> 求所有環的大小。本題求連通塊大小也可以  

或是：  
> 求置換環數量  

dfs 求環大小。  

```python
class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        N = len(nums)

        # expected pos of val after sorting
        target = [[sum(int(c) for c in str(val)), val] for val in nums]
        target = [x[1] for x in sorted(target)]
        mp = {val: i for i, val in enumerate(target)}

        ans = 0
        vis = [False] * N

        def dfs(i):
            if vis[i]:
                return 0
            vis[i] = True
            return dfs(mp[nums[i]]) + 1

        for i in range(N):
            if not vis[i]:
                ans += dfs(i) - 1 # cycle sz - 1

        return ans
```

也可以用併查集找連通塊，然後再算大小。  

```python
class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        N = len(nums)

        # expected pos of val after sorting
        target = [[sum(int(c) for c in str(val)), val] for val in nums]
        target = [x[1] for x in sorted(target)]
        mp = {val: i for i, val in enumerate(target)}

        uf = UnionFind(N)
        for i, x in enumerate(nums):
            uf.union(i, mp[x])

        return N - uf.component_cnt


class UnionFind:
    def __init__(self, n):
        self.parent = [0] * n
        self.component_cnt = n  # 連通塊數量
        for i in range(n):
            self.parent[i] = i

    def union(self, x, y):
        px = self.find(x)
        py = self.find(y)
        if px != py:
            self.component_cnt -= 1  # 連通塊減少 1
            self.parent[px] = py 

    def find(self, x):
        if x != self.parent[x]:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
```
