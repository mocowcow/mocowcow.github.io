---
layout      : single
title       : LeetCode 2818. Apply Operations to Maximize Score
tags        : LeetCode Hard Array Math Stack Sorting HashTable
---
周賽358。腦力被Q3耗掉一大半，做這題的時候不太清醒，還以為要搞線段數。  
開悟正解時，比賽已經結束10分鐘了。  

## 題目

輸入長度n的正整數陣列nums，還有整數k。  

你的起始分數為1。為了使分數最大化，你可以執行以下操作最多k次：  

- 選擇一個沒選過的**非空**子陣列nums[l, ..., r]  
- 從nums[l, ..., r]中找到**質數分數**最高的元素x。如果有多個元素符合，則選擇索引最小者  
- 將分數乘以x  

nums[l, ..., r]指的是閉區間的nums子陣列。  

一個整數x的**質數分數**等同於其不同的質因數個數。例如300的質因數分數是3，因為300 = 2\*2\*3\*5\*5。  

回傳最多k次操作可以達到的**最高分數**。  

答案可能很大，先模10^9+7後回傳。  

## 解法

先說結論：這題要素可真多，質因數分解、單調堆疊、貢獻法、快速冪，要同時搞懂這幾種東西才能過。  

總之先計算出每個元素的**質數分數**，質因數分解就不贅述了。  

為了使最終分數盡可能大，每次選擇的子陣列，其x值當然越大越好。  
如果我們想要找到x值為nums[i]的子陣列，他必須：  

- 右方元素的質數分數必須**小於等於**nums[i]的質數分數  
- 左方元素的質數分數必須**小於**nums[i]的質數分數(相等的話左邊會優先)  

例如：  
> nums = [8,3,9,3,8]  
> 質數分數pc = [1,1,1,1,1]  
> 若想要以找到x=9的子陣列  
> 左邊不能接任何元素這一個選擇  
> 右邊可以不接、或接上[3]或[3,8]，共三種選擇  
> 根據乘法原理，總共有1\*3 = 3種子陣列滿足  
> 也就是[9],[9,3],[9,3,8]三種子陣列  

那怎麼找到哪些子陣列會貢獻x=nums[i]？就像[2763. sum of imbalance numbers of all subarrays]({% post_url 2023-07-02-leetcode-2763-sum-of-imbalance-numbers-of-all-subarrays %})一樣擴展左右邊界。  
利用單調堆疊保存每個索引，若當前索引i的質數分數超出堆疊頂端元素的限制，則將其彈出並更新邊界。  

注意：從左向右遍歷是處理右邊界，彈出條件是**大於**；第二次從又向左是處理左邊界，彈出條件是**大於等於**。  

處理完左右邊界後，就知道每個元素nums[i]可以貢獻幾次了。遞減排序後找前k個順序去乘上分數。  
一定要使用快速冪，因為k的上限是10^9，直接乘法一定會TLE。  

瓶頸在於最後貢獻的排序，時間複雜度O(N log N)。  
空間複雜度O(N)。  

```python
def pscore(n):
    fact = set()
    p = 2
    while p*p <= n:
        while n % p == 0:
            fact.add(p)
            n //= p
        p += 1
    if n != 1:
        fact.add(n)
    return len(fact)
    
class Solution:
    def maximumScore(self, nums: List[int], k: int) -> int:
        MOD=10**9+7
        N=len(nums)
        
        psc=[pscore(x) for x in nums]
        lb=[0]*N
        rb=[N-1]*N
    
        st=[]
        for i,x in enumerate(psc): # rb
            while st and x>psc[st[-1]]:
                j=st.pop()
                rb[j]=i-1
            st.append(i)
            
        st=[]
        for i in reversed(range(N)): # lb
            x=psc[i]
            while st and x>=psc[st[-1]]:
                j=st.pop()
                lb[j]=i+1
            st.append(i)
            
        arr=[]
        for i,x in enumerate(nums):
            l=i-lb[i]+1
            r=rb[i]-i+1
            arr.append([x,l*r])

        arr.sort(reverse=True)
        ans=1
        for x,rep in arr:
            if k<=0:
                break
            ans*=pow(x,min(k,rep),MOD)
            ans%=MOD
            k-=rep

        return ans
```
