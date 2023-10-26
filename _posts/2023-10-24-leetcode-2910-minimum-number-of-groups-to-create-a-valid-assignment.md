---
layout      : single
title       : LeetCode 2910. Minimum Number of Groups to Create a Valid Assignment
tags        : LeetCode Medium Array Math HashTable Greedy
---
模擬周賽368。這題複雜度還真不太好想。  

## 題目  

輸入長度n的整數陣列nums。  

我們要將所有介於[0, n-1]之間的索引i分組，且每個索引**正好**屬於一個組別。  

一個**有效**的分組方式需滿足以下條件：  

- 對於每個組別g，屬於g組的索引i在nums中的值都相同  
- 對於任意兩個組別g1和g2，兩者分配到的索引**數量差**最多**不超過1**  

求**最少**需要幾組才能建立有效的分組。  

## 解法

任意兩組別大小相差最多不超過1，就是所有組別大小只能是k或k+1。  
最差最差的情況下，每個索引獨立一組，一定是有效的。  

其他情況下，nums[i]值相同的才能分到同一組，先以nums[i]的值計算出現次數。  
為了使組別盡可能少，則一組容納人數越多越好。  
例如nums = [1,1,2,2,2,2]，出現次數freq=[2,4]，一個組別最多只能容納k=min(freq)，也就是每組必須是k=2或k+1=3。  

將min(freq)記做mn_k，枚舉1\~mn_k之間的所有值k，試著判斷能不能將freq中各個元素正好分成k或k+1組：  

1. 枚舉freq中各元素的出現次數x，x可以分成q個正好大小為k的組，且剩r個沒分到組  
2. 如果r不超過q，則可以分配到q組中任意組去，構成r個大小為k+1的組；否則不合法  
3. 若freq全部都合法，則以組數更新答案  

舉個例子：  
> nums = [10,10,10,3,1,1]  
> freq = [3,1,2]  
> 枚舉1 <= k <= 1  
> 第一個x = 3，分成[1,1,1]餘0  
> 第二個x = 1，分成[1]餘0  
> 第三個x = 2，分成[1,1]餘0  

怎麼算出來是6組，但是範例給的答案是4才對啊？？  
原來是x=3可以分成[2,1]，然後x=2自成[2]，剩的x=1依舊[1]，正好4組。  
那好吧，x就用k+1去分組，不夠r的自成一組。  

那如果餘數r不等於k怎麼辦？  
> x = 10, k=2  
> 可分q=5組2，剩餘r=0  
> q>=r，確定可以分成[2,2,2,2,2]共五組  

但最佳解應是[3,3,2,2]共四組。試以k+1分組：  
> 設k1 = k+1 = 2+1 = 3  
> x = 10, k1 = 3  
> 可分q=3組3，剩餘r=1  
> 變成[3,3,3,1]，最後一組不滿k1人，可以從其他k1組拆出來  
> 最後得到[3,3,2,2]  

總共會有q組大小為k1，每一組都可以出讓一個索引來幫助r。只要q+r>=k，就可以把剩餘的r湊滿k個。  

nums長度為N，而freq中共有M種種出現頻率。  
最小的頻率為k，迴圈總共會跑k\*M次。  
而freq中所有頻率之和為N，在只有一種頻率時kM=N；否則kM<N。  

時間複雜度O(N)。  
空間複雜度O(N)。  

```python
class Solution:
    def minGroupsForValidAssignment(self, nums: List[int]) -> int:
        freq=Counter(nums).values()
        mn_k=min(freq)
        
        def f(x,k):
            # try k+1
            k1=k+1
            q,r=divmod(x,k1)
            if r==0: # exact q groups
                return q
            elif q+r>=k: # can make r become k
                return q+1
            
            # try k
            q,r=divmod(x,k)
            if r==0 or q>=r: 
                return q
            return inf 
        
        ans=inf
        for k in range(1,mn_k+1):
            cnt=sum(f(x,k) for x in freq)
            ans=min(ans,cnt)
                
        return ans
```

如果一組的大小k越大，那麼分出來的組數會越小。  
改成由大到小枚舉k，碰到第一個有效的k，直接回傳答案。  

還有第二個優化點。  
在x能以k和k+1有效分組的前提下，則ceil(x/k1)正好就是分出的組數。  

```python
class Solution:
    def minGroupsForValidAssignment(self, nums: List[int]) -> int:
        freq=Counter(nums).values()
        mn_k=min(freq)
        
        for k in reversed(range(1,mn_k+1)):
            k1=k+1
            cnt=0
            for x in freq:
                ok=True
                q,r=divmod(x,k)
                if q<r:
                    ok=False
                    break
                cnt+=(x+k1-1)//k1
                
            if ok:
                return cnt
```
