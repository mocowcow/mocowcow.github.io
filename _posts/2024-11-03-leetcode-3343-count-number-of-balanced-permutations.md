---
layout      : single
title       : LeetCode 3343. Count Number of Balanced Permutations
tags        : LeetCode Hard Math DP
---
weekly contest 422。  
本篇題解寫得不太好，老實說我也不太確定正確性，建議隨便看看就好。  

## 題目

輸入字串 num。  
如果字串偶數索引數字的和等於奇數索引數字的和，則稱為**平衡的**。  

求 nums 的**不同排列**中，有多少是**平衡的**。  

答案可能很大，先模 10^9 + 7 後回傳。  

## 解法

延續 Q1 的**平衡字串**。  

奇偶索引是交替出現。所以偶數索引若有 x 個，則奇數索引只可能是 x 或 x-1 個。  
問題轉換成：把 N 個數字**分成兩堆**，各 sz1 + sz2 個，且**兩堆的和相同**。  
因為要平分成兩堆，所以 sum(num) 必須是偶數，若非偶數可直接回傳 0。  

在 N 個數中找 sz 個數，使總和正好為 target，我馬上想到 [494. Target Sum](https://leetcode.com/problems/target-sum/)。  
只是多加了一個選擇數量限制而已。  

---

再來想想怎麼求排列。  

一個長度為 x 的字串，全排列共有 x! 種。例如 "112" 的全排列為 3! 種。  
若要去除重複，則必須除去每個**元素數量的階乘**。例如 "112" 中有 2 個 1、1個 2，所以要除 1! 和 2!。  

舉個實際例子：  
> 構造字串長度為 5，且和為 20  
> 全排列共有 5! 種  
> 從 0~9 依序枚舉要**選幾個**  
> 假設選 1 個 1，子問題變成**字串長度 4，和為 19**，除去重複的 1!  
> 假設選 2 個 1，子問題變成**字串長度 3，和為 18**，除去重複的 2!  
> 以此類推  

不同選法也可能造成相同的限制，有**重疊的子問題**，因此考慮 dp。  

定義 dp(i, cnt, val)：在 i~9 的數字之中，選擇 cnt 個數字且總合為 val 的**不重複**方案數。  
轉移：dp(i, cnt, val) = sum( (dp(i+1, cnt-j, val-i*j) / j!) FOR ALL 0 <= j <= min(freq[i], cnt))。  
base：當 i = 10 時，所有數字都選完了，只有在 cnt = val = 0 時才滿足要求，回傳字串的全排列，即 sz!。  

---

根據乘法原理，答案應是兩堆的方案數相乘。  
但上面的 dp 狀態只能處理其中一堆的方案數，要如何知道另一堆的方案數？  

這邊我卡了很久沒想通，因為 dp 不知道到底選了哪些數，一度以為不是正確做法，但只是我想多了。  
舉個例子：  
> num = "112112"  
> 很明顯兩堆分別是 "112" 和 "112"  
> "112" 的方案數是 3! / 2! / 1! = 3  
> 因此答案是 3 \* 3 = 9 種  

注意每個數都必須在其中一堆，也就是說對於這 4 個 1 來說，若在第一堆用了 2 個，**剩餘的** 4-2 個**必定在第二堆**。  
因此兩堆 sz1 和 sz2 的全排列方案數共有 sz! \* sz2! 種，而在 dp 轉移時，除了扣除當前選擇的 j! 種排列以外，也要順便扣除另一堆的 (freq[i] - j)! 種排列。  

---

剩下最後一個問題，由於取模後的方案數涉及除法，必須使用**乘法逆元**，才能確保答案的正確性。  
答案入口為 dp(0, sz1, target)，其中 target = sum(num) / 2。  

時間複雜度不太確定，就不亂寫了。  
空間複雜度 O(10 \* N \* S)。  

```python
MOD = 10 ** 9 + 7
MX = 85
f = [0]*(MX+1)
finv = [0]*(MX+1)
f[0] = finv[0] = 1
f[1] = finv[1] = 1

for i in range(2, MX+1):
    f[i] = (f[i-1]*i) % MOD
    finv[i] = pow(f[i], -1, MOD)

class Solution:
    def countBalancedPermutations(self, num: str) -> int:
        N = len(num)

        d = Counter()
        tot = 0
        for c in num:
            d[int(c)] += 1
            tot += int(c)

        if tot%2 == 1:
            return 0

        target = tot // 2
        sz1 = N // 2
        sz2 = N - sz1

        @cache
        def dp(i, cnt, val):
            if i == 10:
                if cnt == 0 and val == 0:
                    return f[sz1] * f[sz2] # factorial(sz1) * factorial(sz2) 
                return 0

            res = 0
            for j in range(d[i] + 1):
                if j > cnt or i*j > val:
                    break
                t = dp(i+1, cnt-j, val - i*j)
                t *= finv[j] # /= factorial(j)
                t *= finv[d[i]-j] # /= factorial(d[i]-j)
                res += t
            return res % MOD

        return dp(0, sz1, target)
```
