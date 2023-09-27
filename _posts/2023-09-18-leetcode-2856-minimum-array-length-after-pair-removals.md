---
layout      : single
title       : LeetCode 2856. Minimum Array Length After Pair Removals
tags        : LeetCode Medium Array Greedy Heap Math
---
雙周賽113。最近三次的Q2都很噁心，這題AC率大概才11%。  

## 題目

輸入有序的整數陣列nums。  

你可以執行以下操作任意次：  

- 選擇兩個索引i和j，其中i < j，且nums[i] < nums[j]  
- 將位於索引i和j的兩個元素刪除。其餘的元素會保持原本的順序，且索引重新計算  

求任意次操作後nums的**最小長度**(可以是0)。  

注意：nums是以非遞減排序。  

## 解法

本來以為是單調堆疊貪心，只要比先前的元素大就可以刪掉。結果被[2,3,4,4]卡死。  
然後又以為是雙指針，用最大元素配最小的，結果又被[1,3,3,3,4]卡死。  

最後花半小時才想出改良版的貪心法，主要思路是**反悔**：  
維護可被匹配的元素ready，還有裝匹配成功的**nums[j]**，也就是較大那個元素，記做used。  
遍歷nums中的元素x，如果ready中有任意數小於x，匹配成功；否則可以用x去**替換**已經配對過的nums[j]，讓他重新回到ready；前兩者都不行，那x只能乖乖進ready等之後的其他元素配他。  

再次以[2,3,4,4]為例：  
> x=2，進去ready，ready=[2], used=[]  
> x=3，跟ready中的2配，ready=[], used=[3]  
> x=4，把used中的3替換出來，read=[3], used=[]
> x=4，跟ready中的3配，ready=[], used=[4]  
> 總共配成功2組，減少4個元素，最後nums剩下0個  

接下來決定資料結構：  
因為nums有序，可以保證早進去ready的元素一定較小(至少不會較大)，與x匹配時優先找最小的。先進先出，所以選用隊列queue。  
同理，進去used的元素也是越早越小，選擇最小的元素最有可能匹配成功。而且會進到**反悔**這步，代表ready中沒有比x更小的元素，又因為nums有序，更不可能有比x大的元素，所以ready必定為空。這時直接把**反悔**出來的元素加入ready中就好，一樣選queue。  

~~其實比賽時根本沒想這麼嚴謹，只知道我要選最小的，所以用了min heap。~~  

每個元素最多進出used和ready各一次，時間複雜度O(N)。  
空間複雜度O(N)。  

```python
class Solution:
    def minLengthAfterRemovals(self, nums: List[int]) -> int:
        N=len(nums)
        ans=N
        ready=deque()
        used=deque()
        for x in nums:
            if ready and ready[0]<x:
                ans-=2
                ready.popleft()
                used.append(x)
            elif used and used[0]<x:
                ready.append(used.popleft())
            else:
                ready.append(x)
                
        return ans
```

數學好的人根本不用搞這麼多，直接找出眾數的出現次數。  

某個數佔了最多的出現次數，共x次。  
若x不足總數一半，其他數的次數也不可能超過x，因此一定倆倆抵銷；除非總數是奇數個，則會剩下一個。  

否則，x超過一半，其餘的數不足x個，自然會剩下一些。  
x可以和y = (N-x)個數相抵，只剩下x-y個數。  

時間複雜度O(N)。  
空間複雜度O(N)。  

```python
class Solution:
    def minLengthAfterRemovals(self, nums: List[int]) -> int:
        N=len(nums)
        d=Counter(nums)
        x=max(d.values())
        
        if mx<=N/2: # mx*2 <= N
            return N%2
        
        return mx-(N-mx) # mx*2 - N
```
