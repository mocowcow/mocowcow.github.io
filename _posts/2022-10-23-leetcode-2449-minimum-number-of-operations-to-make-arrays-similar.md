--- 
layout      : single
title       : LeetCode 2449. Minimum Number of Operations to Make Arrays Similar
tags        : LeetCode Hard Array Greedy
---
周賽316。想快一小時才想通，其實和[2386. find the k sum of an array]({% post_url 2022-08-23-leetcode-2386-find-the-k-sum-of-an-array %})有異曲同工之妙。

# 題目
輸入兩個長度相同的正整數陣列nums和target。  
在一次操作中，你可以選擇任意兩個不同的索引i和j，其中0 <= i, j < nums.length，且：  
- 使nums[i]加2
- 使nums[j]減2  

如果每個元素的出現頻率相同，則稱兩個陣列**相似**。  
求使nums**相似**target所需的最小操作次數。測資保證兩者一定可以相似。  

# 解法
這題範例給的很好，本來想用排序還是heap之類的，直接被範例2擋下來。  
難點在於決定要操作的索引i後，沒有辦法馬上找到目標的j在哪裡。  

我們的目的在於使兩格陣列元素數量相同，不注重元素本身的值。若對nums某位置加上2，在對target某位置加上2，其總和一樣會維持不變。如此一來，**減少i增加j**的動作等價於**增加nums和target各一次**。  

> nums = [1,2,5], target = [1,3,4]  
> 5減2，2加2，nums = [1,3,4]  

等價於  
> nums = [1,2,5]，2加2，nums = [1,4,5]  
> target = [1,3,4]，3加2，target = [1,4,5]  

所以我們只要開一個陣列統計各元素出現頻率的差。最後遍歷每個元素i，將差值cnt[i]取絕對值加入答案中，然後將差值加入到cnt[i+2]中。我們把原本一次操作拆成兩次，所以記得答案要除2再回傳。  

時空間複雜度都是O(N)，其中N為target[i]的上限10^6。  
當然python還是TLE。  

```python
class Solution:
    def makeSimilar(self, nums: List[int], target: List[int]) -> int:
        ans=0
        cnt=[0]*1000005
        
        for n in nums:
            cnt[n]+=1
            
        for n in target:
            cnt[n]-=1
            
        for i in range(1,1000001):
            ans+=abs(cnt[i])
            cnt[i+2]+=cnt[i]

        return ans//2
```

附上最後通過的go版本。  
go本身沒有提供abs, max, min等函數，需要自己寫，算是美中不足的點。  

```go
func makeSimilar(nums []int, target []int) int64 {
    ans:=0
    cnt:=make([]int,1000005)
    
    for _,n:=range nums{
        cnt[n]++
    }
    for _,n:=range target{
        cnt[n]--
    }
    
    for i:=1;i<=1000000;i++{
        ans+=abs(cnt[i])
        cnt[i+2]+=cnt[i]
    }
    
    return int64(ans/2)
}


func abs(a int) int {
    if a<0{
        return -a
    }
    return a
}
```