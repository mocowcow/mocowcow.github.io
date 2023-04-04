--- 
layout      : single
title       : LeetCode 2611. Mice and Cheese
tags        : LeetCode Medium Array Sorting Greedy
---
周賽339。一開始想錯方法，又WA一次。  

# 題目
有兩隻老鼠以及n個不同的乳酪，每個乳酪**必須**分配給其中一隻老鼠吃。  

以下是第i個乳酪的得分：  
- 第一隻老鼠吃，可得reward1[i]  
- 第二隻老鼠吃，可得reward2[i]  

輸入正整數陣列reward1和reward2，還有非負整數k。  

求第一隻老鼠正好吃掉k個乳酪時的**最大得分**。  

# 解法
本來以為找reward1[i]較大，reward2[i]較小的前k個分給一號鼠，剩下的丟給二號鼠。  
但是碰到這個例子就炸了：  
> reward1 = [5,3], reward2 = [5,1], k = 1  
> 選reward1[0]和reward2[1] = 5 + 1  
> 最佳解為reward1[1]和reward2[0] = 3 + 5  

正確方法應該是判斷乳酪給一號鼠吃的**效益**為多少，例如：  
> reward1[i] = 10, reward2[i] = 20  
> 一號鼠吃可得10，二號鼠吃可得20  
> 所以一號鼠吃的效益為10 - 20 = -10

在回到剛才的例子：  
> reward1 = [5,3], reward2 = [5,1], k = 1  
> reward[0]給一號鼠的損益為5 - 5 = 0  
> reward[1]給一號鼠的損益為3 - 1 = 2  
> 所以要將最大效益的前k個乳酪給一號鼠  

維護一個陣列，同時記錄reward1[i]和reward2[i]以及效益，以效益遞減排序。  
然後將效益最大的前k個乳酪給一號鼠，剩下的都給二號鼠。  

瓶頸在於排序，時間複雜度O(N log N)。空間複雜度O(N)。  

```python
class Solution:
    def miceAndCheese(self, reward1: List[int], reward2: List[int], k: int) -> int:
        N=len(reward1)
        a=[]
        for r1,r2 in zip(reward1,reward2):
            profit=r1-r2
            a.append([profit,r1,r2])
            
        a.sort(reverse=True)
        
        ans=0
        for i in range(k):
            ans+=a[i][1]

        for i in range(k,N):
            ans+=a[i][2]

        return ans
```
