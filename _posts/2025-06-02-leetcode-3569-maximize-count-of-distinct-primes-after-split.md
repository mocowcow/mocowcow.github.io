---
layout      : single
title       : LeetCode 3569. Maximize Count of Distinct Primes After Split
tags        : LeetCode Hard Math SortedList SegmentTree
---
weekly contest 452。  
想通了其實沒很難，只是很煩，而且 python 又卡常數。  

## 題目

<https://leetcode.com/problems/maximize-count-of-distinct-primes-after-split/description/>

## 解法

每次查詢步驟：  

- 把 nums[i] 改成 val  
- 選一個索引 k，把 nums 劃分成 nums[0..k-1], nums[k..N-1] 兩半  
- 使得兩半**不同的質數個數**相加最大  

---

從特殊到一般，先考慮**不帶修改**的版本要怎麼切才能最大化。  
分類討論某質數 p 對於答案的影響：

- 若 p 在 nums 中只出現一次，那麼怎麼切都無所謂，因為只會對左右其中一半的個數加 1。  
- 若出現兩次以上，只有切在中間才能使兩邊貢獻都加 1；否則只能讓其中一邊的個數加 1。  

---

問題轉換成：求所有質數 p 對於所有分割點 i 的貢獻。  

需有序維護 p 的出現位置，使用 sorted list。  
記 contribution[i] 為選擇分割點 i 可獲得的不同質數個數和。  

若 p 只出現一次，則所有分割點 i 都可以獲得 1 個數的貢獻。  
若 p 出現至少兩次， 第一次出現在 l，最後一次出現在 r：  

- 分割點 k = [0..l]，所有 p 都在右半，答案加 1  
- 分割點 k = [l+1..r]，兩半都有 p，答案加 2  
- 分割點 k = [r+1..N-1]，所有 p 都在左半，答案加 1  

整理後其實增量看起來就像是 [..,1,1,2,2,1,1..]。  
可以先把整段都加 1，然後再把中間段在加 1。  

```python
d = defaultdict(SL)
contribution = [0]*N

def calc(p):
    sl = d[p]
    if len(sl) == 1:
        # 只出現一次，每個位置貢獻加 1
        for i in range(N):
            contribution[i] += 1
    elif len(sl) >= 2:
        # 出現至少兩次，最左最右在 l, r
        # 中間段 [l+1..r] 貢獻加 2
        # 其餘兩邊 [0..l], [r+1..N1-] 貢獻加 1
        l, r = sl[0], sl[-1]
        for i in range(N):
            contribution[i] += 1
        for i in range(l+1, r+1):
            contribution[i] += 1
```

處理完所有不同質數 p 後，答案即 max(contribution)。  
時間複雜度 O(N)。  

---

再來討論帶修改的版本。  

若按照出現次數的變化分類討論會很麻煩，例如：  
> 0 次變 1 次，所有位置都加 1  
> 1 次變 2 次，只有中間位置會加 1  
> 3 次以上，視第一個 / 最後一個位置是否改變，決定那些位置加 1  

光想就很囉嗦。  
更簡單的方法是把拆成三個步驟：  
先**撤銷** p 原本的貢獻，增減 p 的位置，然後**重新套用** p 的貢獻。  

把剛才的貢獻函數稍微調整，加上權重 val，其中 1 代表套用，-1 代表撤銷。  

```python
def calc(p, val):
    sl = d[p]
    if len(sl) == 1:
        # 只出現一次，每個位置貢獻加 1
        for i in range(N):
            contribution[i] += val
    elif len(sl) >= 2:
        # 出現至少兩次，最左最右在 l, r
        # 中間段 [l+1..r] 貢獻加 2
        # 其餘兩邊 [0..l], [r+1..N1-] 貢獻加 1
        l, r = sl[0], sl[-1]
        for i in range(N):
            contribution[i] += val
        for i in range(l+1, r+1):
            contribution[i] += val
```

每次修改只需分開判斷新舊元素是否為質數，就可以複用貢獻函數。  

```python
# 舊元素是質數
if old_val in prime:
    calc(old_val, -1)  # 先撤銷原本的貢獻
    d[old_val].remove(i)
    calc(old_val, 1)  # 再套用新的貢獻
# 新元素是質數
if new_val in prime:  # 先撤銷原本的貢獻
    calc(new_val, -1)
    d[new_val].add(i)
    calc(new_val, 1)  # 再套用新的貢獻

nums[i] = new_val  # 記錄修改
```

---

因為查詢次數過多，每次複雜度 O(N) 還需要優化。  
calc 需要**區間修改**、**區間查詢**最大值，可用**線段樹**優化成 O(N log N)。  

但是因為本題卡 python 常數容易超時，所以整個區間 [0..N-1] 修改的操作改用 p_cnt 紀錄次數。  

時間複雜度 O((N+Q) log N)。  
空間複雜度 O(N)。  

```python
MX = 10 ** 5 + 5
sieve = [True] * (MX + 1)
prime = set()
for i in range(2, MX + 1):
    if sieve[i]:
        prime.add(i)
        for j in range(i * i, MX + 1, i):
            sieve[j] = False


class Solution:
    def maximumCount(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        N = len(nums)

        d = defaultdict(SL)
        seg = SegmentTree(N)
        p_cnt = 0

        def calc(p, val):
            # 計算質數 p 對各位置的貢獻
            # val = 1/-1 為套用/撤銷
            nonlocal p_cnt
            sl = d[p]
            if len(sl) == 1:
                # 只出現一次，每個位置貢獻加 1
                p_cnt += val
            elif len(sl) >= 2:
                # 出現至少兩次，最左最右在 l, r
                # 中間段 [l+1..r] 貢獻加 2
                # 其餘兩邊 [0..l], [r+1..N-1] 貢獻加 1
                l, r = sl[0], sl[-1]
                p_cnt += val
                seg.update(1, 0, N-1, l+1, r, val)

        # 維護質數位置
        for i, x in enumerate(nums):
            if x in prime:
                d[x].add(i)

        # 計算初始貢獻
        for p in d.keys():
            calc(p, 1)

        ans = []
        for i, new_val in queries:
            old_val = nums[i]
            # 舊元素是質數
            if old_val in prime:
                calc(old_val, -1)  # 先撤銷原本的貢獻
                d[old_val].remove(i)
                calc(old_val, 1)  # 再套用新的貢獻
            # 新元素是質數
            if new_val in prime:  # 先撤銷原本的貢獻
                calc(new_val, -1)
                d[new_val].add(i)
                calc(new_val, 1)  # 再套用新的貢獻

            nums[i] = new_val  # 記錄修改
            ans.append(seg.tree[1] + p_cnt)  # 找最大貢獻

        return ans


class SegmentTree:

    def __init__(self, n):
        self.tree = [0]*(n*4)
        self.lazy = [0]*(n*4)

    def op(self, a, b):
        """
        任意符合結合律的運算
        """
        return a if a > b else b

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
