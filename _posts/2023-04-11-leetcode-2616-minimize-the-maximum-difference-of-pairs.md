--- 
layout      : single
title       : LeetCode 2616. Minimize the Maximum Difference of Pairs
tags        : LeetCode Medium Array BinarySearch Greedy Sorting DP
---
周賽339。python內建二分函數真的很好用，大概可以省下一分鐘的打字時間。  

# 題目
輸入整數陣列nums和整數p。  

你要找到p個nums中的數對，使得所有數對中的**最大差值最小化**。每一個索引只能被使用一次。  

而索引i和j組成的數對，其差值為\|nums[i] - nums[j]\|，其中\|x\|表示x的**絕對值**。  

求p個數對中**最大差**的**最小值**為多少。  

# 解法
答案具有單調性：如果你能在最大差不超過x的情況下找到p組數對，那麼大於x的情形一定也可以；反之，若x不行，小於x也不行。  
而且nums中元素的順序不影響答案，那就排序吧。  

那怎樣才是最佳的配對法？  
試想以下例子：  
> nums = [0,5,6,10]  
> 當limit = 10時，你可以選擇[0,10]+[5,6]  
> 或是[0,5]+[6,10]  
> 當limit = 5時，你只能選擇[0,5]+[6,10]  
> 如果拿0和10配對的話，只有可能使差值加大，不可能變小  

所以將相鄰的數字配對總是最佳的選擇。  
根據上述所說，最佳的方式一定是相鄰數配對，如果無法配對其前後一位的數，則永遠不會配對成功。例如：  
> nums = [0,5,6,10], limit = 1  
> [0,5]不能配，就不管0了，因為後面的數只會至少是5，不可能跟0得到更小差  
> [5,6]可以配  

而題目說明一個索引只能使用一次，所以配對成功的話直接跳到下兩個數；配對失敗則嘗試下一個數。  

時間複雜度O(N log N + N log MX)，其中MX為max(nums)-min(nums)。空間複雜度O(1)。  

```python
class Solution:
    def minimizeMax(self, nums: List[int], p: int) -> int:
        N=len(nums)
        nums.sort()
        
        def ok(limit):
            i=0
            cnt=0
            while i+1<N:
                # make pair with nums[i] and nums[i+1]
                if nums[i+1]-nums[i]<=limit:
                    i+=2
                    cnt+=1
                # discard nums[i]
                else:
                    i+=1
            return cnt>=p
        
        return bisect_left(range(max(nums)+1),True,key=ok)
```

另外一個思路是動態規劃。  

定義dp[i]：從子陣列nums[0:i]個元素中可以配對的最大數對。  
轉移方程式：
- 若nums[i]-nums[i-1]<=limit，則dp[i]=max(dp[i-1],dp[i-2]+1)  
- 否則dp[i]=dp[i-1]  
base cases：dp[0]沒東西可以配。dp[-1]代表初始狀態，也是0，但因為python支援負數索引，所以不用特別處理。  

對於nums[i]來說，如果不配對，那就是接續前面0\~i-1的結果，也就是dp[i-1]；如果要配對，必須用上前一個數，所以要從0\~i-2的結果在加1，也就是dp[i-2]+1。  

假設nums[i]可以配對，可選拿或不拿，那麼dp[i]=max(dp[i-1], dp[i-2]+1)。  
但是dp[i-1]又是從dp[i-2]或是dp[i-3]轉移而來，所以dp[i]=max(dp[i-2], dp[i-3]+1, dp[i-2]+1)。  
而dp[i-2]已經包含dp[i-3]+1的情形，而dp[i-2]+1一定比dp[i-2]還大，所以乾脆直接取dp[i-2]+1就好。  

時間複雜度O(N log N + N log MX)，其中MX為max(nums)-min(nums)。空間複雜度O(N)，如果改成滾動dp可以降到O(1)。  

```python
class Solution:
    def minimizeMax(self, nums: List[int], p: int) -> int:
        N=len(nums)
        nums.sort()
        
        def ok(limit):
            dp=[0]*N
            for i in range(1,N):
                if nums[i]-nums[i-1]<=limit:
                    # dp[i]=dp[i-2]+1
                    dp[i]=max(dp[i-1],dp[i-2]+1)
                else:
                    dp[i]=dp[i-1]
            return dp[-1]>=p
        
        return bisect_left(range(max(nums)+1),True,key=ok)
```

最後優化完的滾動DP。  

```python
class Solution:
    def minimizeMax(self, nums: List[int], p: int) -> int:
        N=len(nums)
        nums.sort()
        
        def ok(limit):
            pprev=prev=curr=0
            for i in range(1,N):
                if nums[i]-nums[i-1]<=limit:
                    curr=pprev+1
                else:
                    curr=prev
                pprev=prev
                prev=curr
            return curr>=p
                
        return bisect_left(range(max(nums)+1),True,key=ok)
```