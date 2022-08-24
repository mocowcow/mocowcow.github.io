--- 
layout      : single
title       : LeetCode 2386. Find the K-Sum of an Array
tags        : LeetCode Hard Array Heap Sorting
---
周賽307。雖然我有想到用heap，但是用的方法不對，還是TLE。

# 題目
輸入整數陣列nums和正整數k。你可以選擇nums中的任意元素組成子序列，並將其加總。  
求nums可產生的所有子序列中，第k大的總和值為多少。  

注意，空子序列的總和為0，且子序列並**不需要是獨特**的。  

# 解法
主要有兩個困難點：  
1. 其中參雜了負數，使得總和的成長不規律  
2. N非常大，若要產生所有2^N個子序列一定超時  

要得到最大總和mx，則應選擇所有非負數的元素。  
將mx扣掉第一小的子序列(空序列)，等於第一大的子序列；  
將mx扣掉第二小的子序列，等於第二大的子序列，以此類推，只需要找到第k小的子序列，並從mx中扣除其總和。  

還有負數的問題。考慮以下情況：  
> nums = [-2,2,4]  
> mx = [2,4] = 6  
> 對mx加上-2或是拿掉2實際上是等價的(都是使總和降低2)
> [4] = [-2,2,4] = 4  

我們可以把所有數字轉換成絕對值，排序後方便找出最小的子序列。  
空序列永遠是最小的子序列，實際上我們只需要找出k-1個較小子序列。  

將轉換成絕對值的數列abs_nums遞增排序，最小的子序列一定是[abs_nums[0]]，以此為基礎裝進heap，建構出其他次小的子序列。  
每次從heap取出最小者，可以選擇直接在後方加入i+1元素，或是以i+1替換當前元素。  

最後拿最大子序列mx扣掉第k-1個最小的子序列，得到答案。排序複雜度為O(N log N)，建構子序列複雜度O(k log k)，整體為O(N log N + k log k)。  

其實我對於子序列的構造方法有點疑惑，還是不確定到底怎樣的情況下才能憑空想出這種作法。[這篇文](https://leetcode.cn/problems/find-the-k-sum-of-an-array/solution/by-asdfasdf-1-syv0/)對構造方法有比較詳細的討論。  

```python
class Solution:
    def kSum(self, nums: List[int], k: int) -> int:
        N=len(nums)
        mx=sum(x for x in nums if x>0)
        abs_nums=[abs(x) for x in nums]
        abs_nums.sort()
        sm=0
        h=[[abs_nums[0],0]]
        
        for _ in range(k-1):
            sm,i=heappop(h)
            if i+1<N:
                heappush(h,[sm+abs_nums[i+1]-abs_nums[i],i+1])
                heappush(h,[sm+abs_nums[i+1],i+1])
        
        return mx-sm
```