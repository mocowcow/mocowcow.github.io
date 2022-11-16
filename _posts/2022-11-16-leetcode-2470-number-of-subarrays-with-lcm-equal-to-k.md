--- 
layout      : single
title       : LeetCode 2470. Number of Subarrays With LCM Equal to K
tags        : LeetCode Medium Array Math
---
周賽319。相似題[2447. number of subarrays with gcd equal to k]({% post_url 2022-10-23-leetcode-2447-number-of-subarrays-with-gcd-equal-to-k %})。  
比賽時忘記python內建有lcm函數，自己寫了奇怪的判斷有通過，後來被rejudge掉，真是死的莫名其妙。  

# 題目
輸入陣列nums和整數k，求nums有多少子陣列的**最小公倍數**正好為k。  

若有某個最小的正整數可以被陣列所有元素整除，則稱為**陣列的最小公倍數**。  

# 解法
測資範圍很小，一樣可以用暴力法窮舉所有子陣列，並計算lcm。若lcm為k時答案+1。  
這題有個小陷阱：如果在lcm大於k之後沒有終止回圈，在某些語言會使lcm溢出，拿到免費WA。  

求lcm的時候要先求gcd，而gcd的時間是O(log N)。兩層回圈共N^2次計算，總時間複雜度為O(N^2\*log N)，空間複雜度O(1)。  

```python
class Solution:
    def subarrayLCM(self, nums: List[int], k: int) -> int:
        N=len(nums)
        ans=0
        for i in range(N):
            x=nums[i]
            for j in range(i,N):
                x=lcm(x,nums[j])
                if x==k:ans+=1
                elif x>k:break
        
        return ans
```

> lcm(a,b) = a\*b/gcd(a,b)  

自己寫gcd和lcm的解法。再也不想在這鬼地方上失分。  

```python
class Solution:
    def subarrayLCM(self, nums: List[int], k: int) -> int:
        N=len(nums)
        ans=0
        
        def gcd(a,b):
            if b==0:return a
            return gcd(b,a%b)
        
        def lcm(a,b):
            return a*b//gcd(a,b)
        
        for i in range(N):
            x=nums[i]
            for j in range(i,N):
                x=lcm(x,nums[j])
                if x==k:ans+=1
                elif x>k:break
                    
        return ans
```