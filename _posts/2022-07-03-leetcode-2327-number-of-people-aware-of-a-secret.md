--- 
layout      : single
title       : LeetCode 2327. Number of People Aware of a Secret
tags        : LeetCode Medium DP PrefixSum
---
周賽300。寫這題差點沒氣死，窗外還飛來一堆鴿子瘋狂咕咕咕，腦子整個打結，好險最後是有做出來。

# 題目
在第一天，只有1個人知道秘密。  

輸入整數n、delay還有forget。人們會在得知祕密的第delay天開始和另一個人分享祕密，並在得知後的第forget天忘記秘密。在忘記的當天以及之後的日子都不會和其他人分享祕密。  

求在第n天結束時知道秘密的人數。答案很大，模10^9+7後再回傳。  

# 解法
一開始我總覺得需要三個陣列，分別紀錄知曉人數、新增人數和忘記人數。  
最後才想通只需要兩個，know[i]紀錄第i天的知曉人數，而inc[i]紀錄第i天新增的人數。  

n最多和delay最多到1000，方便起見將陣列長度開到2005，保證能夠處理第1000天得知，並在2000天忘記的情況。  
首先初始化第一天的情形，知曉者1人，而他將會在1+forget天後忘記，所以將know[1]設為1，know[1+forget]-=1。  
而這個人在[1+delay,1+forget)這個日期區間中，每天都會洩密給新的人，我們應將這區間的每個日期都加上1。  
但是在delay=1, forget=1000的情況下，複雜度會變成O(N^2)，有點慢，所以採用difference array，在區間的開始日期加上1，結束日期檢掉1，並對inc陣列做前綴和，可以將整體複雜度降到O(N)。  

最後從第2天開始計算到第n天，和上述所做的事情大同小異：  
- 對inc[i]做差分，求出今天增加人數  
- 今天多了inc[i]個人知道秘密，know[i]加上inc[i]  
- 這inc[i]個人在forget天之後會忘記，know[i+forget]扣掉inc[i]  
- 在[i+delay, i+forget)區間每天會多增加inc[i]人，inc[i+delay]加上inc[i]，inc[i+forget]扣掉inc[i]  

最後回傳know[n]就是答案，超出n之後的部分不管。  

```python
class Solution:
    def peopleAwareOfSecret(self, n: int, delay: int, forget: int) -> int:
        MOD=10**9+7
        know=[0]*2005
        inc=[0]*2005
        # init 
        know[1]=1
        know[1+forget]-=1
        inc[1+delay]+=1
        inc[1+forget]-=1
        
        for i in range(2,n+1):
            inc[i]+=inc[i-1]
            know[i]=(know[i]+know[i-1]+inc[i]) %MOD
            know[i+forget]-=inc[i]
            inc[i+delay]+=inc[i]
            inc[i+forget]-=inc[i]

        return know[n] %MOD
```

後來想想，出題者應該沒想要考差分，畢竟N才1000，就算是O(N^2)也是可以過的。  
將差分陣列改回暴力迴圈的方法。

```python
class Solution:
    def peopleAwareOfSecret(self, n: int, delay: int, forget: int) -> int:
        MOD=10**9+7
        dp=[0]*2005
        inc=[0]*2005
        #init
        dp[1]=1
        dp[1+forget]-=1
        for j in range(1+delay,1+forget):
            inc[j]+=1
        
        for i in range(2,n+1):
            dp[i]=(dp[i-1]+dp[i]+inc[i]) %MOD
            dp[i+forget]-=inc[i]
            for j in range(i+delay,i+forget):
                inc[j]+=inc[i]
                
        return dp[n] %MOD
```