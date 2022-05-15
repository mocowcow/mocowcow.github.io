--- 
layout      : single
title       : LeetCode 2271. Maximum White Tiles Covered by a Carpet
tags        : LeetCode Medium Array PrefixSum BinarySearch
---
雙周賽78。這次Q3難度異常高，真的有病，我整整花了一小時調整，總算是過了。  
這次雖然只有做出三題，但是沒有出任何BUG，個人還算滿意。

# 題目
輸入二維整數陣列tiles，其中tiles[i] = [li, ri]，表示li <= j <= ri範圍內的每個磁磚j都是白色的。  
還有整數carpetLen，代表你有一條長度為carpetLen的地毯，可以放在任何位置。

求地毯可以覆蓋的最大白色磁磚數量。

# 解法
看到N<=10^9就覺得是二分搜了，但是想半天又覺得很難處理，中間一度想改用滑動窗口。結果寫不出來，最後還是回來二分搜。  

我們會有N個白色磁磚區塊，先建立長度同樣為N的前綴和ps，代表從第0區到第i區的白色磁磚總數。  
再把tiles拆分成兩個陣列S和E，分別代表第i區的起點和終點，如此一來二分搜就很方便了。  

接下來枚舉S中所有起點s，分別求出可以覆蓋多少磁磚：  
1. 從s起計算carpetLen格，得到最後一個覆蓋位置為e  
2. 到E中二分搜，找到最後一個小於等於e的區塊索引r  
3. 到S中二分搜，找到最後一個小於s的區塊索引l  
4. 以l, r回到ps裡面找到對應的前綴和L, R，而R-L就是此地毯能夠**完全覆蓋**到的區塊和  
5. 地毯末端e有可能**部分覆蓋**下一個區塊，計算第r+1區塊能夠被蓋到多少  
6. 更新答案  

```python
class Solution:
    def maximumWhiteTiles(self, tiles: List[List[int]], carpetLen: int) -> int:
        N=len(tiles)
        tiles.sort()
        S=[]
        E=[]
        ps=[]
        sm=0
        ans=0
        for s,e in tiles:
            S.append(s)
            E.append(e)
            sm+=e-s+1
            ps.append(sm)
            
        for s in S:
            e=s+carpetLen-1
            r=bisect_right(E,e)-1
            l=bisect_left(S,s)-1
            R=ps[r]
            L=ps[l] if l>=0 else 0
            cover=R-L
            if r+1<N and S[r+1]<=e:
                cover+=e-S[r+1]+1
            ans=max(ans,cover)
            
        return ans  
```

整理思路後，發現在二分搜找最後一個小於當前起點的區塊根本是多餘動作，因為對於每個tiles[i]來說，區塊tiles[i-1]一定就是前一個(廢話)。  
順便用一些內建函數減少行數。

```python
class Solution:
    def maximumWhiteTiles(self, tiles: List[List[int]], carpetLen: int) -> int:
        tiles.sort()
        N=len(tiles)
        S,E=zip(*tiles)
        ps=list(accumulate([e-s+1 for s,e in tiles]))
        ans=0
        for i,s in enumerate(S):
            e=s+carpetLen-1
            r=bisect_right(E,e)-1
            R=ps[r]
            L=ps[i-1] if i>0 else 0
            cover=R-L
            if r+1<N and S[r+1]<=e:
                cover+=e-S[r+1]+1
            ans=max(ans,cover)
            
        return ans
```

搞了半天，終於把滑動窗口寫了出來。  
變數j指向考慮是否加入的磁磚區塊，cover為完全覆蓋磁磚格數。  
列舉每個tiles[i]的起點s開始放地毯，計算出地毯最後尾e，在可以被e完整覆蓋情況下，盡可能加入右方的磁磚區塊。  
窗口右邊界j停止擴展後，檢查區塊j是否能被地毯蓋住某部分，若有則cover加上部分覆蓋數量更新答案；否則只用cover更新。  
最後縮減左邊界，將cover扣除區塊i的磁磚數。

```python
class Solution:
    def maximumWhiteTiles(self, tiles: List[List[int]], carpetLen: int) -> int:
        tiles.sort()
        N=len(tiles)
        j=cover=ans=0
        for i in range(N):
            s=tiles[i][0]
            e=tiles[i][0]+carpetLen-1
            while j<N and tiles[j][1]<=e:
                cover+=tiles[j][1]-tiles[j][0]+1
                j+=1
            if j<N and e>=tiles[j][0]:
                ans=max(ans,cover+e-tiles[j][0]+1)
            else:
                ans=max(ans,cover)
            cover-=tiles[i][1]-tiles[i][0]+1
                
        return ans
```