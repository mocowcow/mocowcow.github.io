--- 
layout      : single
title       : LeetCode 2502. Design Memory Allocator
tags        : LeetCode Medium Array Design
---
周賽323。又是考驗數據範圍，其實根本配不上Q3的難度。  

# 題目
輸入整數n，代表一條長度為n的連續記憶體空間。記憶體初始值都為空。  

設計類別Allocator：  
- 建構子：初始化長度為n的連續記憶體  
- int allocate(int size, int mID)：找到為size，且最靠左的連續記憶體，將其分配給mID，並回傳第一格記憶體位置。若空間不足則回傳-1  
- int free(int mID)：釋放所有屬於mID的記憶體空間，並回傳釋放的數量  

# 解法
剛開始看到連續區塊、最靠左，還以為又是sorted list搭配二分。在看看測資範圍，n<=1000，最多呼叫1000次，那不就是叫我暴力法嗎？  

初始化長度n的陣列arr，代表記憶體。  

分配的時候先從頭遍歷arr，找到連續為size的空間。有找到就再來一次迴圈分配給mID，否則回傳-1。  

釋放的時候遍歷整個arr，碰到mID則清空，計數+1。  

分配和釋放的時間都是O(N)，空間也是O(N)。  

```python
class Allocator:

    def __init__(self, n: int):
        self.arr=[0]*n
        self.n=n

    def allocate(self, size: int, mID: int) -> int:
        start=end=0
        cnt=0
        for end,x in enumerate(self.arr):
            if x!=0:
                start=end+1
            if end-start+1==size:
                self.write(start,end,mID)
                return start
        return -1
        
    def write(self,i,j,id):
        for i in range(i,j+1):
            self.arr[i]=id

    def free(self, mID: int) -> int:
        cnt=0
        for i in range(self.n):
            if self.arr[i]==mID:
                self.arr[i]=0
                cnt+=1
        return cnt
```
