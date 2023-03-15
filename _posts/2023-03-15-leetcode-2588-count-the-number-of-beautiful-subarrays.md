--- 
layout      : single
title       : LeetCode 2588. Count the Number of Beautiful Subarrays
tags        : LeetCode Medium Array BitManipulation PrefixSum HashTable
---
模擬周賽336。又是大家的好朋友位元運算，不過這次沒有這麼明目張膽。  

# 題目
輸入整數陣列nums。每次操作，你可以：  
- 選擇兩個不同的索引i和j，其中0 <= i, j < nums.length  
- 選擇一個非負整數k，且nums[i]和nums[j]在二進位表示中的第k個位元都是1  
- 將nums[i]和nums[j]減去2^k  

如果一個子陣列在執行上述動作任意次後，其元素和為0，則稱為**美麗子陣列**。  

求nums中有多少**美麗子陣列**。  

# 解法
為了使子陣列元素和為0，一旦在相同位置出現兩次1位元，就該進行一次操作將其減掉。  
而兩兩相消這個特性正是XOR運算，將子陣列元素全部XOR，把可以消的1位元都消掉。  

窮舉所有元素n作為子陣列的右端點，並找出左方有哪些出現過的子陣列，與其XOR可以為0。  

時間複雜度O(N)。共有N個前綴，空間複雜度O(N)。  

```python
class Solution:
    def beautifulSubarrays(self, nums: List[int]) -> int:
        d=Counter()
        d[0]=1
        ans=0
        
        ps=0
        for n in nums:
            ps^=n
            ans+=d[ps]
            d[ps]+=1
            
        return ans
```
