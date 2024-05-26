---
layout      : single
title       : LeetCode 3164. Find the Number of Good Pairs II
tags        : LeetCode Medium Array Math HashTable
---
周賽 399。今天不知怎樣從 Q3 開始做，看到這爛測資範圍就覺得完蛋，肯定會卡常數免費吃 TLE。  
然後看看 Q4 也不會做，乾脆不打了。  

周賽結束後，我馬上交答案，python 果不其然 TLE，加了一些優化才過。  
然後 golang, java 隨便寫隨便過，就算硬掰說剪枝優化是這題的考核重點也沒人信。  

## 題目

輸入兩個整數陣列 nums1, nums2，長度分別是 n, m。  
還有一個正整數 k。  

一個數對 (i, j) 若滿足 nums1[i] 可被 nums2[j] \* k 整除，則稱為**好的**。  

求有多少**好的**數對。  

## 解法

測資比起 Q1 大非常多，n, m 高達 10^5，而 nums1[i], nums2[j] 高達 10^6。  

一個數 x 若可被 a 整除，則 a 必定是 x 的**因數**，同時還存在另一個因數 b = x / a。  
先遍歷 nums2，以作為因數的 nums2[j] \* k 統計出現次數。  
然後遍歷 x = nums1[i] 做**因數分解**，枚舉所有因數，並將因數的出現次數加入答案。  

時間複雜度 O(N \* sqrt(MX))，其中 MX = max(nums1[i], nums2[j])。  
空間複雜度 O()。  

MX 最大值高達 10^6，代入複雜度公式後將近 10^8 計算量，能不能過真的都是賭運氣。  
反正比賽剛結束時，我交幾次都沒過，寫題解的時候又交了幾次都全過，非常神秘。  

```python
class Solution:
    def numberOfPairs(self, nums1: List[int], nums2: List[int], k: int) -> int:
        d = Counter(x * k for x in nums2)
        ans = 0
        for x in nums1:
            for a in range(1, int(x ** 0.5) + 1):
                if x % a == 0:
                    b = x // a
                    ans += d[a]
                    if a != b:
                        ans += d[b]
                
        return ans
```
