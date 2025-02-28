---
layout      : single
title       : LeetCode 3454. Separate Squares II
tags        : LeetCode Hard HashTable SegmentTree
---
biweekly contest 150。  

## 題目

<https://leetcode.com/problems/separate-squares-ii/description/>

## 解法

[3453. separate squares i]({% post_url 2025-02-19-leetcode-3453-separate-squares-i %})。  
[850. rectangle area ii]({% post_url 2025-02-26-leetcode-850-rectangle-area-ii %})。  

兩題的綜合板。  
**線段樹**加上**掃描線**解決。  

時間複雜度 O()。  
空間複雜度 O()。  

```python
class Solution:
    def separateSquares(self, squares: List[List[int]]) -> float:
        rectangles = [[x, y, x+l, y+l]for x, y, l in squares]

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

        # first sweep line
        # get tot area
        seg = SegmentTree(xs)
        events.sort()
        tot = 0
        for i, (y, x1, x2, val) in enumerate(events):
            if i > 0:
                pre_y = events[i-1][0]
                y_height = y - pre_y
                x_width = xs[-1] - xs[0] - seg.get_uncovered()
                tot += x_width * y_height

            l = mp_x[x1]
            r = mp_x[x2]
            seg.update(1, l, r - 1, val)

        # second sweep line
        # find split point
        half = tot / 2
        seg = SegmentTree(xs)
        cnt = 0
        for i, (y, x1, x2, val) in enumerate(events):
            if i > 0:
                pre_y = events[i-1][0]
                y_height = y - pre_y
                x_width = xs[-1] - xs[0] - seg.get_uncovered()
                cnt += x_width * y_height

                if cnt >= half:
                    extra = cnt - half
                    return y - (extra / x_width)

            l = mp_x[x1]
            r = mp_x[x2]
            seg.update(1, l, r - 1, val)

        return -1


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
