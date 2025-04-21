---
layout      : single
title       : LeetCode 3524. Find X Value of Array I
tags        : LeetCode Medium Math DP
---
weekly contest 446。

## 題目

<https://leetcode.com/problems/find-x-value-of-array-i/description/>

## 解法

題目講得落落長，什麼刪前綴後綴的很難看懂。  
其實就是求 nums 所有**非空子陣列**，按照乘積 prod % k = x 來分組。  
ans[x] 指的是餘 x 的子陣列個數。  

先想想怎麼暴力枚舉所有子陣列？  
從左向右枚舉 nums[i] 作為子陣列的右端點，並加到原有的所有子陣列上。  
> nums = [1,2,3]  
> 右端點 i = 0  
> [1]  
> 右端點 i = 1  
> [1,2], [2]  
> 右端點 i = 2  
> [1,2,3], [2,3], [3]  

至多可達 O(N^2) 種乘積，而且還會溢位，肯定不行。  

---

我們不在乎原始的乘積，只在乎乘積取模後的結果。因此可以在計算途中就取模。  
如此按照餘數統計個數，至多只有會有 k 種餘數。  

在原本餘 r 的子陣列加上 nums[i]，其乘積餘數相當於 (x \* nums[i]) % k。  
按照此思路遞推以 nums[i] 為右端點、且餘數為 r 的子陣列個數 cnt[x]，並加入答案 ans[x]。  

時間複雜度 O(Nk)。  
空間複雜度 O(k)。  

```python
class Solution:
    def resultArray(self, nums: List[int], k: int) -> List[int]:
        ans = [0]*k
        cnt = [0]*k
        for val in nums:
            # calc prod(nums[..i]) % k
            cnt2 = [0]*k
            cnt2[val % k] += 1
            for x in range(k):
                cnt2[x*val % k] += cnt[x]
            cnt = cnt2

            # update ans
            for x in range(k):
                ans[x] += cnt[x]

        return ans

```
