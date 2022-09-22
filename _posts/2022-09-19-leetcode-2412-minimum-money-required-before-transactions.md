--- 
layout      : single
title       : LeetCode 2412. Minimum Money Required Before Transactions
tags        : LeetCode Hard Array Greedy
---
雙周賽87。本來想用排序+二分搜來解，結果被範例1擋掉，剩下時間不夠沒能寫出來。  

# 題目
輸入二維整數陣列transactions，其中transactions[i] = [costi, cashbacki]。  
該陣列代表著許多筆交易，其中每個交易必須以任意順序完成一次。每次要交易之前，你手上至少要有money數量的資金，滿足money>=costi才能夠使交易成立。交易結束後，money會變成money-costi+cashbacki。  

求至少要有多少資金，才能夠讓**所有順序**都成功完成交易。  

# 解法
這好像是我第一次碰到要求**所有順序**都要合法，而非**任一**交易。  
我們必須找到最差的交易順序，只要最差的合法，其他一定也行。  

某些交易的花費高於收益，會使得手上資金減少，故需要更多的初始資金，所以我們應該優先做完所有虧本的交易，才去做有賺錢的交易。  
首先遍歷一次transactions中每個cost和back，若為虧本則將虧本額加入sm中，最後得到sm=總最大虧本額。  
做完全部虧本的交易後，再找找剩下的賺錢交易中，誰的成本cost最高，總虧本額sm加上最高成本cost就會是初始所需的總金額。  

但是還漏掉一個可能性：虧本的交易中也可能有超大成本、超大收益，例如cost=10^9，back=10^9-1，實際上只虧一塊錢，但卻是所有交易的最大門檻。  
所以我們碰到虧本交易時，需要假設他為**最後一筆的虧錢交易**，先求出除了當筆交易以外的總虧本額，然後才加上當筆的cost。  

遍歷兩次，時間複雜度O(N)，空間複雜度O(1)。  

```python
class Solution:
    def minimumMoney(self, transactions: List[List[int]]) -> int:
        sm=0
        ans=0
        
        for cost,back in transactions:
            if cost>back:
                sm+=cost-back
                
        for cost,back in transactions:
            if cost>back:
                ans=max(ans,sm-(cost-back)+cost)
            else:
                ans=max(ans,sm+cost)   
        
        return ans
```

可以發現上面公式相消之後，虧錢交易為sm+back，而賺錢交易為sm+cost，可以把兩項壓縮成同一個變數，而加總sm的部分也可以放進同一次迴圈。  

```python
class Solution:
    def minimumMoney(self, transactions: List[List[int]]) -> int:
        sm=0
        mx=0

        for cost,back in transactions:
            if cost>back:
                sm+=cost-back
                mx=max(mx,back)
            else:
                mx=max(mx,cost)   
        
        return sm+mx
```

看見[zerotrac大神](https://leetcode.cn/problems/minimum-money-required-before-transactions/solution/fen-bie-kao-lu-mei-bi-jiao-yi-suo-dui-yi-t5ry/1758961)的評論，才知道原來可以排序，只是很難排而已。  
主要要拆成兩大部分：虧錢的交易擺前面，賺錢的交易擺後面。然後虧錢部分back小排前面；賺錢部分cost大排前面。  
最後再以貪心法不斷更新初始資金即可。  

使用到排序，時間複雜度上升至O(N log N)，空間複雜度維持O(1)。  

```python
class Solution:
    def minimumMoney(self, transactions: List[List[int]]) -> int:
        
        def compare(a,b):
            cost1,back1=a
            profit1=back1-cost1
            cost2,back2=b
            profit2=back2-cost2
            if profit1<0 and profit2<0:
                return -1 if back1<back2 else 1
            if profit1>0 and profit2>0:
                return -1 if cost1>cost2 else 1
            return profit1-profit2
        
        transactions.sort(key=cmp_to_key(compare))
        ans=0
        money=0
        for cost,back in transactions:
            if cost>money:
                ans+=cost-money
                money=cost
            money=money-cost+back
            
        return ans
```

comparator真的很難寫，不如分開把虧錢、賺錢部份各自排好再合起來，也得到一樣的效果。  
使用到額外空間保存交易，空間複雜度上升至O(N)。  

```python
class Solution:
    def minimumMoney(self, transactions: List[List[int]]) -> int:
        lose=[[c,b] for c,b in transactions if c>b]
        lose.sort(key=lambda x:x[1])
        earn=[[c,b] for c,b in transactions if c<=b]
        earn.sort(key=lambda x:-x[0])
        
        ans=0
        money=0
        for cost,back in lose+earn:
            if money<cost:
                ans+=cost-money
                money=cost
            money=money-cost+back
            
        return ans       
```
