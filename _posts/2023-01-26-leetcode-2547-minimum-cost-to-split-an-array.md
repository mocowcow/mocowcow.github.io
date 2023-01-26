--- 
layout      : single
title       : LeetCode 2547. Minimum Cost to Split an Array
tags        : LeetCode Hard Array DP HashTable
---
周賽329。靠python有時候真的很吃運氣，明明複雜度是對的，可是就是會TLE。比賽當時優化了兩次才AC。  
後來再把TLE的程式碼交一次，竟然又AC了，莫名其妙。  

# 題目
輸入整數陣列nums和整數k。  

試將nums分割成數個非空的子陣列。分割**成本**為每個分割出的子陣列的**重要度**總和。  

定義trimmed(subarray)為修剪過後的子陣列，其中刪除了所有只出現一次的數字。  
- 例如trimmed([3,1,2,4,3,4]) = [3,4,3,4]  

而子陣列的**重要度**為k+修剪後的子陣列長度。  
- 例如子陣列是[1,2,3,3,3,4,4]，則trimmed([1,2,3,3,3,4,4]) = [3,3,3,4,4]。該子陣列的重要度為k+5  

求分割陣列的**最小成本**。  

# 解法
題目問的是找出成本最小的切法，部在乎你切幾段，甚至不切也可以，那麼我們只需要在每個位置決定**切或不切**。  

試想以下例子：  
> nums = [1,2,3]  
> 可以切成 [1], [2,3]
> 或是[1], [2], [3]  
> 或是[1,2], [3]  

對於[1],[2]和[1,2]兩種切法，都會重複計算到[3]的結果，因此可以使用dp。  

定義dp(i)：從i開始的子陣列的最小分割成本。  
轉移方程式：dp(i)=min(cost(i, j) + dp(j+1))，其中cost(i, j)代表將i\~j分割出一個子陣列的成本。  
base case：當i=N時，整個字串都分割完畢，不需要繼續分割，回傳成本0。  

在計算**重要度**的時候，只出現一次的數字不會增加成本，而會在出現第二次後開始計算，因此當每個數字第二次出現的時候直接將成本加2，之後每出現一次成本再加1，從i\~N-1中找到最低成本的切割點。  

對於長度為N的nums來說，共有N個切割點，而每個切割點狀態都需要N次轉移，因此時間複雜度O(N^2)。空間複雜度O(N)。  

順帶一提，python的min / max函數非常慢，如果TLE的話手動改成if判斷會加速不少。  
 
```python
class Solution:
    def minCost(self, nums: List[int], k: int) -> int:
        N=len(nums)
        
        @cache
        def dp(i):
            if i==N:
                return 0
            best=inf
            d=Counter()
            cost=k
            for j in range(i,N):
                c=nums[j]
                d[c]+=1
                if d[c]==2:
                    cost+=2
                elif d[c]>2:
                    cost+=1
                best=min(best,cost+dp(j+1))
            return best
        
        return dp(0)
```
