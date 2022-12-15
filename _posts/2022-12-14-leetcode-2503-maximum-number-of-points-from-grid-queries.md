--- 
layout      : single
title       : LeetCode 2503. Maximum Number of Points From Grid Queries
tags        : LeetCode Hard Array Matrix Heap BFS
---
周賽323。成績最好的一次，35分鐘清掉四題，排名144，真是開心。  

# 題目
輸入大小m\*n的矩陣grid，還有大小為k的陣列qeuries。  

產生一個長度同為k的陣列answer，並以qeuries[i]從矩陣的**最左上角**進行以下動作：  
- 如果qeuries[i]嚴格大於當前格子：若是第一次抵達該點格子，則獲得1分。然後可以移動到上下左右任一格相鄰的格  
- 否則，結束這次動作  

在動作結束之後，令answer[i]為可獲得的**最大分數**。  
注意：同一個格子**可以重複訪問**。  

回傳查詢的答案陣列answer。  

# 解法
題目描述有點繞口，其實等價於：  
- 每次queries[i]，從左上角出發，可以移動到任何相鄰且嚴格小於queries[i]的相鄰格子  
- 可以抵達的格子數即為查詢分數answer[i]  

隨著查詢值增加，可抵達的格子一定只增不減。  
雖然一看就知道併查集可以做，但是不是很好寫，最後改成BFS了。  

查詢的範圍為1\~10^6，但格子中最小值也是1，使得查詢1永遠為0。所以可以從查詢2開始預處理。  
維護一個min heap，初始化時放入左上角的格子，以格子的值作為鍵值，如此以來heap頂端一定會是最小的格子。  
窮舉所有查詢值i，如果heap中有小於i的格子，則訪問該格子獲得分數，並將其四周相鄰格子放入heap中。直到heap中所有格子都不小於i，則將分數保存到查詢答案point中。  

最後遍歷qeuires，根據查詢值到point中取得對應結果後回傳。  

m\*n<=10^5，如果矩陣元素排列方式非常極端的狀況下，會有將近一半的元素都塞在heap中，如此一來heap單次操作時間為O(log mn)。然後每個元素都要出入heap各一次，時間複雜度為O(mn log mn)。  
查詢範圍k<=10^6，只要將預處理結果寫入，時間複雜度O(k)。  

整題時間複雜度為O(mn log mn + max(queries))，空間為O(mn + max(queries))。   

```python
class Solution:
    def maxPoints(self, grid: List[List[int]], queries: List[int]) -> List[int]:
        M,N=len(grid),len(grid[0])
        point=[0]*1000005
        
        h=[[grid[0][0],0,0]]
        grid[0][0]=inf
        cnt=0
        
        for i in range(2,1000005):
            while h and h[0][0]<i:
                curr,r,c=heappop(h)
                cnt+=1
                for dx,dy in zip([0,1,0,-1],[1,0,-1,0]):
                    rr=r+dx
                    cc=c+dy
                    if rr<0 or rr==M or cc<0 or cc==N:continue
                    heappush(h,[grid[rr][cc],rr,cc])
                    grid[rr][cc]=inf
            point[i]=cnt
       
        return [point[q] for q in queries]
```
