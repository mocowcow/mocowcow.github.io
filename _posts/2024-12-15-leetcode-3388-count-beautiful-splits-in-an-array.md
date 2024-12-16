---
layout      : single
title       : LeetCode 3388. Count Beautiful Splits in an Array
tags        : LeetCode Medium
---
weekly contest 428。  
Q3 比前面兩題更垃圾。  
超級迷惑測資範圍，出題者預期 O(N^2) 解，但是給 N = 5000。光看就很危險，寫下去不是 TLE 就是 MLE。  

更智障的是 nums[i] 最大 50，這數字不知道有什麼意義，直接把陣列硬轉成字串後竟然可以 O(N^3) 過。  
該過的全死光，該擋的檔不住，希望出題者以後別再出了。  

## 題目

輸入陣列 nums。  

一個**美麗**的陣列分割方案滿足：  

- 將 nums 分割成三個**非空**子陣列 nums1, nums2, nums3，滿足 nums1 + nums2 + nums3 = nums。  
- nums1 是 nums2 的前綴，**或者**， nums3 是 nums3 的前綴。  

求滿足以上條件的**分割方案數**。  

## 解法

以下簡稱三個子陣列為 a1, a2, a3。  

---

廢話不多說，先上一個不該過卻通過的做法。  

MX = max(nums) 至多 51，對應到大小寫字母綽綽有餘。小於 26 轉大寫、大於等於 26 轉小寫。  
然後枚舉 a1 的右端點 i，再枚舉 a2 的右端點 j，用內建函數檢查是否為前綴即可。  

時間複雜度 O(N^3)。  
空間複雜度 O(N)。  

```python
class Solution:
    def beautifulSplits(self, nums: List[int]) -> int:
        N = len(nums)
        a = []
        for x in nums:
            if x < 26:
                a.append(chr(97-65+x))
            else:
                a.append(chr(97-26+x))
        s = "".join(a)

        # a1 = [..i-1], sz1 = i
        # a2 = [i..j-1], sz2 = j-i
        # a3 = [j..], sz3 = N-j
        ans = 0
        for i in range(1, N-1):
            a1 = s[:i]
            for j in range(i+1, N):
                a2 = s[i:j]
                a3 = s[j:]
                if a2.startswith(a1) or a3.startswith(a2):
                    ans += 1

        return ans
```
