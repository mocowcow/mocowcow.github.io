---
layout      : single
title       : LeetCode 2217. Find Palindrome With Fixed Length
tags 		: LeetCode Medium Math
---
周賽286。看到回文真是又驚又喜，數不清我曾經被他害死幾次。這題要推算的東西有夠多，好險有成功算出來。  
然後範例竟然還有打錯，只是錯得太明顯，應該大部分人都有發現。

# 題目
回文數字指的是沒有前導零，且順讀與逆讀相同的數字。  
輸入整數intLength，代表回文數字的位數，陣列queries[i]代表要找第n小的回文數字。  
回傳一個陣列保存queries所對應的回文數字，若找不到則為-1。  
例：  
>  queries = [1,2,3,4,5,90], intLength = 3  
> [101,111,121,131,141,999]

# 解法
範例雖然沒有明說，但很明顯999就是最後一個回文數，從91開始就是出界的-1。  
我就想說把數字當成洋蔥分層，數字長度1\~2的是一層，2\~3是兩層，類推計算。只有一層的話總數為9，每多一層總數*10。計算出總數後就很好過濾了。  
遍歷queries，若超出總數則為-1，否則以函數轉換成回文數字。  

重點在這個轉換函數，搞了我好久才出來，還感覺不太有效率，特地加上快取看能不能稍微加速。  
因為題目要求的是第n小的回文數，所以數字一定要從內部開始向外增長且而最外圈不能用0，所以一進去先把q-1。  
我們知道999是第90個，實質上對應q=89，可以推導出是從101生成，最裡面那層+9，而第二層+8。所以只要從最內層開始，逐漸往外加，直到q用完，再把最外層加上1，就得到每層對應的數字。  
最後最後依據數字長度決定最內層需不需要重複，外層逐一包起來轉回數字就大功告成了。

```python
class Solution:
    def kthPalindrome(self, queries: List[int], intLength: int) -> List[int]:
        N=len(queries)
        ans=[]
        layer=(intLength+1)//2
        mx=9*10**(layer-1)

        @lru_cache(None)
        def getPal(q):
            q-=1
            pal=[]
            for _ in range(layer):
                l=q%10
                pal.append(l)
                q//=10
            pal[-1]+=1
            s=[str(pal[0])]
            if intLength%2==0:
                s*=2
            for i in range(1,layer):
                s=[str(pal[i])]+s+[str(pal[i])]
            return ''.join(s)
        
        for q in queries:
            if q>mx:
                ans.append(-1)
            else:
                ans.append(getPal(q))
                
        return ans
        
```

