--- 
layout      : single
title       : LeetCode 2411. Smallest Subarrays With Maximum Bitwise OR
tags        : LeetCode Medium Array BitManipulation HashTable
---
雙周賽87。花了將近半小時才想出來，以前好像都沒碰過類似題目，寫得好痛苦，至少是AC了。  
後來才發現執行時間9754ms，根本貼在超時邊界上，算我好狗運。  

# 題目
輸入長度n且由由非負整數組成的陣列nums。對於從0到n-1的每個索引i，你必須找出從i開始的所有子陣列中，將所有元素做OR運算後得到的**最大值**，最少需要長度多少的**非空**子陣列。  
換句話說，你要找到從索引i開始的最小子陣列nums[i...j]，使得該子陣列的OR運算總和為max(nums[i...k])，其中i <= k <= n-1。  

回傳長度n的整數陣列answer，其中answer[i]是從i開始、且符合上述要求的最短子陣列長度。  

# 解法
每個數字nums[i]都要嘗試和i之後的其他數字做OR，看能不能使得結果變大。  
OR運算會使得所有出現過的1 bit保留下來，意味著nums[i]想變大，就要在右方找到目前缺少的1 bit。  
但是又要求子陣列長度越小越好，所以一旦找到缺少的1 bit，就要停留於該位置。  

先遍歷一次nums，把紀錄各數字中那些位置出現過1 bit，保存到雜湊表bits中。  
第二次遍歷nums，查看數字n中有哪些bit還是0，回到bits表裡面查找是否存在nums[j]擁有該bit，且j>i。若有則以j更新子陣列右邊界mx。最後將子陣列nums[i...mx]的長度mx-i+1加入答案中。  

統計各數字1 bit的時空間複雜度為O(N\*30)，而查找子陣列時間複雜度也是O(N\*30)，但是空間複雜度O(N)。  
雖然去掉常數一樣都是O(N)，但常數高達60，已經快要讓運算次數多兩個零，實在是有點尷尬。  

```python
class Solution:
    def smallestSubarrays(self, nums: List[int]) -> List[int]:
        bits=defaultdict(deque)
        for i,n in enumerate(nums):
            for j in range(30):
                if n&(1<<j):
                    bits[j].append(i)
            
        ans=[]
        for i,n in enumerate(nums):
            mx=i
            for j in range(30):
                if not n&(1<<j):
                    while bits[j] and bits[j][0]<i:bits[j].popleft()
                    if bits[j]:
                        mx=max(mx,bits[j][0])
            ans.append(mx-i+1)
            
        return ans
```

後來才發現逆向處理比較方便又簡潔。  
可以簡單的用長度30的陣列bits代表各1 bit的最後出現位置，而對其取最大值，即為子陣列的右邊界，而左邊界為i。  
需要注意的是子陣列長度最小為1，算出來的長度要記得和1取max。  

```python
class Solution:
    def smallestSubarrays(self, nums: List[int]) -> List[int]:
        N=len(nums)
        ans=[0]*N
        bits=[0]*30
        
        for i in range(N-1,-1,-1):
            n=nums[i]
            for j in range(30):
                if n&(1<<j):
                    bits[j]=i
            ans[i]=max(1,max(bits)-i+1)
            
        return ans
```

從右邊往左對每個nums[i]做OR運算，其值會呈現單調遞增。  
而因為10^9內只有30個位元，最多只會同時存在30種不同的OR結果。對於重複的OR值，只要保留索引最小者。  
第一個OR結果一定是最大值，以其索引為右邊界，和當前遍歷到的i所組成區間，更新答案ans[i]。  

時間複雜度O(N log MX)，其中MX為nums[i]的最大值。空間複雜度O(log MX)。  

```python
class Solution:
    def smallestSubarrays(self, nums: List[int]) -> List[int]:
        N=len(nums)
        ans=[0]*N
        ors=[] # [OR_val, right]
        
        for i in reversed(range(N)):
            x=nums[i]
            
            # update ors
            for o in ors:
                o[0]|=x
            ors.append([x,i])
            
            # de dup
            j0=0
            for j in range(len(ors)):
                if ors[j][0]!=ors[j0][0]:
                    j0+=1
                    ors[j0]=ors[j]
                else:
                    ors[j0][1]=ors[j][1]
            del ors[j0+1:]  

            ans[i]=ors[0][1]-i+1
            
        return ans
```