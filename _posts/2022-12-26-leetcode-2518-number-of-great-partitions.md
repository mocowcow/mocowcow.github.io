--- 
layout      : single
title       : LeetCode 2518. Number of Great Partitions
tags        : LeetCode Hard Array DP
---
周賽325。又死在DP上，只能想到O(k^2\*N)的方法，當然是沒過。開始懷疑我是不是真的會DP。  

# 題目
輸入由**正整數**組成的陣列nums，以及正整數k。  

將陣列**分割**成兩個有序的**組別**，令每個元素恰好屬於其中一組。若兩組別的元素和都大於等於k，則稱其為**好的分割**。  

求**不同**的**好分割**數量，答案可能很大，先模10^9+7後回傳。  

若有兩種分割方式，其中nums[i]被分到不同的組別，則視為**不同的分割**。  

# 解法
將nums分成兩組，其實可以看做01背包問題：拿的話就放在A組，不拿就放在B組。兩組總和都超過k就是**好的分割**。  
但是nums[i]非常大，隨便都超過k，非常難算。乾脆反過來找**不好的分割**，用總分割數扣掉不好的分割就是答案。  

設nums總和為sm，若AB兩組總和都要超過k，則sum必須大於等於k\*2；否則一個都不可能成功，答案為0。  
而在sm>=k\*2的前提之下，任何一個壞的分割總和最多只會到k-1，而另一組的總和必然大於k+1。  
對於每個nums[i]只有A或B組兩種選擇，分割總共有2^N種方式。  
以nums = [1,2,3,4], k= 4為例：  
> 共有2^4 = 16種分割  
> 不好的分割 = [1], [1,2], [1,3], [2], [3] 共5種  
> 這5種可以是在A也可以在B組，所以5*2 = 10  
> 答案16-10 = 6種好的分割  

首先找到所有總和小於k的**不好的分割**方式，定義dp[i][j]：總和為j的分組方式。  
轉移方程式：dp[i][j]=dp[i-1][j]+dp[i-1][j-nums[i]]  
base case：完全不拿也是一種選擇，dp[0][0]=1；若j<0則為非法狀況，只有0種方法  

因為每次疊代新的元素之後，只會參考到上一次的DP結果，所以可以壓縮成一維陣列。  

時間複雜度O(Nk)。空間複雜度O(k)。  

```python
class Solution:
    def countPartitions(self, nums: List[int], k: int) -> int:
        MOD=10**9+7
        N=len(nums)
        
        if sum(nums)<k*2:return 0
        
        dp=[0]*k
        dp[0]=1
        for n in nums:
            for i in reversed(range(k)):
                if i>=n:
                    dp[i]=(dp[i]+dp[i-n])%MOD

        return (pow(2,N,MOD)-sum(dp)*2)%MOD
```

一直很好奇如果沒有判定sum<k\*2會怎樣，所以花了一些時間研究其中奧妙，順便換個語言當練習。  
01背包DP的部分也使用原汁原味的二維陣列，如果上面那種空間壓縮的版本看不懂，可以先從這版本開始理解。  

舉個例子：  
> nums = [2,3], k = 4  
> 要求0\~3的分割方法數量  
> dp[0] = 1, dp[2] = 1, dp[3] = 1  

如果直接照著上面sum(dp)\*2的話會得到6種壞的分割，某些地方重複計算到使得答案不正確。來看看哪邊算錯：  
> 全部的分割方式有4種：  
> [] + [2,3]  
> [2] + [3]  
> [3] + [2]  
> [2,3] + []  

原來是[2]+[3]和[3]+[2]分別被重複計算到了。因為我們窮舉dp[2]時，另一邊剩餘的數為5-2=3，比k還要小，其實已經算在裡面了。  
當sum-i\<k時，他的反向組合已經包含在dp中，只要計算一次就夠了。  

```go
func countPartitions(nums []int, k int) int {
    MOD:=int(1e9+7)
    N:=len(nums)
    
    // get all partitions and sum of nums
    total:=1
    sum:=0
    for i:=0;i<N;i++{
        total=(total*2)%MOD
        sum=(sum+nums[i])%MOD
    }
        
    // bad partitions using knapsack DP
    dp:=make([][]int,N+1)
    for i:=0;i<=N;i++{
        dp[i]=make([]int,k)   
    }
    dp[0][0]=1
    for i:=1;i<=N;i++{
        n:=nums[i-1]
        for j:=0;j<k;j++{
            if j>=n{
                dp[i][j]=(dp[i-1][j]+dp[i-1][j-n])%MOD
            }else{ 
                dp[i][j]=dp[i-1][j]
            }
        }
    }
    
    // total - bad
    for i:=0;i<k;i++{
        if sum-i>=k{
            total=(total-dp[N][i]*2)%MOD            
        }else{
            total=(total-dp[N][i])%MOD
        }
        total=(total+MOD)%MOD
    }
    
    return total
}
```