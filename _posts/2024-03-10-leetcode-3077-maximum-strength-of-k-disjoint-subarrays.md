---
layout      : single
title       : LeetCode 3077. Maximum Strength of K Disjoint Subarrays
tags        : LeetCode Hard Array DP
---
周賽388。真的得抱怨一下，題目原文非常爛，只講選擇 k 個不相交的子陣列，但沒有提到選擇的順序。  
如果講清楚一點，我相信 AC 人數不至於這麼悲慘。  

## 題目

輸入長度 n 的整數陣列 nums，還有**奇數正整數** k。  

x 個子陣列的強度定義為：  
> strength = sum[1] \*x - sum[2]\* (x - 1) + sum[3] \*(x - 2) - sum[4]\* (x - 3) + ... + sum[x] *1  

其中 sum[i] 是第 i 個子陣列的總和。更正式的說，強度是滿足 1 <= i <= x 的所有 i 對應的 (-1)<sup>i+1</sup> \*sum[i]\* (x - i + 1) 之和。  

你必須**從左到右**選擇 k 個**不相交**的子陣列，並使得強度最大化。  
求**最大**強度。  

注意：所選的子陣列不需要完全覆蓋整個陣列。  

## 解法

比賽時因為這個爛描述，還以為選擇的子陣列是可以任意順序，完全不知道怎麼下手。  
結束後看人家講才知道，原來他想講的是**從左到右**選擇子陣列。  

再加上測資的範圍有保證 n \* k <= 10^6，這其實就在提示會有兩個迴圈總共跑 n \* k 次。  
更露骨的說，就是 dp 的**狀態個數**。  

到目前為止，已經得到初步的狀態定義。  
定義 dp(i, need_grp)：從子陣列 nums[i..N-1] 中，求出 need_grp 個不相交子陣列的最大值。  

---

常見的子陣列劃分型 dp 之中，每個元素都必須劃分到某個子陣列之中。  
本題則不太相同，某些元素可以被**跳過**。也就是第 i 和第 i+1 個子陣列之間可以有任意個元素可以不選。  
因此需要多一個變數來表示 nums[i] **選或不選**。  

定義 dp(i, need_grp, take = 0/1)：從子陣列 nums[i..N-1] 中，求出 need_grp 個不相交子陣列的最大值。  
若 take = 0 則不選，否則根據當前子陣列編號求出相應的變化量 delta。  

如果 nums[i] 不選，nums[i+1] 當然也可以不選。  
若還有剩餘的子陣列的話，也可以選擇用 nums[i+1] 做為新的開頭。  
轉移：dp(i, need_grp, 0) = max( dp(i + 1, need_grp, 0), dp(i + 1, need_grp - 1, 1) )  

如果 nums[i] 選，除了上面兩個轉移來源，還多一個新的選擇：將 nums[i+1] 分到與 nums[i] 同一組。  
轉移：dp(i, need_grp, 1) = max( .., dp(i + 1, need_grp, 1) ) + delta  

BASE：當 need_grp 為負數，代表分割太多子陣列了，不合法，回傳 -inf。  
只有在**剩餘 0 個子陣列**，且不選擇 nums[i] 的情況下能合法 (保證 nums[i] 沒有被算入開頭而占用 need_grp)，回傳 0。  

---

選擇 nums[i] 產生的變化量 delta 需要透過子陣列的編號 grp_id 計算。  
而 grp_id 可以直接透過 k - need_grp 得出。  

我們不確定第一個子陣列是不是由 nums[0] 開頭。  
是的就是 dp(0, k - 1, 1)；否則 dp(0, k, 0) 自己會找到一個合適的開頭。  
答案是兩者取最大值。  

時間複雜度 O(nk)。  
空間複雜度 O(nk)。  

```python
class Solution:
    def maximumStrength(self, nums: List[int], k: int) -> int:
        N = len(nums)
        
        @cache
        def dp(i, need_grp, take):
            if need_grp == 0 and not take:
                return 0
            
            if i == N:
                return -inf
            
            delta = 0 # contribution of nums[i]
            if take: 
                grp_id = k - need_grp
                delta = nums[i] * (k - grp_id + 1)
                if grp_id % 2 == 0:
                    delta = -delta
                
            res = dp(i + 1, need_grp, False) # no take nums[i+1]
            if take: # take nums[i+1] with same group
                res = max(res, dp(i + 1, need_grp, True)) 
            if need_grp > 0: # take nums[i+1] with new group
                res = max(res, dp(i + 1, need_grp - 1, True)) 
            return res + delta
        
        ans = max(
            dp(0, k - 1, True), # take nums[0]
            dp(0, k, False) # no take nums[0]
        )
        dp.cache_clear()
        
        return ans
```
