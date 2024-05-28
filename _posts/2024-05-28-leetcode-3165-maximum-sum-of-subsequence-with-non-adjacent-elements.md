---
layout      : single
title       : LeetCode 3165. Maximum Sum of Subsequence With Non-adjacent Elements
tags        : LeetCode Hard Array DP SegmentTree
---
周賽 399。連續兩場都出線段樹，太狠了。  
本題知識重點：如果一個題目可以用分治解決，那他的帶修改版本可以用線段樹解決。  

## 題目

輸入整數陣列 nums。
還有二維整數陣列 queries，其中 queries[i] = [pos<sub>i</sub> , x<sub>i</sub>]。  

對於第 i 個查詢，首先將 nums[pos<sub>i</sub>] 設為 x<sub>i</sub>，然後計算 nums 中**不含相鄰元素**的**子序列**的**最大和**。  

回傳所有查詢結果的加總。  
答案可能很大，先模 10^9 + 7 後回傳。  

## 解法

[198. house robber]({% post_url 2022-02-07-leetcode-198-house-robber %}) 的進化版本。  

在原始版本的問題中，dp(i) 代表的是子陣列 nums[0..i] 的最大利潤。  
假如更改了 nums[i] 的值，那麼從所有包含 nums[i] 的子陣列結果可能被改變。改變 nums[i] 最差情況下，需要重新計算 O(N) 次。  

---

既然說包含 nums[i] 的狀態要被重新計算，那沒包含的狀態不是就可以複用？沒錯。  
這給出一個靈感：將已經計算過的狀態**合併**計算出新的狀態。  

考慮有兩個獨立的陣列 A = [1,0,1], B = [0,3,0]，最大和 = 2, 3。  
不難看出兩陣列合併後 [1,\_,1,\_,3,\_] 最大和 = 2 + 3。但只是巧合。  

考慮另一個例子 A = [1,0,1], B = [3,0,3]，最大和 = 2, 6。  
但很明顯連接邊界的兩個元素不能都選，只能最多擇一。  
枚舉放棄哪邊，合併的結果有兩種可能：  

- 情形 1  
    A 保留右邊元素，保持完整；B 放棄左邊元素，左開右閉。  
    [1,\_,1] + [\_,\_,3] 最大和 = 2 + 3 = 5  

- 情形 2  
    A 放棄右邊元素，左閉右開；B 保留左邊元素，保持完整。  
    [1,\_,\_] + [3,\_,3] 最大和 = 1 + 6 = 7  

---

完整的閉區間，需要參考到子區間的半閉狀態轉移而來。  
所以每個子區間都需要維護**完整區間** [L,R]、**左開右閉** (L,R]、**左閉右開** [L,R) 三種狀態，供合併使用。  
這三種狀態分辨以 f11, f01, f10 表示，其中 0/1 代表邊界元素**能不能選**。  

設左右子區間分別為 A, B，完整區間的轉移公式為：  
> f11 = max(A.f10 + B.f11, A.f11 + B.f01)  

有人可能想問為什麼沒有 A.f10 + B.f01 這個選項？  
因為 A.f11 已經包含 A.f10 這個狀態。注意 f11 代表著最左右兩邊的元素**都可以選**，但並**不一定要選**。  

---

處理完 f11，那另外兩個狀態 f01, f10 如何轉移？  

先來暴力枚舉 f11, f01, f10 的所有排列組合。
首先 f\_1 + f1\_ 這種肯定不行。再扣掉等於 f11 的，只剩下：  

- f01 + f01 = f01  
- f10 + f10 = f10  

難到 f01 只能由兩個左開右閉區間組成嗎？  
隨便舉一個例子 [0,99] + [0,99]，如果是 A.f10 + B.f10 的話兩個 99 都選不到，總和只有 0！  
正確方式是 [\_,\_] + [\_,99] 總和 99，同樣滿足 f01 最左選、最右不選的限制。  
因此需引入一個新的狀態 f00，表示**兩邊界元素都不選**。  

---

對於左閉右開的 f01 來說，A 必定左開；B 必定右閉。  
根據以上兩點，加上中間相鄰元素擇一，轉移公式為：  
> f01 = max(A.f00 + B.f11, A.f01 + B.f01)  

f10 同理，轉移公式為：  
> f10 = max(A.f10 + B.f10, A.f11 + B.f00)  

對於 f00 來說，A 肯定左閉；B 肯定右閉。  
轉移公式：  
> f00 = max(A.f00 + B.f10, A.f01 + B.f00)  

將原本的 nums 不斷一分為二，最終拆成 N 個長度 1 的子區間，每次更新只會影響到 log(N) 個子區間。正是**線段樹**。  
對於單一元素的子區間，想清楚原本 f = 0/1 的定義是**能不能選**，四個狀態分別是：  

- f00 不能選  
- f01 不能選最左。但最右同時也是最左，會衝突，只能不選  
- f10 不能選最右。但最左同時也是最右，會衝突，只能不選  
- f11 可以選  

---

實現上述狀態轉移，每次修改後對答案加入最大區間總和即可。  

時間複雜度 O(Q log N)。  
空間複雜度 O(N)。  

```python
MOD = 10 ** 9 + 7
class Solution:
    def maximumSumSubsequence(self, nums: List[int], queries: List[List[int]]) -> int:
        N = len(nums)
        seg = SegmentTree(N)
        seg.build(nums, 1, 0, N - 1)
        ans = 0
        for pos, x in queries:
            seg.update(1, 0, N - 1, pos, x)
            ans += seg.f11[1] # whole segment
            
        return ans % MOD


class SegmentTree:
    def __init__(self, n):
        self.f00 = [0]*(n*4)  # (L, R)
        self.f01 = [0]*(n*4)  # (L, R]
        self.f10 = [0]*(n*4)  # [L, R)
        self.f11 = [0]*(n*4)  # [L, R]

    def build(self, init, id, L, R):
        if L == R:
            self.f11[id] = max(0, init[L])
            return
        M = (L+R)//2
        self.build(init, id*2, L, M)
        self.build(init, id*2+1, M+1, R)
        self.push_up(id)

    def push_up(self, id):
        l, r = id*2,  id*2+1
        self.f00[id] = max(self.f00[l] + self.f10[r],
                           self.f01[l] + self.f00[r])
        self.f01[id] = max(self.f00[l] + self.f11[r],
                           self.f01[l] + self.f01[r])
        self.f10[id] = max(self.f10[l] + self.f10[r],
                           self.f11[l] + self.f00[r])
        self.f11[id] = max(self.f10[l] + self.f11[r],
                           self.f11[l] + self.f01[r])

    def update(self, id, L, R, i, val):
        if L == R:  
            self.f11[id] = max(0, val)
            return
        M = (L+R)//2
        if i <= M:
            self.update(id*2, L, M, i, val)
        else:
            self.update(id*2+1, M+1, R, i, val)
        self.push_up(id)
```
