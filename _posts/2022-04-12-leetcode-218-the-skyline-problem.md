---
layout      : single
title       : LeetCode 218. The Skyline Problem
tags 		: LeetCode Hard Array BinarySearch 
---
放在待辦清單裡面好久，今天終於拉出來寫。

# 題目
從定點往遠處看去，所有建築物共同構成的最高點連線稱為天際線。  
輸入buildings代表建物的[起點, 終點, 高度]，平地高度為0，回傳buildings所構成的天際線。  

只有在天際線高度改變時才將[起點, 高度]加入答案陣列中。且多個連續建物為同高度時視為一個輸出，例如[2,3,10],[3,4,10]視為一體，只應將[2,10]加入答案。

# 解法
雖然底下分類標籤有一堆什麼分治法、樹狀陣列、線段樹、heap之類的，結果我選擇座標壓縮+二分搜。  

先遍歷一次buildings，把所有出現的起、終點座標加進集合co中，再將co排序，供後續二分搜使用。  
這時co大小為N，建立一個長度同為N的陣列skyline，對映co區段中的天際線。  
在遍歷一次buildings，這次分別以起點、終點在co中找到對應位置left和right，對skyline[left:right]的位置更新最大高度。  
最後建立ans陣列，先把[第一個座標,高度]加入，接下來的座標若高度改變時，再分別加入ans中。

跑了8536ms，有夠久，但至少是有通過。

```python
class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        co = set()
        for a, b, _ in buildings:
            co.add(a)
            co.add(b)

        co = sorted(co)
        N = len(co)
        skyline = [0]*N
        for a, b, h in buildings:
            left = bisect_left(co, a)
            right = bisect_left(co, b)
            for i in range(left, right):
                skyline[i] = max(skyline[i], h)

        ans = [(co[0], heighs[0])]
        for i in range(1, N):
            if skyline[i] != skyline[i-1]:
                ans.append((co[i], skyline[i]))

        return ans
```

看大部分人都用heap解法，自己試著做了一次。這種應該就是所謂的掃描線。
題目其實有提到，在天際線高度改變時稱為key point。我們先把每棟建物轉成上升的下降的key point，依照發生位置做排序。  

heap保存的是進行中的上升key point，以及其結束時間，以高度為鍵值排序。  
遍歷keyPoints，如果當前start已經超過heap頂端的結束時間，則此key point已經失效，將其彈出。  
若當前的key point為上升，則將其押入heap中。這時heap頂端應該會是所有有效上升key point中高度最大者，檢查其高度是否與答案中上一個key point是否相同，若不同則將其加入答案。

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