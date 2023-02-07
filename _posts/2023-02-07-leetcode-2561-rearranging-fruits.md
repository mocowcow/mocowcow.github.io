--- 
layout      : single
title       : LeetCode 2561. Rearranging Fruits
tags        : LeetCode Hard Array HashTable Sorting Greedy
---
周賽331。這題有點小陷阱，一次AC的人是真的非常細心。  

# 題目
你有兩個水果籃，各裝了n個水果。輸入整數陣列basket1和basket2代表籃中各水果的成本。  

你想要使兩籃水果**相等**。你可以執行以下動作任意次：  
- 選擇兩個索引i和j，將basket1[i]和basket2[j]交換  
- 交換的成本為min(basket1[i], basket2[j])  

只要籃中水果經過排序後，結果完全一樣，則認為兩籃水果**相等**。  

求使兩籃水果相等的**最小成本**。若無法達成則回傳-1。  

# 解法
兩籃的水果種類數量要完全相同才能相等，那就有個大前提：每種成本水果的總數必為偶數。  

試看例題1：  
> basket1 = [4,2,2,2], basket2 = [1,4,1,2]  
> 兩籃子中原本就有的水果可以相消，所以實際上等價於  
> basket1 = [2,2], basket2 = [1,1]  
> 第一籃多兩個2，第二籃多兩個1。只需要將多餘水果的**一半**和對方交換即可相等  
> 2和1換，成本為1  

再想想，若有多個不同成本的水果：  
> basket1 = [1,1,99,99], basket2 = [2,2,88,88]  
> 如果[1,2], [99,88]這樣換，成本1+88  
> 如果[1,88], [99,2]這樣換，成本1+2  
> 結論：最小值配上最大值能夠將成本最低化  

因此分別計算出兩籃各多出哪些水果要換，一個遞增排序，一個遞減排序，倆倆配對取最小值就是交換成本。  

但是漏掉一個**特殊狀況**！！  
> basket1 = [1,99,99], basket2 = [1,88,88]  
> 照上面的作法會得到[99,88]換，成本88  
> 正確做法應該是[1,88]換，然後[99,1]換回去，成本1+1=2  

瓶頸在於排序，時間複雜度O(N log N)。空間複雜度O(N)。  

```python
class Solution:
    def minCost(self, basket1: List[int], basket2: List[int]) -> int:
        d1=Counter(basket1)
        d2=Counter(basket2)
        tot=d1+d2
        
        a1=[]
        a2=[]
        mn=inf
        for k,v in tot.items():
            if v%2==1:
                return -1
            mn=min(k,mn)
            need=v//2
            if d1[k]<need:
                a1+=[k]*(need-d1[k])
            elif d2[k]<need:
                a2+=[k]*(need-d2[k])
            
        a1.sort()
        a2.sort(reverse=True)
        ans=0
        for a,b in zip(a1,a2):
            ans+=min(a,b,mn*2)
        
        return ans
```
