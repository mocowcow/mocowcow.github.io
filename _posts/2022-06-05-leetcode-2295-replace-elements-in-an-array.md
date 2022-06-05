--- 
layout      : single
title       : LeetCode 2295. Replace Elements in an Array
tags        : LeetCode Medium Array HashTable
---
周賽296。寫到第三題腦子突然又當機，明明知道不能但還是寫出O(N^2)解，當然是拿到免費WA。  

# 題目
輸入長度為n，且由不同正整數組成的陣列nums。對nums執行m次操作，在第i個操作中，將數字operations[i][0]替換為operations[i][1]。  

在每次操作中，保證：  
- operation[i][0]
- operation[i][1]不存在於nums中  

回傳執行完所有操作後的陣列。  

# 解法
多次在nums中找到某數並修改太過沒有效率，而且最大的問題是怎麼找。不如先把operations全部化簡，算出每個數字經過多次操作後的最終對應結果，再回去nums中一次改成最終答案。  

維護雜湊表index，紀錄某個數n的對應索引位置，並遍歷nums將所有n和對應索引i加入index。   
接下來遍歷operations，每個操作要將數字a改成b，所以我們把a所對應的索引丟給b。這時候nums中不會有a了，所以把a清空。  
最後遍歷index，將所有數塞到對應的索引中就是答案。  

```python
class Solution:
    def arrayChange(self, nums: List[int], operations: List[List[int]]) -> List[int]:
        index=defaultdict(int)
        for i,n in enumerate(nums):
            index[n]=i
            
        for a,b in operations:
            index[b]=index[a]
            del index[a]
            
        for n,i in index.items():
            nums[i]=n
            
        return nums
```

把第一個迴圈改得pythonic，然後把第二、三個迴圈合併起來的版本。  

```python
class Solution:
    def arrayChange(self, nums: List[int], operations: List[List[int]]) -> List[int]:
        index={n:i for i,n in enumerate(nums)}
        for a,b in operations:
            index[b]=index[a]
            nums[index[a]]=b
            del index[a]
            
        return nums
```
