---
layout      : single
title       : LeetCode 2913. Subarrays Distinct Element Sum of Squares I
tags        : LeetCode Easy Array HashTable Math SegmentTree
---
雙周賽116。既是Q1又是Q4，測資範圍不同，難度大概差了二十倍。  

## 題目

輸入整數陣列nums。  

nums子陣列的**不同計數**定義為：  

- 令nums[i..j]為nums的子陣列，其中包含介於[i, j]之間的所有索引對應的元素  
- nums[i..j]的**不同計數**等於nums[i..j]中不同值的數量  

求所有子陣列**不同計數**的**平方和**。  
答案可能很大，先模10^9+7後回傳。  

## 解法

暴力枚舉所有子陣列，集合去重後得到**不同計數**，平方後加入答案。  

時間複雜度O(N^3)。  
空間複雜度O(N)。  

```python
class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        N=len(nums)
        ans=0
        
        for i in range(N):
            for j in range(i,N):
                sub=nums[i:j+1]
                s=set(sub)
                ans+=len(s)**2
                
        return ans
```

Q4的nums長度高達10^5，大概得找個小於O(N^2)的方法才行。  
以下簡稱**不同計數**為dis。  

先試著枚舉nums中的每個索引i，並找出以i為右邊界的所有子陣列sub的dis值，觀察其變化規律：  
> nums = [1,3,1]  
> i = 0  
> sub = [[1]], dis = [1]  
> i = 1  
> sub = [[1,3],[3]], dis = [2,1]  
> i = 2  
> sub = [[1,3,1],[3,1],[1]], dis = [2,2,1]  

答案正是這6個dis值的平方總合，共15。  

其實有點像是[2262. total appeal of a string]({% post_url 2022-05-01-leetcode-2262-total-appeal-of-a-string %})這題。  
觀察發現，每次加入元素x後，所有不包含x的的子陣列的dis值都會**加1**。那麼有哪些個子陣列符合？  
若x上次出現的索引為j，則左邊界大於等於j+1子陣列都符合，共i-(j+1)+1 = i-j個。  

好吧，到目前為止我們知道dis值的變化規律。但本題求的是dis值的**平方和**啊！！  
延續上例：  
> i = 1  
> dis1 = 2^2 + 1^2
> i = 2  
> dis2 = 2^2 + 2^2 + 1^2  

將兩式子的總變化量記為delta：  
> delta = dis2 - dis1  
> delta = (2^2 - 1^2) + (1^2 - 0^2)  

每個有變化的dis值d，其變化量為(d+1)^2 - d^2。  

> d變化量 = (d+1)^2 - d^2  
> 展開 = (d^2 + 2d + 1) - d^2  
> 相消 = 2d + 1  

也就是從左邊界大於等於j+1的所有子陣列，其dis平方值會增加2d+1。  
繼續用剛才的例子來加幾個元素驗證看看：  
> nums = [1,3,1]  
> i = 2  
> sub = [[1,3,1],[3,1],[1]], dis = [2,2,1]  
> dis平方總和 = 4+4+1 = 9  

加入沒出現過的新元素2，所有子陣列的dis值都增加1，每個平方值都會增加2d+1。  
則新的dis平方值應為[4+(2*2+1),4+(2*2+1),1+(1*2+1),0+(0*2+1)] = [9,9,4,1]。  
列出子陣列看看：  
> nums = [1,3,1,2]  
> i = 3  
> sub = [[1,3,1,2],[3,1,2],[1,2],[2]], dis = [3,3,2,1]  
> dis平方總合 = 9+9+4+1 = 23  

到目前為止，方法簡化成：  

- 遍歷每個nums[i]=x  
- 找到x上次出現的位置j  
- 平方總合 += sum( dis[idx]*2+1 FOR ALL j<idx<=i)  
- dis[idx] += 1 FOR ALL j<idx<=i  

但這樣還只是O(N^2)，還要繼續優化。  

假設有j-i=cnt個符合的索引。  
可以把dis[idx]*2+1拆成兩部分，+1的部分就是一開始用到的j-i。  
dis[idx]加總則交給**線段樹**來做**區間查詢**。  

時間複雜度O(N log N)。  
空間複雜度O(N)。  

```python
class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        # 區間查詢
        # 回傳[i, j]的總和
        def query(id, L, R, i, j):
            if i <= L and R <= j:  # 當前區間被目標範圍包含
                return tree[id]
            push_down(id, L, R)
            ans = 0
            M = (L+R)//2
            if i <= M:
                ans += query(id*2, L, M, i, j)
            if M+1 <= j:
                ans += query(id*2+1, M+1, R, i, j)
            return ans


        # 區間更新
        # 對[i, j]每個索引都增加val
        def update(id, L, R, i, j, val):
            if i <= L and R <= j:  # 當前區間被目標範圍包含
                tree[id] += (R-L+1)*val
                lazy[id] += val  # 標記每個位置都加val
                return
            push_down(id, L, R)
            M = (L+R)//2
            if i <= M:
                update(id*2, L, M, i, j, val)
            if M+1 <= j:
                update(id*2+1, M+1, R, i, j, val)
            push_up(id)


        # 將區間懶標加到答案中
        # 下推懶標記給左右子樹
        def push_down(id, L, R):
            M = (L+R)//2
            if lazy[id]:
                lazy[id*2] += lazy[id]
                tree[id*2] += lazy[id]*(M-L+1)
                lazy[id*2+1] += lazy[id]
                tree[id*2+1] += lazy[id]*(R-(M+1)+1)
                lazy[id] = 0


        # 以左右子樹更新答案
        def push_up(id):
            tree[id] = tree[id*2]+tree[id*2+1]


        MOD=10**9+7
        N = len(nums)
        tree = [0]*(N*4)
        lazy = [0]*(N*4)
    
        last={}
        ans=0
        sub=0
        for i,x in enumerate(nums):
            j=last[x] if x in last else -1 # last position we saw "x" 
            # dis[j+1, i] will be increase
            # delta = (d+1)^2 - d^2 = 2d + 1
            sub+=i-j # (i-j)*1
            sub+=query(1,0,N-1,j+1,i)*2 # sum(dis[j+1, i])*2 
            ans=(ans+sub)%MOD
            update(1,0,N-1,j+1,i,1) # dis[j+1, i] increased by 1
            last[x]=i
            
        return ans
```
