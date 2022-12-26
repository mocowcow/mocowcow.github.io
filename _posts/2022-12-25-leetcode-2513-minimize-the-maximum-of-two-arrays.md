--- 
layout      : single
title       : LeetCode 2513. Minimize the Maximum of Two Arrays
tags        : LeetCode Medium Math BinarySearch
---
雙周賽94。數學果然還是門神，又一次Q3通過率比Q4還低。當然我也沒做出來。  
相似題[878. nth magical number]({% post_url 2022-05-05-leetcode-878-nth-magical-number %})。  

# 題目
你最初有兩個空陣列arr1和arr2，你必須向他們加入一些正整數，使得其符合以下條件：  
- arr1擁有uniqueCnt1個不同的正整數，而且全部不可被divisor1整除  
- arr2擁有uniqueCnt2個不同的正整數，而且全部不可被divisor2整除  

輸入divisor1, divisor2, uniqueCnt1和uniqueCnt2，求滿足條件的情況下，arr1和arr2之中**最大元素**的**最小值**為多少。  

# 解法
雖然當下看到測資範圍10^9，又有**最大值最小化**，馬上知道是二分，但卻想不出怎麼搜，非常難受。  
既然要讓使用到的數字盡可能小，那麼當然是從最小值開始往上加。如果使用的數字越大，能夠滿足條件的機會也越大，答案符合單調性，確實可以使用二分。  

兩個陣列至少都會擁有一個元素，那麼代表最少需要2個數字，所以下界定為2。兩個陣列加起來最多2\*10^9個數字，要再加上一些無法使用的元素，不知道會有多少個。方便起見將上界設為10^10，保證一定足夠。  
寫一個函數ok(x)來判斷以total為最大值能否滿足需求，開始二分。如果mid不滿足，則代表mid以下的數字也不可能滿足，更新下界為mid+1；反之代表mid以上的數字一定可以滿足，更新上界為mid。  

arr1中共有n/divisor1個元素不能選，可用的剩下n-(n/divisor1) = A個；arr2中共有n/divisor2個元素不能選，可用的剩下n-(n/divisor2) = B個。  
而divisor1和divisor2的最小公倍數和其倍數，則是兩者都不能用的。所以arr1和arr2兩者總共有x-(x/lcm)個元素，只要超過uniqueCnt1+uniqueCnt2，就可以保證不會選到重覆的數字。  
只要符合以上三點，就可以確定n能夠滿足條件。  

求lcm的時間複雜度O(divisor1 + divisor2)，二分為O(log(10^10))。空間複雜度O(1)。  

```python
class Solution:
    def minimizeSet(self, divisor1: int, divisor2: int, uniqueCnt1: int, uniqueCnt2: int) -> int:
        lo=2
        hi=10**10
        _lcm=lcm(divisor1,divisor2)
        
        def ok(x):
            A=x-x//divisor1
            B=x-x//divisor2
            AB=x-x//_lcm
            return A>=uniqueCnt1 and B>=uniqueCnt2 and AB>=uniqueCnt1+uniqueCnt2
        
        while lo<hi:
            mid=(lo+hi)//2
            if not ok(mid):
                lo=mid+1
            else:
                hi=mid
 
        return lo
```
