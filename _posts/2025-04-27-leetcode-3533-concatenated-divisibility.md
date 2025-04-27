---
layout      : single
title       : LeetCode 3533. Concatenated Divisibility
tags        : LeetCode Hard Math BitManipulation Bitmask DP
---
weekly contest 447。  
沒看清楚答案 WA 好幾次。  

## 題目

<https://leetcode.com/problems/concatenated-divisibility/description/>

## 解法

nums 排列串接起來的數字能要能被 k 整除。  
求**字典序最小**的答案陣列。  

注意：是串接前的陣列，不是串接後的結果。  

---

很明顯看出沒有特定的選擇規律，只能靠暴力枚舉所有排列。  

跟昨天雙周賽 Q4 一樣，回溯會超時，要想辦法優化。  
不同選法會剩下相同元素，有**重疊子問題**，考慮 dp。  

---

那怎麼處理整除？寫過數位 dp 的同學應該有印象。  
> x % k = r  

若要在 x 後面串接一個新的數字 y，則要將餘數乘 10 後加上 y 再模次 k 即可。  

> (x \* 10 + y) % k  s
> = ((x % k) \* 10 + y) % k  

本題串接不只一個數字，同理，加幾個數字就要將原本餘加乘上幾個 0。  

例如：  
> "1" + "23"  
> "123" % 5 = 3  
> = ("1" % 5 \* 100 + "23") % 5  
> = (5 \* 100 + 23) % 5  
> = 523 % 5  
> = 3  

預處理 zeros[i] 表示與 nums[i] 相同位數的 0 供後續使用。  

---

定義 dp(mask, r)：剩餘元素為 mask、餘數為 r 時是否能被 k 整除。  

為了使得答案陣列字典序最小，先將 nums 排序，按此順序枚舉可保證先嘗試較小的數。  
因為只要字典序最小的答案，因此遞迴過程中發現能整除立刻中止，並將所選數加入答案。  

注意：判斷整除後，離開遞迴時才會紀錄答案，因此會是相反順序的，記得反轉。  

時間複雜度 O(N \* k \* 2^N)。  
空間複雜度 O(k \* 2^N)。  

```python
class Solution:
    def concatenatedDivisibility(self, nums: List[int], k: int) -> List[int]:
        N = len(nums)
        nums.sort()

        zeros = [1] * N
        for i, x in enumerate(nums):
            while x > 0:
                zeros[i] *= 10
                x //= 10

        FULL = (1 << N)-1
        ans = []

        @cache
        def dp(mask, r):
            if mask == FULL:
                return r == 0
            for i in range(N):
                bit = 1 << i
                if mask & bit > 0:
                    continue
                new_r = (r * zeros[i] + nums[i]) % k
                new_mask = mask | bit
                if dp(new_mask, new_r):
                    ans.append(nums[i])
                    return True
            return False

        if not dp(0, 0):
            return []

        return ans[::-1]
```
