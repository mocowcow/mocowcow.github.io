---
layout      : single
title       : LeetCode 3176. Find the Maximum Length of a Good Subsequence I
tags        : LeetCode Medium Array DP HashTable SegmentTree
---
雙周賽 132。

## 題目

輸入整數陣列 nums 和非負整數 k。  

若一個整數序列 seq 滿足在索引範圍 [0, seq.length - 2] 中，存在**最多 k 個**索引滿足 seq[i] != seq[i + 1]，則稱其為**好的**序列。  

求 nums 的**好的子序列**的最大長度。  

## 解法

經典的**相鄰相關**子序列 dp。  
除了當前第 i 個元素**選或不選**之外，還需要紀錄上次選的元素 prev，以及**相鄰不同**的次數 j。  

定義 dp(i, j, prev)：在 nums[i..N-1] 的子陣列中，找出的最大好的子序列長度，且當前不同次數為 j，前一個元素為 prev。  
轉移：dp(i, j, prev) = max(選, 不選)  

- 選，根據 nums[i] 和 prev 的關係判斷：  
  - 若 prev = -1 或 nums[i] = prev，則 dp(i + 1, j, nums[i]) + 1  
  - 否則若 j < k，則 dp(i + 1, j + 1, nums[i]) + 1  
- 不選：dp(i + 1, j, prev)  

base：當 i = N 時，代表沒元素可選，回傳 0。  

答案入口為 dp(0, 0, -1)。  

時間複雜度 O(N^2 \* k)。  
空間複雜度 O(N^2 \* k)。  

```python
class Solution:
    def maximumLength(self, nums: List[int], k: int) -> int:
        N = len(nums)
        
        @cache
        def dp(i, j, prev):
            if i == N:
                return 0
            # no take
            res = dp(i + 1, j, prev)
            # take
            if nums[i] == prev or prev == -1: # same or frist
                res = max(res, dp(i + 1, j, nums[i]) + 1)
            elif j < k: # different
                res = max(res, dp(i + 1, j + 1, nums[i]) + 1)
            return res
        
        ans = dp(0, 0, -1) 
        dp.cache_clear() # prevent MLE
        
        return ans
```

對於更大的測資範圍，則需要更佳的時間複雜度。  
先改寫成遞推，看看什麼地方可以優化。  

nums[i] 的上限高達 10^9，但受限於 nums 的大小，實際上最多也只會有 M = N 種數字。  
先把 nums 離散化，dp 陣列狀態數為 N \* k \* M。  

```python
class Solution:
    def maximumLength(self, nums: List[int], k: int) -> int:
        N = len(nums)
        mp = {x:i for i, x in enumerate(set(nums))}
        a = [mp[x] for x in nums]
        M = len(mp)
        
        ans = 0
        dp = [[[0] * M  for _ in range(k + 1)] for _ in range(N + 1)]
        for i in reversed(range(N)):
            for j in range(k + 1):
                for prev in range(M):
                    # no take
                    res = dp[i + 1][j][prev]
                    # take
                    if a[i] == prev:
                        res = max(res, dp[i + 1][j][prev] + 1)
                    elif j < k:
                        res = max(res, dp[i + 1][j + 1][a[i]] + 1)
                    dp[i][j][prev] = res
                    ans = max(ans, res)
                    
        return ans
```

仔細觀察 dp[i][j][prev] 的轉移來源，除了共通的 dp[i + 1][j][prev] 以外，還有：  

- prev = nums[i] 時，dp[i + 1][j][prev] + 1  
- prev != nums[i] 且 j < k 時，dp[i + 1][j + 1][prev] + 1  

設 x = nums[i]，在不選 x 的情況下，dp[i][j] 會直接繼承 dp[i][j + 1] 既有的結果。  
若選 x 的情況下，也只有 dp[i][j][x] 會改變，並從 dp[i + 1][j][x] 和所有 dp[i + 1][j + 1][x != prev] 之中**取最大值**後加 1。  

基於**繼承上次結果**的特性，且 dp[i][j] 只依賴於 dp[i][j + 1]，確保從小到大枚舉 j，就可以**複用**上次的結果，空間優化掉一個維度。  
並且又只需要對 dp[i][j][x] 進行**單點更新**，枚舉 prev 的第三個迴圈也被優化掉了。  

---

為了支持最大值的**單點更新**還有**區間查詢**，又是**線段樹**出場了。  
建立 k + 1 個線段樹，分別維護第**相鄰不同次數為 j**時的區間最大值，依序枚舉 nums[i] 及次數 j，最後從所有 dp[j] 中取最大值即可。  

時間複雜度 O(N \* k \* log M)，其中 M = nums 中不同元素個數。  
空間複雜度 O(k \* M)。  

---

線段樹很有用，但是：  
> 551 / 551 test cases passed, but took too long.  

複雜度代入 N = M = 5000, k = 50，大概才 3e6，反正 python 不給過，但是 golang 還有尊貴的 C++ 倒是過了。  

```python
class Solution:
    def maximumLength(self, nums: List[int], k: int) -> int:
        mp = {x:i for i, x in enumerate(set(nums))}
        M = len(mp)
        
        ans = 0
        dp = [SegmentTree(M) for _ in range(k + 1)]
        for x in nums:
            x = mp[x]
            for j in range(k + 1):
                # prev = x
                res = dp[j].query(1, 0, M - 1, x, x) + 1
                # prev != x
                if j < k:
                    res = max(res, dp[j + 1].tree[1] + 1)
                dp[j].update(1, 0, M - 1, x, res)
                ans = max(ans, res)
                    
        return ans
    
    
class SegmentTree:

    def __init__(self, n):
        self.tree = [0]*4

    def op(self, a, b):
        """
        任意符合結合律的運算
        """
        return max(a, b)

    def push_up(self, id):
        """
        以左右節點更新當前節點值
        """
        self.tree[id] = self.op(self.tree[id*2], self.tree[id*2+1])

    def query(self, id, L, R, i, j):
        """
        區間查詢
        回傳[i, j]的最大值
        """
        if i <= L and R <= j:  # 當前區間目標範圍包含
            return self.tree[id]
        res = 0
        M = (L+R)//2
        if i <= M:
            res = self.op(res, self.query(id*2, L, M, i, j))
        if M+1 <= j:
            res = self.op(res, self.query(id*2+1, M+1, R, i, j))
        return res

    def update(self, id, L, R, i, val):
        """
        單點更新
        對索引i設為val
        """
        if L == R:  # 當前區間目標範圍包含
            self.tree[id] = val
            return
        M = (L+R)//2
        if i <= M:
            self.update(id*2, L, M, i, val)
        else:
            self.update(id*2+1, M+1, R, i, val)
        self.push_up(id)
```

可能有細心的同學會問：不是從 dp[i + 1][j + 1][x != prev] 轉移而來嗎？怎麼區間查詢包含了 dp[i + 1][j + 1][x = prev]？  
其實照理說是不能包含這一塊，應該要分成 x 的左右兩半區間查詢。  
但是 dp[i + 1][j + 1][x] 比起 dp[i + 1][j][x] 少了一次不同的機會，不可能得到更好的結果，永遠不會影響答案，所以可以不用管他。  

最初我也沒想清楚這點，所以才會選擇線段樹。  

---

再認真想一想，其實還有可以優化的地方。  

對於每個 dp[j]，真正需要查詢的只有**單點最大值**和**整體最大值**，並沒有部分區間，也就是說根本不需要**線段樹**。  
只需要單獨維護 dp[j][prev] 的值，還有整個 dp[j] 的最大值。  

時間複雜度 O(N \* k)。  
空間複雜度 O(k \* M)。  

```python
class Solution:
    def maximumLength(self, nums: List[int], k: int) -> int:
        mp = {x:i for i, x in enumerate(set(nums))}
        M = len(mp)
        
        ans = 0
        dp = [[0] * M for _ in range(k + 1)] # dp[j][prev]
        dpj = [0] * (k + 1) # max(dp[j])
        for x in nums:
            x = mp[x]
            for j in range(k + 1):
                # prev = x
                res = dp[j][x] + 1
                # prev != x
                if j < k:
                    res = max(res, dpj[j + 1] + 1)
                dpj[j] = max(dpj[j], res)
                dp[j][x] = res
                ans = max(ans, res)
                    
        return ans
```
