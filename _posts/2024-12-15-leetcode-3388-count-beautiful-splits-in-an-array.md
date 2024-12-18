---
layout      : single
title       : LeetCode 3388. Count Beautiful Splits in an Array
tags        : LeetCode Medium String DP
---
weekly contest 428。  
Q3 比前面兩題更垃圾。  
超級迷惑測資範圍，出題者預期 O(N^2) 解，但是給 N = 5000。光看就很危險，寫下去不是 TLE 就是 MLE。  

更智障的是 nums[i] 最大 50，這數字不知道有什麼意義，直接把陣列硬轉成字串後竟然可以 O(N^3) 過。  
該過的全死光，該擋的檔不住，希望出題者以後別再出了。  

## 題目

輸入陣列 nums。  

一個**美麗**的陣列分割方案滿足：  

- 將 nums 分割成三個**非空**子陣列 nums1, nums2, nums3，滿足 nums1 + nums2 + nums3 = nums。  
- nums1 是 nums2 的前綴，**或者**， nums3 是 nums3 的前綴。  

求滿足以上條件的**分割方案數**。  

## 解法

以下簡稱三個子陣列為 a1, a2, a3。  

---

廢話不多說，先上一個不該過卻通過的做法。  

MX = max(nums) 至多 51，對應到大小寫字母綽綽有餘。小於 26 轉大寫、大於等於 26 轉小寫。  
然後枚舉 a2 的起點 i，再枚舉 a3 的起點 j，用內建函數檢查是否為前綴即可。  

時間複雜度 O(N^3)。  
空間複雜度 O(N)。  

```python
class Solution:
    def beautifulSplits(self, nums: List[int]) -> int:
        N = len(nums)
        a = []
        for x in nums:
            if x < 26:
                a.append(chr(97-65+x))
            else:
                a.append(chr(97-26+x))

        s = "".join(a)
        # a1 = [..i-1], sz1 = i
        # a2 = [i..j-1], sz2 = j-i
        # a3 = [j..], sz3 = N-j
        ans = 0
        for i in range(1, N-1):
            a1 = s[:i]
            for j in range(i+1, N):
                a2 = s[i:j]
                a3 = s[j:]
                if a2.startswith(a1) or a3.startswith(a2):
                    ans += 1

        return ans
```

再來是作者預期的作法。  

a1, a2, a3 屬於 nums。  
要檢查是否互為前綴關係，可以求 nums 的**最長公共子陣列** LCS (Longest Common Subarray)。  
注意是 substring 不是 subsequence，但大同小異。  
相似題 [718. Maximum Length of Repeated Subarray](https://leetcode.com/problems/maximum-length-of-repeated-subarray/)。  

---

lcs[i][j] 指的是 nums[i..] 和 nums[j..] 的最長公共前綴長度。  
為符合本題題意，改叫 LCP (Longest Common Prefix)。  

若 nums[i] == nums[j]，則 lcp[i][j] = lcp[i+1][j+1] + 1；否則為 0。  
注意：lcp[i][j] 和 lcp[j][i] 是等價的，但因為本題測資很爛的關係，全算會噴 MLE，所以只能限制 i<j。  

---

同樣枚舉 a2 和 a3 的起點 i, j，檢查子陣列對應的 lcp。  

- a1 和 a2 求 lcp[0][i]。  
- a2 和 a3 求 lcp[i][j]。  

lcp 在計算時沒有考慮到子陣列的右端點，因此可能發生**重疊**。例如：  
> nums = [1,0,1,0,1,0]  
> i, j = 2, 3  
> 分割成 [1,0], [1], [0,1,0]  
> 很明顯不滿足條件，但 lcp[0][i] = lcp[0][2] = 4  
> [1,0] 和 [1] 的 lcp 明顯不是 4  

前綴不可能比本身更長。  
為避免誤判，需保證作為前綴的子陣列長度不大於另一者。  
並且 lcp 還是可能超過兩者長度，故使用**大於等於**比較。  

時間複雜度 O(N^2)。  
空間複雜度 O(N^2)。  

```python
class Solution:
    def beautifulSplits(self, nums: List[int]) -> int:
        N = len(nums)
        lcp = [[0] * (N+1) for _ in range(N+1)]
        for i in reversed(range(N)):
            for j in reversed(range(i+1, N)): # prevent MLE
                if nums[i] == nums[j]:
                    lcp[i][j] = lcp[i+1][j+1] + 1

        # a1 = [0..i-1], sz1 = i
        # a2 = [i..j-1], sz2 = j-i
        # a3 = [j..N-1], sz3 = N-j
        ans = 0
        for i in range(1, N-1):
            sz1 = i
            for j in range(i+1, N):
                sz2 = j-i
                sz3 = N-j
                # a1 cannot longer than a2
                case1 = sz1 <= sz2 and lcp[0][i] >= sz1
                # a2 cannot longer than a3
                case2 = sz2 <= sz3 and lcp[i][j] >= sz2
                if case1 or case2:
                    ans += 1

        return ans
```

a1 和 a2 匹配前綴，本質上是 nums 和**自己的後綴**找**共通前綴**。  
有持續打周賽的同學應該會想到 z-function。  

---

總之先拿 nums 求一次 z，記做 z0。  
對於所有 a2 各算一次 z。每次 O(N)，總共要算 O(N) 次。  

然後可以 O(1) 求**最長共通前綴** lcp：  

- 若 a2 = nums[i..]，則 a1 和 a2 的 lcp = z[i]。  
- 若 a3 = nums[j..]，則 a2 和 a3 的 lcp = z[j-i]，因為要扣掉最前方沒用到的 a1 偏移量。  

同樣需注意子陣列的**重疊**問題，透過檢查子陣列長度保證沒有重疊。  
雖然我比賽時就是這個作法，但被重疊卡了很久，太苦了。  

雖然時間複雜度和 dp 求 lcp 相同，但是只需要同時保留兩個 z，節省更多空間。  

時間複雜度 O(N^2)。  
空間複雜度 O(N)。  

```python
class Solution:
    def beautifulSplits(self, nums: List[int]) -> int:
        N = len(nums)
        z0 = z_function(nums)

        # a1 = [0..i-1], sz = i
        # a2 = [i..j-1], sz = j-i
        # a3 = [j..N-1], sz = N-j
        ans = 0
        for i in range(1, N-1):
            sz1 = i
            z = z_function(nums[i:])
            for j in range(i+1, N):
                sz2 = j-i
                sz3 = N-j
                if sz1 <= sz2 and z0[i] >= sz1 or \
                sz2 <= sz3 and z[j-i] >= sz2:
                    ans += 1

        return ans


def z_function(s):
    N = len(s)
    z = [0]*N
    L = R = 0
    for i in range(1, N):
        if R < i:  # not covered by previous z-box
            # z[i] = 0
            pass
        else:  # partially or fully covered
            j = i-L
            if j+z[j] < z[L]:  # fully covered
                z[i] = z[j]
            else:
                z[i] = R-i+1

        while i+z[i] < N and s[i+z[i]] == s[z[i]]:  # remaining substring
            z[i] += 1
        if i+z[i]-1 > R:  # R out of prev z-box, update R
            L = i
            R = i+z[i]-1

    return z
```

其實 rolling hash 也可以做，只是我看這測資感覺會 TLE 就沒嘗試。  
然而並不會超時，而且寫起來還很快。  

- 若 a2 = nums[i..]，則 a1 和 a2 比對 h[0..i-1] 和 h[i..i+i-1]。  
- 若 a3 = nums[j..]，則 a2 和 a3 比對 h[i..j-1] 和 h[j..j+(j-1)-1]。  

時間複雜度 O(N^2)。  
空間複雜度 O(N)。  

```python
MOD = 1_000_000_901
class Solution:
    def beautifulSplits(self, nums: List[int]) -> int:
        N = len(nums)
        rh = RollingHash(nums, MOD)

        # a1 = [0..i-1], sz = i
        # a2 = [i..j-1], sz = j-i
        # a3 = [j..N-1], sz = N-j
        ans = 0
        for i in range(1, N-1):
            sz1 = i
            for j in range(i+1, N):
                sz2 = j-i
                sz3 = N-j
                if sz1 <= sz2 and rh.get(0, i-1) == rh.get(i, i+sz1-1) or \
                sz2 <= sz3 and rh.get(i, j-1) == rh.get(j, j+sz2-1):
                    ans += 1

        return ans


class RollingHash:
    def __init__(self, s, mod):
        # self.s = s
        self.mod = mod
        base = 87
        ps = self.ps = [0] * (len(s) + 1)
        base_pow = self.base_pow = [1] * (len(s) + 1)
        for i, c in enumerate(s):
            ps[i+1] = (ps[i] * base + c) % mod
            base_pow[i+1] = (base_pow[i] * base) % mod

    def get(self, L, R):
        # print(self.s[L:R+1])
        return (self.ps[R+1] - self.ps[L] * self.base_pow[R-L+1]) % self.mod
```
