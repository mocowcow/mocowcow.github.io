---
layout      : single
title       : LeetCode 3392. Count Subarrays of Length Three With a Condition
tags        : LeetCode Easy Simulation
---
biweekly contest 146。

## 題目

輸入整數陣列 nums，求有多少長度為 3 的子陣列，滿足：  

- 第一個數與第三個數的和，正好為第二個數的一半。  

## 解法

尊貴的 python 可以無視陷阱，直接模擬。  

時間複雜度 O(N)。  
空間複雜度 O(1)。  

```python
class Solution:
    def countSubarrays(self, nums: List[int]) -> int:
        N = len(nums)
        ans = 0
        for i in range(N-2):
            if nums[i] + nums[i+2] == nums[i+1] / 2:
                ans += 1

        return ans
```

對於其他語言，需額外判斷中間的數是否為偶數，否則下取整會出問題。  

```go
func countSubarrays(nums []int) int {
    N := len(nums)
    ans := 0
    for i := 0; i < N-2; i++ {
        if nums[i+1] % 2 == 0 && nums[i] + nums[i+2] == nums[i+1] / 2 {
            ans++
        }
    }

    return ans
}
```

或是把等式移項：  
> a + c = b / 2  
> 2a + 2c = b  

```go
func countSubarrays(nums []int) int {
    N := len(nums)
    ans := 0
    for i := 0; i < N-2; i++ {
        if (nums[i] + nums[i+2])*2 == nums[i+1] {
            ans++
        }
    }

    return ans
}
```
