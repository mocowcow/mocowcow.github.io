--- 
layout      : single
title       : LeetCode 2653. Sliding Subarray Beauty
tags        : LeetCode Medium Array SortedList HashTable SlidingWindow TwoPointers Heap
---
周賽342。其實也是模板題，甚至暴力解都可以過。不太懂為何一堆人按爛。  

# 題目
輸入長度n的整數陣列nums，找出每個長度為k的子陣列的**美麗值**。  

如果子陣列中不足x個負數，則美麗值為0；否則為第x小的負數。  

回傳長度為n-k+1的陣列ans，依序代表各子陣列的**美麗值**。  

# 解法
使用sorted list維護大小為k的滑動窗口中的元素。拿其中第x小的值和0取較小者，即為美麗值。  

時間複雜度O(N log N)。空間複雜度O(k)。  

```python
from sortedcontainers import SortedList

class Solution:
    def getSubarrayBeauty(self, nums: List[int], k: int, x: int) -> List[int]:
        sl=SortedList()
        ans=[]
        left=0
        
        for n in nums:
            sl.add(n)
            if len(sl)==k:
                ans.append(min(0,sl[x-1]))
                sl.remove(nums[left])
                left+=1
                
        return ans
```

這題nums[i]的範圍比較小，只有從-50\~50，而且我們只在乎-50\~-1的部分。  
就算每次從-50開始累加出現次數來找第x小的元素，也完全沒有問題。  

時間複雜度O(N\*MX)，其中MX為abs(min(nums))，在此為50。空間複雜度O(MX)。  

```python
class Solution:
    def getSubarrayBeauty(self, nums: List[int], k: int, x: int) -> List[int]:
        d=Counter()
        ans=[]
        left=0
        
        def beauty():
            cnt=0
            for i in range(-50,0):
                cnt+=d[i]
                if cnt>=x:
                    return i
            return 0
                
        for right,n in enumerate(nums):
            d[n]+=1
            if right-left+1==k:
                ans.append(beauty())
                d[nums[left]]-=1
                left+=1
                
        return ans
```

補個heap搭配懶刪除做法。相似題[480. sliding window median]({% post_url 2023-04-28-leetcode-480-sliding-window-median %})。  

維護兩個heap，左邊的L是max heap，保存窗口中最小的x個元素，而L頂端正好是第x小的元素；剩下的元素都放右邊的min heap，也就是R。  

因為**L一定不為空**，在移動窗口時，可以根據L頂端元素來判斷新元素add和要刪除的元素rmv分別位於L或R。  
總共有四種情況：  
1. L刪L加，bal=0平衡  
2. R刪R加，bal=0平衡  
3. L刪R加，bal<0，R多一個，從R拿一個補到L  
4. R刪L加，bal>0，L多一個，從L拿一個補到R  

最後把兩heap頂端需要懶刪除元素刪除。  

時間複雜度O(N log N)。  
空間複雜度O(N)。  

```python
class Solution:
    def getSubarrayBeauty(self, nums: List[int], k: int, x: int) -> List[int]:
        N=len(nums)
        ans=[]
        L=[] # max heap
        R=[] # min heap
        lazy=Counter() # lazy removal count
        
        def get_beauty():
            return min(0,-L[0])
        
        # init window
        for i in range(k):
            heappush(L,-nums[i])
            if len(L)>x:
                t=-heappop(L)
                heappush(R,t)
                
        ans.append(get_beauty())
        
        # slide window
        for i in range(k,N):
            add=nums[i]
            bal=0
            
            # lazy remove
            rmv=nums[i-k]
            lazy[rmv]+=1
            
            if L and rmv<=-L[0]:
                bal-=1
            else:
                bal+=1
                
            if L and add<=-L[0]:
                heappush(L,-add)
                bal+=1
            else:
                heappush(R,add)
                bal-=1

            if bal<0:
                t=heappop(R)
                heappush(L,-t)
            elif bal>0:
                t=-heappop(L)
                heappush(R,t)
            
            while L and lazy[-L[0]]:
                lazy[-L[0]]-=1
                heappop(L)
            while R and lazy[R[0]]:
                lazy[R[0]]-=1
                heappop(R)
                
            ans.append(get_beauty())
            
        return ans
```