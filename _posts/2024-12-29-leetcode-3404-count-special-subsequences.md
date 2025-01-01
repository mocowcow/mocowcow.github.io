---
layout      : single
title       : LeetCode 3404. Count Special Subsequences
tags        : LeetCode Medium Math HashTable PrefixSum
---
weekly contest 430。  
比 Q4 還難的奇妙題，但我竟然做出來了。  
雖然當下很開心，但是看到 Q4 一堆人過，排名爛掉就有夠難受。  

## 題目

輸入正整數陣列 nums。  

**特殊序列**是一個長度為 4，以 (p q, r, s) 表示的索引，其中 p < q < r < s。  
且滿足以下條件：  

- nums[p] \* nums[r] == nums[q] \* nums[s]。  
- 相鄰索引之間至少間隔**一個**元素。也就是 q - p > 1, r - q > 1 且 s - r > 1。  

求 nums 有多少**特殊子序列**。  

## 解法

p, q, r, s 對應的值以下記做 x, a, y, b，要滿足：  
> x \* y = a \* b  

我第一個直覺是**移項**，變成：  
> x / b = a / y  

雖然在數學上是正確的，但是考慮到浮點數**精度誤差**，很有可能有誤差問題，馬上改想其他辦法。  

---

注意到 nums 的長度 N = 1000，應該是在暗示 O(N^2)，枚舉 (a, b) 的話應該可行。  
既然知道 ab，就可以枚舉滿足 xy = ab 的因子對 (x, y)。  

為了知道 xy 的因子有哪些，先枚舉 nums 中的所有 (x, y) 數對，加入 xy 的因子，並以集合去重維護。  
例如：  
> x, y = 2, 2  
> 4 的因子對有 (2, 2)  
> x, y = 1, 4  
> 4 的因子對有 (1, 4)  

當然，x, y 對調也可以。方便起見我們只維護 x < y，實際使用到時再處理。  

粗估一下，在 x <= y <= 1000 時，任意乘積 xy 的組成至多 29 種，複雜度 O(sqrt(N))。  
但在 nums 中不可能每個都達到最大值，實際計算量不會這麼多。  

---

現在知道因子對有哪些，還需要快速求區間 x, y 頻率的方法。  
既然是區間查詢，就想到**前綴和**。剛好 nums 中至多 1000 種數。這部分複雜度也是 O(N^2)。  

時間複雜度 O(N^2 \* sqrt(N))。  
空間複雜度 O(N^2)。  

```python
class Solution:
    def numberOfSubsequences(self, nums: List[int]) -> int:
        N = len(nums)

        factors = defaultdict(set)
        for i in range(N):
            for j in range(i+2, N):
                x, y = nums[i], nums[j]
                if x > y:
                    x, y = y, x
                factors[x*y].add((x, y))

        ps = [None for _ in range(N+1)]
        ps[0] = [0] * 1001
        for i, x in enumerate(nums):
            ps[i+1] = ps[i].copy()
            ps[i+1][x] += 1

        # (x, a, y, b)
        ans = 0
        for i in range(2, N):
            for j in range(i+4, N):
                mul = nums[i] * nums[j]  # (a, b)
                for x, y in factors[mul]:
                    # x in [0, i-2]
                    # y in [i+2, j-2]
                    cnt_x = ps[i-2+1][x]
                    cnt_y = ps[j-2+1][y]-ps[i+2-1+1][y]
                    ans += cnt_x * cnt_y

                    if x != y:
                        # y in [0, i-2]
                        # x in [i+2, j-2]
                        cnt_y = ps[i-2+1][y]
                        cnt_x = ps[j-2+1][x]-ps[i+2-1+1][x]
                        ans += cnt_x * cnt_y

        return ans
```
