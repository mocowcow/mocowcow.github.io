--- 
layout      : single
title       : LeetCode 2306. Naming a Company
tags        : LeetCode Hard Array String HashTable
---
周賽297。當時想到了以前綴、後綴分組，但就是沒想到用集合做運算，只通過74/89測資。  

# 題目
輸入字串陣列ideas，代表公司名稱的候選清單。公司命名流程如下：  
- 從ideas中選擇2個不同的名稱，分別稱為ideaA和ideaB  
- 交換ideaA和ideaB的首字母  
- 交換完，如果兩個新名稱都不在原本的ideas陣列中，則為有效的命名  

ideas中每個字串都是唯一的。  
回傳公司的不同有效命名的數量。

# 解法
ideas長度最大5*10^4，暴力法O(N^2)肯定是不行的，肯定需要用某種方法減少計算次數。  

每次只會交換各個idea的首字母，因此我們將字串切成兩個部分：首字母prefix，剩下的為suffix。  
維護雜湊表d，依首字母將各idea依照suffix進行分組。例如：  
> ideas = ["coffee","donuts","time","toffee"]  
> c = ['offee']  
> d = ['onuts']  
> t = ['ime','offee']  

第一眼就可以確認在同一組內的後綴互換後一定不合法，因此跳過不管。  
那還有沒有什麼情況不合法？像是'coffee'和'toffee'雖然不同組，但是後綴都是'offee'，以致交換完還是相同。  
所以c組和t組無法以'offee'進行交換。  

列舉所有前綴，使用set找出兩組的交集，將雙方的後綴數量扣掉交集大小後相乘，得到合法的命名數量，加入答案中。  
如此一來檢查交換的複雜度就固定為O(26*26)，主要剩下依前綴分組的部分O(N)，整體複雜度為O(N)。  

```python
class Solution:
    def distinctNames(self, ideas: List[str]) -> int:
        d=defaultdict(set)
        ans=0
        for s in ideas:
            pref=s[0]
            suff=s[1:]
            d[pref].add(suff)
            
        for p1 in d:
            for p2 in d:
                if p1==p2:continue
                dup=len(d[p1]&d[p2])
                ans+=(len(d[p1])-dup)*(len(d[p2])-dup)

        return ans
```
