--- 
layout      : single
title       : LeetCode 2681. Power of Heroes
tags        : LeetCode Hard Array Sorting DP PrefixSum
---
雙周賽104。這題也繞好大一圈的遠路，搞出一個沒什麼人用的解法，但好歹是過了。  

# 題目
輸入整數陣列nums，代表每個英雄的能力值。  
而一個英雄團隊的**力量**定義如下：  
- 設i0, i1, ... , ik為團隊中英雄的索引。其力量為max(nums[i0], nums[i1], ... , nums[ik])^2 \* min(nums[i0], nums[i1], ... , nums[ik])  

求所有**非空**團隊的**力量**總和。答案很大，先模10^9+7後回傳。  

# 解法
順序不影響答案，總之先排序。  

每個英雄可選可不選，共有2^N-1種非空團隊的選法。  
而每個團隊的力量為團隊內**最大值^2 \* 最小值**。  

接下來遍歷排序好的nums，窮舉每個nums[i]作為最大值，並維護先前出現過的最小值貢獻。  
以[1, 2, 3, 4]為例：  
- 加入1，mn=[1]，力量 = (1^2)\*(1) = 1    
- 加入2，mn=[1, 2]，力量 = (2^2)\*(1 + 2) = 12  

接下來不太一樣了：加入3之後，因為1和mx=3之間存在一個元素2，可選可不選：  
- 所以1實際上在[1, 2, 3]和[1, 3]兩種選法中做出貢獻  
- 加入3，mn=[1\*2, 2, 3]，力量 = (3^2)\*(1\*2 + 2 + 3) = 63  

加入4之後，1和mx=4中間又多一個元素，所以1貢獻次數從2倍變成4倍；  
至於2和mx=4之間也有一個元素，所以貢獻也變2倍：  
- 加入4，mn=[1\*4, 2\*2, 3]，力量 = (4^2)\*(1\*4 + 2\*2 + 3 + 4) = 240  
- 總力量為1 + 12 + 63 + 240 = 316  

可以發現，在i=0和1的時候，mn只會單純的加上nums[i]；但是從i=2開始，mn不僅是加上nums[i]，還要加上[0, i-2]區間的所有mn。  
因此在遍歷每個i時，除了維護當前的mn值，還要維護0\~i所有mn的前綴和。  

瓶頸在於排序，時間複雜度O(N log N)。  
空間複雜度O(N)。  

```python
class Solution:
    def sumOfPower(self, nums: List[int]) -> int:
        MOD=10**9+7
        N=len(nums)
        nums.sort()
        
        ans=0
        mn=0
        ps=[0]*N
        
        for i,x in enumerate(nums):
            mn+=x
            if i>1:
                mn+=ps[i-2]
            mn%=MOD
            
            ps[i]=mn
            if i>0:
                ps[i]+=ps[i-1]
            ps[i]%=MOD
            
            ans+=x*x*mn
            ans%=MOD

        return ans
```

前綴和其實是多此一舉。  

再仔細研究[1, 2, 3, 4]這個例子：  
- 最初，mn=[]  
- 加入1，mn=[1]  
- 加入2，mn=[1, 2]  
- 加入3，mn=[1\*2, 2, 3]  
- 加入4，mn=[1\*4, 2\*2, 3]  

可以發現，每加入一個元素x，mn中除了最後加入的元素prev以外，其他元素的貢獻都會變成2倍，也就是mn\*2-prev再加上新來的x。  
只要維護上一個加入的數字prev，就可以透過公式快速推出貢獻值。  

瓶頸在於排序，時間複雜度O(N log N)。  
空間複雜度O(1)。  

```python
class Solution:
    def sumOfPower(self, nums: List[int]) -> int:
        MOD=10**9+7
        nums.sort()
        ans=0
        mn=0
        prev=0
        
        for x in nums:
            mn=mn*2-prev+x
            mn%=MOD
            ans+=x*x*mn
            ans%=MOD
            prev=x
            
        return ans
            
```