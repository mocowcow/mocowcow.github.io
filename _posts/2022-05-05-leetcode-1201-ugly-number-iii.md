--- 
layout      : single
title       : LeetCode 1201. Ugly Number III
tags        : LeetCode Medium Math BinarySearch
---
二分搜學習計畫。[878. nth magical number]({% post_url 2022-05-05-leetcode-878-nth-magical-number %})的困難版，但是難度卻是medium，莫名其妙。

# 題目
**醜數字**指的是某個能被a,b或c整除的整數。  
輸入整數n,a,b,c，求第n個醜數字。

# 解法
跟魔法數字一樣，只是交集的地方變多了。  
![示意圖](/assets/img/1201-1.jpg)  
所以要扣除掉AB和AC還有BC的部分，再補回多扣的ABC。  

然後題目還有講，答案最大只會到2*10^9，可以直接拿來當上界。  

```python
class Solution:
    def nthUglyNumber(self, n: int, a: int, b: int, c: int) -> int:
        # precompute lcm
        ab=a*b//math.gcd(a,b)
        ac=a*c//math.gcd(a,c)
        bc=b*c//math.gcd(b,c)
        abc=a*bc//math.gcd(a,bc)            
        
        def countUgly(x):
            cnt=x//a+x//b+x//c
            cnt-=x//ab
            cnt-=x//ac
            cnt-=x//bc
            cnt+=x//abc
            return cnt
        
        lo=1
        hi=2*(10**9)
        while lo<hi:
            mid=(lo+hi)//2
            if countUgly(mid)<n:
                lo=mid+1
            else:
                hi=mid
    
        return lo
```
