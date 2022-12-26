--- 
layout      : single
title       : LeetCode 2516. Take K of Each Character From Left and Right
tags        : LeetCode Medium Array HashTable TwoPointers SlidingWindow
---
周賽325。這鬼題目花了好久才想通，絕對不是Q2該出現的東西。  

# 題目
輸入由字元'a', 'b'和'c'組成的字串s，還有一個非負整數k。  
每一分鐘，你可以拿走s**最左**或是**最右**方的字元。  

求**最少**需要幾分鐘，才能取得三種字元**至少**各k個。若無法滿足則回傳-1。  

# 解法
有可能無法滿足各k個，總而言之先檢查一次，若無法滿足直接回傳-1。  

當我們從左側取得一個字元，只有可能使得右側減少一個字元，或是不變。  
因此可以使用雙指針，窮舉左側取得N\~0個字元的情況，同時調整右指針位置以滿足要求。  

從左側取得N個字元的情況開始：  
- 丟掉左方最末尾的字元  
- 若不滿足要求，則不斷從右方加入字元  
- 以當前字元數更新答案  

一開始已經特別過濾掉不滿足k的情形，因此右指針擴張的過程中一定不會超過左指針。  

最多遍歷三次，時間複雜度O(N)。字串s中只有三種字元，空間複雜度O(1)。  

```python
class Solution:
    def takeCharacters(self, s: str, k: int) -> int:
        N=len(s)
        d=Counter(s)
        if any(d[x]<k for x in "abc"):return -1
        
        cnt=ans=N
        l=r=N-1
        while l>=0:
            d[s[l]]-=1
            l-=1
            cnt-=1
            while any(d[x]<k for x in "abc"):
                d[s[r]]+=1
                r-=1
                cnt+=1
            ans=min(ans,cnt)
        
        return ans
```

其實還有優化空間：如果求的不只是abc三個字元，而是好幾種的話，while判斷右指針擴張的成本就會變得非常高。  
我們每次只丟棄左指針的一個字元s[l]，意味著只有可能使得s[l]少於k個，因此只要以s[l]<k做為右指針擴張的條件即可。  

```python
class Solution:
    def takeCharacters(self, s: str, k: int) -> int:
        N=len(s)
        d=Counter(s)
        if any(d[x]<k for x in "abc"):return -1
        
        cnt=ans=N
        l=r=N-1
        while l>=0:
            d[s[l]]-=1
            cnt-=1
            while d[s[l]]<k:
                d[s[r]]+=1
                r-=1
                cnt+=1
            l-=1
            ans=min(ans,cnt)
        
        return ans
```

大佬的寫法是窮舉0\~N個字元的情形，要先從右方加入元素直到滿足條件為止。  
壞處是初始化右方元素比較麻煩，感覺我的方法更方便一些。  

```python
class Solution:
    def takeCharacters(self, s: str, k: int) -> int:
        N=len(s)
        d=Counter(s)
        if any(d[x]<k for x in "abc"):return -1
        
        d.clear()
        r=N
        cnt=0
        while any(d[x]<k for x in "abc"):
            r-=1
            d[s[r]]+=1
            cnt+=1
            
        ans=cnt
        for i,n in enumerate(s):
            d[n]+=1
            cnt+=1
            while r<N and d[s[r]]>k:
                d[s[r]]-=1
                r+=1
                cnt-=1
            ans=min(ans,cnt)

        return ans
```
