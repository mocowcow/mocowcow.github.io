--- 
layout      : single
title       : LeetCode 2741. Special Permutations
tags        : LeetCode Medium Array BitManipulation Bitmask DP
---
周賽350。一開始以為是回溯，差點被騙。  

# 題目
輸入整數陣列nums，由n個**不同**的正整數組成。  
若nums的排序符合以下條件則稱為**特殊**：  
- 對於所有0 <= i < n-1 的索引i，必須滿足nums[i] % nums[i+1] == 0 或 nums[i+1] % nums[i] == 0  

求有多少**特殊排列**。答案很大，先模10^9+7後回傳。  

# 解法
暴力窮舉所有排列有14!種，大概是8e10個，肯定不行。  

當我們選擇某個nums[i]時，必須符合其一：  
- 是此排列中第一個  
- nums[i] % prev == 0  
- prev % nums[i] == 0  

同時還要保存所有nums的狀態，哪些可選，哪些可不選。  
這時候可以使用bitmask，1位元代表選過，0位元代表選過，初始mask=0，全選完mask=(1<<N)-1。  

不同的選擇順序可能會得到同樣的狀態，例如：  
> nums = [1,2,4,8]  
> 選 1 2 4，得到mask=0111, prev=4  
> 選 2 1 4，得到mask=0111, prev=4  

有重疊的子問題，可以使用動態規劃。  
定義dp(mask,prev)：當前nums的可用狀態為mask，且前一個選擇的數字是prev時，有多少排列方式。  
轉移方程式：dp(mask,prev)=sum( dp(new_mask,nums[i]) FOR ALL nums[i]可選)  
base case：當mask等於(1<<N)-1，每個位元都是1，代表排列完成，接下來只有不選1種方式。  

mask共有2^N種，prev共有N種，所以dp狀態是2^N \* N種。每個狀態需要轉移N次。  
時間複雜度O(2^N \* N^2)。  
空間複雜度O(2^N \* N)。  

```python
class Solution:
    def specialPerm(self, nums: List[int]) -> int:
        MOD=10**9+7
        N=len(nums)
        
        @cache
        def dp(mask,prev):
            if mask==(1<<N)-1:
                return 1
            ans=0
            for i in range(N):
                if not mask&(1<<i) and (prev is None or nums[i]%prev==0 or prev%nums[i]==0):
                    new_mask=mask|(1<<i)
                    ans+=dp(new_mask,nums[i])
            return ans%MOD
        
        return dp(0,None)
```
