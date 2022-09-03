--- 
layout      : single
title       : LeetCode 967. Numbers With Same Consecutive Differences
tags        : LeetCode Medium Array Backtracking BFS DFS
---
每日題。看到測資就很明確可以用回溯法，但其實普通的DFS或BFS也可以過。  

# 題目
回傳所有長度為n的非負整數，使得每兩個連續數字之間的絕對差為k。  

注意，數字不能有前導零。例如01有一個前導零，是無效的。  
您可以按任何順序返回答案。  

# 解法
題目要求長度為n的整數，而相鄰數字絕對差為k，代表每次只會產生+k或是-k兩個分支。  
回溯法暴力生成所有可能的複雜度O(2^(N-1)\*9)，忽略常數為(2^N)。  

因前導零不合法，故第一個數字只能從1\~9中選擇。  
從第二個數字開始，則要根據上一位數字x，來產生x+k或是x-k兩種分支。要特別考慮**k=0**的情形，這時後只會有一個分支，可以用set保證不會重複使用。  
等選滿n個數字，則把數字全部接起來，加入答案中。  

下列程式碼有點偷吃步，雖然答案要求回傳整數陣列，但python不管型別，給他字串也不會出錯。不過還是給他整數比較好  

```python
class Solution:
    def numsSameConsecDiff(self, n: int, k: int) -> List[int]:
        ans=[]
        
        def bt(curr):
            if len(curr)==n:
                ans.append(reduce((lambda x,y:x*10+y),curr)) 
                # 其實下面這行也可以    
                # ans.append(''.join(map(str,curr)))
                return
            cand=set([curr[-1]+k,curr[-1]-k])
            for i in cand:
                if i<0 or i>9:continue
                curr.append(i)
                bt(curr)
                curr.pop()

        for i in range(1,10):
            bt([i])
        
        return ans
```

其實前一位的數字也可以透過MOD運算得到，直接用整數計算做BFS也可以。  
同樣從數字1\~9開始出發，進行n-1次BFS後得到答案。複雜度一樣是O(2^N)。  

```python
class Solution:
    def numsSameConsecDiff(self, n: int, k: int) -> List[int]:
        q=deque(range(1,10))
        
        for _ in range(n-1):
            for _ in range(len(q)):
                curr=q.popleft()
                x=curr%10
                for i in set([x+k,x-k]):
                    if i<0 or i>9:continue
                    q.append(curr*10+i)
        
        return q
```

改成遞迴dfs的版本。比起回溯版本，不用把所有數字串起來真的方便不少，而且執行速度也比較快。  

```python
class Solution:
    def numsSameConsecDiff(self, n: int, k: int) -> List[int]:
        ans=[]
        
        def dfs(size,curr):
            if size==n:
                ans.append(curr)
                return 
            x=curr%10
            for i in set([x+k,x-k]):
                if i<0 or i>9:continue
                dfs(size+1,curr*10+i)
                
        for i in range(1,10):
            dfs(1,i)
            
        return ans
```            
