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

剛才提到答案符合**單調性**，有些朋友可能想問能不能二分答案？  
當然可以！  

定義函數ok(size)，代表是否能以左右共size個元素滿足條件。  
abc都要找k個，至少要有k\*3個元素，下界定為k\*3。最差情況下整個字串都要用到，上界定為N。  
開始二分，若mid無法滿足條件，代表mid以下也都不可能，更新下界為mid+1；否則代表mid以上也都符合條件，更新上界為mid。  

判斷size是否合法的部分，初始化可以先加入左邊size個元素，逐次刪除左邊一個，同時右邊加入一個，途中滿足條件則直接回傳true。  
其實也可以想像成一個N-size的滑動窗口，窗口內包含的是不選的元素。  

每次判斷答案需要遍歷s，共要log N次，時間複雜度O(N log N)。最差同時保存整個陣列，空間複雜度O(N)。  

```python
class Solution:
    def takeCharacters(self, s: str, k: int) -> int:
        N=len(s)
        d=Counter(s)
        if any(d[x]<k for x in "abc"):return -1
        
        def ok(size):
            window=Counter()
            l=0
            r=N-1
            for _ in range(size):
                window[s[l]]+=1
                l+=1
            while l>0:
                if all(window[x]>=k for x in "abc"):return True
                l-=1
                window[s[l]]-=1
                window[s[r]]+=1
                r-=1
            return all(window[x]>=k for x in "abc")
        
        lo=k*3
        hi=N
        while lo<hi:
            mid=(lo+hi)//2
            if not ok(mid):
                lo=mid+1
            else:
                hi=mid
        
        return lo
```