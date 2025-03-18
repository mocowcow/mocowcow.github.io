---
layout      : single
title       : LeetCode 3488. Closest Equal Element Queries
tags        : LeetCode Medium BinarySearch
---
weekly contest 441。
出題者最近好像很喜歡循環陣列。  

## 題目

<https://leetcode.com/problems/closest-equal-element-queries/description/>

## 解法

查詢 queries[i] = q ，找到距離 q 最近且滿足 nums[q] = nums[j] 的索引 j。  

先按照 nums[i] 的值將索引分組。按照遍歷 nums 的順序，各組索引也會是有序的。像是：  
> nums = [1,3,1,4,1,3,2]  
> nums[i] = 1 的索引有 [0,2,4]  
> nums[i] = 2 的索引有 [6]  
> nums[i] = 3 的索引有 [1,5]  
> nums[i] = 4 的索引有 [3]  

如果是**非循環**陣列，在對應組中二分找 q，最靠近的肯定是前一個或是下一個。  
> [...,a,q,b,..]  
> 答案是 min(q - a, b - q)  

---

但本題是**循環**陣列，q 往左找 a 可能會跑到另一邊去：  
> [q,b,y,z,a]  

a 不一定是在 q 左邊，所以要用絕對值求距離 abs(a - q)。  

絕對值求的是**不走循環**的距離 dist。  
整個陣列長度是 N，走另一個方向的距離是 N - dist。  

q 與 b 的距離同理。  

時間複雜度 O(N + Q log N)。  
空間複雜度 O(N)。  

```python
class Solution:
    def solveQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        N = len(nums)

        group = defaultdict(list)
        for i, x in enumerate(nums):
            group[x].append(i)

        ans = []
        for q in queries:
            x = nums[q]
            xs = group[x]
            if len(xs) == 1:
                ans.append(-1)
            else:
                idx = bisect_left(xs, q)
                sz = len(xs)

                # go left
                dis1 = abs(q - xs[idx-1])
                dis1 = min(dis1, abs(N - dis1))

                # go right
                dis2 = abs(q - xs[(idx+1) % sz])
                dis2 = min(dis2, abs(N - dis2))

                ans.append(min(dis1, dis2))

        return ans
```

仔細探討循環陣列的性質。  

有個長度 5 的陣列，其索引分別為 [0,1,2,3,4]。  
因為是循環，所以 0 往左走到 4，繼續往左走到 3，以此類推。  

若先忽略循環，並**允許負數索引**，那麼 0 往左會走到 -1，在來是 -2，以此類推。  
-1 和 -2 對陣列大小 N = 5 取餘數後，對應到 4 和 3，與預期答案相符。  

同理，4 往右會走到 5，繼續往右走到 6。  
5 和 6 對 N 取餘數，對應到 1 和 2，也與預期答案相符。  

---

對於長度 N 陣列中的任意索引 i，加上 N 的任意倍數後對 N 取餘數，肯定還是 i。  

因此可以把 xs 陣列整個向左位移 N 步，充當負數索引；同理，右邊部分向右位移 N 步。例如：  
> xs = [0,1,2]  
> left = [-3,-2,-1], right = [3,4,5]  
> new_xs = left + xs + right  
> new_xs = [-3,-2,-1,0,1,2,3,4,5]  

如此一來，二分找到 q 的位置後就可以直接取前 / 後一個索引算距離。  
注意：原本在 len(xs) == 1 時，答案為 -1。因為 xs 變三倍長度，所以改判斷 len(xs) == 3。  

---

再仔細想想，我們其實只是找前 / 後一個位置，根本不需要複製整個陣列。  
只要把最後一個左移 N 步、第一個右移 N 步即可。  
> xs = [0,1,2]  
> first = [0], last = [2]  
> new_xs = [-1,0,1,2,3]  

在原本 len(xs) == 1 時，複製完長度會變 len(xs) + 2，所以依然判斷 len(xs) == 3 時答案為 -1。  

```python
class Solution:
    def solveQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        N = len(nums)

        group = defaultdict(list)
        for i, x in enumerate(nums):
            group[x].append(i)

        for k, v in group.items():
            # group[k] = [x - N for x in v] + v + [x + N for x in v]
            first, last = v[0], v[-1]
            group[k] = [last - N] + v + [first + N]

        ans = []
        for q in queries:
            x = nums[q]
            xs = group[x]
            if len(xs) == 3:
                ans.append(-1)
            else:
                idx = bisect_left(xs, q)
                dis1 = xs[idx] - xs[idx-1]
                dis2 = xs[idx+1] - xs[idx]
                ans.append(min(dis1, dis2))

        return ans
```
