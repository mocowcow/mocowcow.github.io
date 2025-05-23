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

以下將 nums 記做 a。  
將 a 排序後的結果記做 b。  

逐一檢查每個位置 a[i]，查看是否與 b[i] 相同：  

- 相同，不需操作  
- 不同，則找到 b[i] 當前位置 j，把 a[i], a[j] 交換  

需要快速查找某個元素 x 當前位於 a 的位置。  
建立映射表 mp_a，其中 mp_a[x] = j，代表 x 位於 a[j]。  
每次換位 a[j] 的值會改變，記得要更新映射表。  

時間複雜度 O((N log MX) + (N log MX))，其中 MX = max(nums)。  
空間複雜度 O(N)。  

```python
class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        a = nums
        N = len(a)

        b = [[sum(int(c) for c in str(x)), x] for x in a]
        b = [x for _, x in sorted(b)]
        mp_a = {x: i for i, x in enumerate(a)}  # 元素 x 當前位於 a 的位置

        cnt = 0
        for i, x in enumerate(b):
            if a[i] != x:
                j = mp_a[x]  # x 當前位於 a[i] 的位置
                a[i], a[j] = a[j], a[i]
                mp_a[a[j]] = j  # a[j] 的元素換位過，記得更新
                cnt += 1

        return cnt
```

本題其實有個經典結論，不需要模擬交換過程。  
很多大神都是直接照結論算答案，而且出題者的提示也是如此。  

一個長度 N 的陣列 a，最差情況下需要交換幾次？
先來看看相對單純的案例：  
> a = [5,1,2,3,4]  
> b = [1,2,3,4,5]  
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
> b = [1,2,3,4]  
> a = [1,2,3,4] 不需要換  
> a = [1,2,4,3] 需要換 1 次  
> a = [2,1,4,3] 需要換 2 次  
> a = [4,1,2,3] 需要換 3 次  

對於每個 val，其原本位置為 i，正確位置為 j。  
若把 j 畫一個箭頭指向 i，最後會得到若干個**環**。例如：  

![示意圖](/assets/img/3551.jpg)  

根據上述結論，每個大小為 sz 的環需交換 sz-1 次。  

---

b 是排序後的正確位置，而 a 可以透過換位變成 b  
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
        a = nums
        N = len(a)

        b = [[sum(int(c) for c in str(x)), x] for x in a]
        b = [x for _, x in sorted(b)]
        mp_b = {x: i for i, x in enumerate(b)}

        def dfs(i):
            if vis[i]:
                return
            vis[i] = True
            dfs(mp_b[a[i]])

        vis = [False] * N
        cnt = 0
        for i in range(N):
            if not vis[i]:
                cnt += 1
                dfs(i)

        return N - cnt
```

也可以用併查集找連通塊，然後再算大小。  

```python
class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        a = nums
        N = len(a)

        b = [[sum(int(c) for c in str(x)), x] for x in a]
        b = [x for _, x in sorted(b)]
        mp_b = {x: i for i, x in enumerate(b)}

        uf = UnionFind(N)
        for i, x in enumerate(a):
            uf.union(i, mp_b[x])
            
        return N - uf.component_cnt

class UnionFind:
        def __init__(self, n):
            self.parent = list(range(n))
            self.component_cnt = n  # 連通塊數量

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
