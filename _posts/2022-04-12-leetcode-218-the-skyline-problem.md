---
layout      : single
title       : LeetCode 218. The Skyline Problem
tags 		: LeetCode Hard Array BinarySearch Heap
---
放在待辦清單裡面好久，今天終於拉出來寫。搞了好多種解法，十分快樂。

# 題目
從定點往遠處看去，所有建築物共同構成的最高點連線稱為天際線。  
輸入buildings代表建物的[起點, 終點, 高度]，平地高度為0，回傳buildings所構成的天際線。  

只有在天際線高度改變時才將[起點, 高度]加入答案陣列中。且多個連續建物為同高度時視為一個輸出，例如[2,3,10],[3,4,10]視為一體，只應將[2,10]加入答案。

# 解法
雖然底下分類標籤有一堆什麼分治法、樹狀陣列、線段樹、heap之類的，結果我選擇座標壓縮+二分搜。  

先遍歷一次buildings，把所有出現的起、終點座標加進集合co中，再將co排序，供後續二分搜使用。  
這時co大小為N，建立一個長度同為N的陣列skyline，對應co區段中的天際線。  
在遍歷一次buildings，這次分別以起點、終點在co中找到對應位置left和right，對skyline[left:right]的位置更新最大高度。  
最後建立ans陣列，遍歷一次天際線高度，並在高度改變時將[原座標, 新高度]加入ans中。  

~~跑了8536ms，有夠久，但至少是有通過。~~  

2023/4/18更新，更新區間其實不用二分搜，直接單純迴圈就快了不少。  

在每個點都不重複的情況下，將近每個節點都要更新N次，時間複雜度O(N^2)。空間複雜度O(N)。  

```python
class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        a=set()
        for s,e,_ in buildings:
            a.add(s)
            a.add(e)
            
        indexes=sorted(a)
        mp={x:i for i,x in enumerate(indexes)}
        heights=[0]*len(a)
        
        for s,e,h in buildings:
            for i in range(mp[s],mp[e]):
                if h>heights[i]:
                    heights[i]=h
        
        ans=[]
        prev=-1
        for i,h in enumerate(heights):
            if h!=prev:
                ans.append([indexes[i],h])
            prev=h
        
        return ans
        return ans
```

看大部分人都用heap解法，自己試著做了一次。這種應該就是所謂的掃描線。
題目其實有提到，在天際線高度改變時稱為key point。我們先把每棟建物轉成上升的下降的key point，依照發生位置做排序。  

heap保存的是進行中的上升key point，以及其結束時間，以高度為鍵值排序。  
遍歷keyPoints，如果當前start已經超過heap頂端的結束時間，則此key point已經失效，將其彈出。  
若當前的key point為上升，則將其押入heap中。這時heap頂端應該會是所有有效上升key point中高度最大者，檢查其高度是否與答案中上一個key point是否相同，若不同則將其加入答案。

162ms，加速超級多。

```python
class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        keyPoints = []
        for start, end, h in buildings:
            keyPoints.append((start, -h, end))
            keyPoints.append((end, 0, 0))
        keyPoints.sort()

        ans = [(0, 0)]
        heap = [(0, math.inf)]
        for start, h, end in keyPoints:
            while start >= heap[0][1]:
                heappop(heap)
            if h != 0:
                heappush(heap, (h, end))
            if ans[-1][1] != -heap[0][0]:
                ans.append((start, -heap[0][0]))

        return ans[1:]
```

再來個merge sort解法。136ms，第一種解法已經看不到車尾燈。  

把所有建物形成的地平線倆倆合併，最後成為一個答案。  
當分割的大小=1時為base case，拆分成上升、下降key point各一個。  
否則遞迴拆成左右邊，每次取出起點較早的key point，並更新對應高度；兩端起點相同時則同時取出，更新兩方高度。最後檢查高度是否有變化，若是則加入ans。

```python
class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:

        def merge(l, r):
            if l > r:
                return []
            if l == r:  # base case
                return [(buildings[l][0], buildings[l][2]), (buildings[l][1], 0)]  # up and down
            mid = (l+r)//2
            q1 = deque(merge(l, mid))
            q2 = deque(merge(mid+1, r))
            h1 = h2 = 0
            ans = []
            while q1 or q2:
                sl = q1[0][0] if q1 else math.inf
                sr = q2[0][0] if q2 else math.inf
                if sl < sr:
                    S, h1 = q1.popleft()
                elif sl > sr:
                    S, h2 = q2.popleft()
                else:  # equal
                    S, h1 = q1.popleft()
                    _, h2 = q2.popleft()
                H = max(h1, h2)
                if not ans or ans[-1][1] != H:
                    ans.append((S, H))

            return ans

        return merge(0, len(buildings)-1)
```