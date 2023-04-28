--- 
layout      : single
title       : LeetCode 480. Sliding Window Median
tags        : LeetCode Hard Array SortedList Heap BinarySearchTree SlidingWindow HashTable
---
最近一直heap，就來搞一些難搞的heap題。  

# 題目
中位數指的是位於有序序列正中間的數；如果序列長度是偶數，則是最中間兩數的平均值。  

例如：  
- [2,3,4]，中位數是3  
- [2,3]，中位數是(2+3)/2 = 2.5  

輸入整數陣列nums和整數k。  
有一個大小為k的滑動窗口，從最左方一直移動到最右方，每次移動一格。  

求出每個窗口中的中位數。  

# 解法
先來個python作弊解法。  

直接用sorted list維護大小k的滑動窗口，直接取中位數即可。  

時間複雜度O(N log k)。空間複雜度O(N)。  

```python
from sortedcontainers import SortedList

class Solution:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        ans=[]
        sl=SortedList()
        left=0
        
        for n in nums:
            sl.add(n)
            if len(sl)==k:
                median=sl[k//2]+sl[(k-1)//2]
                ans.append(median/2)
                sl.remove(nums[left]) 
                left+=1
                
        return ans
```

但是像java、c++沒有提供這種**可隨機存取**的有序容器，那就沒辦法直接找到中位數，非常尷尬。  
而且嚴格來說sorted list不是python內建函數。沒有這種東西要怎麼辦？  

可以用類似[295. Find Median from Data Stream]的作法：維護兩個heap，一個max heap裝k/2個較小的數，另一個min heap裝(k+1)/2個較大的數，中位數就剛好夾在兩個heap的中間。  
但又有另外一個問題：窗口移動的時候要**刪除左邊出界的元素**，但是heap只能刪頂端的東西，這又怎麼辦？  

這時只好先**假裝刪除**，先記下要刪的東西，等以後碰到才真正的刪除。  
沒有及時刪除heap中的元素，所以heap大小不會維持在k/2。我們得判斷要刪除的元素是在哪個heap中，而新加入的元素又在哪個heap中，以此判斷窗口移動後的heap是否平衡。  

如果要刪的元素是rmv，先把懶刪除lazy[rmv]加1。根據max heap的頂端元素，判斷刪除/加入的元素是屬於哪方。  
維護整數bal，如果從左邊刪元素，則bal-1；否則bal+1。如果往左邊加元素，則bal+1；否則bal-1。  
最後bal若為0，代表兩者平衡；bal<0代表左邊比右邊少；bal>0代表右邊比左邊少。  

根據bal值調整重新平衡兩個heap之後，才來檢查heap頂端的元素是不是**剛才沒刪掉的**的元素，這時候才**真正的刪除**。  
刪完後heap頂端才是真正的中位數。  

最差情況下，可能所有元素都沒有被**真正的刪除**，讓heap中達到將近N個數，那麼時間複雜度O(N log N)。  
同理，空間複雜度O(N)。  

```python
class Solution:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        N=len(nums)
        ans=[]
        L=[] # max heap
        R=[] # min heap
        lazy=Counter() # lazy removal count
        
        def get_median():
            if k%2==1:
                return R[0]
            return (-L[0]+R[0])/2
        
        # init window
        for i in range(k):
            heappush(R,nums[i])
        for i in range(k//2):
            t=heappop(R)
            heappush(L,-t)
        
        ans.append(get_median())
        
        # slide window
        for i in range(k,N):
            add=nums[i]
            
            # bal<0: L has less
            # bal=0: balanced
            # bal>0: R has less
            bal=0
            
            # element to be removed
            rmv=nums[i-k]
            lazy[rmv]+=1
            
            # pop rmv from L
            if L and rmv<=-L[0]:
                bal-=1
            else: 
                bal+=1
            
            # insert n into L
            if L and add<=-L[0]:
                heappush(L,-add)
                bal+=1
            else:
                heappush(R,add)
                bal-=1
             
            # make two heaps balanced
            if bal>0: # L>R, take largest one from L
                t=-heappop(L)
                heappush(R,t)
            elif bal<0: # L<R, take smallest one from R
                t=heappop(R)
                heappush(L,-t)
            
            # check if elements should be removed
            while L and lazy[-L[0]]>0:
                lazy[-L[0]]-=1
                heappop(L)
            while R and lazy[R[0]]>0:
                lazy[R[0]]-=1
                heappop(R)
                
            ans.append(get_median())
            
        return ans
```