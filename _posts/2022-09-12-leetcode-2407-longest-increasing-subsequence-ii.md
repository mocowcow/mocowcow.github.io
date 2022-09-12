--- 
layout      : single
title       : LeetCode 2407. Longest Increasing Subsequence II
tags        : LeetCode Hard Array DP SegmentTree
---
周賽310。每次python寫線段樹都很痛苦，很容易出bug就算了，還常常超時。明明就是正確的複雜度還是TLE，嘔氣到不行。  
比賽結束後我自己又拿當時TLE的程式碼再交一次，竟然就過了(????)，真的氣氣氣氣，還我300名來。  

# 題目
輸入整數陣列nums和整數k。  

找到滿足以下要求的nums子序列：  
- 子序列嚴格遞增  
- 子序列中，每個相鄰元素之間的差異最多為k  

求最長子序列長度。  

# 解法
看到子序列，又看到相鄰元素限制就想到dp。  
而且又要是上升子序列，每個元素n可以接在n-k\~n-1之間的元素後面。k=10^5，代表每次有10^5轉移可能。  
如果使用普通的dp方法要轉移N次，每次k種可能，O(N\*k)肯定是超時的，需要一種有效率的方法找到n-k\~n-1之間的最大值。  
但是每次出現的n並沒有規律，要維護區間最大值只能靠線段樹了。線段樹每次更新查詢都是O(log k)，可以把時間複雜度降低到O(N log k)，空間複雜度O(N)。  

先講講當時比賽交出去TLE的動態開點線段樹。雖然後來再交就直接AC，大約執行7\~9秒鐘。但是把member改成slots之後超級加速到3秒多，這個關鍵要好好把握。  

先不管線段樹的實作如何，總之樹上保存的是以各個元素結尾的最大子序列長度，而我們在遍歷nums中每個數字n時要找的就是n-k\~n-1之中的最大長度mx。  
在樹上查詢完mx之後，將n的值更新為mx+1。最後回傳整顆樹的最大值就是答案。  

```python
class Node:
    __slots__ = ['L','R','mx','left','right'] # !!!!!!!!重要!!!!!!!!!!!
    def __init__(self, L, R, mx):
        self.L = L
        self.R = R
        self.mx = mx
        self.left = self.right = None

class SegmentTree:
    def __init__(self, L, R):
        self.root = Node(L, R, 0)

    def query(self, i, j):
        return self._q(self.root, i, j)

    def _q(self, node, i, j):
        if i > node.R or j < node.L:  # out of range
            return 0
        if i <= node.L and j >= node.R:  # fully covered
            return node.mx
        if not node.left:
            return node.mx
        return max(self._q(node.right, i, j), self._q(node.left, i, j))

    def update(self, i, j, val):
        self._u(self.root, i, j, val)

    def _u(self, node, i, j, val):
        if i > node.R or j < node.L:  # out of range
            return
        if i <= node.L and j >= node.R:  # fully covered
            node.mx = val
            node.left = node.right = None
            return
        M = (node.L+node.R)//2
        if not node.left:
            node.left = Node(node.L, M, node.mx)
            node.right = Node(M+1, node.R, node.mx)
        if M >= i:
            self._u(node.left, i, j, val)
        if M < j:
            self._u(node.right, i, j, val)
        node.mx = max(node.left.mx, node.right.mx)


class Solution:
    def lengthOfLIS(self, nums: List[int], k: int) -> int:
        MAXN=10**5
        st=SegmentTree(1,MAXN)
        
        for n in nums:
            lb=max(1,n-k)
            rb=n-1
            mx=st.query(lb,rb)
            st.update(n,n,mx+1)

        return st.query(1,MAXN)
```

接下來是最基本款的單點更新+範圍查詢線段樹，直接開出四倍空間，所以空間複雜度同樣是O(N)。  
稍微提一下，樹的範圍是1\~10^5，但是在n=1的情況下，查詢範圍會變成[1,0]，這時候會是無效查詢，實際上不會有任何計算，所以不需要特別處理。  

```python
class Solution:
    def lengthOfLIS(self, nums: List[int], k: int) -> int:
        MAXN=100005
        tree=[0]*(MAXN*4)
        
        def update(id,L,R,i,val):
            if L==R:
                tree[id]=val
                return
            M=(L+R)//2
            if i<=M:
                update(id*2,L,M,i,val)
            else:
                update(id*2+1,M+1,R,i,val)
            tree[id]=max(tree[id*2],tree[id*2+1])
        
        def query(id,L,R,i,j):
            if i<=L and R<=j:
                return tree[id]
            ans=0
            M=(L+R)//2
            if i<=M:
                ans=query(id*2,L,M,i,j)
            if j>M:
                ans=max(ans,query(id*2+1,M+1,R,i,j))
            return ans
        
        for n in nums:
            lb=max(1,n-k)
            mx=query(1,0,MAXN,lb,n-1)
            update(1,0,MAXN,n,mx+1)
            
        return tree[1]
```