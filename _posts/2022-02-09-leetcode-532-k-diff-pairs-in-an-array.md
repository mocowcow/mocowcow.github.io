---
layout      : single
title       : LeetCode 532. K-diff Pairs in an Array
tags 		: LeetCode Medium HashTable TwoPointers Sorting BinarySearch
---
這題有好多種解法，不知道為何一堆人點爛就是。

# 題目
輸入一個整數陣列nums及正整數k，求滿足條件的數對(nums[i], nums[j])有多少個。  
>   0 <= i < j < nums.length  
    |nums[i] - nums[j]| == k

# 解法
使用雜湊表計算各整數出現次數。  
當k=0時，該數必須出現2次以上才能成對；k>0時，則檢查n+k是否存在。

```python
class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        ctr=Counter(nums)
        ans=0
        
        for n in ctr:
            if k==0 and ctr[n]>1 or k>0 and (n+k) in ctr:
                ans+=1
        
        return ans
```

排序後，使用雙指標。  
j必須保持在i之後，若j被i趕上或是nums[i]+k超過nums[j]時，j往後移動。  
且必須去重複，題目只要求數對而不是指針，當nums[i]與nums[i-1]相同時，直接跳過，或是nums[i]+k不足nums[j]時，i往後移動。  
若不滿足以上條件，則代表nums[i]+k=nums[j]了，答案+1，把i,j都往後移動。

```python
class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        N = len(nums)
        nums.sort()
        ans = i = j = 0
        while i < N and j < N:
            if j <= i or nums[i]+k > nums[j]:
                j += 1
            elif i > 0 and nums[i] == nums[i-1] or nums[i]+k < nums[j]:
                i += 1
            else:
                ans += 1
                i += 1
                j += 1

        return ans
```

其實也可以用二分搜解決，程式碼就不附上了。  
排序後，每個nums[i]，對i+1~N-1找nums[i]+k值，找到就更新答案。一樣要去重複，如果nums[i]=nums[i-1]則跳過。