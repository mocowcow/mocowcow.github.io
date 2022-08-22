--- 
layout      : single
title       : LeetCode 2380. Time Needed to Rearrange a Binary String
tags        : LeetCode Medium String Simulation
---
雙周賽85。剛做完Q1感覺這次有難度，Q2果然也有點意思。

# 題目
輸入二進位字串s。在一秒鐘內，可以把字串中所有的"01"同時替換為"10"。重複此動作，直到不存在"01"為止。  
求總共需要多少秒才能達成要求。  

# 解法
當我們把01換成10時，若左邊還有0的話，下一秒勢必要繼續替換。最差的狀況如00001，那麼我們必須替換4次才能把1趕到最左方。  
字串長度最多1000，使用暴力法模擬上述過程的話複雜度是O(N^2)，還算可以接受。  

因為字串不好修改，所以先換成整數陣列。設立變數ok表示是否需要繼續替換，每次檢查兩個索引，若剛好形成01的話則替換成10。

```python
class Solution:
    def secondsToRemoveOccurrences(self, s: str) -> int:
        N=len(s)
        s=[int(c) for c in s]
        ans=0
        
        while True:
            ok=True
            i=0
            while i+1<N:
                if s[i]==0 and s[i+1]==1:
                    s[i]=1
                    s[i+1]=0
                    ok=False
                    i+=2
                else:
                    i+=1
            if ok:break
            ans+=1

        return ans
```

在來是O(N)的DP作法。  
首先必須觀察出01替換為10的動作，實際上是把**1往左邊推**。對於每個1來說，左邊有多少個0，最終他便會向左移動多少次。  

考慮以下的例子：  
> s = "0011"  
> 對於第一個1來說，要移到左方至少需要2秒，變成"1001"
> 但第二個1也一樣要往左邊移動兩次，但是要等到第一個1移動完，才輪到他  
> 所以需要2+1秒  

實際上過程為：  
> s = "0011"  
> 第一秒 "0101"  
> 第二秒 "1010"  
> 第三秒 "1100"  

定義dp[i]：到s[i]為止的子字串，全部移動完需要幾秒。  
轉移方程式：若s[i]為0，則dp[i]=dp[i-1]；若為1且前方有出現過0，則dp[i]=max(dp[i-1]+1,zero)
base case：當i等於0時，dp[i-1]不合法，應直接設成0。但是python負數索引會往後方找，剛好也是0，所以沒問題。  

```python
class Solution:
    def secondsToRemoveOccurrences(self, s: str) -> int:
        N=len(s)
        dp=[0]*N
        zero=0
        
        for i,c in enumerate(s):
            if c=='0':
                zero+=1
                dp[i]=dp[i-1]
            elif zero>0:
                dp[i]=max(dp[i-1]+1,zero)

        return dp[-1]
```

每次dp只會取到前一次的狀態，所以可以把一維陣列壓縮成常數。  

```python
class Solution:
    def secondsToRemoveOccurrences(self, s: str) -> int:
        N=len(s)
        dp=zero=0
        
        for c in s:
            if c=='0':
                zero+=1
            elif zero>0:
                dp=max(dp+1,zero)

        return dp
```

最後附上懶人解法：使用內建函數replace all。  
比賽中覺得這東西很危險，不太敢隨便用，沒想到真的可以過，而且前幾名的人很多都這樣寫。  


```python
class Solution:
    def secondsToRemoveOccurrences(self, s: str) -> int:
        ans=0
        
        while '01' in s:
            s=s.replace('01','10')
            ans+=1
            
        return ans
```