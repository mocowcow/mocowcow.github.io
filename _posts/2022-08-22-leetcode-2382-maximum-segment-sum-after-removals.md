--- 
layout      : single
title       : LeetCode 2382. Maximum Segment Sum After Removals
tags        : LeetCode Hard Array SortedList
---
雙周賽85。這次拿到了383名，刷新個人最佳紀錄。雖然客觀來說這題偏難，不過剛好對上我的電波，就輕鬆AC了。  

# 題目
輸入兩個長度為n的整數陣列nums和removeQueries。對於第i次查詢，刪除nums中索引為removeQueries[i]的元素，並將nums分成不同**段**。  

**段**指的是nums的連續正整數序列。**段總和**是段中每個元素的總和。  
回傳長度為n的整數陣列answer，其中answer[i]是查詢完第i次之後的最大**段總合**。  

注意：每個索引只會被刪除一次。  

# 解法
如果要把某個序列切成兩段，有兩個問題：  
1. 根據下刀的位置不同，要重新計算兩段的總合  
2. 不知道當前切開的段是不是**最大段總和**  

感覺太麻煩了，我們試著逆向處理，變成在idx索引處加上某數字，使得左右兩邊的段合併。因為nums[i]只會出現正數，所以段總合永遠不可能變小，只需要以新產生的段來更新**最大段總和**。  

答案陣列ans長度為N，但是N次查詢之後每個元素都被刪除了，ans[N-1]必定為0，所以要從倒數第二格開始往前填答案；同理，removeQueries[0]可以不必處理。  

接下來開始寫程式，維護一個叫做sl的SortedList，用來有序地儲存各個段。還有變數mx紀錄當前**最大段總合**。  
遍歷N-1\~1中的第i個查詢，執行以下步驟：  
- 用二分搜找到插入點j  
- 檢查左右兩方的段是否能夠合併，若可合併則更新左右邊界及總合，刪除已合併的段，並插入新的段  
- 更新最大段總合mx，填入ans[i-1]中  

總共需要處理N-1個查詢，每次查詢最多需要4次二分搜(找插入點+刪除合併段2次+插入新段)，整體複雜度為O(N log N)。  

```python
from sortedcontainers import SortedList

class Solution:
    def maximumSegmentSum(self, nums: List[int], removeQueries: List[int]) -> List[int]:
        N=len(nums)
        ans=[0]*N
        sl=SortedList() # [l,r,sum]
        i=N-1
        mx=0
        
        while i>0:
            l=r=idx=removeQueries[i]
            sm=nums[idx]
            j=sl.bisect_left([l])
            to_remove=[]
            # merge left
            if j>0 and sl[j-1][1]==idx-1:
                l=sl[j-1][0]
                sm+=sl[j-1][2]
                to_remove.append(sl[j-1])
            # merge right
            if j<len(sl) and sl[j][0]==idx+1:
                r=sl[j][1]
                sm+=sl[j][2]
                to_remove.append(sl[j])
            # remove merged
            for x in to_remove:
                sl.remove(x)                
            sl.add([l,r,sm])
            mx=max(mx,sm)
            i-=1
            ans[i]=mx
            
        return ans
```

要照順序刪除其實也是可以，只是二分搜找區間調整起來很麻煩，一個不小心就出錯。  
至於最大區間總和的部分可以搭配前綴和以O(1)計算新的段總合，放到sortedlist裡面就可以快速得到最大值。  

```python
from sortedcontainers import SortedList

class Solution:
    def maximumSegmentSum(self, nums: List[int], removeQueries: List[int]) -> List[int]:
        N=len(nums)
        psum=[0]+list(accumulate(nums))
        ans=[0]*N
        segment_sum=SortedList()
        segment_sum.add(psum[-1])
        sl=SortedList() # [l,r,sum]
        sl.add([0,N-1,psum[-1]])

        for i in range(N-1):
            idx=removeQueries[i]
            j=sl.bisect_left([idx+1])-1
            l,r,sm=sl[j]
            # remove old
            sl.pop(j)
            segment_sum.remove(sm)
            # add left
            if l<idx:
                sm=psum[idx]-psum[l]
                sl.add([l,idx-1,sm])
                segment_sum.add(sm)
            # add right
            if r>idx:
                sm=psum[r+1]-psum[idx+1]
                sl.add([idx+1,r,sm])
                segment_sum.add(sm)
            ans[i]=segment_sum[-1]
            
        return ans
```

同樣是逆向操作，可以使用併查集，將時間複雜度降低至O(N)。  

對於每個要插入的點idx，初始化段總合為nums[i]，檢查左右是否存在，若存在則將其root指向idx，並將總和加到idx上。  

```python
class UnionFind:
    def __init__(self):
        self.parent = {}
        self.sm = {}

    def union(self, x, y):
        px = self.find(x)
        py = self.find(y)
        if px != py:
            self.sm[py]+=self.sm[px]
            self.parent[px] = py

    def find(self, x):
        if x != self.parent[x]:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

class Solution:
    def maximumSegmentSum(self, nums: List[int], removeQueries: List[int]) -> List[int]:
        N=len(nums)
        ans=[0]*N
        uf=UnionFind()
        mx=0
        i=N-1
        
        while i>0:
            idx=removeQueries[i]
            uf.parent[idx]=idx
            uf.sm[idx]=nums[idx]
            # merge left
            if idx-1 in uf.parent:
                uf.union(idx-1,idx)
            # merge right
            if idx+1 in uf.parent:
                uf.union(idx+1,idx)
            mx=max(mx,uf.sm[idx])
            i-=1
            ans[i]=mx
                
        return ans
```    
            

        