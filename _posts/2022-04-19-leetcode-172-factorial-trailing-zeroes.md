---
layout      : single
title       : LeetCode 172. Factorial Trailing Zeroes
tags 		: LeetCode Medeium Math
---
跟[2245. Maximum Trailing Zeros in a Cornered Path]({% post_url 2022-04-18-leetcode-2245-maximum-trailing-zeros-in-a-cornered-path.md %})有點關係。  
很久以前理應看過這題，八成是因為沒什麼想法就略過不管，沒想到那時欠下的債竟在比賽的時候被催繳，太苦了。

# 題目
輸入整數n，求n的階乘有多少尾隨0。  

# 解法
上次有說過，尾隨0是由2和5的因素所組成，我們只要在意這兩個數有多少就好。  
n的乘階為1連乘到n，遍歷所有數字，將他們的因數2和5分別加總，算出可以產生多少0。

```python
class Solution:
    def trailingZeroes(self, n: int) -> int:
        c2=c5=0
        for i in range(1,n+1):
            t=i
            while t%2==0:
                c2+=1
                t//=2
            t=i
            while t%5==0:
                c5+=1
                t//=5
                
        return min(c2,c5)
```

但是在這題中，2出現的次數多得要命，隨便撿都有，其實只要算5就好。  

```python
class Solution:
    def trailingZeroes(self, n: int) -> int:
        c5=0
        for i in range(1,n+1):
            while i%5==0:
                c5+=1
                i//=5
                
        return c5
```

但還能繼續優化。  
當第一個因數5出現後，下一次出現的時候是在25、125、625..，都是5的倍數成長。  
那直接把乘階除5就好，例：  
> n=15  
> 5,10,5 各取出一個因數5  
> 15/5=3  
> 5,10 各取出一個因數5  
> 3/5=0 停止  
> 共2+1個因數  

```python
class Solution:
    def trailingZeroes(self, n: int) -> int:
        cnt=0
        while n>=5:
            n//=5
            cnt+=n
            
        return cnt
```