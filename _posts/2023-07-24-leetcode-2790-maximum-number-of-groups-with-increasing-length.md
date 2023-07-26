--- 
layout      : single
title       : LeetCode 2790. Maximum Number of Groups With Increasing Length
tags        : LeetCode Hard Array Greedy Sorting
---
周賽355。史上最難的Q3。  
當初第一眼覺得是二分答案，但是看比賽中的AC率不到2%，嚇得直接跳過不做。  
後來仔細想想發現其實沒這麼難，主要是範例給的提示不明顯。  

# 題目
輸入長度n的整數陣列usageLimits。  

你的目標是利用數字0 \~ n-1來構造一些群組，且每個數字i的可用次數為usageLimits[i]。你必須符合以下條件：  
- 每個群組中必須由**不同**的數字組成，也就是數字不可重複  
- 除第一組以外，每一組的長度都必須**嚴格大於**前一組  

求**最多**可以建構出幾個群組。    

# 解法
反正數字大小本身不影響答案，只在乎可用次數，先將usageLimits排序。  

如果想要一組一組的建構，每次都要找好幾個不同的數，到第n組要找n個，很沒有效率。  
將問題稍微轉換，改成對原本的群組加入1個數，然後重新建立一個大小1的群。  
例如：  
> [1]  
> [1,2],[2]  
> [1,2,3],[2,3],[3]  

假如我們想要組成n個群組，那麼至少要有n個數，其可用次數分別至少為[1,2,...,n]。  
但像是[2,2,2]這個例子，乍看之下可能以為只能組成2組，其實是3組：  
> [1] 但是剩下一個1沒用到  
> [1,2],[2] 剩的1還是沒用  
> [1,2,3],[2,3],[1]  

可以發現，先前沒用完的數字，可以**留給之後的群組**繼續用。那怎麼保證群組中不會出現重複的數字？  
因為已經按照可用次數遞增排序，後面遇到的數字b，其可用次數一定不少於前面的數字a。只要先使用b，不足的在使用先前剩餘的數字就不會重複。  

維護變數lvl代表下一次要擴建的組數，所以每次需要使用lvl個數字。extra代表之前沒用完的數字。  
由小到大遍歷每個可用次數x，如果x剛好可以足夠lvl個群，那就直接使用，然後把用剩的丟到extra；不夠的話，就看extra+x夠不夠lvl，夠的話就可以湊合著擴建一組。  

注意：lvl指的是**下次**要擴建的組數，所以lvl要減1才是**現有的組數**。  

時間複雜度O(N log N)。  
空間複雜度O(1)。  

```python
class Solution:
    def maxIncreasingGroups(self, usageLimits: List[int]) -> int:
        N=len(usageLimits)
        usageLimits.sort()
        
        lvl=1
        extra=0
        for x in usageLimits:
            if x>=lvl:
                extra+=x-lvl
                lvl+=1
                continue
                
            extra+=x
            if extra>=lvl:
                extra-=lvl
                lvl+=1
                
        return lvl-1
```
