--- 
layout      : single
title       : LeetCode 2333. Minimum Sum of Squared Difference
tags        : LeetCode Medium Array Heap BinarySearch
---
雙周賽82。這題也挺難的，需要兩個心眼才能解決，可惜時間不夠我解決。

# 題目
輸入兩個長度為n的陣列nums1和nums2。  
**平方差和**指的是所有(nums1[i]-nums2[i])^2的總和。  

另有兩個整數k1和k2，代表你可以對nums1中任意元素加1或是減1最多k1次，且對nums2中任意元素加1或是減1最多k2次。  
求最小的**平方差和**。  

注意：你可以將陣列中的元素修改為負數。  

# 解法
若差為x-y，對x+1或是對y-1是等價的，這意味著k1和k2沒有區別，總共可以使差值縮減k=k1+k2次。  
如此一來只需要每次挑出最大的差，每次將其縮減1，重複k次就好。  

但是第二個難點來了：k1和k2高達10^9，加起來最多2*10^9。  
就算用heap找最大差，肯定也是會TLE的，要想辦法減少計算次數。  

這時二分搜就派上用場了，所有元素的值介於0和10^5之間，我們可以找出一個適當的臨界點x，將所有超過x的差降低為x，且總降低的數值不超過k。這時k剩下的大小就減少很多，繼續使用heap找最大差慢慢減小，最後算出**平方差和**即可。  

提供一個簡陋的證明k為什麼會變得夠小：  
1. 若k足夠消除所有差，那答案為0  
2. 每次將臨界點降低1，k的使用量變化值最多為nums的長度，也就是10^5  
3. 故k剩餘不會超過10^5  

```python
class Solution:
    def minSumSquareDiff(self, nums1: List[int], nums2: List[int], k1: int, k2: int) -> int:
        k=k1+k2
        diff=[]
        for a,b in zip(nums1,nums2):
            diff.append(abs(a-b))
        diff.sort(reverse=1)
        
        def canDo(x):
            cnt=0
            for n in diff:
                if n>x:
                    cnt+=n-x
            return cnt<=k
        
        # find critical
        lo=0
        hi=10**5
        while lo<hi:
            mid=(lo+hi)//2
            if not canDo(mid):
                lo=mid+1
            else:
                hi=mid

        h=[]
        # shave off to critical
        for n in diff:
            if n>lo:
                k-=n-lo
                heappush(h,-lo)
            else:
                heappush(h,-n)

        for _ in range(k):
            if h[0]==0:
                break
            t=-heappop(h)
            heappush(h,-(t-1))

        ans=0
        for x in h:
            ans+=x*x
        
        return ans
```
