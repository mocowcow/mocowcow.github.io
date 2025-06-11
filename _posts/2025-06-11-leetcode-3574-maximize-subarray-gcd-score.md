---
layout      : single
title       : LeetCode 3574. Maximize Subarray GCD Score
tags        : LeetCode Hard Math
---
biweekly contest 158。

## 題目

<https://leetcode.com/problems/maximize-subarray-gcd-score/description/>

## 解法

子陣列的分數等於長度乘 gcd。  
先考慮不能修改的情況，只需要暴力枚舉所有子陣列求 gcd 即可。  

---

若可以把某些元素修改成兩倍，要改誰才能讓 gcd 變大？  

回想小學時候怎麼算 gcd 的：  
> 把數字質因數分解，然後每個質因數取兩邊較小的出現次數  

例如 gcd(12,30)：  
> 12 = 2^2 \* 3^1  
> 30 = 2^1 \* 3^1 \* 5^1  
> gcd(12,30) = 2^1 \* 3^1  

換句話說，gcd 中質因數的出現次數，是取決於在兩數中的最小出現次數而定。  

如果把某數乘 2，也只會影響到 2，其餘質因數不受影響。  
我們可以先把 nums[i] 的因子 2 提取出來，次數記做 pow2[i]。  

---

兩數 gcd 質因數的 2 的指數是取較小者。  
同理，多數求 gcd 的質因數指數是求**最小**者。  

因此應該選擇子陣列中 **2 出現次數最小者**進行修改。  
設陣列中元素的 2 的最少出現次數為 mn，而次數為 mn 的元素有 cnt 個。  
若能把 cnt 個元素都修改，則能使 2 在 gcd 的次數變成 mn + 1 次；否則維持 mn 次。  

時間複雜度 O(N^2 log MX)，其中 MX = max(nums)。  
空間複雜度 O(1)。  

```python

class Solution:
    def maxGCDScore(self, nums: List[int], k: int) -> int:
        N = len(nums)

        pow2 = [0] * N
        for i in range(N):
            while nums[i] % 2 == 0:
                pow2[i] += 1
                nums[i] //= 2

        ans = 0
        for i in range(N):
            g = 0
            mn = inf
            cnt = 0
            for j in range(i, N):
                g = gcd(g, nums[j])
                if pow2[j] < mn:
                    mn = pow2[j]
                    cnt = 1
                elif pow2[j] == mn:
                    cnt += 1

                score = g * (j-i+1) * (1 << mn)
                if cnt <= k:
                    score *= 2

                # ans = max(ans, score)
                if score > ans:  # speed up
                    ans = score

        return ans
```
