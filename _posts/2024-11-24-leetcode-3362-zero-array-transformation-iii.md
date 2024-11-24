---
layout      : single
title       : LeetCode 3362. Zero Array Transformation III
tags        : LeetCode Medium PrefixSum Sorting Greedy SegmentTree Heap
---
biweekly contest 144。  
這屌題也是 5 分，其實應該給個 6 分。  

## 題目

輸入長度 n 的整數陣列 nums，還有二維陣列 queries，其中 queries[i] = [l<sub>i</sub>, r<sub>i</sub>]。  

對於每個 queries[i]：  

- 對於 nums 在 [l<sub>i</sub>, r<sub>i</sub>] 之間的索引**至多**減少 1。  
- 同一個查詢中，對於不同索引的減少量都是**獨立的**，不必相同。  

一個陣列的所有元素都等於 0，稱做**零陣列**。  

若執行所有操作後能使得 nums 變成**零陣列**，則回傳 true，否則回傳 false。  

求**最多**可從 queries 移除多少元素，並且依然使得 nums 成為**零陣列**。  
若不可能成為**零陣列**則回傳 -1。  

## 解法

先講講我賽時的想法，有點囉嗦，想看最佳解可以直接往下拉。  

有打上次周賽的同學應該很熟悉，這題應該可以用**差分**做。  
總之先用差分檢查能不能變成**零陣列**。  

---

如果可以，再來想辦法刪除某些查詢。要優先刪誰？  

一個查詢區間越寬，能夠滿足的 nums[i] 越多。  
或是說 [l, r] 區間可以由一個查詢組成，或是由多個查詢組成，因此**先刪短的**更優。  

---

但是有個小問題：  
> nums = [0,1,1,0], queries = [[1,2], [0,1], [2,3]]  
> 差分前綴和求出的刪除次數 = [1,2,2,1]，可變成零陣列  
> 扣除 nums 後多餘的次數 = [1,1,1,1]  

如果只按照長度遞增排序，首先第一個碰到的區間就是 [1,2]，刪掉的話剩下 [1,0,0,1]。  
之後再碰到 [0,1], [2,3] 都不能刪了。  

正確方式應該是刪除 [0,1], [2,3]，只保留 [1,2]，剛好滿足 nums = [0,1,1,0] 的需求。  

為了更有效利用每個區間，除了先以長度遞增排序之外，還需要再以**左端點**遞增排序。  

---

剩下最後一個問題：怎麼判斷這個查詢能不能刪？  

用差分求出每個索引 i 的操作次數 ps[i]，扣除 nums[i] 即為多餘的操作次數 extra[i]。  
若想刪除查詢 [l,r] 則區間 extra[l..r] 都必須大於 0，也就是**區間最小值**大於 0。  

確認要刪除查詢 [l,r] 後，則需要對 extra[l..r] 每個位置都減 1。  

需要**區間查詢**最小值，又要**區間修改**，剛好**線段樹**可以滿足需求。  

時間複雜度 O(N log N + Q log Q)。  
空間複雜度 O(N)。  

備注：可能有同學想到，nums[i] 也可以直接線段樹處理，幹嘛要差分？  
問得很好，因為 python 會 TLE。  

```python
class Solution:
    def maxRemoval(self, nums: List[int], queries: List[List[int]]) -> int:
        N = len(nums)
        diff = [0] * (N+5)
        for s, e in queries:
            diff[s] += 1
            diff[e+1] -= 1

        # check if valid
        extra = [0] * N
        ps = 0
        for i in range(N):
            ps += diff[i]
            if ps < nums[i]: # not possible to zero
                return -1
            extra[i] = ps - nums[i]

        seg = SegmentTree(N+5)
        seg.build(extra, 1, 0, N-1) # init extra count for each position

        # try remove
        ans = 0
        queries.sort(key=lambda x: (x[1]-x[0], x[0]))
        for s, e in queries:
            mn = seg.query(1, 0, N-1, s, e)
            if mn > 0: # remove this query
                ans += 1
                seg.update(1, 0, N-1, s, e, -1)

        return ans


class SegmentTree:

    def __init__(self, n):
        self.tree = [0]*(n*4)
        self.lazy = [0]*(n*4)

    def build(self, init, id, L, R):
        """
        初始化線段樹
        若無初始值則不需執行
        """
        if L == R:  # 到達葉節點
            self.tree[id] = init[L]
            return
        M = (L+R)//2
        self.build(init, id*2, L, M)
        self.build(init, id*2+1, M+1, R)
        self.push_up(id)

    def op(self, a, b):
        """
        任意符合結合律的運算
        """
        return a if a < b else b

    def push_down(self, id, L, R, M):
        """
        將區間懶標加到答案中
        下推懶標記給左右子樹
        """
        if self.lazy[id]:
            self.tree[id*2] += self.lazy[id]
            self.lazy[id*2] += self.lazy[id]
            self.tree[id*2+1] += self.lazy[id]
            self.lazy[id*2+1] += self.lazy[id]
            self.lazy[id] = 0

    def push_up(self, id):
        """
        以左右節點更新當前節點值
        """
        self.tree[id] = self.op(self.tree[id*2], self.tree[id*2+1])

    def query(self, id, L, R, i, j):
        """
        區間查詢
        回傳[i, j]的總和
        """
        if i <= L and R <= j:  # 當前區間目標範圍包含
            return self.tree[id]
        M = (L+R)//2
        self.push_down(id, L, R, M)
        res = inf
        if i <= M:
            res = self.op(res, self.query(id*2, L, M, i, j))
        if M+1 <= j:
            res = self.op(res, self.query(id*2+1, M+1, R, i, j))
        return res

    def update(self, id, L, R, i, j, val):
        """
        區間更新
        對[i, j]每個索引都增加val
        """
        if i <= L and R <= j:  # 當前區間目標範圍包含
            self.tree[id] += val
            self.lazy[id] += val
            return
        M = (L+R)//2
        self.push_down(id, L, R, M)
        if i <= M:
            self.update(id*2, L, M, i, j, val)
        if M < j:
            self.update(id*2+1, M+1, R, i, j, val)
        self.push_up(id)
```

上述方法有兩個很重要的重點：  

- 循序，由左至右處理 (掃描線)。  
- 貪心，優先刪除**較小區間** (優先保留較大區間)。  

其實我們只需要將所有區間按照左端點排序，並且**由左至右**依序處理每個 nums[i]，並在區間數量不足之時嘗試加入新區間。  

試想以下例子：  
> 當前 nums[5] = 1，但 ps[i] = 0 的區間數不足  
> 有 [2,5], [2,7], [4,8] 三個區間可選，選哪個最佳？  

因為我們是**由左至右**處理，所以 num[0..4] 肯定已經被滿足，不需要考慮。  
而 [4,8] 可以對 [5..8] 三個位置做出貢獻，因此選擇 [4,8] 是最佳方案。  

---

計算每個位置的覆蓋區間數，同樣使用**差分陣列**。  

另外還需要**維護可用的區間**，並取出**右端點最大者**，可使用 max heap。  
注意：在 ps[i] 不足時，heap 裝的區間有可能位於 i 左方，無法使用。  

時間複雜度 O(N + Q log Q)。  
空間複雜度 O(N + Q)。  

```python
class Solution:
    def maxRemoval(self, nums: List[int], queries: List[List[int]]) -> int:
        N = len(nums)
        diff = [0] * (N+5)
        ps = 0

        q = deque(sorted(queries))
        h = [] # right bound of available invervals
        ans = len(queries)
        for i in range(N):
            # maintain available intervals
            while q and q[0][0] == i:
                t = q.popleft()
                heappush(h, -t[1])


            ps += diff[i]
            # add new intervals while not enough
            while ps < nums[i] and h:
                e = -heappop(h)
                if e >= i: # [i, r] increased by 1
                    ans -= 1
                    ps += 1
                    diff[e+1] -= 1
            
            # still not possible to zero
            if ps < nums[i]:
                return -1

        return ans
```
