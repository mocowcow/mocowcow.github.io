---
layout      : single
title       : LeetCode 2827. Number of Beautiful Integers in the Range
tags        : LeetCode Hard String DP math
---
雙周賽111。第三次數位dp，賽候補題的朋友有福了。  

## 題目

輸入整數low, high還有k。  

若一個數字number滿足以下條件，則稱為**美麗的**：  

- 奇數和偶數位的出現次數相同  
- number被k整除  

求有多少**美麗的**數字介於區間[low, high]。  

## 解法

相似題[2801. count stepping numbers in range]({% post_url 2023-07-30-leetcode-2801-count-stepping-numbers-in-range %})，核心思路都一樣，懶得再寫了。  

差別在於這次high的範圍比較小，只有到10^9，可以直接用整數型別減1。  

在確保奇偶出現次數相同時，不需要odd, even兩個變數，只需要維護均衡度bal，碰到奇數+1，偶數則-1。  

整除的部分比較奇妙，我也想了一段時間才想通。  
例如num=121, k=11：  
> 從最高位開始遞迴  
> i=0, nums[0]=1，代表1個100，不足k=11個1100，剩餘100  
> i=1, nums[1]=2，代表2個10，加上剛才剩的100共120，可以滿足一個11\*10，剩餘10  
> i=2, nums[2]=1，代表1個1，加上剛才剩的10共11，可以滿足一個11\*1，剩餘0  
> i=3, 沒有數字了，餘數也為0，因此合法  

反正就像是普通的除法一樣，每次試著用k的倍數去除，餘數丟給下一個較小的倍數繼續除。

i有N種，bal範圍[-N, N]，總共有N^2\*k種狀態，每個狀態需要轉移D次。  
時間複雜度O(N^2\*k\*D)，其中N為O(log high)，也就是high轉成數字的長度。D為10種數字。  
空間複雜度O(N^2\*k)。  

```python
class Solution:
    def numberOfBeautifulIntegers(self, low: int, high: int, k: int) -> int:
        
        def f(x):
            s=str(x)
            N=len(s)

            @cache
            def dp(i,is_limit,is_num,bal,remain):
                if i==N:
                    return int(is_num and bal==0 and remain==0)
                up=int(s[i]) if is_limit else 9
                down=0 if is_num else 1
                ans=0
                if not is_num:
                    ans=dp(i+1,False,False,0,0)
                for j in range(down,up+1):
                    new_limit=is_limit and j==up
                    new_bal=bal+1 if j%2==1 else bal-1
                    new_remain=(remain*10+j)%k
                    ans+=dp(i+1,new_limit,True,new_bal,new_remain)
                return ans

            return dp(0,True,False,0,0)
        
        ans=f(high)-f(low-1)
                
        return ans
```
