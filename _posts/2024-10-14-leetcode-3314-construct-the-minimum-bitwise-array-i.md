---
layout      : single
title       : LeetCode 3314. Construct the Minimum Bitwise Array I
tags        : LeetCode Easy Simulation BitManipulation
---
biweekly contest 141。  

## 題目

輸入 n 個質數組成的整數陣列 nums。  

你必須構造一個長度同為 n 的陣列 ans，其中 ans[i] 滿足 ans[i] OR (ans[i] + 1) = nums[i]。  
此外，每個 ans[i] 還必須**最小化**。  

若不存在合法的 ans[i]，則 ans[i] = -1。  

## 解法

OR 運算的特性是**只增不減**。  
因此 ans[i] 肯定不超過 nums[i]。  

在 nums[i] 不大的情況下，可以從小開始枚舉所有可能的 ans[i]，第一個找到的就是答案。  

時間複雜度 O(N \* MX)，其中 MX = max(nums)。  
空間複雜度 O(1)。  

```python
class Solution:
    def minBitwiseArray(self, nums: List[int]) -> List[int]:
        ans = []
        for x in nums:
            res = inf
            for i in range(x+1):
                if i | (i+1) == x:
                    ans.append(i)
                    break
            else:
                ans.append(-1)

        return ans
```

仔細觀察 ans[i] OR (ans[i] + 1)，不管怎樣結果一定都是奇數，因此 nums[i] = 2 時肯定沒有答案。  
而 nums[i] 除了 2 以外全都是奇數，最差情況下 ans[i] = nums[i] - 1 一定可以滿足答案。  

---

除此之外暫時沒看出什麼線索，來觀察範例看看：  

| nums[i] | ans[i] |
| --- | --- |
| 3 = 0b11 | 1 = 0b1 |
| 5 = 0b101 | 4 = 0b100 |
| 7 = 0b111 | 3 = 0b11 |
| 11 = 0b1011 | 9 = 0b1001 |
| 13 = 0b1101| 12 = 0b1100 |

發現 ans[i] 似乎都是從 nums[i] **刪掉某個 1 位元**而來。  
對於 nums[i] 枚舉刪掉的位元得到 ans[i]，若合法則更新最小值。  

時間複雜度 O(N log MX)，其中 MX = max(nums)。  
空間複雜度 O(1)。  

```python
class Solution:
    def minBitwiseArray(self, nums: List[int]) -> List[int]:
        ans = []
        for x in nums:
            if x == 2:
                ans.append(-1)
            else:
                res = inf
                for i in range(x.bit_length()):
                    mask = 1 << i
                    if x & mask > 0:
                        t = x - mask
                        if t | (t + 1) == x:
                            res = min(res, t)
                ans.append(res)

        return ans
```
