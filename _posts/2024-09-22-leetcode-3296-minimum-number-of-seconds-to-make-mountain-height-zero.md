---
layout      : single
title       : LeetCode 3296. Minimum Number of Seconds to Make Mountain Height Zero
tags        : LeetCode Medium Math BinarySearch Heap
---
weekly contest 416。  
滿有趣的二分二分題。  

## 題目

輸入整數陣列 mountainHeight，代表一座山的高度。  
另外還有整數陣列 workerTimes，代表每個工人的工作耗時 (以秒計)。  

所有工人**同時**進行挖山工程。對於工人 i：  

- 若想將山的高度減少 x，則須 workerTimes[i] + workerTimes[i] \* 2 + ... + workerTimes \* x 秒。例如：  
  - 減少高度 1，需要 workerTimes[i] 秒。  
  - 減少高度 2，需要 workerTimes[i] + workerTimes[i] \* 2秒，以此類推。  

求將山的高度減少至 0 所需的**最小秒數**。  

## 解法

關鍵字：工人**同時**工作。  
若有數個工人分別耗時 x1, x2, x3,.. 秒，則總工程耗時為 max(x1, x2, x3,..)，以**最大者**為準。  

而為了使最大時間盡可能小，即**最大值最小化**，根據經驗通常可以**二分答案**。  
並且，若在 x 秒可以完成工作，則 x+1 秒也可以；若 x 不行，則 x-1 也不行。  
答案具有單調性，確定可以二分答案。  

---

維護含數 ok(limit)，判斷能否在 limit 秒內完成工作。  
需要遍歷每個工人，分別算出他們在 limit 秒內**能夠減少的高度**。  
若減少總高度 cnt 大於等於 mountainHeight 則合法。  

另一個問題來了，怎麼知道工人在特定時間內可以減多少高度？  

---

答案還是二分。  

工人的耗時公式是**等差級數和**，再乘上其基本耗時。  
若在 limit 秒內能減少高度 x，則減少 x-1 肯定也合法；反之，x 不合法，則 x+1 也不合法。  
答案具有單調性，可以二分。  

注意：兩次二分的**邊界更新邏輯不同**，取中位數時注意補 1。  

---

最後來確定二分的上下界。  
比賽中我隨便都填 1e18 居然給我超時，太苦了。  

外層二分：  
最佳情況下 1 秒就能完成工作。下界 = 1。  
最差情況下只有一個耗時超大的工人，而且山又超大。上界 = 10^5 \* (10^5 + 1) \/ 2 \* 10^6，不超過 1e16。  

內層二分：  
最差情況下沒法減少任何高度。下界 = 0。  
最佳情況下可以減少整座山。上界 = mountainHeight。  

時間複雜度 O(N \* log MX \* log mountainHeight)，其中 MX = 外層二分上界。  
空間複雜度 O(1)。  

```python
class Solution:
    def minNumberOfSeconds(self, mountainHeight: int, workerTimes: List[int]) -> int:

        def work(base, limit):
            lo = 0
            hi = mountainHeight
            while lo < hi:
                mid = (lo + hi + 1) // 2
                work_cnt = mid * (mid+1) // 2
                work_sec = work_cnt * base
                if work_sec > limit:
                    hi = mid - 1
                else:
                    lo = mid
            return lo

        def ok(limit):
            cnt = 0
            for base in workerTimes:
                cnt += work(base, limit)
            return cnt >= mountainHeight

        lo = 1
        hi = 10 ** 16
        while lo < hi:
            mid = (lo + hi) // 2
            if not ok(mid):
                lo = mid + 1
            else:
                hi = mid

        return lo
```

其實我有想到用 min heap，可惜思路不正確。  

如果是求**總時間最小**，那麼主要的 key 是**當前成本**沒錯。  
但本題的工人是**平行工作**，需要比較的是個人的**總時間**，所以 key 是**下次工作後的總時間**。  

很重要，是找**下次工作後的總時間**最小者！！不是當前總時間！！  
如果只找當前總時間最少的，他如果下次耗時超大就完蛋。  
以當前總時間為 key 的反例：  
> 工人一：當前總時間 1，下次耗時 10000  
> 工人二：當前總時間 2，下次耗時 1  

怎麼看都是錯的。  

時間複雜度 O(mountainHeight log N)，其中 N = len(workerTimes)。  
空間複雜度 O(N)。  

```python
class Solution:
    def minNumberOfSeconds(self, mountainHeight: int, workerTimes: List[int]) -> int:
        h = []
        for base in workerTimes:
            # tot cost after next work,
            # curr cost
            # base cost
            heappush(h, [base, base, base]) 

        ans = 0
        for _ in range(mountainHeight):
            tot, curr, base = heappop(h)
            ans = max(ans, tot)
            
            # update costs
            curr += base
            tot += curr
            heappush(h, [tot, curr, base])

        return ans
```
