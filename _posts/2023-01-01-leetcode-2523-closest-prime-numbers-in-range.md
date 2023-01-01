--- 
layout      : single
title       : LeetCode 2523. Closest Prime Numbers in Range
tags        : LeetCode Medium Array Math
---
周賽326。還是質數，我願稱本次為質數周賽。  
話說回來，這似乎是我第一次碰到沒有hard題壓軸的周賽。  

# 題目
輸入兩個正整數left和right，找到兩個整數num1和num2，滿足：  
- left <= nums1 < nums2 <= right  
- nums1和nums2都是質數  
- nums2 - nums1為滿足以上條件的數對中的**最小值**  

回傳正整數陣列ans = [nums1, nums2]。如果有多個數對滿足條件，則回傳nums1值最小者。若不存在則回傳[-1, -1]。  

# 解法
使用[埃拉托斯特尼篩法](https://zh.wikipedia.org/zh-tw/%E5%9F%83%E6%8B%89%E6%89%98%E6%96%AF%E7%89%B9%E5%B0%BC%E7%AD%9B%E6%B3%95)，預處理範圍內所有的質數。  

和原版的篩法稍微有點不同，我們只要保留大於等於left的質數以供接下來使用。  
先初始化答案為[-1, -1]，以及最小差值mn為inf。因為篩出來的質數已經是有序的，只要直接遍歷兩兩相鄰的數對，如果兩者絕對差小於mn，則以當前數對更新答案。  

這個篩法複雜度真不好算，姑且忽略標記非質數的操作，時間複雜度O(right)。需要紀錄1\~right是否為質數，空間複雜度O(right)。  

```python
class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:
        ok=[True]*(right+1)     
        p=[]
        
        for i in range(2,right+1):
            if ok[i]:
                if i>=left:
                    p.append(i)
                j=i*i
                while j<=right:
                    ok[j]=False
                    j+=i

        mn=inf
        ans=[-1,-1]
        for a,b in pairwise(p):
            if b-a<mn:
                mn=b-a
                ans=[a,b]
                
        return ans
```

也可以把只做一次預處理，之後分別取出介於left和right之間的值來使用就好。  
執行時間降低到595ms，比上面的5296ms降低許多。  

```python
ok=[True]*1000005     
primes=[]
for i in range(2,1000005):
    if ok[i]:
        primes.append(i)
        j=i*i
        while j<=1000000:
            ok[j]=False
            j+=i

class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:
        p=[x for x in primes if left<=x<=right]
        mn=inf
        ans=[-1,-1]
        for a,b in pairwise(p):
            if b-a<mn:
                mn=b-a
                ans=[a,b]
                
        return ans
```