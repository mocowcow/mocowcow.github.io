--- 
layout      : single
title       : LeetCode 2286. Booking Concert Tickets in Groups
tags        : LeetCode Hard Design Array SegmentTree BinarySearch
---
雙周賽79。難度爆表的Q4，本來想說用兩個sorted list硬上，調了一小時出不來。結束時才發現整體AC率竟然只有2.8%，有夠誇張。

# 題目
一個音樂廳有n排，每排有m個座位，索引都從0開始。設計一個處理以下情形的訂票系統：  
- k個觀眾是否能**連續**坐在某一排中  
- k個觀眾**不要求連續或同排**，只要全部都有位置  

而且觀眾還很囉唆，要求：  
- 每個人的排數最多只能到maxRow  
- 如果有多種合法情況，則優先選擇靠前、靠左的座位  

實作BookMyShow類別：  
- BookMyShow(int n, int m)：初始化n*m個座位  
- int[] gather(int k, int maxRow)：回傳二維陣列，代表這群連續座位的**第一個位置**座標。如果不可能則回傳[]  
- boolean scatter(int k, int maxRow)：如果能成功分配到位置則回傳true，並優先選擇靠前的排、靠左的座位；否則回傳false  

# 解法
gather方法需要對單點修改一次，而scatter需要對單點修改多次。而這兩個需要一個共通的動作，就是找到第一排剩餘位置至少k個位置的排數。  
排數n最多只會到5*10^4，可以使用原版的線段樹，直接開出n\*4的空間，不需要動態開點。  
tree代表每個區間的座位占用數，而mx代表每個區間的最大連續空位數。  

定義幾個會用到的輔助函數：  
- add：對某個排的佔用位置加上val，並更新座位總和、最大連續座位  
- query：區間查詢，查詢從第i\~j排的座位總占用數  
- bisect：在maxRow之前，找到第一排剩餘座位數至少val的排數。若找不到回傳-1  

利用以上三個功能來實現gather和scatter：  
- gather：使用bissect找到第一排剩餘至少k的排數r，若r=-1則回傳[]；否則將第r排加上k個人，並回傳起始座標。  
- scatter：先以(0\~maxRow)*m計算座位數，並扣掉query查詢到已占用的部分，若不足k直接結束；否則以bisect找到第一排剩餘至少1個排數r，並貪心的安排位置，直到滿足k的位置為止。


參考詳解：https://leetcode.cn/problems/booking-concert-tickets-in-groups/solution/by-endlesscheng-okcu/  
修改成自己能夠接受的版本，主要差別是該作者是紀錄區間最小座位占用數min，再以m扣掉min得到空座位，而我直接紀錄max，比較直觀。  
這題複習了基本的線段樹做法，更讓我學習到**線段樹上的二分搜**，獲益良多。

```python
class BookMyShow:

    def __init__(self, n: int, m: int):
        self.n = n
        self.m = m
        self.tree = [0]*(n*4)
        self.mx = [m]*(n*4)

    def add(self, id, L, R, index, val):
        if L == R:
            self.tree[id] += val
            self.mx[id] -= val
            return
        M = (L+R)//2
        if index <= M:
            self.add(id*2, L, M, index, val)
        else:
            self.add(id*2+1, M+1, R, index, val)
        # push up
        self.tree[id] = self.tree[id*2]+self.tree[id*2+1]
        self.mx[id] = max(self.mx[id*2], self.mx[id*2+1])

    def query(self, id, L, R, i, j):
        if i <= L and R <= j:
            return self.tree[id]
        sm = 0
        M = (L+R)//2
        if i <= M:
            sm += self.query(id*2, L, M, i, j)
        if M+1 <= j:
            sm += self.query(id*2+1, M+1, R, i, j)
        return sm

    # first row with at least val seat
    def bisect(self, id, L, R, j, val):
        if self.mx[id] < val:
            return -1
        if L == R:
            return L
        M = (L+R)//2
        if self.mx[id*2] >= val:
            return self.bisect(id*2, L, M, j, val)
        if j > M:
            return self.bisect(id*2+1, M+1, R, j, val)
        return -1

    def gather(self, k: int, maxRow: int) -> List[int]:
        r = self.bisect(1, 0, self.n-1, maxRow, k)
        if r == -1:
            return []
        c = self.query(1, 0, self.n-1, r, r)
        self.add(1, 0, self.n-1, r, k)
        return [r, c]

    def scatter(self, k: int, maxRow: int) -> bool:
        if k > (maxRow+1)*self.m-self.query(1, 0, self.n-1, 0, maxRow):
            return False
        r = self.bisect(1, 0, self.n-1, maxRow, 1)
        while True:
            free = self.m-self.query(1, 0, self.n-1, r, r)
            if free >= k:
                self.add(1, 0, self.n-1, r, k)
                return True
            self.add(1, 0, self.n-1, r, free)
            k -= free
            r += 1
```
