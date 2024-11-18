---
layout      : single
title       : LeetCode 3354. Make Array Elements Equal to Zero
tags        : LeetCode Easy Simulation PrefixSum
---
weekly contest 424。  

## 題目

輸入整數陣列 nums。  

選擇一個起點 curr，滿足 nums[curr] == 0，並選擇移動**方向**朝左或右。  
重複以下步驟：  

- 若 curr 超出 [0, n - 1] 之外，停止操作。  
- 若 nums[curr] == 0，若當前朝左則將 curr 減 1；否則將 curr 加 1。  
- 若 nums[curr] > 0，則將 nums[curr] 減 1，並變換方向、朝新方向移動一步。  

若能使得 nums 中所有元素變成 0，則稱做**有效選擇**。  

求有幾種**有效選擇**。  

## 解法

測資範圍不大，暴力模擬即可。  
寫個函數 ok(curr, dir) 代表起點與方向，若合法則答案加 1。  

每次檢查，最差情況下需要折返 sum(nums) 次。至多需檢查 2N 次。  

時間複雜度 O(MX \* N^2)，其中 MX = max(nums)。  
空間複雜度 O(N)。  

```python
class Solution:
    def countValidSelections(self, nums: List[int]) -> int:
        N = len(nums)

        def ok(curr, dir):
            a = nums[:]
            while 0 <= curr < N:
                if a[curr] == 0:
                    curr += dir
                else:
                    a[curr] -= 1
                    dir = -dir
                    curr += dir
            return sum(a) == 0

        ans = 0
        for i in range(N):
            if nums[i] == 0:
                for dir in [1, -1]:
                    if ok(i, dir):
                        ans += 1

        return ans
```

仔細想想，有效的情況只有兩種：  

- 起點左右兩方的元素和**相等**。  
- 起點左右兩方的元素和**相差 1**。  

使用**前綴和**就可以 O(1) 得出區間和。  
注意：兩方和相等時的有效方案數是 2。  

時間複雜度 O(N)。  
空間複雜度 O(N)。  

```python
class Solution:
    def countValidSelections(self, nums: List[int]) -> int:
        N = len(nums)
        ps = list(accumulate(nums, initial=0))
        ans = 0
        for i in range(N):
            if nums[i] == 0:
                l = ps[i] # [0..i-1]
                r = ps[N] - ps[i+1] # [i+1..N-1]
                if l == r:
                    ans += 2
                elif abs(l-r) == 1:
                    ans += 1

        return ans
```

前後綴是同步變化的，可以只用兩個變數維護。  

時間複雜度 O(N)。  
空間複雜度 O(1)。  

```python
class Solution:
    def countValidSelections(self, nums: List[int]) -> int:
        N = len(nums)
        l = 0
        r = sum(nums)
        ans = 0
        for i in range(N):
            r -= nums[i]
            if nums[i] == 0:
                if l == r:
                    ans += 2
                elif abs(l-r) == 1:
                    ans += 1
            l += nums[i]

        return ans
```
