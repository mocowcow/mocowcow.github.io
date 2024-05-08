---
layout      : single
title       : LeetCode 3139. Minimum Cost to Equalize Array
tags        : LeetCode
---
周賽 396。小小吐槽一下，答案好像沒必要模 10^9 + 7。  

## 題目

輸入整數字串 nums 和兩個整數 cost1, cost2。  
你可以執行以下兩種操作**任意次**：

- 選擇索引 i，以成本為 cost1 將 nums[i] 增加 1  
- 選擇不同的索引 i, j，以成本為 cost2 將 nums[i], nums[j] 都增加 1  

求使得陣列中所有元素相同的**最小成本**。  

答案可能很大，先模 10^9 + 7 後回傳。  

## 解法

操作一選一個數，操作二選兩個數。  
先考慮特殊情況：

- N = 1，只能用操作一  
- N = 2，操作二沒意義，也只能用操作一  
- cost1 \* 2 <= cost2，只用操作一更省錢  

除此之外的一般情況，則優先使用操作二，剩下的才使用操作一。

---

本題的操作都只能把值增加，要把所有元素都變成目標值 T。  
對於 nums 中每個元素 x，各需 T - x 次操作。將各元素所需操作次數記做陣列 diff。  

問題等價轉換成：  
> 有 N 種不同顏色的石頭，每個顏色的數量為 diff[i]  
> 每次可以挑**兩個不同顏色**的石頭一組，最多能挑幾組  
> 組數就是操作二，剩下的石頭就是操作一  

設 D = max(diff), S = sum(diff)。分類討論以下情況：  

- 情況一：S - D >= D  
    可以選 S / 2 組  
  - 若 S 是偶數，剩下 0 個石頭  
  - 若 S 是奇數，剩下 1 個石頭  
- 情況二：S - D < D  
    可以選 S - D 組，剩下 S - (S - D) \* 2 個石頭  

按照公式代入 cost，大概會變成這樣子。  

```python
def f(D, S): 
    if S - D >= D:
        op1 = S % 2
        op2 = S // 2
    else: # S - D < D
        op1 = S - (S - D) * 2
        op2 = S - D
    return cost1 * op1 + cost2 * op2
```

雖然會覺得 mx = max(nums) 是 T 的最佳選擇，然而並不是。  
在 cost1 > cost2 的情況下，有時候更大的 T 反而更划算。  
例如：  

> nums = [1,14,14,15], cost1 = 2, cost2 = 1  
> 若 T = 15, diff = [14,1,1,0], D = 14, S = 16  
> 總成本 cost = 2 \* 12 + 1 \* 2 = 26  
> 若 T = 18, diff = [17,4,4,3], D = 17, S = 28  
> 總成本 cost = 2 \* 8 + 1 \* 8 = 24  
> 若 T = 21, diff = [20,7,7,6], D = 20, S = 40  
> 總成本 cost = 2 \* 0 + 1 \* 20 = 20  

那我怎麼知道 T 最大會到多少？  

首先釐清增加 T 是為了**改變 S 和 D**，至於 T 本身並不重要。  
在一般情況下，保證 N 至少為 3。每當 T 增加 1，會使得 D 增加 1，然後 (S - D) 增加 N - 1。  

情況一的成本只和 S 的值有關，因此 T 繼續增大**必定使總成本上升**，沒有必要繼續增加。  
但情況二會因為 T 增加逐漸降低成本，最後**變成情況一**。  
成本曲線應該是類似 V 或是 U 型圖。最粗糙的判斷方式，是在**成本上升**之時停止。  

---

為了計算複雜度，還是要大概知道一下會枚舉的上界。  
在 N >= 3 的一般情況下，每次增加上界只會使得 D 和 (S - D) 的差減少 1。  
而最壞情況下 D 會是 10^6，而 (S - D) 只有 2，大概需要枚舉到兩倍的 D。  
但還要考慮到奇偶數的出現順序不同，搞不好情況二的第二個值更小，還是把上界設更大一些比較保險。  

時間複雜度 O(N + base_d)，其中 base_d = max(nums) - min(nums)。  
空間複雜度 O(1)。  

```python
MOD = 10 ** 9 + 7
class Solution:
    def minCostToEqualizeArray(self, nums: List[int], cost1: int, cost2: int) -> int:
        N = len(nums)
        mx, mn = max(nums), min(nums)
        base_d = mx - mn
        base_s = mx * N - sum(nums)
        
        # use cost1 only
        if N <= 2 or cost1 * 2 <= cost2: 
            return cost1 * base_s % MOD
        
        # make all elements to target
        def f(D, S): 
            if S - D >= D:
                op1 = S % 2
                op2 = S // 2
            else: # S - D < D
                op1 = S - (S - D) * 2
                op2 = S - D
            return cost1 * op1 + cost2 * op2
        
        ans = inf
        for d in range(base_d, base_d * 2 + 1):
            s = base_s + (d - base_d) * N
            res = f(d, s)
            if res < ans:
                ans = res
            else: # cost increasing
                break
        
        return ans % MOD
```
