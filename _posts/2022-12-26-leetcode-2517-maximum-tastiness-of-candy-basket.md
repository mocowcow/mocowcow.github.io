--- 
layout      : single
title       : LeetCode 2517. Maximum Tastiness of Candy Basket
tags        : LeetCode Medium Array BinarySearch Sorting
---
周賽325。當時腦子被Q2搞亂，沒有馬上意識到又是二分答案。  

# 題目
輸入正整數k，還有正整數陣列price，其中price[i]代表第i個糖果的價格。  

商店一次要出售k種**不同**的糖果的禮盒。禮盒的**甜蜜度**是盒中任意兩種糖果價格絕對差的**最小值**。  

求禮盒的**最大甜蜜度**。  

# 解法
將糖果排序之後，每顆糖果與其相鄰之間的絕對差一定會是最小值。  
若我們選擇絕對差至少為x，x越小可以拿的糖果越多；反之x越大，能拿的糖果越少，答案符合單調性可二分。  

最差情況下不管絕對差，糖果全拿，下界設為0。最好的情況下只需要兩顆糖果，只拿最便宜和最貴的，上界設為max(price)-min(price)。  
開始二分答案，如果mid無法拿滿k種糖果，則代表mid以上的都不可能合法，需要降低絕對差限制，更新上界為mid-1；否則mid代表以下都可以拿滿k種糖果，更新下界為mid。注意：當lo=0, hi=1, mid=0的情況下，若取左中位數則會死循環，所以要使用右中位數(lo+hi+1)//2。  

至於如何判斷糖果拿不拿？我們可以維護一個變數prev紀錄上種糖果的價格，遍歷所有糖果curr，若prev與curr絕對差滿足絕對差x，則計數+1，更新prev。  

排序成本O(N log N)，二分成本O(N log M)，其中N為糖果數量，M為max(price)-min(price)，整體時間複雜度O(N log N + N log M)。空間複雜度O(1)。  

```python
class Solution:
    def maximumTastiness(self, price: List[int], k: int) -> int:
        price.sort()
        
        def ok(x):
            cnt=0
            prev=-inf
            for curr in price:
                if curr-prev>=x:
                    cnt+=1
                    prev=curr
            return cnt>=k
        
        lo=0
        hi=price[-1]-price[0]
        while lo<hi:
            mid=(lo+hi+1)//2
            if not ok(mid):
                hi=mid-1
            else:
                lo=mid

        return lo
```
