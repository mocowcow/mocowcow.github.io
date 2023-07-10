--- 
layout      : single
title       : LeetCode 2772. Apply Operations to Make All Array Elements Equal to Zero
tags        : LeetCode Medium Array Greedy PrefixSum SegmentTree
---
周賽353。垃圾測資，10^5的範圍竟然允許C++的O(N^2)解法通過，但python的O(N log k)卻有機率被卡掉。  
更妙的是，一堆作弊仔都貼了C++那個O(N^2)的程式碼，看來洩露答案和抄襲兩方都有點不太可靠。  

# 題目
輸入整數陣列nums和整數k。  

你可以執行以下操作**任意次**：  
- 選擇**任一**長度為k的子陣列，並將裡面每個元素都**減**1  

若能使所有元素都變成0，則回傳true；否則回傳false。  

# 解法
每次操作會影響k個元素，就算你只想要減nums[i]，另外k-1個也會同時被碰到。  
假設想改的索引i位於子陣列的中間，那麼左右兩邊都會被改變，很麻煩。  
不如選擇讓nums[i]位於子陣列的最左端，並且由左到右處理，如此可保證左方的元素不會再被修改到。  

從左到右處理索引i，可以使用差分陣列diff來維護區間的變化量，當前i的值remain即為nums[i]+difff[i]。  
如果remain因為先前的修改，已經小於0，沒辦法補救，直接回傳false；否則使區間[i,i+k-1]都減去remain。    

注意每次修改必須是長度k，所以只能選擇[0,N-k]這個區間內的索引作為左邊界。  
所以修改到最後，只要[N-k+1,N-1]區間內還有元素不為0，那無論怎樣都不可能讓他變0了，回傳false。  

時間複雜度O(N)。  
空間複雜度O(N)。  

```python
class Solution:
    def checkArray(self, nums: List[int], k: int) -> bool:
        N=len(nums)
        diff=[0]*(N+5)
        
        for i in range(N-k+1):
            diff[i]+=diff[i-1]
            remain=nums[i]+diff[i]
            
            if remain<0:
                return False
        
            diff[i]-=remain
            diff[i+k]+=remain
            
        for i in range(N-k+1,N):
            diff[i]+=diff[i-1]
            
            if nums[i]+diff[i]!=0:
                return False
                
        return True
```

同樣邏輯，只是大神寫起來更簡潔。  

```python
class Solution:
    def checkArray(self, nums: List[int], k: int) -> bool:
        N=len(nums)
        diff=[0]*(N+5)
        ps=0
        
        for i,x in enumerate(nums):
            ps+=diff[i]
            x+=ps
            
            if x==0:
                continue
            
            if x<0 or i+k-1>=N:
                return False
            
            ps-=x
            diff[i+k]+=x
            
        return True
```

當然也可以使用懶標線段樹來處理區間修改。但就和先前提到的一樣，細節沒有處理好不小心就會TLE。  

時間複雜度O(N log k)。  
空間複雜度O(N)。  

```python
class Solution:
    def checkArray(self, nums: List[int], k: int) -> bool:

        def build(id, L, R):
            if L == R:  
                tree[id] = init[L]
                return
            M = (L+R)//2
            build(id*2, L, M)
            build(id*2+1, M+1, R)
            tree[id] = tree[id*2]+tree[id*2+1]  

        def query(id, L, R, i, j):
            if i <= L and R <= j: 
                return tree[id]
            push_down(id, L, R)
            ans = 0
            M = (L+R)//2
            if i <= M:
                ans += query(id*2, L, M, i, j)
            if M+1 <= j:
                ans += query(id*2+1, M+1, R, i, j)
            return ans

        def update(id, L, R, i, j, val):
            if i <= L and R <= j:  
                tree[id] += (R-L+1)*val
                lazy[id] += val 
                return
            push_down(id, L, R)
            M = (L+R)//2
            if i <= M:
                update(id*2, L, M, i, j, val)
            if M+1 <= j:
                update(id*2+1, M+1, R, i, j, val)
            push_up(id)

        def push_down(id, L, R):
            M = (L+R)//2
            if lazy[id]:
                lazy[id*2] += lazy[id]
                tree[id*2] += lazy[id]*(M-L+1)
                lazy[id*2+1] += lazy[id]
                tree[id*2+1] += lazy[id]*(R-(M+1)+1)
                lazy[id] = 0

        def push_up(id):
            tree[id] = tree[id*2]+tree[id*2+1]

        N=len(nums)
        tree = [0]*(N*4)
        lazy = [0]*(N*4)
        init = nums
        build(1, 0, N-1)
        
        for i in range(N):
            remain=query(1,0,N-1,i,i)+nums[i]
            
            if remain==0:
                continue
            
            if remain<0 or i+k-1>=N:
                return False

            update(1,0,N-1,i,i+k-1,-remain)
                
        return True
```