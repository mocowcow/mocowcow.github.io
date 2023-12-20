---
layout      : single
title       : LeetCode 2968. Apply Operations to Maximize Frequency Score
tags        : LeetCode Hard Array TwoPointers SlidingWindow BinarySearch PrefixSum Math Greedy
---
周賽376。腦子被Q3搞壞掉，寫Q4的時候已經沒腦力了。其實只需要幾個常見技巧結合而已。  

## 題目

輸入整數陣列nums，還有整數k。  

你可以執行以下操作**最多**k次。  

- 選擇任意索引i，並使nums[i]**增加**或**減少**1  

最終，陣列的分數等於出現最多次元素的**出現頻率**。  

求最大分數為多少。  

## 解法

要選擇某個數t，把nums中盡可能多的元素都變成t。  
因為修改受限於k，最好是從靠近t的元素開始修改，才能只用最少的成本。  
先將nums排序，修改後的t必定會成為一個連續的區間，像是[x,..,t,t,t,..,y]。  

那要如何決定目標t是多少？其實最暴力的方法就是枚舉所有元素作為中心點，朝左右擴展，直到修改成本即將超過k為止。  
但是在k很大的情況下，每個中心擴展之後都能包含整個nums，複雜度高達O(N^2)。  

既然t會形成連續區間，假設某個t最多能有x個，那麼一定也能找到長度小於x的區間；反之，絕對找不到大於x的區間。  
答案具有**單調性**，可以用二分搜+滑動窗口來找到t最多有幾個。  

講這麼多，還是不知道t是誰。  
那在枚舉長度為size的滑動窗口的時候，怎麼知道要把窗口的元素變成什麼？  
想想老朋友**中位數**，把窗口中所有元素都變成當前的中位數就是最佳方案。如果修改成本不超過k，則代表能找到長度size的窗口。  

假設當前窗口區間為[left, right]，中位數的索引為mid=(left+right)/2，中位數值為median=nums[mid]。  
則左半區間L=[left, mid]的修改成本為len(L)\*median-sum(L)；右半區間R=[mid,right]的修改成本為sum(R)-median\*len(R)。  
區間總和使用前綴和達到O(1)查詢。  

排序為O(N log N)，之後每次枚舉窗口O(N)，最多log N次。  
時間複雜度O(N log N)。  
空間複雜度O(N)。  

```python
class Solution:
    def maxFrequencyScore(self, nums: List[int], k: int) -> int:
        N=len(nums)
        nums.sort()
        ps=list(accumulate(nums,initial=0))
        
        def ok(size):
            left=0
            for right,x in enumerate(nums):
                if right-left+1==size:
                    mid=(right+left)//2
                    median=nums[mid]
                    cost=(mid-left+1)*median-(ps[mid+1]-ps[left])
                    cost+=(ps[right+1]-ps[mid])-(right-mid+1)*median
                    if cost<=k:
                        return True
                    left+=1
            return False
        
        lo=1
        hi=N
        while lo<hi:
            mid=(lo+hi+1)//2
            if not ok(mid):
                hi=mid-1
            else:
                lo=mid
                
        return lo
```

仔細想想，**單調性**同樣也存在窗口本身存在。  
當窗口左邊界不變，右邊界不斷擴展時，總修改成本**只增不減**。  
也就是說對於如果[left, right]區間不合法，那麼left對於大於right的右邊界來說肯定也不合法，所以可以直接收縮左邊界。  

只需要保留上面方法計算修改成本的部分，在成本大於k時收縮左邊界，最後以當前窗口大小更新答案即可。  

雖然瓶頸依然在於排序，但是找區間加速很多。  
時間複雜度O(N log N)。  
空間複雜度O(N)。  

```python
class Solution:
    def maxFrequencyScore(self, nums: List[int], k: int) -> int:
        N=len(nums)
        nums.sort()
        ps=list(accumulate(nums,initial=0))
        ans=0
        
        def get_cost(left,right):
            mid=(right+left)//2
            median=nums[mid]
            cost=(mid-left+1)*median-(ps[mid+1]-ps[left])
            cost+=(ps[right+1]-ps[mid])-(right-mid+1)*median
            return cost

        left=0
        for right,x in enumerate(nums):
            while get_cost(left,right)>k:
                left+=1
            ans=max(ans,right-left+1)
                
        return ans
```
