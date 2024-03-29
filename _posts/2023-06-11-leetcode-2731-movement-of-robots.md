--- 
layout      : single
title       : LeetCode 2731. Movement of Robots
tags        : LeetCode Medium Array Sorting
---
雙周賽106。這種腦筋急轉彎題真的是很垃圾，講一堆廢話結果都沒有用，每次都被這種爛題浪費時間。  

# 題目
有一些機器人在無邊界的直線上，他們的初始位置由整數陣列nums表示。機器人每秒可以移動一個單位距離。  

輸入陣列s，代表機器人的移動方向，"L"代表向左，而"R"向右。  

如果兩個機器人發生碰撞，則會向反方向移動。  

求經過d秒後，所有機器人對之間的距離總和。答案很大，先模10^9+7後回傳。  

注意：  
- 機器人對(i,j)和(j,i)視為相同  
- 如果發生碰撞，會**立刻**轉向，不需要等待任何時間  
- 如果兩個機器人停在同一個位置才視為碰撞，例如兩個機器人分別從1向右走、從3向左走，下一秒鐘都處於2，所以兩者都會改變方向，分別從2向左和向右走  
- 如果是從0向右走、從1向左走，下一秒位置分別為1和0，沒有碰撞，會維持原本的方向  

# 解法
先說結論：根本不用管轉向。  

舉個例子，兩機器人AB分別朝同方向移動3步：  
> [A, _, B]
> 第一步移動完[\_, AB, _]需要轉向
> 第二步[A, _, B]  
> 第三步[A, _, _, _, B]  

如果假裝不用轉向：  
> [A, _, B]
> 第一步移動完[\_, AB, _]發生碰撞，但不管  
> 第二步[B, _, A]  
> 第三步[B, _, _, _, A]  

會發現停留的位置都是一樣的，只是機器人編號不同而已。  
反正我們也只要知道最後哪些位置有機器人存在，而不在乎編號。  
直接將初始位置往移動方向加d步就是最終位置。  

將位置pos排序後，對於第i個機器人來說，pos[i]會作為左邊i個機器人組成對(left, i)，所以pos[i]會貢獻i次；同樣，pos[i]會和右邊N-1-i個機器人組成對(i, right)，所以pos[i]會被扣除N-1-i次。  

瓶頸為排序，時間複雜度O(N log N)。  
空間複雜度O(N)。  

```python
class Solution:
    def sumDistance(self, nums: List[int], s: str, d: int) -> int:
        MOD=10**9+7
        N=len(nums)
        pos=[]
        for i,dir in zip(nums,s):
            if dir=="L":
                pos.append(i-d)
            else:
                pos.append(i+d)
                
        pos.sort()
        ans=0
        for i,x in enumerate(pos):
            ans+=x*i
            ans-=x*(N-1-i)
            
        return ans%MOD
```
