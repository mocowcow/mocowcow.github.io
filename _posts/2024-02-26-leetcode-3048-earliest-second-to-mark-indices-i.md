---
layout      : single
title       : LeetCode 3048. Earliest Second to Mark Indices I
tags        : LeetCode Medium Array HashTable BinarySearch Greedy
---
周賽386。索引從1開始算真的是很煩，超佩服腦子能自帶偏移量的人。  

## 題目

輸入**索引從 1 開始**的整數陣列 nums 和 changeIndices，兩者大小分別為 n 和 m。  

起初，nums 中的所有索引都是**未標記**的，而你必須要標記他們。  
依序從 1\~m 中的第 s 秒，你可以執行以下操作**之一**：  

- 選擇 [1, n] 之間的索引 i，並使 nums[i] 減 1  
- 如果 nums[changeIndices[s]] 等於 0，則標記索引 changeIndices[s]  
- 不做任何事  

求 [1, m] 之間的一個整數，代表在最佳情況下，能夠標記**所有**索引的**最早秒數**。若無法全部標記則回傳 -1。  

## 解法

有[題解](https://leetcode.cn/problems/earliest-second-to-mark-indices-i/solutions/2653101/er-fen-da-an-pythonjavacgo-by-endlessche-or61/)比喻的非常妙：  

- nums 代表 n 門課程，各需要 nums[i] 天做複習。每天只能複習一門課程  
- 而第 s 天也可以選擇參加第 changeIndices[s] 門課的考試，但考試就不能複習  

每門課程都各自需要複習 nums[i] 次，然後參加一次考試。  
求所有課程**複習且考試完**最快要多久。  

這個比喻的玄妙之處，繼續看下去才會理解。  

---

反正對於第 i 天來說，只有兩個有效選項：  

1. 複習任意課程  
2. 參加第 changeIndices[s] 門課的考試  

對於某門課程若需要 x 次複習，然後有好幾個考試日期可以選擇，那當然是選**越晚**的考試日，複習天數**越充足**。  
所以每門課程都選**最晚的日期**來考試，考過比較重要。  

知道了哪天要考試，那麼沒考試的天數就拿來複習吧。  
維護變數 cnt 代表複習次數，從頭遍歷 changeIndices，如果第 i 天不考試，則 cnt 加 1。  
本題不關心何時複習什麼科目，只要在考試當天從 cnt 中扣除所需要的次數即可。若複習次數不足，則不可能全部合格，回傳 -1。  

---

但有時候時間太充裕，根本不用拖到最後一天也能考過。如範例2：  
> nums = [1,3], changeIndices = [1,1,1,2,1,1,1]  
> 科目1 會拖到第 7 天才考試  
> 其實第 6 天就可以完成  

這種**時間點**的問題通常具有**單調性**，也就是一旦某個時刻 s 能夠滿足條件，那麼大於 s 的時間點也能完成；反之亦然。  
因此我們可以透過**二分**來找到最後一天的日期。  

注意：雖然時間範圍是 [1, M]，但也有可能 M 天也無法通過，要記得檢查。  

時間複雜度 O(M log M)。  
空間複雜度 O(min(M, N))。  

```python
class Solution:
    def earliestSecondToMarkIndices(self, nums: List[int], changeIndices: List[int]) -> int:
        N = len(nums)
        M = len(changeIndices)

        def ok(limit):
            sub = changeIndices[:limit]
            exam = 0
            last_day = {x: i for i, x in enumerate(sub)}
            study = 0  # days can study
            for day, x in enumerate(sub):
                if day == last_day[x]:
                    exam += 1
                    study -= nums[x-1]
                    if study < 0:
                        return False
                else:
                    study += 1
            return exam == N

        lo = 1
        hi = M
        while lo < hi:
            mid = (lo + hi) // 2
            if not ok(mid):
                lo = mid + 1
            else:
                hi = mid

        if not ok(lo):
            return -1

        return lo

```

二分可以把範圍改成 [1, M+1]，判斷答案大於 M 就回傳 -1。  

二分內部邏輯也可以逆向處理。  
從最後一天開始倒序遍歷，首次碰到的考試日就直接考，把需要的複習天數記起來，之後非考試日在來複習。  
最後檢查是否考過 N 個科目，且需要複習日為 0 即可。  

```python
class Solution:
    def earliestSecondToMarkIndices(self, nums: List[int], changeIndices: List[int]) -> int:
        N = len(nums)
        M = len(changeIndices)

        def ok(limit):
            vis = set()
            study = 0  # days need to study
            exam = 0
            for day in reversed(range(limit)):
                x = changeIndices[day]
                if x not in vis:
                    vis.add(x)
                    exam += 1
                    study += nums[x-1]
                elif study > 0:
                    study -= 1
            return exam == N and study == 0

        ans = 1 + bisect_left(range(1, M + 1), True, key=ok)

        if ans > M:
            return -1

        return ans

```
