--- 
layout      : single
title       : LeetCode 2766. Relocate Marbles
tags        : LeetCode Medium Array HashTable Sorting Simulation
---
雙周賽108。這Q2相對佛心，還保證移動來源一定有彈珠，讓不少人逃過WA，不如跟Q1交換。  

# 題目
輸入整數陣列nums，代表彈珠的初始位置。還有兩個長度相同的整數陣列moveFrom和moveTo。  

你會執行數次操作，在第i次操作，將所有位於moveFrom[i]的彈珠移動到moveTo[i]。  

在所有操作結束後，將所有被**占用**的的索引位置排序後回傳。  

注意：  
- **占用**指的是該位置存在至少一顆彈珠  
- 一個位置可能有數顆彈珠  

# 解法
每個位置有幾顆彈珠並不重要，只要知道哪裡有。  
~~不問敵人有多少，只問敵人在哪裡。~~  

用集合初始化nums中所有位置，按照題意模擬，遍歷所有移動操作，將moveFrom[i]從集合移除，在把moveTo[i]加入集合。  
最後將集合中的元素排序後回傳。  

時間複雜度O(N log N + M)，其中N為初始彈珠數量，M為操作次數。  
空間複雜度O(N)。  

```python
class Solution:
    def relocateMarbles(self, nums: List[int], moveFrom: List[int], moveTo: List[int]) -> List[int]:
        s=set(nums)
        
        for x,y in zip(moveFrom,moveTo):
            s.remove(x)
            s.add(y)
                
        return sorted(s)
```
