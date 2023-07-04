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