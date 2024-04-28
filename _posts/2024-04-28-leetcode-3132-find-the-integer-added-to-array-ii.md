---
layout      : single
title       : LeetCode 3132. Find the Integer Added to Array II
tags        : LeetCode Medium Array Sorting HashTable
---
周賽395。這題還真不太好想。  

## 題目

輸入兩個整數陣列 nums1 和 nums2。  

若兩個陣列中，各整數的出現頻率相同，則稱兩陣列**相等**。  
你必須先從 nums1 中移除兩個元素，然後對 nums1 的每個元素都加上一個值 x，使得 nums1 和 nums2 **相等**。  

回傳整數 x 可能的**最小值**。  

## 解法

跟前一題有點像，兩個陣列**排序後**，每組數對的差等於 x。  
只是原本的 nums1 被多塞了兩個東西 a, b。  

假設原本的 nums1 = [10, 20, 30]。  
分類討論三種情況：  

- a, b 占用了**最小、次小值**。例如：[a, b, 10, 20, 30]  
    nums1 真正的最小值應是 nums1[2]  
- a, b 只占用**最小值**，但沒占用次小值。例如：[a, 10, b, 20, 30]  
    nums1 真正的最小值應是 nums1[1]  
- a, b 沒占用最小值，也沒占用次小值。例如：[10, 20, a, b, 30]  
    nums1 真正的最小值還是 nums1[0]  

所以 x 值有可能是 nums2[0] 扣掉 nums1[0], nums1[1], nums1[2] 三者之一。  

---

雖然知道 x 可能的值，但又不知道 a, b 被塞在哪，要怎麼驗證正確性？  

建立雜湊表 freq，分別維護每個元素 val 的出現次數。如果在 nums1 出現就加 1；在 nums2 出現就減 1。  
如果某個 freq[val] 出現負數，代表 nums2 中某個元素沒有被配對到，該 x 不合法。  
若合法則更新 x 的最小值。  

時間複雜度 O(N log N)。  
空間複雜度 O(N)。  

```python
class Solution:
    def minimumAddedInteger(self, nums1: List[int], nums2: List[int]) -> int:
        nums1.sort()
        nums2.sort()
        
        def ok(x):
            freq = Counter()
            for val in nums1:
                freq[val + x] += 1
            for val in nums2:
                freq[val] -= 1
                if freq[val] < 0:
                    return False
            return True
        
        ans = inf
        for i in range(3):
            x = nums2[0] - nums1[i]
            if ok(x):
                ans = min(ans, x)
                
        return ans
```
