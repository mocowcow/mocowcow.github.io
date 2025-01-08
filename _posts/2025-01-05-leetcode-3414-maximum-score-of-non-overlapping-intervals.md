---
layout      : single
title       : LeetCode 3414. Maximum Score of Non-overlapping Intervals
tags        : LeetCode Hard DP BinarySearch
---
weekly contest 431。  
雖然我也是馬上想到原題，但是附加條件讓我卻步了。
總之就是很麻煩的題，雖然大概知道做法，但是寫起來全身不舒服。  

## 題目

輸入二維整數陣列 intervals，其中 intervals[i] = [l <sub>i</sub>, r <sub>i</sub>, weight <sub>i</sub>]。  
第 i 個區間從 l <sub>i</sub> 開始，於 r <sub>i</sub> 結束，且權重為 weight <sub>i</sub>。  
你至多可以選擇 **4 個互不重疊**的區間，所選擇區間的得ㄈ選擇區間的**得分**定義為區間權重的總和。  

回傳一個至多包含 4 個索引且**字典序最小**的陣列，表示從 intervals 中選擇的**互不重疊**且**得分最大**的區間。  

若兩個區間沒有任何重疊點，則稱兩者**互不重疊**。  
特別地，若兩個區間共享左邊界或右邊界，也認為是重疊的。  

## 解法

相似題 [1235. maximum profit in job scheduling]({% post_url 2022-03-24-leetcode-1235-maximum-profit-in-job-scheduling %})。  
原題是將區間以右端點排序，定義 dp[i]：前 i 個區間的最大總和。  
轉移時，透過二分搜前一個適合的區間 dp[j] 銜接。  

本題多了限制**最多選 4 個**，以及要求**最小索引**。  

---

選 4 個很簡單，只要在原本的狀態加上一次新的參數就行。  
定義 dp[i][j]：前 j 個區間選 i 個的最大總和。  

注意：因為 dp[i] 是依賴於 dp[i-1]，所以轉移時 i 要從倒序枚舉，從 dp[4] 往 dp[1] 更新。  
注意：每個 dp[i] 最初都是空的，為避免二分出界，都需要加上哨兵。  

至於維護選擇的索引，就是字面上意思，暴力維護選過的而已。  
每次加入新索引就整個排序一次，反正至多才 4 個，可以看成常數忽略不計。  

時間複雜度 O(N log N)。  
空間複雜度 O(N)。  

```python
class Solution:
    def maximumWeight(self, intervals: List[List[int]]) -> List[int]:
        a = [x + [i] for i, x in enumerate(intervals)]  # [s, e, w, index]
        a.sort(key=itemgetter(1))

        dp = [[] for _ in range(5)]
        for i in range(5): # sentinel
            dp[i] = [[0, 0, []]]  # [endtime, weight, [indexes]]

        for s, e, w, idx in a:
            for i in reversed(range(1, 5)):
                j = bisect_left(dp[i-1], s, key=lambda x: x[0]) - 1
                pre = dp[i-1][j]
                new_weight = pre[1] + w
                new_indexes = sorted(pre[2] + [idx])

                t = [e, new_weight, new_indexes] # take 
                res = dp[i][-1] # no take
                if new_weight > res[1]: # greater sum
                    res = t
                elif new_weight == res[1] and new_indexes < res[2]: # smaller indexes
                    res = t

                dp[i].append(res)

        weight = 0
        indexes = []
        for i in range(1, 5):
            t = dp[i][-1]
            if t[1] > weight: # greater sum
                weight = t[1]
                indexes = t[2]
            elif t[1] == weight and t[2] < indexes: # smaller indexes
                indexes = t[2]

        return indexes
```
