---
layout      : single
title       : LeetCode 3448. Count Substrings Divisible By Last Digit
tags        : LeetCode Hard Math DP
---
weekly contest 436。  
又是有點卡 python 的題，優化好幾次才過。  
只能說好險這次周賽沒打，不然大概會氣死。  

## 題目

<https://leetcode.com/problems/count-substrings-divisible-by-last-digit/description/>

## 解法

求子字串轉成整數後是否能被 k 整除，讓我想到**數位 dp**。  
相似題 [2827. number of beautiful integers in the range]({% post_url 2023-08-21-leetcode-2827-number-of-beautiful-integers-in-the-range %})。  

數位 dp 是在固定格子內枚舉要填什麼數字，最後判斷是否被能 k 整除。  
只是本題固定只能填 s[i]，不需枚舉。  

根據模運算的性質：
> (10 \* y + x) % k  
> = ((y % k) \* 10 + x) % k  

所以每在後面填一個數字 x，可以把餘數 rem 更新成 (rem + x) % k。  

---

定義 dp(i, rem)：從 s[i] 為起點的子字串，有多少個是 k 結尾且被 k 整除。當前餘數為 rem。  

我們可以枚舉結尾元素 k，再枚舉子字串起點 i，加起來就是答案。  

時間複雜度 O(ND^2)，其中 D = 9，為合法的結尾數字個數。  
空間複雜度 O(ND)。  

---

本來把 target 也寫進 dp 狀態裡面，會 MLE。  
要一直清 cache 才不會爆記憶體。  

然後 k 也要剪枝，不然也會 TLE。  
真的是很煩的題。  

```python
class Solution:
    def countSubstrings(self, s: str) -> int:
        N = len(s)
        a = list(map(int, s))

        def solve(k):

            @cache
            def dp(i, rem):
                if i == N:
                    return 0
                x = a[i]
                rem = (rem * 10 + x) % k
                res = 0
                if x == k and rem == 0:  # can end here
                    res = 1
                res += dp(i + 1, rem)
                return res

            res = 0
            for i in range(N):
                res += dp(i, 0)
            dp.cache_clear()  # prevent MLE
            return res

        ans = 0
        for k in set(a):
            if k > 0:
                ans += solve(k)

        return ans
```

改成遞推寫法。  
注意到 dp[i] 只依賴 dp[i+1]，可以壓縮掉一個空間維度。  

時間複雜度 O(ND^2)，其中 D = 9，為合法的結尾數字個數。  
空間複雜度 O(D)。  

```python
class Solution:
    def countSubstrings(self, s: str) -> int:
        N = len(s)
        a = list(map(int, s))

        def solve(k):
            cnt = 0
            f = [0] * k
            for i in reversed(range(N)):
                x = a[i]
                f2 = [0] * k
                for rem in range(k):
                    rem2 = (rem*10 + x) % k
                    res = 0
                    if x == k and rem2 == 0:  # can end here
                        res = 1
                    res += f[rem2]
                    f2[rem] = res
                    
                # iterate and update answer
                f = f2
                cnt += f[0]
            return cnt

        ans = 0
        for k in set(a):
            if k > 0:
                ans += solve(k)

        return ans
```
