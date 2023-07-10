--- 
layout      : single
title       : LeetCode 2771. Longest Non-decreasing Subarray From Two Arrays
tags        : LeetCode Medium Array DP
---
周賽353。一開始往貪心的方向去想，吃了一個WA。  

# 題目
輸入長度n的整數陣列nums1和nums2。  

定義長度同為n的整數陣列nums3，其中nums3[i]可以由nums1[i]或nums2[i]組成。  

你的目標是在nums3中，找到**最長的非遞減子陣列**。  

求nums3的**最長的非遞減子陣列**長度。  

# 解法
當在考慮nums3[i]要選誰時，前一個選的可能是nums1[i-1]或是nums2[i-1]，或是根本沒選。  
不同的選法會產生重疊子問題，故考慮dp。  

定義dp(i,prev)：前一個選的數字是prev，以nums3[i]開頭的**最長的非遞減子陣列**長度。  
轉移方程式：max(選nums1, 選nums2, 都不選)。若nums1>=prev則可考慮nums1，若nums2>=prev則可考慮nums2。  
base case：當i=N時，沒東西可選，回傳0。  

最長的子陣列有可能以任意一個索引為起點。起點的數字不受限制，故枚舉所有索引i，以dp(i,0)更新答案。  

對於每個索引i來說，prev只有三種可能：nums1[i-1]、nums2[i-1]或0。  
時間複雜度O(N)。  
空間複雜度O(N)。  

```python
class Solution:
    def maxNonDecreasingLength(self, nums1: List[int], nums2: List[int]) -> int:
        N=len(nums1)
        
        @cache
        def dp(i,prev):
            if i==N:
                return 0
            res=0
            if nums1[i]>=prev:
                res=max(res,dp(i+1,nums1[i])+1)
            if nums2[i]>=prev:
                res=max(res,dp(i+1,nums2[i])+1)
            return res
        
        ans=0
        for i in range(N):
            ans=max(ans,dp(i,0))
            
        return ans
```

上面這種使用到prev的定義太難寫了，換一種比較通俗的。  
令nums = [nums1, nums2]。  

定義dp(i,j)：以nums[j][i]為右邊界時，**最長的非遞減子陣列**長度。  
轉移方程式：dp[i][j] = max(1, dp[i-1][0], dp[i-1][1])。若nums[j][i]>=nums1[i-1]可選擇dp[i-1][0]；若nums[j][i]>=num2[i-1]可選擇dp[i-1][1]。  
base case：當i=0，左邊沒有可以連接的子陣列，只有自己一個，長度1。  

時間複雜度O(N)。  
空間複雜度O(N)。  

```python
class Solution:
    def maxNonDecreasingLength(self, nums1: List[int], nums2: List[int]) -> int:
        N=len(nums1)
        nums=[nums1,nums2]
        ans=0
        
        @cache
        def dp(i,j):
            if i==0:
                return 1
            x=nums[j][i]
            res=1
            for k in range(2):
                if x>=nums[k][i-1]:
                    res=max(res,dp(i-1,k)+1)
            return res
            
        ans=0
        for i in range(N):
            ans=max(ans,dp(i,0),dp(i,1))
            
        return ans
```

最後改成遞推，在計算dp狀態的過程中順便更新答案。  
注意：base case的i=0並沒有計算，所以答案初始值要設成1才不會出錯。  

```python
class Solution:
    def maxNonDecreasingLength(self, nums1: List[int], nums2: List[int]) -> int:
        N=len(nums1)
        ans=1
        dp=[[1]*2 for _ in range(N)]
        
        for i in range(1,N):
            # using nums1
            if nums1[i]>=nums1[i-1]:
                dp[i][0]=max(dp[i][0],dp[i-1][0]+1)
            if nums1[i]>=nums2[i-1]:
                dp[i][0]=max(dp[i][0],dp[i-1][1]+1)
                
            # using nums2
            if nums2[i]>=nums1[i-1]:
                dp[i][1]=max(dp[i][1],dp[i-1][0]+1)
            if nums2[i]>=nums2[i-1]:
                dp[i][1]=max(dp[i][1],dp[i-1][1]+1)
                
            ans=max(ans,dp[i][0],dp[i][1])
            
        return ans
```