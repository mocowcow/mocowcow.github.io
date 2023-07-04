--- 
layout      : single
title       : LeetCode 2763. Sum of Imbalance Numbers of All Subarrays
tags        : LeetCode Hard Array SortedList
---
雙周賽352。本來還想說複雜度很尷尬，深怕被卡常數，好險這次官方很良心。  

# 題目
一個長度為n的整數陣列arr的**不平衡數**定義，是指在sarr=sorted(arr)陣列中，符合以下條件的索引個數：  
- 0 <= i < n - 1  
- 且sarr[i+1] - sarr[i] > 1  

sorted(arr)指的是排序過後的arr。  

輸入整數陣列nums，求所有子陣列的**不平衡數**總和。  

# 解法
簡單來說就是子陣列排序後，倆倆相鄰的數對中，有幾對的差超過1。  

分類討論，當一個有序陣列插入新元素x時，他的**不平衡數**個數cnt會怎樣改變？  
當x會插入到a,b兩數中間，變成a,x,b：  
- 若b-a>1，則cnt會少一個  
- 若x-a>1，則cnt會多一個  
- 若b-x>1，則cnt會多一個  

注意，要特殊判斷x的插入位置是否為最前方或最後方，才去檢查差值。  

枚舉所有索引r作為右邊界，並維護所有子陣列subs，對每個子陣列sub插入nums[r]，執行上述判斷後將**不平衡數**cnt值加入答案。  

枚舉N個右邊界，每個右邊界最多N個子陣列，每次子陣列插入O(log N)。時間複雜度O(N^2 log N)。  
最多同時存在N個子陣列，每個最多N個元素。空間複雜度O(N^2)。  

```python
from sortedcontainers import SortedList as SL

class Solution:
    def sumImbalanceNumbers(self, nums: List[int]) -> int:
        ans=0
        subs=[]

        for x in nums:
            for sub in subs:
                sl,cnt=sub
                i=sl.bisect_left(x)
                if i<len(sl) and sl[i]-sl[i-1]>1:
                    cnt-=1
                if i<len(sl) and sl[i]-x>1:
                    cnt+=1
                if i>0 and x-sl[i-1]>1:
                    cnt+=1
                sl.add(x)
                sub[1]=cnt
                ans+=cnt
                
            subs.append([SL([x]),0])
            
        return ans
```

改成枚舉左邊界的話，同時只會存在一個子陣列，空間複雜度降低。  

時間複雜度O(N^2 log N)。  
空間複雜度O(N)。  

```python
from sortedcontainers import SortedList as SL

class Solution:
    def sumImbalanceNumbers(self, nums: List[int]) -> int:
        N=len(nums)
        ans=0
        
        for left in range(N):
            sl=SL([nums[left]])
            cnt=0
            for right in range(left+1,N):
                x=nums[right]
                i=sl.bisect_left(x)
                if i<len(sl) and sl[i]-sl[i-1]>1:
                    cnt-=1
                if i<len(sl) and sl[i]-x>1:
                    cnt+=1
                if i>0 and x-sl[i-1]>1:
                    cnt+=1
                sl.add(x)
                ans+=cnt
            
        return ans
```

因為不平衡指的是**差>1**的情況，換言之，只有檢查出現**差<=1**時不會增加不平衡數。  

例如當前的有序子陣列為[1,3,5]，cnt為2，若插入已經出現過的元素，如1,3,5，cnt都會保持不變。  
若插入未出現過的元素x，只有在x+1或x-1也存在的情況下會使成立**差=1**，檢查兩者：  
- x+1, x-1都存在，則cnt會少1。如插入4，得到[1,3,4,5]，cnt變成1  
- x+1, x-1只存在一個，則cnt不變。如插入6，得到[1,3,5,6]，cnt維持2  
- x+1, x-1都不存在，則cnt會加1。如插入7，得到[1,3,5,7]，cnt變成3  

時間複雜度O(N^2)。  
空間複雜度O(N)。  

```python
class Solution:
    def sumImbalanceNumbers(self, nums: List[int]) -> int:
        N=len(nums)
        ans=0
        
        for left in range(N):
            vis=[False]*(N+2)
            vis[nums[left]]=True
            cnt=0
            for right in range(left+1,N):
                x=nums[right]
                if not vis[x]:
                    vis[x]=True
                    # if vis[x+1]==vis[x-1]: # both exist or both not exist
                    #     if vis[x+1]:
                    #         cnt-=1
                    #     else:
                    #         cnt+=1
                    cnt+=1
                    if vis[x+1]:
                        cnt-=1
                    if vis[x-1]:
                        cnt-=1
                ans+=cnt
                
        return ans
```

也可以使用貢獻法，考慮nums[i]=x這個元素在哪些子陣列中，能夠對**不平衡數**做出貢獻。  
假設a<x<b，則x有可能對a和b都做出貢獻，所以考慮x和a的情形。  
而x和a要能做出貢獻，必須符合x-a>1。也就是說這個子陣列中，不可以存在x-1。  

以例題1為例，nums = [2,3,1,4]，找到nums[i]有哪些不含nums[i]-1的子陣列：  
> 2在[2],[2,3]  
> 3在[3],[3,1],[3,1,4]  
> 1在[1],[1,4],[3,1],[3,1,4],[2,3,1],[2,3,1,4]  
> 4在[4],[1,4]  

可以發現，當x作為子陣列最小值時，找不到配合的a，所以這些子陣列全都是無效的。  
實際上只有這幾個有做出貢獻：  
> [3,1]中的3  
> [3,1,4]中的3  
> [1,4]中的4  

所以只要從nums[i]=x擴展左右邊界，直到碰到x-1時停止不加入。元素x可以和左右兩方的元素任意組成子陣列，若左邊有left個，右邊有right個，根據乘法原理，總共有left\*right個子陣列。  
而每個子陣列中都存在一個被誤算的最小值，所以答案最後要扣掉所有子陣列的數量N\*(N+1)/2。  

但還有另一個問題，重複的元素會被多次計入貢獻，例如nums = [1,3,3,4]：  
> 1沒有貢獻  
> 第一個3有[1,**3**,3],[1,**3**,3,4]  
> 第二個3,也有[1,3,**3**],[1,3,**3**,4]  
> 4沒有貢獻  

看到第二個3在[1,3,**3**,4]的貢獻是錯的，在nums[i]=x左方不可以出現x，所以左邊界必須碰到x或是x-1就馬上停止。  
反正左右邊界其中一個必須包含x，另一個不包含x。  

時間複雜度O(N)。  
空間複雜度O(N)。  

```python
class Solution:
    def sumImbalanceNumbers(self, nums: List[int]) -> int:
        N=len(nums)
        ans=0
        
        rb=[0]*N
        last=[N]*(N+1)
        for i in reversed(range(N)):
            x=nums[i]
            rb[i]=last[x-1]-1
            last[x]=i
            
        last=[-1]*(N+1)
        for i,x in enumerate(nums):
            lb=max(last[x],last[x-1])+1
            left=i-lb+1
            right=rb[i]-i+1
            ans+=left*right
            last[x]=i
            
        return ans-N*(N+1)//2
```