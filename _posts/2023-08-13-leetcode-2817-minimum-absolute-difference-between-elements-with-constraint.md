---
layout      : single
title       : LeetCode 2817. Minimum Absolute Difference Between Elements With Constraint
tags        : LeetCode Medium Array SlidingWindow TwoPointers SortedList BinarySearch
---
周賽358。又被輸入參數的x卡掉一點時間，這點真的很麻煩。  

## 題目

輸入整數陣列nums，還有正數x。  

找到最小的數對元素**絕對差**，其中兩個索引至少相隔x。  

也就是說找到兩個索引i和j，滿足abs(i-j) >= x，且 abs(nums[i] - nums[j])是最小值。  

回傳至少相隔x的**最小**的絕對差。  

## 解法

其實有點像是滑動窗口，差別在於窗口內的元素不能選。  

題目要求找數對絕對差，可以枚舉所有元素nums[i]，試著在nums[0, i-x]和nums[i+x, N-1]之間，找到最接近nums[i]的數來組成數對。  

看看例題二：  
> nums = [5,3,2,10,15], x = 1  
> nums[0]=5，可以和[3,2,10,15]成對  
> nums[1]=3，可以和[5]、[2,10,15]成對  
> nums[2]=2，可以和[5,3]、[10,15]成對  
> nums[3]=10，可以和[5,3,2]、[15]成對  
> nums[4]=15，可以和[5,3,2,10]成對  

在遍歷nums的時，不可用區間窗口也向右移動。  
維護一個sorted list，初始化時將nums整個加入。在遍歷過程中，將進入窗口範圍的元素從sl中刪除；並將離開窗口的元素加回sl。  
調整完可用的元素後，在從sl中找到最接近nums[i]的數，以絕對差更新答案。  

需要注意的是：我們在sl中找第一個大於等於val的數，其索引為idx。但有可能不存在，記得要檢查邊界；同理，val也可能和最後一個小於他的數組成對，若idx不為0，則代表存在小於val的數。  

時間複雜度O(N log N)。  
空間複雜度O(N)。  

```python
from sortedcontainers import SortedList as SL

class Solution:
    def minAbsoluteDifference(self, nums: List[int], x: int) -> int:
        sl=SL(nums)

        ans=inf
        lb=rb=-1
        for val,i in enumerate(nums):
            R=i+x-1 # [L, R] cant be used
            L=i-x+1
            while rb+1<N and rb<R: # expand right bound
                rb+=1
                sl.remove(nums[rb])
            while lb+1<L: # shrink left bound
                lb+=1
                sl.add(nums[lb])
            
            # update abs diff
            idx=sl.bisect_left(val)
            if idx<len(sl):
                ans=min(ans,abs(sl[idx]-val))
            if idx>0:
                ans=min(ans,abs(sl[idx-1]-val))
        
        return ans
```

仔細想想，上面的方法很冗餘，多出一堆不必要的操作，重點還很容易寫錯。我比賽中沒錯真是奇蹟。  

nums[i]可以和nums[0, i-x]或[i+x, N-1]中的某個nums[j]組成答案。  
假設j在i的右邊。那我們之後繼續遍歷到j之時，他必定也會在左邊找到nums[i]，這就是對稱性。  

如此一來，其實只要維護其中一邊的可用元素，程式碼簡潔不少。  

時間複雜度O(N log N)。  
空間複雜度O(N)。  

```python
from sortedcontainers import SortedList as SL

class Solution:
    def minAbsoluteDifference(self, nums: List[int], x: int) -> int:
        sl=SL()
        ans=inf
        
        for i,val in enumerate(nums):
            if i-x>=0:
                sl.add(nums[i-x])
            idx=sl.bisect_left(val)
            if idx<len(sl):
                ans=min(ans,abs(sl[idx]-val))
            if idx>0:
                ans=min(ans,abs(sl[idx-1]-val))

        return ans
```

最後來想想，bisect_left能不能換成bisect_right呢？  

bisect_left找的是第一個**大於等於**val的數的索引idx。如果val正好存在，則sl[idx]就是val；如果val不存在，則sl[idx]就會是第一個大於val的數，而sl[idx-1]就是最後一個小於val的數。最小絕對差肯定是和兩者其一組成。  

bisect_right找的是第一個**大於**val的數的索引idx。不管val存不存在，sl[idx]一定大於val。如果val存在，則sl[idx-1]正好會是val；若不存在，則sl[idx-1]會是最後一個小於val的數。  

因此兩者都可以適用。  
