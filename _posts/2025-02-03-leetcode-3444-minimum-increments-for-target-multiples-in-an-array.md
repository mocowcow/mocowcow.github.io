---
layout      : single
title       : LeetCode 3444. Minimum Increments for Target Multiples in an Array
tags        : LeetCode Hard BitManipulation Bitmask DP
---
weekly contest 435。  
還挺難的，大概是以前偏難的 Q4 水準。  
而且時間卡的有點緊，差點沒過。  

## 題目

<https://leetcode.com/problems/minimum-increments-for-target-multiples-in-an-array/description/>

## 解法

target 中的元素簡稱 t。  
可以透過操作使得 nums 中的元素 x，變成若干個 t 的倍數 mul，成本為 mul - x。  
當然也可以不操作。  

不同的操作方案可以成為相同 t 的倍數，有**重疊的子問題**，考慮 dp。  
t 至多 4 個，可以用 bitmask 表示每個 t 是否已經找到倍數。考慮**狀壓 dp**。  

---

若想把 x 變成 t 的倍數 mul，且**成本最小**，應選擇**第一個大於等於 t** 的 mul。  
則 mul = ceil(q / t) * t。成本為 x - mul。  

```python
def get_cost(x, t):
    q = (x + t - 1) // t
    mul = q * t
    return mul - x

    # 等價一行
    return (x + t - 1) // t * t - x
```

---

原本以為枚舉 x 變成任意 t，但這是不對的。  
範例二很好心告訴我們：  
> nums = [8,4], target = [10,5]  
> 把 8 變成 10，同時滿足 t = 10,5  

一個 mul 可以同時滿足多個 t。  
甚至有時候 mul 根本都不在 target 中：  
> nums = [2,3,11], target = [3,4]  
> 把 11 變成 12，同時滿足 t = 3,4  

問題來了：怎麼有效率的找 mul？  

---

其實也很簡單，一堆元素的**共同倍數**，又要**越小越好**。  
正是**最小公倍數** lcm。  

枚舉任意 target 所有子集的遮罩 sub，維護對應的 lcm。  
dp 時枚舉子集 sub 與對應的 lcm，嘗試使 x 變成 lcm 的倍數 mul，以成本更新答案。  

定義 dp(i, mask)：使得 nums[i..N-1] 滿足 mask 對應 t 的倍數的最小成本。  
答案入口為 dp(0, (1 << M) - 1)。  

時間複雜度 O(N \* 4^M)，其中 N = len(nums)，M = len(target)。  
空間複雜度 O(N \* 2^M)。  

```python
class Solution:
    def minimumIncrements(self, nums: List[int], target: List[int]) -> int:
        N, M = len(nums), len(target)

        mask_to_lcm = {}
        for mask in range(1 << M):
            l = 1
            for i, t in enumerate(target):
                if (1 << i) & mask:
                    l = lcm(l, t)
            mask_to_lcm[mask] = l

        @cache
        def dp(i, mask):
            if mask == 0:
                return 0
            if i == N:
                return inf

            # no change
            res = dp(i + 1, mask)

            # try lcm of subsets
            x = nums[i]
            for sub, t in mask_to_lcm.items():
                if mask & sub != sub: # not subset
                    continue
                new_mask = mask ^ sub
                cost = (x + t - 1) // t * t - x
                res = min(res, dp(i + 1, new_mask) + cost)
            return res

        return dp(0, (1 << M) - 1)
```
