---
layout      : single
title       : LeetCode 3488. Closest Equal Element Queries
tags        : LeetCode Medium BinarySearch
---
weekly contest 441。
出題者最近好像很喜歡循環陣列。  

## 題目

<https://leetcode.com/problems/closest-equal-element-queries/description/>

## 解法

查詢 queries[i] = q ，找到距離 q 最近且滿足 nums[q] = nums[j] 的索引 j。  

先按照 nums[i] 的值將索引分組。按照遍歷 nums 的順序，各組索引也會是有序的。像是：  
> nums = [1,3,1,4,1,3,2]  
> nums[i] = 1 的索引有 [0,2,4]  
> nums[i] = 2 的索引有 [6]  
> nums[i] = 3 的索引有 [1,5]  
> nums[i] = 4 的索引有 [3]  

如果是**非循環**陣列，在對應組中二分找 q，最靠近的肯定是前一個或是下一個。  
> [...,a,q,b,..]  
> 答案是 min(q - a, b - q)  

---

但本題是**循環**陣列，q 往左找 a 可能會跑到另一邊去：  
> [q,b,y,z,a]  

a 不一定是在 q 左邊，所以要用絕對值求距離 abs(a - q)。  

絕對值求的是**不走循環**的距離 dist。  
整個陣列長度是 N，走另一個方向的距離是 N - dist。  

q 與 b 的距離同理。  

時間複雜度 O(N + Q log N)。  
空間複雜度 O(N)。  

```python
class Solution:
    def solveQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        N = len(nums)

        group = defaultdict(list)
        for i, x in enumerate(nums):
            group[x].append(i)

        ans = []
        for q in queries:
            x = nums[q]
            xs = group[x]
            if len(xs) == 1:
                ans.append(-1)
            else:
                idx = bisect_left(xs, q)
                sz = len(xs)

                # go left
                dis1 = abs(q - xs[idx-1])
                dis1 = min(dis1, abs(N - dis1))

                # go right
                dis2 = abs(q - xs[(idx+1) % sz])
                dis2 = min(dis2, abs(N - dis2))

                ans.append(min(dis1, dis2))

        return ans
```
