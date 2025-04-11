---
layout      : single
title       : LeetCode 3510. Minimum Pair Removal to Sort Array II
tags        : LeetCode Hard Simulation SortedList BinarySearch
---
weekly contest 444。  

## 題目

<https://leetcode.com/problems/minimum-pair-removal-to-sort-array-ii/description/>

## 解法

Q1 強化版，樸實無華的大模擬題。  
把 nums 中每個元素看做獨立的區間，使用有序容器維護區間進行合併即可。  

---

N 個區間會有 N-1 個相鄰對。  
為了快速判斷陣列是否非遞減，只要確保所有數對 (x, y) 都滿足 x <= y；或是說維護 x > y 的數對個數。  
若遞增數對個數 bad 大於 0，即不滿足要求，需要刪除最小的數對。  

---

設有 A, B, C, D 四個相鄰區間，對應的元素值分別為 a, b, c, d，有數對 a+b, b+c, c+d。  
試著合併合併區間 B, C：  
變成 A, B, D，元素值 a, (b+c), d，有數對 a+(b+c), (b+c)+d。  
發現除了 C 消失之外，還間接影響到了 A, B 以及 C, D 產生的數對。  

因此在合併 B, C 之前，需先移除 A, B 與 C, D 的舊數對 (如果有的話)。  
然後拿 BC 合併後的值重新計算 A, BC 與 BC, D 產生的新數對。  
最後才執行 B, C 的合併。  

注意：在新增 / 刪除數對時，也要更新 bad 的計數。  

時間複雜度 O(N log N)。  
空間複雜度 O(N)。  

```python
class Solution:
    def minimumPairRemoval(self, nums: List[int]) -> int:
        N = len(nums)
        ids = SL(range(N))  # id for each segment
        pairs = SL()  # [sm, id], where id if for left segment
        bad = 0  # count seg[i].val > sge[i+1].val

        for i in range(N-1):
            x, y = nums[i], nums[i+1]
            pairs.add([x+y, i])
            if x > y:
                bad += 1

        ans = 0
        while bad > 0:
            ans += 1

            # assume we have seg: A,        B,      C,        D
            # corresponding to:   ids[i-1], ids[i], ids[i+1], ids[i+2]
            sm, B = pairs.pop(0)  # min pair sum from seg B, C
            i = ids.bisect_left(B)  # idx for B
            C = ids[i+1]  # id for C

            # check if A, B exists
            if i > 0:
                A = ids[i-1] # id for A
                # old pair
                pairs.remove([nums[A]+nums[B], A])
                if nums[A] > nums[B]:
                    bad -= 1
                # new pair
                pairs.add([nums[A]+sm, A])
                if nums[A] > sm:
                    bad += 1

            # check if C, D exists
            if i+2 < len(ids):
                D = ids[i+2] # id for D
                # old pair
                pairs.remove([nums[C]+nums[D], C])
                if nums[C] > nums[D]:
                    bad -= 1
                # new pair
                pairs.add([sm+nums[D], B])
                if sm > nums[D]:
                    bad += 1

            # merge B, C by remove C
            ids.pop(i+1)  # or seg.remove(C)
            if nums[B] > nums[C]:
                bad -= 1
            nums[B] = sm

        return ans
```
