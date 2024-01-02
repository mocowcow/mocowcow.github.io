---
layout      : single
title       : LeetCode 2981. Find Longest Special Substring That Occurs Thrice I
tags        : LeetCode Medium String TwoPointers SlidingWindow BinarySearch HashTable Heap
---
周賽378。這題真的很垃圾，常數不知道在卡什麼意思，基本上只有O(N)的能過，O(N log N)很大機率吃TLE。  
本以為是卡python，換了golang來寫，結果過的測資反而更少。目前只有看過C++能用O(N log N)過。  

真心覺得，只接受O(N)解法可以直接講清楚，沒必要這樣噁心人。  

## 題目

輸入小寫字母組成的字串s。  

若一個字串只由一種字母組成，則稱為**特別的**。例如"abc"不特別，但"ddd", "zz", "f"都是特別的。  

找到s中出現**至少三次**的**特別子字串**的最大長度，若不存在則回傳-1。  

## 解法

假設存在一個長度為x的特殊子字串至少出現三次，那麼小於x的肯定也超過三次；反之，若不存在長度為x的，也不可能有長度比x還大的。  
答案具有單調性，可以二分答案。  

維護一個函數ok(size)，以長度為size的滑動窗口在s中查找。  
若窗口中全部元素都是某個字元c，則將c的頻率加1。最後判斷是否某個元素至少出現三次。  

時間複雜度O(N log N)。  
空間複雜度O(N)。  

明明N也才5\*10^5，交10次才會過一次。  

```python
class Solution:
    def maximumLength(self, s: str) -> int:
        N=len(s)
        a=[ord(x)-97 for x in s]
        
        def ok(size):
            char_freq=[0]*26
            d=[0]*26
            left=0
            for right,x in enumerate(a):
                d[x]+=1
                if right-left+1==size:
                    if d[x]==size:
                        char_freq[x]+=1
                        if char_freq[x]==3:
                            return True
                    d[a[left]]-=1
                    left+=1
            return False
        
        lo=0
        hi=N
        while lo<hi:
            mid=(lo+hi+1)//2
            if not ok(mid):
                hi=mid-1
            else:
                lo=mid
                
        if lo==0:
            return -1
        
        return lo
```

仔細看看範例1的"aaaa"，提供三次"aa"。這是很大的提示。  
若存在一個長度為size的特殊子字串，他可以貢獻三個長度**size-2**。  
當然，還貢獻了size-1兩次，size一次。  

我們先依照相同字元來分割子字串，對於每個長度為size的子字串分別對該字元c的長度size, size-1, size-2貢獻出現次數。  

時間複雜度O(N)。  
空間複雜度O(N)。  

```python
class Solution:
    def maximumLength(self, s: str) -> int:
        N=len(s)
        i=0
        d=Counter()
        while i<N:
            c=s[i]
            j=i
            while j+1<N and s[j+1]==c: # group by same char
                j+=1
            size=j-i+1
            d[(c,size)]+=1
            d[(c,size-1)]+=2
            d[(c,size-2)]+=3
            i=j+1
            
        ans=0
        for (c,size),freq in d.items():
            if freq>=3:
                ans=max(ans,size)
        
        if ans==0:
            return -1
        
        return ans
```

剛才說到，size可以貢獻size-2三次。也就是說，保存小於size-2的大小沒有意義。  
我們只需要每個字元前三大的字串長度，分別記做a,b,c。

答案的來源可能有三種情況：  

- a,b,c三個都相等，答案是c  
- 從a中找三個a-2，答案是a-2  
- 從b中找b，從a中找兩個b，答案是min(a-1,b)  

第三種情況有點小陷阱：在a=b時，可以找到三個a-1；如果a>b，可以找到三個b。合併起來才變成min(a-1,b)。  

老實說不太好想，但是只需要對26個字母各維護3個最大值，常數空間還是很厲害的。  

時間複雜度O(N)。  
空間複雜度O(1)。  

```python
class Solution:
    def maximumLength(self, s: str) -> int:
        N=len(s)
        char_size=[[0]*3 for _ in range(26)]
        i=0
        while i<N:
            j=i
            while j+1<N and s[j]==s[j+1]: # group by same char
                j+=1
            c=ord(s[i])-97
            size=j-i+1
            heappushpop(char_size[c],size)
            i=j+1
            
        ans=0
        for vals in char_size:
            a,b,c=nlargest(3,vals)
            ans=max(ans,
                    c,
                    min(a-1,b),
                    a-2
                   )
            
        if ans==0:
            return -1
        
        return ans
```
