---
layout      : single
title       : LeetCode 850. Rectangle Area II
tags        : LeetCode Hard Matrix HashTable SegmentTree
---

以前只知道一種做法，原來有兩種更快的優化。  
趕緊來還債。  

## 題目

<https://leetcode.com/problems/rectangle-area-ii/description/>

## 解法

矩形至多 N = 200 個，但是座標值域卻高達 10^9。  
先找出可能出現的 x, y 軸座標，進行**離散化**，依序對應到 0\~ 2N-1 的值域。  

若去重後的 x 軸座標有 X 個，那麼其構成的區間線段會有 X-1 個；y 軸同理，有 Y-1 個線段。  
可視作 (X-1) \* (Y-1) 的矩陣 cover  

再次遍歷所有矩形，按照離散化後的座標，將對應到的部分標記覆蓋。  
最後再遍歷矩陣，若 cover[i][j] 已被覆蓋，則查詢原本對應的座標，將面積加入答案中。  

時間複雜度 O(N^3)。  
空間複雜度 O(N^2)。  

```python
class Solution:
    def rectangleArea(self, rectangles: List[List[int]]) -> int:
        # collect coord
        xs = set()
        ys = set()
        for x1, y1, x2, y2 in rectangles:
            xs.add(x1)
            xs.add(x2)
            ys.add(y1)
            ys.add(y2)

        # discretize
        xs = sorted(xs)
        ys = sorted(ys)
        mp_x = {x: i for i, x in enumerate(xs)}
        mp_y = {y: j for j, y in enumerate(ys)}

        # mark cover
        X = len(xs) - 1
        Y = len(ys) - 1
        cover = [[0] * Y for _ in range(X)]
        for x1, y1, x2, y2 in rectangles:
            for x in range(mp_x[x1], mp_x[x2]):
                for y in range(mp_y[y1], mp_y[y2]):
                    cover[x][y] = 1

        # calc cover area
        ans = 0
        for x in range(X):
            for y in range(Y):
                if cover[x][y]:
                    x_width = xs[x+1] - xs[x]
                    y_height = ys[y+1] - ys[y]
                    ans += x_width * y_height

        return ans % (10 ** 9 + 7)
```

想像 y 軸有一條**掃描線**，由下往上移動。  
每次移動，統計 x 軸有多少線段被覆蓋。  

對於矩形 x1, y1, x2, y2 來說，當掃描線掃到 y1 時，線段 [x1, x2] 從此時開始被覆蓋；  
掃到 y2 時，線段 [x1, x2] 的覆蓋結束。  

把每個矩形轉換成覆蓋開始 / 結束的事件，以 y 軸排序。  
每次 y 軸掃瞄線移動，增加的面積即：  
> y 軸差值 \* x 軸覆蓋長度  

我們只需要維護 x 軸被覆蓋的線段，所以只有 x 軸需要離散化。  

時間複雜度 O(N^2)。  
空間複雜度 O(N)。  

```python
class Solution:
    def rectangleArea(self, rectangles: List[List[int]]) -> int:
        # collect coord
        # and turn rect into event
        xs = set()
        ys = set()
        events = []
        for x1, y1, x2, y2 in rectangles:
            xs.add(x1)
            xs.add(x2)
            events.append([y1, x1, x2, 1])
            events.append([y2, x1, x2, -1])

        # discretize
        xs = sorted(xs)
        mp_x = {x: i for i, x in enumerate(xs)}

        # mark cover
        X = len(xs) - 1
        cover = [0] * X 

        # sweep line
        events.sort()
        ans = 0
        for i, (y, x1, x2, val) in enumerate(events):
            if i > 0:
                pre_y = events[i-1][0]
                y_height = y - pre_y
                for j, cnt in enumerate(cover):
                    if cnt > 0:
                        x_width = xs[j+1] - xs[j]
                        ans += x_width * y_height

            for x in range(mp_x[x1], mp_x[x2]):
                cover[x] += val

        return ans % (10 ** 9 + 7)
```

上述統計 x 軸線段覆蓋次數，是**區間修改**。不難想到**線段樹**優化。  
難點在於：除了維護覆蓋次數之外，要怎麼維護**哪些區間沒被覆蓋**？  

---

區間修改線段樹的效率優勢在於：如果修改的區間完全包含當前節點區間，則打上懶標記，停止向下遞迴。  
但對於本題來說，父節點的覆蓋次數改變時，**子節點是否被覆蓋的狀態可能會改變**。  

例如：  
> 原有座標 [0,1,2]，兩個線段 [0,1], [1,2]  
> 分成三個節點 [0,2], [0,1], [1,2]  
> [0,1] 被覆蓋一次，然後 [0,2] 也覆蓋一次  
> 這時 [0,2] **沒被覆蓋的線段**是 0  

如果 [0,2] 刪除一次，[0,1] 依然被覆蓋，但是 [0,2] 變回沒覆蓋了。  
除非繼續向下遞迴檢查，否則節點 [0,2] 沒有辦法知道子節點狀態究竟改變沒有。  
但這樣操作退化成 O(N)，不如暴力維護。  

---

因此需要稍微改變定義，維護：  

- **最小**覆蓋次數，以及  
- 屬於**最小覆蓋**次數的**線段長度**  

如此一來，就算修改節點的覆蓋次數，也不會改變各線段覆蓋次數的相對關係。  

查詢時只需要取根節點，檢查是否被覆蓋即可。  
**有覆蓋的長度**即 x 軸全長減去沒覆蓋的長度。  

注意：線段樹節點的區間是**離散後的座標**，並非原始座標。  

時間複雜度 O(N log N)。  
空間複雜度 O(N)。  

```python
class Solution:
    def rectangleArea(self, rectangles: List[List[int]]) -> int:
        # collect coord
        # and turn rect into event
        xs = set()
        events = []
        for x1, y1, x2, y2 in rectangles:
            xs.add(x1)
            xs.add(x2)
            events.append([y1, x1, x2, 1])
            events.append([y2, x1, x2, -1])

        # discretize
        xs = sorted(xs)
        mp_x = {x: i for i, x in enumerate(xs)}

        # sweep line
        seg = SegmentTree(xs)
        events.sort()
        ans = 0
        for i, (y, x1, x2, val) in enumerate(events):
            if i > 0:
                pre_y = events[i-1][0]
                y_height = y - pre_y
                x_width = xs[-1] - xs[0] - seg.get_uncovered()
                ans += x_width * y_height

            l = mp_x[x1]
            r = mp_x[x2]
            seg.update(1, l, r - 1, val)

        return ans % (10 ** 9 + 7)


class Node:
    def __init__(self):
        self.l = 0
        self.r = 0
        self.min_cnt = 0
        self.min_length = 0
        self.lazy = 0


class SegmentTree:
    def __init__(self, xs):
        N = len(xs) - 1
        self.nodes = [Node() for _ in range(N * 4)]
        self.build(xs, 1, 0, N-1)

    def build(self, xs, id, l, r):
        o = self.nodes[id]
        o.l = l
        o.r = r
        if l == r:
            o.min_length = xs[l+1] - xs[l]
            return

        m = (l + r) // 2
        self.build(xs, id*2, l, m)
        self.build(xs, id*2+1, m+1, r)
        self.push_up(id)

    def push_down(self, id):
        o = self.nodes[id]
        lc = self.nodes[id*2]
        rc = self.nodes[id*2+1]
        if o.lazy:
            lc.lazy += o.lazy
            lc.min_cnt += o.lazy
            rc.lazy += o.lazy
            rc.min_cnt += o.lazy
            o.lazy = 0

    def push_up(self, id):
        o = self.nodes[id]
        lc = self.nodes[id*2]
        rc = self.nodes[id*2+1]
        o.min_cnt = min(lc.min_cnt, rc.min_cnt)
        o.min_length = 0
        if lc.min_cnt == o.min_cnt:
            o.min_length = lc.min_length
        if rc.min_cnt == o.min_cnt:
            o.min_length += rc.min_length

    def update(self, id, i, j, val):
        o = self.nodes[id]
        if i <= o.l and o.r <= j:
            o.min_cnt += val
            o.lazy += val
            return

        m = (o.l + o.r) // 2
        self.push_down(id)
        if i <= m:
            self.update(id*2, i, j, val)
        if m < j:
            self.update(id*2+1, i, j, val)
        self.push_up(id)

    def get_uncovered(self):
        root = self.nodes[1]
        if root.min_cnt > 0:
            return 0
        return root.min_length
```
