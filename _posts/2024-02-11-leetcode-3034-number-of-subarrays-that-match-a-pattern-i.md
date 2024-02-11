---
layout      : single
title       : LeetCode 3034. Number of Subarrays That Match a Pattern I
tags        : LeetCode Medium Array String Simulation
---
周賽384。

## 題目

輸入長度 n 的整數陣列 nums。還有長度 m 的整數陣列 pattern，只由整數 -1, 0 和 1 組成。  

若一個長度為 m+1 的子陣列 nums[i..j] 對於 pattern 中的每個元素 pattern[k] 都滿足以下條件，則該子陣列與 pattern **匹配**：  

- 若 pattern[k] == 1 則 nums[i + k + 1] > nums[i + k]  
- 若 pattern[k] == 0 則 nums[i + k + 1] == nums[i + k]  
- 若 pattern[k] == -1 則 nums[i + k + 1] < nums[i + k]  

求有多少子陣列與 pattern 匹配。  

## 解法

長度 N 的陣列中，需要切出長度為 M+1 的子陣列，共有 N-M 個。  
枚舉所有子陣列，並與 pattern 試著匹配，若成功則答案加 1。  

時間複雜度 O(MN)。  
空間複雜度 O(M)。  

```python
class Solution:
    def countMatchingSubarrays(self, nums: List[int], pattern: List[int]) -> int:
        N, M = len(nums), len(pattern)
        
        def ok(sub):
            for j, sign in enumerate(pattern):
                if sign == 1: # >
                    if not sub[j+1] > sub[j]:
                        return False
                elif sign == 0: # ==
                    if not sub[j+1] == sub[j]:
                        return False
                else: # <
                    if not sub[j+1] < sub[j]:
                        return False
            return True
        
        ans = 0
        for i in range(N - M):
            sub = nums[i:i+M+1]
            if ok(sub):
                ans += 1
        
        return ans
```

可以發現，相鄰的幾個子陣列做匹配的時候會有重複的運算。  
乾脆先根據規則把 nums 根據比較結果轉成對應的數字陣列 a。例如：  
> nums = [1,2,3,4,5,6]
> nums 中的相鄰元素互相比較
> 得到 a = [1,1,1,1,1]  

然後再去找 a 裡面有幾個子陣列等於 pattern：  
> a = [1,1,1,1,1], pattern = [1,1]
> a[0..1] = [1,1]  
> a[1..2] = [1,1]  
> a[2..3] = [1,1]  
> a[3..4] = [1,1]  
> 共 4 個  

怎麼好像有點眼熟。如果把陣列當成一個字串的話，實際上根本就是**字串匹配**問題。  
問題轉換成：在字串 a 裡面，找到有幾個子字串 pattern。  
直接套個 KMP 就過了。  

時間複雜度 O(N+M)。  
空間複雜度 O(M)。  

```python
class Solution:
    def countMatchingSubarrays(self, nums: List[int], pattern: List[int]) -> int:
        a = []
        for c1, c2 in pairwise(nums):
            if c2 > c1:
                a.append(1)
            elif c2 == c1:
                a.append(0)
            else:
                a.append(-1)
                
        ans = KMP_all(a, pattern)
        
        return len(ans)
                
# PMT optimized version
def prefix_function(s):
    N = len(s)
    pmt = [0]*N
    for i in range(1, N):
        j = pmt[i - 1]
        while j > 0 and s[i] != s[j]:
            j = pmt[j - 1]
        if s[i] == s[j]:
            j += 1
        pmt[i] = j
    return pmt

# search p in s, return every starting idnex of p
def KMP_all(s, p):
    M, N = len(s), len(p)
    pmt = prefix_function(p)
    j = 0
    res = []
    for i in range(M):
        while j > 0 and s[i] != p[j]:
            j = pmt[j - 1]
        if s[i] == p[j]:
            j += 1
        if j == N:
            res.append(i - j + 1)
            j = pmt[j - 1]
    return res
```
