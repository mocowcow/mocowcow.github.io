---
layout      : single
title       : LeetCode 1770. Maximum Score from Performing Multiplication Operations
tags 		: LeetCode Medium DP Array
---
DP教學系列。被python內建的cache坑了好幾次TLE，連MLE都出現，不斷調整cache大小才過，太噁心了。

# 題目
輸入長度N的陣列nums，及長度M的陣列multipliers，N>=M。  
你必須執行M次乘法動作，可以選擇nums中最前或是最後的數和multipliers[i]相乘，並獲得分數。nums中使用過的頭或尾必須丟掉，求最多可獲得多少分數。

# 解法
>步驟1：定義狀態  

直覺想用top-down方式，一開始我以dp(i,left,right)表示第i次動作，left、right表示nums可用的最左右方元素位置。  

>步驟2：找出狀態轉移方程式  

對於第i,left,right狀態，要先查看動左邊還是右邊之後造成的影響，何者能夠獲得更大利潤空間，並加上當回合選擇的得分。  
所以dp(i,left,right)=max(左數乘積+dp(i+1, left+1, right),右數乘積+dp(i+1, left, right+1))。

>步驟3：處理base cases  

當i=M-1時，表示處理到最後一個數字了，不必再考慮未來收入，直接回傳max(左數乘積,右數乘積)即可。

後來想到right可以通過計算得到，有點類似之前的[撿櫻桃](https://leetcode.com/problems/cherry-pickup/)，可以節省一個變數，進而將空間從M^3降到M^2。最後變成dp(i,left)。  
程式碼如下，因為懶得手動刻記憶化，結果吃了一堆紅字，得不償失。晚點再更新其他版本。


```python
class Solution:
    def maximumScore(self, nums: List[int], multipliers: List[int]) -> int:
        N = len(nums)
        M = len(multipliers)

        @lru_cache(2000)
        def dp(i, left):
            right = N-1-(i-left)
            if i == M-1:
                return max(nums[left]*multipliers[i], nums[right]*multipliers[i])
            else:
                return max(nums[left]*multipliers[i]+dp(i+1, left+1),
                           nums[right]*multipliers[i]+dp(i+1, left))

        return dp(0, 0)
```

自己做記憶化還是超時，不太確定為什麼，只好改成bottom-up方式。  

```python
class Solution:
    def maximumScore(self, nums: List[int], multipliers: List[int]) -> int:
        N = len(nums)
        M = len(multipliers)
        dp = [[0]*(M+1) for _ in range(M+1)]

        for i in range(M-1, -1, -1):
            for left in range(i, -1, -1):
                right = N-1-(i-left)
                dp[i][left] = max(nums[left]*multipliers[i]+dp[i+1][left+1],
                                  nums[right]*multipliers[i]+dp[i+1][left])

        return dp[0][0]
```

2022-09-17更新。  
今天每日題又輪到這，一看到我按過爛就知道這題有點問題。  
雖然python做top down還是一樣會TLE，但這次定義的dp狀態和之前有些許不同。  
之前是紀錄**第i次動作中，有幾次left次是選擇左邊**，借而推算出右邊界。而今天變成**紀錄左右選擇的次數**來推算出是第i次動作。  
而base case是：總共完成M次動作之後，無法繼續選擇，故回傳0。  

```python
class Solution:
    def maximumScore(self, nums: List[int], multipliers: List[int]) -> int:
        N,M=len(nums),len(multipliers)
        
        @cache
        def dp(left,right):
            if left+right==M:
                return 0
            return max(nums[left]*multipliers[left+right]+dp(left+1,right),
                    nums[N-1-right]*multipliers[left+right]+dp(left,right+1))
            
        return dp(0,0)
```        

同樣的概念換到java做記憶化則可以順利AC。  

```java
class Solution {
    int M,N;
    Integer memo[][];
    int nums[];
    int mul[];
    
    public int maximumScore(int[] nums, int[] multipliers) {
        this.N=nums.length;
        this.M=multipliers.length;
        this.nums=nums;
        this.mul=multipliers;
        this.memo=new Integer[this.M+5][this.M+5];
        return dp(0,0);
    }
    
    int dp(int left, int right){
        if(left+right==M){
            return 0;
        }        
        if(memo[left][right]==null){
            int l=nums[left]*mul[left+right]+dp(left+1,right);
            int r=nums[N-1-right]*mul[left+right]+dp(left,right+1);
            memo[left][right]=Math.max(l,r);
        }
        return memo[left][right];
    }
}
```

我還是不死心，試著把python改成bottom up的方式，總算是順利通過，還勝過98%的提交。  

```python
class Solution:
    def maximumScore(self, nums: List[int], multipliers: List[int]) -> int:
        N,M=len(nums),len(multipliers)
        dp = [[0]*(M+5) for _ in range(M+5)]
        
        for left in range(M-1,-1,-1):
            for right in range(M-left-1,-1,-1):
                dp[left][right]=max(nums[left]*multipliers[left+right]+dp[left+1][right],
                    nums[N-1-right]*multipliers[left+right]+dp[left][right+1])
        
        return dp[0][0]
```