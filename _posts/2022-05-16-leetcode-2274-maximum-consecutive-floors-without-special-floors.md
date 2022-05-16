--- 
layout      : single
title       : LeetCode 2274. Maximum Consecutive Floors Without Special Floors
tags        : LeetCode Medium Array Sorting
---
周賽293。乍看很麻煩，細想後很簡單。

# 題目
Alice開公司，租了一棟大樓的部分樓層當辦公室。Alice選了某幾層當作special floors，當作休息室。
輸入整數bottom和top，表示Alice已經租下了從bottom到top(包含)所有樓層。另外輸入整數陣列special，其中special[i]代表休息室。  
求不包含休息室的最大連續樓層有幾層。

# 解法
最底層是bottom，可以把bottom-1也當作是休息室；最頂層是top，也可以把top+1當作休息室。  
把這兩個加入special後排序，問題就簡化成**兩層休息室之間的最大間格有幾層**。

```python
class Solution:
    def maxConsecutive(self, bottom: int, top: int, special: List[int]) -> int:
        special.append(bottom-1)
        special.append(top+1)
        special.sort()
        ans=0
        for i in range(1,len(special)):
            size=special[i]-special[i-1]-1
            ans=max(ans,size)
            
        return ans
```

也可以不加入新的樓層，直接將bottom, top當作特例處理。  
一樣先將special排序，先計算bottom到第一個休息室的距離，還有最後一個休息室到top的距離。  
最後回去計算每個休息室之間的距離。

```python
class Solution:
    def maxConsecutive(self, bottom: int, top: int, special: List[int]) -> int:
        special.sort()
        ans=max(special[0]-bottom,top-special[-1])
        for i in range(1,len(special)):
            size=special[i]-special[i-1]-1
            ans=max(ans,size)
            
        return ans
```