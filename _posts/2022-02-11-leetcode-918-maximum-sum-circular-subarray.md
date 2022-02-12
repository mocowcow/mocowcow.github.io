---
layout      : single
title       : LeetCode 918. Maximum Sum Circular Subarray
tags 		: LeetCode Medium DP 
---
DP教學系列。官方解答爛到有剩，千萬不要看。想了整天最後找到[這篇](https://leetcode-cn.com/problems/maximum-sum-circular-subarray/solution/java-dp-kan-bu-dong-wei-shi-yao-sum-min-x7q53/)，得到滿意的解釋。

# 題目
輸入整數陣列nums，頭尾是相連的，求最大的子陣列和。

# 解法
kadane可以找最大值，也可以找最小值。  
題目的最大子陣列有幾種情況：
1. 無循環，最大子陣列夾在中間，普通的kadane就可以找到
2. 有循環，最大子陣列分散在頭尾，中間夾雜著其他東西，如：大.小.大

該文提到：
>【重点】使用到了环，则必定包含 A[n-1]和 A[0]两个元素且说明从A[1]到A[n-2]这个子数组中必定包含负数

有環的答案一定包含頭尾元素，那就直接求nums[1:-1]中間那段最小子陣列扣掉就可以，非常漂亮的解決情況2。  
真心感謝這位大神解決我今日的困擾。

```python
class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        N = len(nums)

        def getMax():
            dp = nums[0]
            mx = nums[0]
            for i in range(1, N):
                dp = nums[i]+max(dp, 0)
                mx = max(mx, dp)
            return mx

        def getMin():
            dp = nums[0]
            mn = 0
            for i in range(1, N-1):
                dp = nums[i]+min(dp, 0)
                mn = min(mn, dp)
            return mn

        return max(sum(nums)-getMin(), getMax())
```

[lee215大神](https://leetcode.com/problems/maximum-sum-circular-subarray/discuss/178422/One-Pass)有提出類似的解法，差別在於getMin找的範圍是整個nums陣列，當陣列全為負數時，最小陣列會等於nums合，會得到錯誤的答案0，是需要特別處理的corner case。個人更喜歡本文的解法。

