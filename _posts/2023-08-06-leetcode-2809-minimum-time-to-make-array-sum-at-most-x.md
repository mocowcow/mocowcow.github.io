---
layout      : single
title       : LeetCode 2809. Minimum Time to Make Array Sum At Most x
tags        : LeetCode Hard Array Sorting DP
---
雙周賽110。可能會是全站第二難的題，只有41人通過，太扯了。  
而且明明測資範圍才1000，結果O(N^2)空間還會MLE，沒優化沒辦法過。  

## 題目

輸入兩個長度相同的整數陣列nums1和nums2。
每一秒鐘，對於所有滿足 0 <= i < nums1.length的索引i，將nums1[i]的值增加nums2[i]。然後你可以執行以下操作：

- 選擇滿足 0 <= i < nums1.length的索引i，使nums1[i] = 0  

另外還有另外還有給定整數x。  

求**最少**需要多少時間，才能使得nums1的元素和**小於等於**x。若不可能則回傳-1。  

## 解法

對於每個nums1[i]來說，每一秒都會增加num2[i]。如果同一個索引i被清除超過一次，則第二次清除時，除了nums[i]同樣為0之外，其他所有位置的值只可能變得更大，不會變小。  
因此得出結論：每個索引最多只會被清除一次，總共有N個位置，所以答案最大是N秒。  

題目要求的是最少的時間，可以從小到大依序檢查，在t秒鐘清除t個不同索引後的元素和。  
如果直接求元素和很麻煩，還要額外維護哪些i選過，非常難處理。
但是可以算出t秒時nums1未經修改的成長值，只要計算**選t個索引可以清除的最大元素和**，從成長值中扣掉後得到第t秒的最小元素和。  

假設nums1初始值總和為sm1，且nums2總和為sm2：  
> 在第t秒時，若沒有經過清除，則nums1的元素和會變成sm1 + sm2\*t。  
> 選t個不同的索引，清除後減少的值總共是nums1[i1] + nums2[i1]\*t + nums1[i2] + nums2[i1]\*(t-1) + ...
> 例如t=2，我們選擇兩個索引i,j分別在第1秒和第2秒清除  
> 可清除的值就是nums1[i] + nums2[i]\*1 + nums1[j] + nums2[j]\*2  

可以發現，若nums2[i]的值越大、成長速率越快，越晚清除越好。先把nums1和nums2封裝，並按照nums2的值排序。  
那如何找到選t個索引的最大值？其實就變成簡單的背包問題，在前i個物品中選擇t個，決定第i個選或不選。  

定義dp(i,t)：在前i個索引中，選擇t個索引的最大清除元素和。  
轉移方程式：dp(i,t) = max(選i, 不選i)，不選的話就是dp(i-1,t)；選的話就是dp(i-1,t-1)+nums1[i]+num2[i]\*t。  
base cases：當i<0代表沒東西選了，回傳0；或是t=0時沒有選擇次數了，也回傳0。  

最後從0秒開始往上加，看哪秒可以讓元素和降到x，就是答案。  
注意：是**從0秒開始**，有可能一開始nums1總和就小於x。  
注意2：記憶體限制很嚴苛，動態規劃時，若需要選的次數t大於可選數量i+1，全都是無用的狀態，要剪枝才能通過。  

時間複雜度O(N^2)。  
空間複雜度O(N^2)。  

```python
class Solution:
    def minimumTime(self, nums1: List[int], nums2: List[int], x: int) -> int:
        N=len(nums1)
        sum1=sum(nums1)
        sum2=sum(nums2)
        arr=sorted(zip(nums1,nums2),key=itemgetter(1))
        
        @cache
        def dp(i,t): # nums2[0,i], we can clear t more times
            if t>i+1: # pruning
                return dp(i,i+1)
            if i<0 or t==0: 
                return 0
            res=dp(i-1,t) # no take
            res=max(res,dp(i-1,t-1)+arr[i][0]+arr[i][1]*t) # clear nums[i] at j-th second
            return res
        
        for t in range(N+1):
            if sum1+sum2*t-dp(N-1,t)<=x:
                return t
            
        return -1
```

改成遞推版本，沒有空間優化的版本就可以過，而且記憶體用量少很多。  

```python
class Solution:
    def minimumTime(self, nums1: List[int], nums2: List[int], x: int) -> int:
        N=len(nums1)
        sum1=sum(nums1)
        sum2=sum(nums2)
        arr=sorted(zip(nums1,nums2),key=itemgetter(1))
        
        dp=[[0]*(N+1) for _ in range(N+1)]
        for t in range(1,N+1):
            for i in range(1,N+1):
                dp[i][t]=max(
                    dp[i-1][t],
                    dp[i-1][t-1]+arr[i-1][0]+arr[i-1][1]*t
                )
                
        for t in range(N+1):
            if sum1+sum2*t-dp[N][t]<=x:
                return t
            
        return -1
```
