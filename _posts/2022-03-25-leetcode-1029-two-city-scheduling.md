---
layout      : single
title       : LeetCode 1029. Two City Scheduling
tags 		: LeetCode Medium Greedy Array Sorting
---
每日題。最近真的很greedy，而且我竟然五分鐘就直接想出正解，這就是所謂的題感吧。

# 題目
有一間公司準備要面試2N個人，分別讓N個人在城市a，N個人在城市b。  
costs二維陣列代表第i人飛往城市a和b的成本，求如何分配才能使所有人的移動成本最小化，並回傳最小成本。

# 解法
一定要靠排序，但是怎麼排？我想先把往a機會成本低的排到前面，且往b的成本越高，越優先排到a去。所以排序key為b-a。  
排完後，前N個讓他飛到a去，後面N個飛到b去，全部加起來就是答案。

紀錄一下，本來key有點冗餘，改了幾次，才簡化成現在版本，其實都是相同意思。  
> 第一版  
> key=lambda x:(x[0]-x[1],-abs(x[0]-x[1]))  
> 第二版  
> key=lambda x:(x[0]-x[1],-x[1])  
> 現在版  
> key=lambda x:(x[0]-x[1])  

```python
class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        N=len(costs)//2
        costs.sort(key=lambda x:(x[0]-x[1]))
        ans=0
        for i in range(N):
            ans+=costs[i][0]+costs[i+N][1]
                
        return ans
```

看到人家滿有趣的解法，但是速度比較慢一些。  
首先預設全部人飛往a，並將b和a的差值存到refund裡面，當作是改飛b的價差，多退少補。  
把refund排序後，再把前N的差額最小的加上去。  

| costs     | [10,20] | [30,200] | [400,50] | [30,20] |
| --------- | ------- | -------- | -------- | ------- |
| 全部飛a   | 10      | 30       | 400      | 30      |
| 改飛b差額 | 多10塊  | 多180    | 退350    | 退10    |
 
 全a成本=10+30+400+30=470，選退錢最多的前N個，退350+退10，共退360，答案為470-360=110。

```python
class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        N=len(costs)//2
        refund=[]
        ans=0
        for a,b in costs:
            ans+=a
            refund.append(b-a)
            
        refund.sort()
        for i in range(N):
            ans+=refund[i]
            
        return ans
```
