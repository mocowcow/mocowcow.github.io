---
layout      : single
title       : LeetCode 3395. Subsequences with a Unique Middle Mode I
tags        : LeetCode Hard Math PrefixSum
---
biweekly contest 146。
本來看到 MOD 以為是 dp，原來是數學。  

## 題目

輸入整數陣列 nums，求有多少長度 5 的**唯一中間眾數**序列。  
答案可能很大，先模 10^9 + 7 後回傳。  

**眾數**指的是序列中出現**最多**的元素。  
如果一個序列中只有一個眾數，則稱**唯一眾數**。  
長度 5 的序列 seq，如果他中間的數字 seq[2] 是唯一眾數，則稱**唯一中間眾數**序列。  

## 解法

以下簡稱**唯一中間眾數**為**合法**。  

在各種序列、路徑問題，**枚舉中間**是常用的技巧，可以簡單的分別討論兩側情況。  
況且本題的重點就在於中間元素 seq[2]，可以枚舉 nums[i] = seq[2] = x，再枚舉左右選什麼元素。  

我們需要知道 nums[i] = x 的左邊出現過什麼數才能枚舉，也就是**前綴和**。  
右邊的也要，其實就是**前後綴分解**。  

---

在 x >= 3 時，無論如何都合法。  
在 x = 2 時，加選其他三個都不同的數也合法。  

光是一個序列中要搞 4 種數就快煩死了，直接不想做。  
但是**正難則反**，根據排容原理，合法數 = 總數 - 不合法。  

總共有 comb(N, 5) 種序列，扣掉不合法的，即為合法。  

---

不合法的情況倒是單純不少，但還是很麻煩。分類討論：  

- x = 1，全都不合法。  
- x = 2，且 y = 2 不合法。  
  - case1: yy x x_
  - case2: y_ x xy
  - case3: x_ x yy
  - case4: xy x y_
- x = 2，且 y = 3 不合法。  
  - case3: x_ x yy  
  - case4: xy x y_  

可見至多只會出現三種不同的數。  
x 已經確定，只需要枚舉 y。第三種至多用到一次，非 x, y 的隨便選。  
兩邊分別求**組合數**，然後**乘法原理**相乘即可。  

時間複雜度 O(N^2)。  
空間複雜度 O(N^2)。  

```python
MOD = 10 ** 9 + 7
class Solution:
    def subsequencesWithMiddleMode(self, nums: List[int]) -> int:
        N = len(nums)

        # 前後綴分解
        pre = [None] * N
        pre[0] = Counter([nums[0]])
        for i in range(1, N):
            pre[i] = Counter(pre[i-1])
            pre[i][nums[i]] += 1

        suf = [None] * N
        suf[-1] = Counter([nums[-1]])
        for i in reversed(range(N-1)):
            suf[i] = Counter(suf[i+1])
            suf[i][nums[i]] += 1

        # 全排列，扣掉不合法的
        ans = comb(N, 5)
        keys = suf[0].keys()
        for i in range(2, N-2):
            x = nums[i]
            l_cnt, r_cnt = i, N-1-i
            prei, sufi = pre[i-1], suf[i+1]

            # x = 1，全都不合法
            # 左右各選 2 個不為 x 的
            l, r = l_cnt - prei[x], r_cnt - sufi[x]
            ans -= comb(l, 2) * comb(r, 2)

            for y in keys:
                if y == x:
                    continue

                # x = 2，y = 3 全都不合法
                #   case1: yy x xy
                ans -= comb(prei[y], 2) * sufi[x] * sufi[y]
                #   case2: xy x yy
                ans -= prei[x] * prei[y] * comb(sufi[y], 2)

                # x = 2，y >= 2 不合法
                #   case1: yy x x_
                ans -= comb(prei[y], 2) * sufi[x] * (r_cnt - sufi[x] - sufi[y])
                #   case2: y_ x xy
                ans -= prei[y] * (l_cnt - prei[x] - prei[y]) \
                    * sufi[x] * sufi[y]
                #   case3: x_ x yy
                ans -= prei[x] * (l_cnt - prei[x] - prei[y]) * comb(sufi[y], 2)
                #   case4: xy x y_
                ans -= prei[x] * prei[y] * \
                    sufi[y] * (r_cnt - sufi[x] - sufi[y])

        return ans % MOD
```

其實後綴直接透過前綴計算就好，節省空間，速度也快了不少。  

時間複雜度 O(N^2)。  
空間複雜度 O(N)。  

```python
MOD = 10 ** 9 + 7
class Solution:
    def subsequencesWithMiddleMode(self, nums: List[int]) -> int:
        N = len(nums)

        # 前後綴分解
        pre = Counter()
        suf = Counter(nums)

        # 全排列，扣掉不合法的
        ans = comb(N, 5)
        keys = suf.keys()
        for i, x in enumerate(nums):
            l_cnt, r_cnt = i, N-1-i
            suf[x] -= 1
            pre_x, suf_x = pre[x], suf[x]

            # x = 1，全都不合法
            # 左右各選 2 個不為 x 的
            l, r = l_cnt - pre_x, r_cnt - suf_x
            ans -= comb(l, 2) * comb(r, 2)

            for y in keys:
                if y == x:
                    continue

                pre_y, suf_y = pre[y], suf[y]
                pre_z, suf_z = (l_cnt - pre_x - pre_y), (r_cnt - suf_x - suf_y)
                # x = 2，y = 3 不合法
                #   case1: yy x xy
                ans -= comb(pre_y, 2) * suf_x * suf_y
                #   case2: xy x yy
                ans -= pre_x * pre_y * comb(suf_y, 2)

                # x = 2，y >= 2 不合法
                #   case1: yy x x_
                ans -= comb(pre_y, 2) * suf_x * suf_z
                #   case2: y_ x xy
                ans -= pre_y * pre_z * suf_x * suf_y
                #   case3: x_ x yy
                ans -= pre_x * pre_z * comb(suf_y, 2)
                #   case4: xy x y_
                ans -= pre_x * pre_y * suf_y * suf_z

            pre[x] += 1

        return ans % MOD
```
