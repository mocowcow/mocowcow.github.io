---
layout      : single
title       : LeetCode 410. Split Array Largest Sum
tags 		: LeetCode Hard Array DP BinarySearch Greedy
---
每日題。應該是在以前練二分搜的時候做過，今天仔細看測資，第一直覺是DP，還真可以。

# 題目
輸入正整數數列nums，要把它分成m個連續的非空子陣列，試著將所有子陣列的**最大總和最小化**，並回傳最大的子陣列總和。

# 解法
一般人應該會先想到DP解法吧。  
定義dp(i,m)為nums數列從0到索引i的部分，拆分為m個子陣列時的最大總和最小值。答案就是dp(N-1,m)。  
轉移方程式：dp(i,m)=min(max(nums j~i的總和, dp(j-1,m-1))FOR ALL m-1<=j<=i)。  
簡單講就是試著加入從i開始往左數長度1到i-m+1的子列陣，看加入後會不會讓最小值增加，**如果增加就直接跳出**，因為當前子陣列只會繼續增長，不可能讓結果更小了。  
base cases：i<0，沒有數字要分組，回傳0；m==0，代表分太多組了，不合法，回傳最大值令結果無效。

因為很重要所以再說一次，當子陣列長度超過先前dp結果時就要立即剪枝，不然會TLE。

```python
class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:
        N=len(nums)
        
        @lru_cache(None)
        def dp(i,m): # min largest sum of m subarrys with nums[0~i]
            if i<0:
                return 0
            if m==0:
                return math.inf
            best=math.inf
            sub=0
            for j in range(m-1,i+1)[::-1]:
                sub+=nums[j]
                best=min(best,max(sub,dp(j-1,m-1)))
                if sub>best:
                    break
            return best
        
        return dp(N-1,m)
```

二分法執行時間把DP壓在地上打，直接從2500ms降到50ms。  
寫一個canSplit(most,m)函數來試分組，看能不能把nums分成最多m組，每組最大值為most。  
因為最少每組要有一個數，所以下界為max(nums)，而最差情況就是全部數分到一組去，上界是sum(nums)。  
開始二分搜，如果不能成功以最大值mid分成m組，則試著將每組上限調高，下界更新為mid+1；否則成功分組，上界更新為mid。  

雖然說canSplit函數是計算是否以不超過m組來分，例如nums=[1,2,3], most=100, m=3時，實際上只會用到一組，但是因為組數m不會超過nums大小N，所以必定可以拆成m組，不必考慮組數不足的情況。

```python
class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:
        
        def canSplit(most,m):
            sub=1
            cnt=0
            for n in nums:
                cnt+=n
                if cnt>most:
                    cnt=n
                    sub+=1
                    if sub>m:
                        return False
            return True
        
        lo=max(nums)
        hi=sum(nums)
        while lo<hi:
            mid=(lo+hi)//2
            if not canSplit(mid,m):
                lo=mid+1
            else:
                hi=mid
                
        return lo
```