---
layout      : single
title       : LeetCode 3351. Sum of Good Subsequences
tags        : LeetCode Hard DP
---
weekly contest 423。  

## 題目

輸入整數陣列 num。  

一個**好的**子序列中，**任意兩個**相鄰元素的差都**正好**是 1。  

求 nums 的所有**好的子序列**的總和。  
答案可能很大，先模 10^9 + 7 後回傳。  

## 解法

注意本題求的是子序列總和，**不是個數**。  
但計算總和還是依賴於個數。  

在這種子序列計數 dp 問題，通常考慮某個元素**選或不選**對答案造成的影響。  
每考慮一個新的元素 x，有四種情形：  

- 不選 x。  
- 自成一個新的子序列 [x]。  
- 追加到 x-1 結尾的子序列後方。  
- 追加到 x+1 結尾的子序列後方。  

設 cnt[x] 代表以 x 結尾的子序列數量。  
每次考慮新的 x，則 cnt[x] 會多出 1 + cnt[x-1] + cnt[x+1] 種方案。  

---

那子序列總和怎麼算？  

設 val[x] 代表以 x 結尾的子序列總和。  
每次考慮新的 x，則 cnt[x] 會增加 x + cnt[x-1] \* x + cnt[x+1] \* x。  

同時更新 cnt 和 val 的值，最後把所有 val[x] 加起來就是答案。  

時間複雜度 O(N)。  
空間複雜度 O(N)。  

```python
MOD = 10 ** 9 + 7
class Solution:
    def sumOfGoodSubsequences(self, nums: List[int]) -> int:
        cnt = Counter()
        val = Counter()
        for x in nums:
            # update sum
            inc = x
            inc += val[x-1] + cnt[x-1] * x
            inc += val[x+1] + cnt[x+1] * x
            val[x] += inc
            val[x] %= MOD
            # update freq
            cnt[x] += cnt[x-1] + cnt[x+1] + 1
            cnt[x] %= MOD
            
        return sum(val.values()) % MOD

```
