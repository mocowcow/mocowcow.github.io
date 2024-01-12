---
layout      : single
title       : LeetCode 3002. Maximum Size of a Set After Removals
tags        : LeetCode Medium Array Math HashTable Greedy
---
周賽379。想了二十分鐘，想到個很神奇的解，送出去還真對了。  

## 題目

輸入兩個長度 n 的整數陣列 nums1 和 nums2。  

你必須分別從 nums1 和 nums2 之中移除 n/2 個元素。  
然後將留下來的元素全都加入集合 s 中。  

求 s 的**最大**大小。  

## 解法

將 n/2 記做 m。  
兩者最多合計貢獻 n 個元素。  
考慮 nums1, nums2 分別能夠向答案**加入**那些元素。  

最理想的狀況下，當然是 nums1, nums2 各擁有 n 個的元素，且**無交集**。例如：  
> nums1 = [1,2], nums2 = [3,4], union = {1,2,3,4}  

這種情況隨便選可以選滿 n 個。  

如果**有交集**，就像範例1：  
> nums1 = [1,2,1,2], nums2 = [1,1,1,1], union = {1,2}  

兩者**聯集**是{1,2}，就算無視 n 的限制，最多也只能湊出{1,2}兩個。  
可見答案受限於兩者**聯集大小**。  

再看看這個例子：  
> nums1 = [1,2,3], nums2 = [3,4,5], union = {1,2,3,4,5}  

一樣**有交集**，而且這次聯集大小超過 n。  
但是一邊最多只能提供 m 個，所以 nums1 最多提供 min(set_size(nums1), m) 個；nums2 同理。  

可以發現，聯集大小滿足 n 並不代表一定能找滿 n 個元素；但是聯集大小不足 n，一定找不滿 n 個。  
答案就是**聯集大小**和**兩者貢獻**取最小值。  

時間複雜度 O(n)。  
空間複雜度 O(n)。  

```python
class Solution:
    def maximumSetSize(self, nums1: List[int], nums2: List[int]) -> int:
        N = len(nums1)
        M = N // 2
        
        s1 = set(nums1)
        s2 = set(nums2)
        union = s1 | s2
        
        return min(
            len(union),
            min(len(s1), M) + min(len(s2), M)
        )
```

現在換成考慮答案中要**刪除**那些元素。  

兩者的**聯集** union 包含所有不同的元素。如果超出 n 個元素，則需要選擇一些刪除。  
**優先刪除**同時存在於 nums1, nums2 中的元素，也就是兩者的**交集** inter。  

如果 nums1 大於 m 個元素，則必須刪掉 set_size(nums1) - m 個多餘元素。  
優先從從交集中刪除；如果交集元素不夠，不得已才刪除 nums1 獨有的元素，這時候會使聯集變小。  
num2 同理，先從聯集刪，不夠才從交集刪。  

時間複雜度 O(n)。  
空間複雜度 O(n)。  

```python
class Solution:
    def maximumSetSize(self, nums1: List[int], nums2: List[int]) -> int:
        N = len(nums1)
        M = N // 2
        
        s1 = set(nums1)
        s2 = set(nums2)
        union = len(s1 | s2) 
        inter = len(s1 & s2)
        
        if len(s1) > M:
            to_rmv = len(s1) - M 
            inter_rmv = min(to_rmv, inter)
            union_rmv = to_rmv - inter_rmv
            # apply remove 
            inter -= inter_rmv
            union -= union_rmv
            
        if len(s2) > M:
            to_rmv = len(s2) - M 
            inter_rmv = min(to_rmv, inter)
            union_rmv = to_rmv - inter_rmv
            # apply remove 
            inter -= inter_rmv
            union -= union_rmv
                
        return union
```

另外一種**加入**的思路，是同時構造兩者的子集。  

若某個數 x 只在 nums1 或 nums2 其一出現，那麼先選 x 肯定是更好的。  
先分別找出兩者特有的元素數量。  

如果兩者還找不滿各 m 個，才在共有的**交集**元素中選擇。放到哪邊都無所謂，只要有空位就可以放。  

最後答案是兩子集大小加總。  

```python
class Solution:
    def maximumSetSize(self, nums1: List[int], nums2: List[int]) -> int:
        N = len(nums1)
        M = N // 2
        
        s1 = set(nums1)
        s2 = set(nums2)
        inter = s1 & s2
        
        cnt1 = cnt2 = 0
        for x in s1:
            if cnt1 < M and x not in s2:
                cnt1 += 1
                
        for x in s2:
            if cnt2 < M and x not in s1:
                cnt2 += 1
                
        for x in inter:
            if cnt1 < M:
                cnt1 += 1
            elif cnt2 < M:
                cnt2 += 1
                
        return cnt1 + cnt2
```
