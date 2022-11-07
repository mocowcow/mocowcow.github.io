--- 
layout      : single
title       : LeetCode 2462. Total Cost to Hire K Workers
tags        : LeetCode Medium Array Heap TwoPointers Simulation
---
周賽318。這題藏了很多細節，不同的解法會碰到不同的陷阱，4次WA吃好吃滿。  

# 題目
輸入一個整數數組costs，其中costs[i]是僱用第i個工人的成本。  

你還得到兩個整數k和candidates。請根據以下規則雇用k個工人：  
- 你將招聘k次，每次雇用一個工人。 
- 在每次招聘中，從前candidates個工人或最後candidates個工人中選擇成本最低者，如果有多個最小成本，則選者索引較小者  
> 例如costs = [**3,2**,7,7,**1,2**] 且candidates = 2  
> 第一次招聘中，我們將選擇索引4的工人，因為他的成本最低  
> 第二次招聘中，剩下[**3,2**,7,**7,2**]，我們將選擇索引1的工人，因為他們的成本和索引4工人相同，但是索引較小。**索引可能會在招聘過程中變動**  
- 如果剩下的候選工人不足candidates人，同樣選擇其中成本最低且索引較小者  
- 一個工人只能被選擇一次  

求雇用k個工人的總成本。  

# 解法
照題目描述，可以很明白的知道要在左右端各維護一個heap，哪端的最小值較小，則從該方取出，再補入一位新工人。  
當左右各candidates人超過costs長度時，中間出現**重疊**，造成某些人重複計算而得出錯誤答案。若限制左右邊界後，兩個heap就有可能為空，沒有處理好又會出界。  

當時我氣到把兩個heap合併成一個，把工人裝進deque就不必處理邊界，最後帶上一個標記，0表示左邊要補工人，1表示補右邊。  
最後從heap中取出k次即可。若取出後工人還有剩，則依據標記決定補充來源。  

heap中最多擁有N個工人，共要取出k次，時間複雜度O(k log n)，空間複雜度O(N)。  

```python
class Solution:
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        ans=0
        N=len(costs)
        h=[]
        q=deque()

        for i,n in enumerate(costs):
            q.append([n,i])
        
        for i in range(candidates):
            if not q:break
            heappush(h,q.popleft()+[0])
        
        for i in range(candidates):
            if not q:break
            heappush(h,q.pop()+[1])
        
        for _ in range(k):
            c,idx,lr=heappop(h)
            ans+=c
            if q:
                if lr==0:
                    heappush(h,q.popleft()+[0])
                else:
                    heappush(h,q.pop()+[1])
                
        return ans
```

後來看到人家兩個heap的版本，直接把初始化的部分也合併到本體裡面，先檢查完heap是否為空，才進行比較。經過設計的程式碼比我上面那串可讀太多了。  

和上方一樣，時間複雜度O(k log n)，空間複雜度O(N)。  

```python
class Solution:
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        h1=[]
        h2=[]
        ans=0
        l=0
        r=len(costs)-1
        
        for _ in range(k):
            while l<=r and len(h1)<candidates:
                heappush(h1,costs[l])
                l+=1
            while l<=r and len(h2)<candidates:
                heappush(h2,costs[r])
                r-=1
            v1=h1[0] if h1 else inf
            v2=h2[0] if h2 else inf
            if v1<=v2:
                ans+=heappop(h1)
            else:
                ans+=heappop(h2)
        
        return ans
```
