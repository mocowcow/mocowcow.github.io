--- 
layout      : single
title       : LeetCode 2367. Number of Arithmetic Triplets
tags        : LeetCode
---
周賽305。這題挺好玩的，有三種以上的解法，感覺我當時的作法算是最佳解了。  

# 題目
輸入嚴格遞增的整數陣列nums和正整數diff。如果滿足以下條件，則三元組(i, j, k)稱為**算術三元組**：  
- i < j < k  
- nums[j] - nums[i] == diff  
- nums[k] - nums[j] == diff  

求有多少不同的**算術三元組**。  
注意：nums是**嚴格遞增**的。  

# 解法
首先是最簡單的暴力三迴圈，列舉i,j,k並檢查是否符合條件。  
乍看之下複雜度是O(N^3)，但因為nums是**嚴格遞增**，所以nums[i]+diff == nums[j]至多只會出現一次，所以實際上只有O(N^2)的時間複雜度。  

```python
class Solution:
    def arithmeticTriplets(self, nums: List[int], diff: int) -> int:
        N=len(nums)
        ans=0
        for i in range(N-2):
            for j in range(i+1,N-1):
                if nums[i]+diff==nums[j]:
                    for k in range(j+1,N):
                        if nums[j]+diff==nums[k]:
                            ans+=1
                            
        return ans
```

接下來繼續利用嚴格遞增的特性：每個數只會出現一次。且索引越大者，其對應的整數也一定較大，若i < j則nums[i] < nums[j]必定成立。  
將nums整個裝進集合s中，以供O(1)查詢。列舉nums中所有數字n做為nums[j]，檢查nums[i]和nums[j]是否也存在，若是則答案加1。  

```python
class Solution:
    def arithmeticTriplets(self, nums: List[int], diff: int) -> int:
        s=set(nums)
        ans=0
        
        for n in s:
            if n-diff in s and n+diff in s:
                ans+=1
                
        return ans
```

最後是我的方法，因為**嚴格遞增**寫在題目最下方，我根本就沒看到，還以為一個數可以被使用好多次，結果就變成DP了。  

維護兩個雜湊表d1和d2，分別記錄以各key值作為nums[j]或是nums[k]的合法數量。列舉nums中每個數字n，則d2[n]的值代表能夠以n作為nums[k]產生的**算術三元組**數量，將d2[n]加入答案。而n可以提供之後出現的n+diff組成(n, n+diff)，或是(n-diff, n, n+diff)，所以把d2[n+diff]遞增d1[n]，而d1[n+diff]遞增1。  

```python
class Solution:
    def arithmeticTriplets(self, nums: List[int], diff: int) -> int:
        ans=0
        d1=Counter()
        d2=Counter()
        
        for n in nums:
            ans+=d2[n]
            d2[n+diff]+=d1[n]
            d1[n+diff]+=1
        
        return ans
```
