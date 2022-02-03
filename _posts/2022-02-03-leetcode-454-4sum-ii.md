---
layout      : single
title       : LeetCode 454. 4Sum II
tags 		: LeetCode Medium HashTable
---
# 題目
輸入四個長度為N的整數陣列，求滿足nums1[i] + nums2[j] + nums3[k] + nums4[l] == 0的組合(i, j, k, l)有幾種。

# 解法
題目只要求數量，沒有要詳細組合，那麼只需要用計算的方式就好。  
n1+n2+n3+n4=0移項得到n1+n2=-(n3+n4)，把問題分成兩部分，遍歷所有(i, j)及(k, l)組合，使其兩兩相加，並用dict紀錄出現次數，再遍歷其中一個dict，對另一個dict以相反數查值，並將乘積加入ans。  
>n1+n2=10，n3+n4必須為-10，才符合要求總和為0。  
所以答案必須加上d1[10]*d2[-10]  

>例：nums1 = [1,2], nums2 = [-2,-1], nums3 = [-1,2], nums4 = [0,2]  
ans = d1[1]\*d2[-1] + d1[0]\*d2[0] + d1[-1]\*d2[1]  
ans = 1\*1 + 2\*0 + 1\*1 = 2


key|d1 value| d2 value
----|----|----
-1|1|1
0|2|0
1|1|1
2|0|1
4|0|1


```python
class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        N = len(nums1)
        d1 = defaultdict(int)
        d2 = defaultdict(int)

        for i in range(N):
            for j in range(N):
                d1[nums1[i]+nums2[j]] += 1
                d2[nums3[i]+nums4[j]] += 1

        ans = 0
        for k, v in d1.items():
            ans += v*d2[-k]

        return ans
```
