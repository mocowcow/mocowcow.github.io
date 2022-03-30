---
layout      : single
title       : LeetCode 1157. Online Majority Element In Subarray
tags 		: LeetCode Hard Array BinarySearch SegmentTree Design
---
這三天都在學線段樹，特地找相關題目來學習，但是大部分都要區間更新，好不容易找到這題比較單純。

# 題目
主要元素的定義是，在一個長度N的數列中，某個數字n出現至少N/2次，就稱為主要元素。  

設計一個類別MajorityChecker，包含以下功能：   
- 以陣列為參數的建構子  
- int query(int left, int right, int threshold)，查詢left到right範圍內出現至少threshold次的主要元素。若無則回傳-1

# 解法
起初我用物件型線段樹，每個節點都有counter，用來保存該區間所有數字的出現次數，結果24/29測資就TLE了，可惜。  
後參考[這篇](https://leetcode.com/problems/online-majority-element-in-subarray/discuss/360493/Python-Segment-tree-(merge-in-O(1)-query-O(log-n)))，使用Boyer-Moore多數投票演算法的概念，保存每個區間的候選人及其票數。查詢時先確定區間候選人，再以二分搜取得正確票數，決定是否符合threshold。  

此線段樹主要有三大功能：  
1. build，初始化區間節點，並往下遞迴建立子節點  
2. query，查詢區間的主要元素  
3. merge，合併多個區間，計算出正確值  

沒有更新功能，省了不少事。  
主要邏輯在於merge的部分：以(數字, 領先票數)的格式保存候選人，若兩個區間候選人相同則票數加總；否則回傳(票高者, 兩者票數差)。  

另外在初始化時分別以雜湊表self.idx保存各數字的出現位置，供未來二分搜使用。  
每次查詢先得到該區間主要元素n，r為n第一個大於right的出現位置，而l為n第一個大於等於left的出現位置，r-l即為n出現次數，超過threshold即可回傳，否則-1。

```python
class Node:
    def __init__(self, start, end):
        self.cand = None
        self.start = start
        self.end = end
        self.left = self.right = None


class SegmentTree:
    def __init__(self, nums):
        self.nums = nums
        self.root = self.build(0, len(nums)-1)

    def build(self, start, end):
        if start > end:
            return None
        node = Node(start, end)
        if start != end:
            mid = (start+end)//2
            node.left = self.build(start, mid)
            node.right = self.build(mid+1, end)
            l = node.left.cand if node.left else None
            r = node.right.cand if node.right else None
            node.cand = self.merge(l, r)
        else:
            node.cand = (self.nums[start], 1)
        return node

    def merge(self, a, b):
        if not a or not b:
            return a or b
        if a[0] == b[0]:
            return (a[0], a[1]+b[1])
        if a[1] > b[1]:
            return (a[0], a[1]-b[1])
        else:
            return (b[0], b[1]-a[1])

    def query(self, start, end):
        def _query(node, start, end):
            if not node:
                return None
            if node.start > end or node.end < start:
                return None
            if start <= node.start and node.end <= end:
                return node.cand
            lq = _query(node.left, start, end)
            rq = _query(node.right, start, end)
            return self.merge(lq, rq)

        return _query(self.root, start, end)


class MajorityChecker:

    def __init__(self, arr: List[int]):
        self.nums = arr
        self.st = SegmentTree(arr)
        self.idx = defaultdict(list)
        for i, n in enumerate(arr):
            self.idx[n].append(i)

    def query(self, left: int, right: int, threshold: int) -> int:
        n, _ = self.st.query(left, right)
        l = bisect_left(self.idx[n], left)
        r = bisect_right(self.idx[n], right)
        if r-l >= threshold:
            return n
        else:
            return -1
```

結果看到[這篇](https://leetcode.com/problems/online-majority-element-in-subarray/discuss/356108/C%2B%2B-160-ms-frequency-%2B-binary-search)才發現線段樹根本是多餘的，單純二分搜就可以解決，不管是實作時間還是執行時間都少了一大截。  

一樣儲存每個數字出現的位置，但是將key值依照總出現次數由大到小排序。  
主要的加速點在於透過threshold剪枝，對於每次查詢，先從最大出現次數的數字開始找，如果在區間內次數滿足threshold即回傳，否則繼續找下個。當**某數的總出現次數不及threshold時**，就可以直接跳脫並回傳-1了，畢竟不可能滿足出現次數。

```python
class MajorityChecker:

    def __init__(self, arr: List[int]):
        d=defaultdict(list)
        for i,n in enumerate(arr):
            d[n].append(i)
        self.idx=sorted(d.items(),key=lambda x:-len(x[1]))
        
    def query(self, left: int, right: int, threshold: int) -> int:
        for n,idx in self.idx:
            if len(idx)<threshold:
                break
            l=bisect_left(idx,left)
            r=bisect_right(idx,right)
            if r-l>=threshold:
                return n
        
        return -1
```