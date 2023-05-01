--- 
layout      : single
title       : LeetCode 2659. Make Array Empty
tags        : LeetCode Hard Array BIT Sorting SegmentTree
---
雙周賽103。慶幸我封裝的BIT模板是從索引0開始的，才不用在那邊調邊界。  

# 題目
輸入由**不重複**整數組成的陣列nums，你可以執行以下動作直到**陣列為空**：  
- 如果第一個元素是陣列中的**最小值**，將之刪除  
- 否則，將第一個元素放到陣列**末端**  

求**最少**需幾次動作才能使陣列為空。  

# 解法
第一眼看：拿最前面，放最後面，這不就是普通的隊列嗎？  
考慮最差情況下，陣列會呈遞減，如321，直接模擬的話時間會是O(N^2)。  

仔細想想，把元素拿出、放到末端的動作，相當於一個**指向前端的指針向右一步**。  
例如：  
> nums = [3,2,1]  
> 相當於[3,2,1]，指針prev = 0  
> 執行一次動作，nums = [2,1,3]  
> 相當於[3,2,1]，指針prev = 1  
> 又執行一次動作，nums = [1,3,2]  
> 相當於[3,2,1]，指針prev = 2  
> 刪除掉位於前端的最小值，nums = [3,2]  
> 相當於[3,2,_]，指針prev = 0  
> 再執行一次動作，nums = [2,3]  
> 相當於[3,2,_]，指針prev = 1  
> 刪除掉位於前端的最小值，nums = [3]  
> 相當於[3,_,_]，指針prev = 0  
> 刪除最後一個值，陣列為空  

問題轉換過後，我們只要知道位於索引i的元素應該是**第幾個被刪除**，並從指針原本的位置prev移動過來。  
將nums[i]的值與索引i綁在一起，以nums[i]排序，即可得到刪除的順序。  

從prev移動到i有兩個重點：  
1. 需要紀錄i到prev之間實際上**剩下幾個元素**，才能得到正確的移動次數  
2. 若i在prev左邊，需要走完右邊那段，回到0後，繼續從0走到i  

我們需要一個可以單點修改、區間查詢總和的資料結構，所以我選擇數狀陣列binary indexed tree。  
初始化一個長度N的BIT，把所有索引都設為1，代表這些元素都**還沒被刪除**。之後被刪除掉的元素則將i設為0。  
若要計算從prev到i並刪除i的元素時，只需要求[prev,i]的區間和；若要先走回0，則多求一個[prev,N]的區間和。  

最後遍歷排序好的索引i，將prev移動到i的動作次數加入答案中即可。  

BIT每次更新、查詢都是O(log N)，共N次，時間複雜度O(N log N)。  
空間複雜度O(N)。  

```python
class BinaryIndexedTree:
    def __init__(self, n):
        self.bit = [0]*(n+1)
        self.N = len(self.bit)

    def update(self, index, val):
        index += 1
        while index < self.N:
            self.bit[index] += val
            index = index + (index & -index)

    def prefixSum(self, index):
        index += 1
        res = 0
        while index > 0:
            res += self.bit[index]
            index = index - (index & -index)
        return res
    
    def sumRange(self, left: int, right: int) -> int:
        return self.prefixSum(right)-self.prefixSum(left-1)

class Solution:
    def countOperationsToEmptyArray(self, nums: List[int]) -> int:
        N=len(nums)
        indexes=sorted([[x,i] for i,x in enumerate(nums)])
        indexes.sort()
        
        # init all elements
        bit=BinaryIndexedTree(N+5)
        for i in range(N):
            bit.update(i,1)
        
        ans=0
        prev=0
        for _,i in indexes:
            # move back to leftmost
            if i<prev: 
                ans+=bit.sumRange(prev,N)
                prev=0
            
            # move to i
            ans+=bit.sumRange(prev,i)
            bit.update(i,-1)
            prev=i
        
        return ans
```

用線段樹也可以達成同樣的效果，雖然時間複雜度一樣，但卻慢了不少。  

時間複雜度O(N log N)。  
空間複雜度O(N)。  

```python
class Solution:
    def countOperationsToEmptyArray(self, nums: List[int]) -> int:
        N=len(nums)
        indexes=sorted([[x,i] for i,x in enumerate(nums)])
        indexes.sort()
        
        def build(id,L,R):
            if L==R:
                tree[id]=init[L]
                return
            M=(L+R)//2
            build(id*2,L,M)
            build(id*2+1,M+1,R)
            tree[id]=tree[id*2]+tree[id*2+1]

        def query(id,L,R,i,j):
            if L==R:
                return tree[id]
            if i<=L and R<=j:
                return tree[id]
            ans=0
            M=(L+R)//2
            if i<=M:
                ans+=query(id*2,L,M,i,j)
            if M+1<=j:
                ans+=query(id*2+1,M+1,R,i,j)
            return ans

        def update(id,L,R,i,val):
            if L==R:
                tree[id]+=val
                return
            M=(L+R)//2
            if i<=M:
                update(id*2,L,M,i,val)
            else:
                update(id*2+1,M+1,R,i,val)
            tree[id]=tree[id*2]+tree[id*2+1] # merge nodes
            
        # init seg tree
        tree=[0]*(N*4)
        init=[1]*N
        build(1,0,N-1)
        
        ans=0
        prev=0
        for _,i in indexes:
            # move back to leftmost
            if i<prev: 
                ans+=query(1,0,N-1,prev,N)
                prev=0
            
            # move to i
            ans+=query(1,0,N-1,prev,i)
            update(1,0,N-1,i,-1)
            prev=i
        
        return ans
```

假設所有要元素都按照刪除順序排列，那他們可以**從左到右一輪刪除**。例如[1,2,3]，共3次。  

如果中間插了其他元素破壞順序，則這一輪中，需要**跳過其他元素各一次**。例如[1,2,4,5,6,3]，刪除[1,2,3]的時候需要跳過[4,5,6]一次，然後才刪除[4,5,6]，共6+3次。  

就算中間插的元素是無序的，也一樣道理。例如[1,3,5,4,2]，先跳過[3,5,4]刪除[1,2]，然後跳過[5]刪除[3,4]，最後才刪[5]，總共5+3+1次。  

講起來很簡單，實作起來很難。按照nums[i]的值將索引i排序後，只有在**當前的i小於prev時**，才能知道在上一輪刪除過程中**跳過了多少元素**，也就是**當前剩下的元素**。  

時間複雜度O(N log N)。  
空間複雜度O(N)。  

```python
class Solution:
    def countOperationsToEmptyArray(self, nums: List[int]) -> int:
        N=len(nums)
        indexes=sorted([[x,i] for i,x in enumerate(nums)])
        indexes.sort()
        
        ans=N
        prev=0
        remain=N
        
        for _,i in indexes:
            # these elements should be skipped at previous round
            if i<prev:
                ans+=remain
            prev=i
            remain-=1
            
        return ans
```