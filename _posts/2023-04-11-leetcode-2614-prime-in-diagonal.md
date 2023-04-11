--- 
layout      : single
title       : LeetCode 2614. Prime In Diagonal
tags        : LeetCode Easy Array Matrix Math
---
周賽339。難得Q1的數字這麼大，搞到質數篩直接TLE，太誇張了。  
聽說有不少人沒有把1當成質數吃了WA。說起來我的模板也沒有判斷到這點，趕緊去更新。  

# 題目
輸入二維整數陣列nums。  

求nums在**對角線**上最大**質數**。如果對角線上沒有質數，則回傳0。  

注意：  
- 質數必須大於1，且不可被自己以外的正整數整除  
- 對角線指的是nums[i][i]或是nums[i][nums.length-i-1]的位置  

# 解法
題目很良心的告訴我們斜角線的座標，只要遍歷對角線上的元素，如果是質數則更新答案。  
篩選出質數表，之後每次質數檢查都是O(1)。但是這裡的nums[i][j]高達4\*10^6，每次篩會超時，必須放到全域去。  

時間複雜度O((MX log log MX) + N)，其中MX為max(nums[i][j])。空間複雜度O(MX)。  

```python
MX=4*10**6
sieve=[True]*(MX+1)
sieve[0]=sieve[1]=False
for i in range(2,MX+1):
    if sieve[i]:
        for j in range(i*i,MX+1,i):
            sieve[j]=False

class Solution:
    def diagonalPrime(self, nums: List[List[int]]) -> int:
        N=len(nums)
        ans=0
        
        for i in range(N):
            for j in [i,N-1-i]:
                x=nums[i][j]
                if sieve[x]:
                    ans=max(ans,x)
                    
        return ans
```

這題應該比較適合暴力檢查是否為質數，畢竟判斷一次只要O(sqrt(x))，最多只要判斷600次而已。  
直接寫一個判斷函數，只要x不為1，且無法被2\~sqrt(x)的任一整數整除就是質數。  

另外有個小加速點，先確定數字大於當前答案在去判斷質數，如果小於ans就不管了。  

時間複雜度O(N\*sqrt(MX))，其中MX為max(nums[i][j])。空間複雜度O(1)。  

```python
class Solution:
    def diagonalPrime(self, nums: List[List[int]]) -> int:
        N=len(nums)
        ans=0
        
        def is_prime(x):
            if x==1:
                return False
            for i in range(2,int(x**0.5)+1):
                if x%i==0:
                    return False
            return True
        
        for i in range(N):
            for j in [i,N-1-i]:
                x=nums[i][j]
                if x>ans and is_prime(x):
                    ans=x
                    
        return ans
```