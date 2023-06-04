--- 
layout      : single
title       : LeetCode 2719. Count of Integers
tags        : LeetCode Hard String DP Math
---
周賽348。又忘記取模吃一次WA，好慘。  

# 題目
輸入兩個數字字串num1和num2，以及兩個整數max_sum和min_sum。  
一個**好的**整數x必須滿足：  
- num1 <= x <= num2  
- min_sum <= digit_sum(x) <= max_sum  

求有多少**好的**整數。答案很大，先模10^9+7後回傳。  

注意：digit_sum(x)指的是x中所有數字的加總。  

# 解法
這種求範圍內多少數符合特別條件的，基本上就是**數位DP**。  

要找符合[num1, num2]區間的x很麻煩，可以轉換成[0, nums2]中 扣掉 [0, nums1 - 1]中的個數。  
同理，位數總和digit_sum也要介於[max_sum, min_sum]之間，轉換成[0, max_sum]中 扣掉 [0, min_sum - 1]中的個數。  

定義為f(x, mx_digit)為：小於等於x，且位數和小於等於mx_digit的**好的**整數個數。  
題目要求的是數字x介於[num1, num2]之間，且位數和介於[max_sum, min_sum]之間。  
根據排容原理，公式為：  
> f(num2, max_sum) - f(num1 - 1 , max_sum) - f(num2 , min_sum - 1) + f(num1 - 1 , min_sum - 1)  

做4次數位dp就可以求出，也就是附圖中的紅色區塊。  

![示意圖](/assets/img/2719.jpg)  

```python
class Solution:
    def count(self, num1: str, num2: str, min_sum: int, max_sum: int) -> int:
        MOD=10**9+7
        
        def f(s,mx_digit):
            N=len(s)

            @cache
            def dp(i,cnt_digit,is_limit,is_num):
                if cnt_digit>mx_digit:
                    return 0
                
                if i==N:
                    return is_num
                
                up=int(s[i]) if is_limit else 9
                down=0 if is_num else 1
                ans=0
                if not is_num:
                    ans=dp(i+1,0,False,False)
                for j in range(down,up+1):
                    new_limit=is_limit and j==up
                    ans+=dp(i+1,cnt_digit+j,new_limit,True)
                return ans%MOD
            
            return dp(0,0,True,False)
        
        num1=str(int(num1)-1)
        min_sum-=1
        ans=f(num2,max_sum)-f(num1,max_sum)-f(num2,min_sum)+f(num1,min_sum)
        
        return ans%MOD
```
