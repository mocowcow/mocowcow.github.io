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

時空間複雜度都是O(N+M)，其中，N為nums長度，M為target[i]的上限10^6。  
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

2022-10-24更新。  
大神們的想法果然和我不同，從+2這個動作中可以得到**分成奇數偶數**的結論；同理，若改成+k，則可以分成k組。  

我們先依照奇偶數將元素分組，問題就簡化成如同例題1單純的狀態。  
將分組後的nums和target排序，兩兩成對，其絕對差除2就是移動次數。這邊改成差值不除2，留到答案時一次全部除2，還有原本拆成兩次運算的部分，總共是除4。  

時間複雜度主要成本在於排序，為O(N log N)。空間複雜度O(N)。  

```python
class Solution:
    def makeSimilar(self, nums: List[int], target: List[int]) -> int:
        n_odd=sorted(n for n in nums if n%2)
        n_even=sorted(n for n in nums if n%2==0)
        t_odd=sorted(n for n in target if n%2)
        t_even=sorted(n for n in target if n%2==0)
        ans=0
        
        for a,b in zip(n_odd,t_odd):
            ans+=abs(a-b)
        
        for a,b in zip(n_even,t_even):
            ans+=abs(a-b)
        
        return ans//4
```