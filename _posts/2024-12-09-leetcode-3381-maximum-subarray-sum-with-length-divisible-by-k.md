---
layout      : single
title       : LeetCode 3381. Maximum Subarray Sum With Length Divisible by K
tags        : LeetCode Medium Math DP PrefixSum
---
weekly contest 427。  
這題挺妙的，我本來以為做不出來，後來靠著**從特殊到一般**的技巧找出答案。  

## 題目

輸入整數陣列 nums 和整數 t。  

求 nums 中的一個**非空**子陣列的**最大**和，且子陣列長度可**被 k 整除**。  

## 解法

子陣列問題通常會考慮**滑動窗口**。  

剛開始想枚舉大小為 k 倍數的窗口，但在 k = 1 時會高達 N 種窗口大小，每次滑窗需要 O(N)，肯定超時。  

---

在想不出思路時，先觀察最特殊的情況，然後再去推廣成一般的情況。  

對本題來說最特殊的情況就是 k = 1。  
任意數量、**連續**的大小為 1 的窗口都可以合併成更大的窗口，畢竟所有數都是 1 的倍數。  
問題轉換成 [53. Maximum Subarray](https://leetcode.com/problems/maximum-subarray/)。  

這是一個經典的 dp 問題，依序枚舉元素 x 作為子陣列結尾，並判斷先前子陣列和，若是正數則保留，負數則不保留。  
此算法又稱 Kadane's algorithm。  

---

接下來考慮 k = 2 的情形。  
剛才提到**連續的** k 子陣列可以合併，也就是 2+2+2..。  
試想以下例子：  
> nums = [1,1,0,1,1], k = 2  
> 答案可以是 [1,1,0,1] 或是 [1,0,1,1]。  

發現只有左端點 (或右端點) **奇偶性**相同的子陣列才能無縫接軌合併。  
所以我們在枚舉 k = 2 的子陣列時，需要依照奇偶性分組。  

> nums = [1,1,0,1,1], k = 2  
> left = 0 偶數, sub = [1,1], sum = 2  
> left = 1 奇數, sub = [1,0], sum = 1  
> left = 2 偶數, sub = [0,1], sum = 1  
> left = 3 奇數, sub = [1,1], sum = 2  

偶數組子陣列和依序為 [2,1]，而奇數組為 [1,2]。  
分別對兩個組都做一次 kadane 即可。  

---

最後推廣到更大的 k，依照左端點對 k 取餘數後分組，每組都做 kadane 即可。  

時間複雜度 O(N)。  
空間複雜度 O(N)。  

```python
class Solution:
    def maxSubarraySum(self, nums: List[int], k: int) -> int:
        grp = [[] for _ in range(k)]
        left = 0
        sm = 0
        for right, x in enumerate(nums):
            sm += x
            if right - left + 1 == k:
                grp[left % k].append(sm)
                sm -= nums[left]
                left += 1
        
        # kadane maximum subarray for each group
        ans = -inf
        for g in grp:
            mx = -inf
            curr = 0
            for x in g:
                if curr < 0:
                    curr = x
                else:
                    curr += x
                mx = max(mx, curr)
                
            # update answer
            ans = max(ans, mx)

        return ans
```

另外一種思路是**前綴和**。  

如果有一個子陣列 nums[..i] 長度為 sz，要刪掉的前綴長度為何，才能使得剩餘子陣列長度為 k 的倍數？  

同樣從特殊到一般，k = 1 時隨便刪都行。  
k = 2 時，若 sz 是偶數，則也要扣掉偶數長度的前綴；奇數同理。  
推廣到更大的 k，子陣列必須刪掉對 k 同餘長度前綴。  
有式子：  
> pre_sum[i] - pre_min[i%k]  

為了使子陣列和盡可能大，故刪除的前綴越小越好 (負數更好)，因此維護最小值。  
注意： 在子陣列長度正好為 k 時，可以不刪除任何前綴，故 pre_min[k-1] 初始值 0。  

時間複雜度 O(N)。  
空間複雜度 O(k)。  

```python
class Solution:
    def maxSubarraySum(self, nums: List[int], k: int) -> int:
        pre_min = [inf] * k
        pre_min[k-1] = 0

        ans = -inf
        ps = 0
        for i, x in enumerate(nums):
            grp = i % k
            ps += x
            ans = max(ans, ps - pre_min[grp])
            pre_min[grp] = min(pre_min[grp], ps) 

        return ans
```
