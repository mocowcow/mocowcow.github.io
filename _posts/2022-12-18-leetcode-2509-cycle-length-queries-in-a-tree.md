--- 
layout      : single
title       : LeetCode 2509. Cycle Length Queries in a Tree
tags        : LeetCode Hard Array Tree
---
周賽324。體感比Q3簡單一些，但還是出一個WA，真丟人。  

# 題目
輸入整數n，代表有一顆完整二元樹(complete binary tree)，共有2^n-1個節點：  
- 根節點值為1，且節點值介於[1, 2^(n-1)-1]  
- 左節點值為val\*2，右節點為val\*2+1  

還有長度m的二維陣列queries，其中queries[i] = [a<sub>i</sub>, b<sub>i</sub>]，你必須：  
- 在a<sub>i</sub>, b<sub>i</sub>之間建立一條邊  
- 找到圖中的**環**的長度  
- 移除a<sub>i</sub>, b<sub>i</sub>之間的邊  

回傳長度m的整數陣列answer，其中answer[i]為queries[i]的答案。  

# 解法
其實就是找最近公共祖先LCA(Lowest Common Ancestor)。  

令每次queries[i] = (A, B)，分別讓A和B往上移動，會在某個節點碰面，那邊就是所謂的LCA，也就是循環的起點與終點。  

寫一個輔助函數f(x)，求出從節點x到根結點的路徑。  
若A不等於B，則重複以下動作：  
- 若A深度較深，則往上移動，長度+1  
- 否則使B往上移動，長度+1  

找到LCA，迴圈停止之後，因為A和B之間還要有一條連線，所以長度要再加上1。  

時間複雜度O(nm)，其中n為樹的深度，m為查詢次數。空間複雜度O(m+n)。  

```python
class Solution:
    def cycleLengthQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        
        def f(x):
            q=deque()
            while x>0:
                q.append(x)
                x//=2
            return q
        
        ans=[]
        for a,b in queries:
            a=f(a)
            b=f(b)
            cnt=1
            while a[0]!=b[0]:
                cnt+=1
                if len(a)>len(b):
                    a.popleft()
                else:
                    b.popleft()
            ans.append(cnt)
            
        return ans
```

然而根本不用求出路徑，直接用節點編號計算就可。然後答案也可以直接寫在qeuries裡面。  

時間複雜度O(nm)。空間複雜度O(1)。  

```python
class Solution:
    def cycleLengthQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        for i,(a,b) in enumerate(queries):
            cnt=1
            while a!=b:
                if a>b:
                    a//=2
                else:
                    b//=2
                cnt+=1
            queries[i]=cnt
            
        return queries
```