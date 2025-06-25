---
layout      : single
title       : LeetCode 3589. Count Prime-Gap Balanced Subarrays
tags        : LeetCode Medium Math SlidingWindow TwoPointers SortedList
---
biweekly contest 159。

## 題目

<https://leetcode.com/problems/count-prime-gap-balanced-subarrays/description/>

## 解法

相似題 [3578. count partitions with max min difference at most k]({% post_url 2025-06-09-leetcode-3578-count-partitions-with-max-min-difference-at-most-k %})。  
如果忽略**質數**和**至少 2 個**限制的話，概念幾乎相同。  

---

首先篩質數。方便起見，把非質數的 nums[i] 改成 0。以下討論到的元素都是質數。  

對於子陣列問題，常見技巧是**枚舉右、維護左**。  
枚舉右端點，維護左端點最遠到哪。  

子陣列長度越大，極值差**只增不減**。  
可用 sorted list 維護子陣列的元素，**滑動窗口**維護最大合法子陣列。若極值差超過 k 則縮減左端點。  
右端點 = i，最遠左端點 = j 時，[j..i] 都是極值差不超過 k 的左端點，有 i-j+1 個子陣列。  

---

但題目還要求子陣列**至少兩個元素**。  

同樣道理，另外維護變數 j2，表示**至多一個**質數的最遠左端點。  
一個質數的情況下，極值差等於 0，也滿足不超過 k 的條件，有 j <= j2。  
[j2..i] 質數都不夠，扣除 i-j2+1 個子陣列。  

兩項整理：  
> i-j+1 - (i-j2+1)  
> j2-j  

時間複雜度 O(N log N)。  
空間複雜度 O(N)。  

```python
from sortedcontainers import SortedList as SL

MX = 10 ** 5 + 5
sieve = [True] * (MX + 1)
sieve[0] = sieve[1] = False
for i in range(2, int(MX ** 0.5) + 1):
    if sieve[i]:
        for j in range(i * i, MX + 1, i):
            sieve[j] = False


class Solution:
    def primeSubarray(self, nums: List[int], k: int) -> int:
        for i, x in enumerate(nums):
            if not sieve[x]:
                nums[i] = 0

        ans = 0
        j1 = 0  # leftbound for k-diff
        sl = SL()
        j2 = 0  # to delete: at most 1 prime
        cnt = 0
        for i, x in enumerate(nums):
            if x > 0:
                cnt += 1
                sl.add(x)

                # maintain k-diff
                while sl[-1] - sl[0] > k:
                    if nums[j1] > 0:
                        sl.remove(nums[j1])
                    j1 += 1

                # maintain at most 1 prime
                while cnt > 1:
                    if nums[j2] > 0:
                        cnt -= 1
                    j2 += 1

            # # add k-diff
            # ans += i-j1+1
            # # delete at most 1 prime
            # ans -= i-j2+1
            ans += j2-j1

        return ans
```
