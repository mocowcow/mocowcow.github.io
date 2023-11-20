---
layout      : single
title       : LeetCode 2940. Find Building Where Alice and Bob Can Meet
tags        : LeetCode Hard Array SegmentTree BinarySearch
---
周賽372。前陣子在整理線段樹模板，剛好練習到相似題[2286. booking concert tickets in groups]({% post_url 2022-05-30-leetcode-2286-booking-concert-tickets-in-groups %})。  
樹是有成功搞出來，但是誤會題目的要求，有些小問題會算出錯誤答案，好可惜。  

## 題目

輸入正整數陣列heights，其中heights[i]代表第i個建築的高度。  

如果有人站在建築i，他可以移動到任何滿足i < j且heights[i] < heights[j]的建築j。  

另外輸入陣列qeuries，其中qeuries[i] = [a<sub>i</sub>,b<sub>i</sub>]。代表在第i次查詢時，Alice位於建築a<sub>i</sub>，且Bob位於建築b<sub>i</sub>。  

回傳陣列ans，其中ans[i]代表第i次查詢時，Alice和Bob能夠會合的建築中，**索引最小**的那個建築。  
若無法會合，則ans[i]為-1。  

## 解法

以下將height[i]簡記為H[i]。  

簡單來講，就是只能往**右**且**更高**的建築走。  
但是範例一告訴我們，其實也可以**不走**。  

對於a和b的佔位，分類討論：  

1. a=b已經在同個點，不走，當前就是會合點  
2. a<b，且H[a]<H[b]，直接讓a走到b  
3. a>b，且H[a]>H[b]，直接讓b走到a  
4. a<b，但H[a]>H[b]，要找b右方且比a高的第一個點  
5. a>b，但H[a]<H[b]，要找a右方的點b高的第一個點  

對於第2,3項還有4,5項來說，只是a,b互相調換位置，處理邏輯是相同的。  
這裡有一個小技巧：定一個規格來維持順序，例如a<b。當碰到a>b時則兩者交換，這樣可以把處理分支壓縮起來。  

本題核心在於：怎麼找某個**區間**內，**大於limit**且**索引最小**的值？  
如果只是要普通判斷區間最大值，肯定會想到線段樹吧。  
但是線段樹本身就是由多個子區間來組成一個區間，所以我們也能反著找出是**哪個子區間做出了貢獻**。  

舉個例子：  
> H = [4,1,2,4]，要找介於區間[1,3]且至少為limit=4的最小索引  
> [4,1,2,4]最大值是4。因為要求索引最小，先找左區間  
> [4,1,_,_]最大值是4。左邊[4,_,_,_]超出區間限制；右邊[_,1,_,_]不足4，也不行  
> 回到[4,1,2,4]，找右區間  
> [_,_,2,4]最大值4，先找左區間。左邊[_,_2,_]不足4，不行；右邊[_,_,_4]可以  
> [_,_,_,4]已經是葉節點，正是答案，合法索引為H[3]=4  

定義bisect(i,limit)：在區間[i, N-1]間找到至少limit且最靠左的索引。  
以下幾個步驟轉換成遞迴函數即可實現查找：  

1. 當前節點最大值不足limit就不用找了，子區間一定也不足。回傳-1  
2. 成功到達葉節點，就是答案  
3. 若左區間有涵蓋到查詢範圍，且最大值滿足limit才往左找；有找到就是答案  
4. 左邊沒找到，那答案一定在右邊  

建樹需要O(N log N)，之後每次查詢需要O(log N)。  
時間複雜度O((Q+N) log N)，其中Q為查詢次數。  
空間複雜度O(N)，答案輸出不計。  

```python
class Solution:
    def leftmostBuildingQueries(self, heights: List[int], queries: List[List[int]]) -> List[int]:
        N=len(heights)
        seg=SegmentTree(N)
        seg.build(heights,1,0,N-1)
        
        ans=[]
        for a,b in queries:
            if a==b: # stay a
                ans.append(a)
                continue
            
            if a>b: # keep a<b
                a,b=b,a
            if heights[a]<heights[b]: # a to b
                ans.append(b)
                continue
            
            limit=max(heights[a],heights[b])+1 # a,b to c
            res=seg.bisect(1,0,N-1,b+1,limit)
            ans.append(res)
        
        return ans
        

class SegmentTree:

    def __init__(self, n):
        self.tree = [0]*(n*4)

    def build(self, init, id, L, R):
        """
        初始化線段樹
        若無初始值則不需執行
        """
        if L == R:  # 到達葉節點
            self.tree[id] = init[L]
            return
        M = (L+R)//2
        self.build(init, id*2, L, M)
        self.build(init, id*2+1, M+1, R)
        self.push_up(id)

    def op(self, a, b):
        """
        任意符合結合律的運算
        """
        return max(a,b)

    def push_up(self, id):
        """
        以左右節點更新當前節點值
        """
        self.tree[id] = self.op(self.tree[id*2], self.tree[id*2+1])

    def update(self, id, L, R, i, val):
        """
        單點更新
        對索引i增加val
        """
        if L == R:  # 當前區間目標範圍包含
            self.tree[id] += val
            return
        M = (L+R)//2
        if i <= M:
            self.update(id*2, L, M, i, val)
        else:
            self.update(id*2+1, M+1, R, i, val)
        self.push_up(id)
        
    def bisect(self, id, L, R, i, limit):
        if self.tree[id]<limit:
            return -1
        if L==R:
            return L
        M=(L+R)//2
        if i<=M and self.tree[id*2]>=limit:
            res=self.bisect(id*2,L,M,i,limit)
            if res!=-1:
                return res
        return self.bisect(id*2+1,M+1,R,i,limit)
```
