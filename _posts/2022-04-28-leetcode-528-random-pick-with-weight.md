--- 
layout      : single
title       : LeetCode 528. Random Pick with Weight
tags        : LeetCode Medium Design Array BinarySearch
---
二分搜學習計畫。，剛開始覺得十分複雜，後來越寫越簡單。

# 題目
設計一個資料結構，初始化時輸入長度N的陣列w，w[i]代表第i個位置的權重。  
並實作函數pickIndex()，抽出N個位置中的其中一個。  
> w = [1,3] 總權重為1+3=4  
> 索引0被抽到的機率為1/4  
> 索引1被抽到的機率為3/4  

# 解法
一開始想說開一個list，遍歷每個w[i]，把i加入w[i]次，然後在隨機抽一個位置就好。結果看w<=10^4，w[i]<=10^5，最差狀況下會變成10^9，記憶體肯定爆炸。  

以前在[這題]({% post_url 2022-03-29-leetcode-2213-longest-substring-of-one-repeating-character %})做過連續區間的二分搜，改成那樣的話空間變成10^4，應該可以行。  
起點curr從0開始記起，每次讀入w[i]後產生一個左閉右開的區間(curr,curr+w[i])，例：  
> w = [1,2,3]  
> seg = [(0,1),(1,3),(3,6)]  

區間轉換完成後記錄下總權重sm，來去處理隨機函數。  
總權重為sm，但是以0開始計，所以抽出0~sm-1的隨機位置r，找到r是屬於第i個區間，回傳i即可。

```python
class Solution:

    def __init__(self, w: List[int]):
        self.seg=[]
        curr=0
        for i,x in enumerate(w):
            self.seg.append((curr,curr+x,i))
            curr+=x
        self.sm=curr

    def pickIndex(self) -> int:
        r=random.randint(0,self.sm-1)
        i=bisect_right(self.seg,(r,math.inf))-1
        return self.seg[i][2]
```

後來想想不用這麼麻煩，畢竟每個區間的右邊界都沒有碰到過，化成普通的前綴和就好了。  
> w=[1,2,3]  
> ps=[1,3,6]  

從1~總權重sm中，抽隨機數r，找到前綴和中第一個大於等於r的位置i回傳。

```python
class Solution:

    def __init__(self, w: List[int]):
        self.sm=w[0]
        self.ps=[self.sm]
        for i in range(1,len(w)):
            self.sm+=w[i]
            self.ps.append(self.sm)

    def pickIndex(self) -> int:
        r=random.randint(1,self.sm)
        return bisect_left(self.ps,r)
```