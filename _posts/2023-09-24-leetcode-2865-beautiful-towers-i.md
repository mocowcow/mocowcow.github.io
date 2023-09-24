---
layout      : single
title       : LeetCode 2865. Beautiful Towers I
tags        : LeetCode Medium Array Simulation Stack PrefixSum
---
周賽364。

## 題目

輸入長度n的整數陣列maxHeights。  

你要建造n個塔，第i個塔在座標i上，且高度為heights[i]。  

一個**美麗的**塔，配置方式需要符合以下條件：  

- 1 <= heights[i] <= maxHeights[i]  
- heights是山形陣列  

山形陣列heights必須存在一個索引i：  

- 對於所有 0 < j <= i ，所有 heights[j - 1] <= heights[j]  
- 對於所有 i <= k < n - 1 ，所有 heights[k + 1] <= heights[k]  

求**美麗塔**的**最大高度總和**。  

## 解法

簡單講就是要選一個山頂i，以i為中心，往左右要呈單調遞減。例如：[1,2,3,3,1]。  
但是每個索引j同時要受到maxHeights[j]的限制。  

測資不大可以暴力模擬，枚舉索引i作為山頂，往左右擴散處理。  
得出以i為山頂的各塔高度tower後，以tower總和更新答案。  

時間複雜度O(N^2)。  
空間複雜度O(N)。  

```python
class Solution:
    def maximumSumOfHeights(self, maxHeights: List[int]) -> int:
        N=len(maxHeights)
        ans=0
        
        for i in range(N):
            tower=[0]*N
            tower[i]=maxHeights[i]
            
            for j in range(i+1,N):
                tower[j]=min(tower[j-1],maxHeights[j])
                
            for j in reversed(range(i)):
                tower[j]=min(tower[j+1],maxHeights[j])
                
            ans=max(ans,sum(tower))
            
        return ans
```

測資大一點，上面方法就吃土了。  

延續剛才所說的，山頂兩邊是向兩方**單調遞減**，那麼八九不離十就是**單調堆疊**。  
先預處理前綴pref和後綴suff，其中pref[i]以i為山頂時，左半邊的塔高總和，suff[i]是右半邊的塔高總和。  

以範例2為例：  
> maxHeights = [6,5,3,9,2,7]  
> pref[0] = sum[6]  
> pref[1] = sum[**6**, 5] 要把超過5的都改成5  
> pref[1] = sum[5, 5]  
> pref[2] = sum[**5, 5**, 3] 要把超過3的都改成3  
> pref[2] = sum[3, 3, 3]  
> pref[3] = sum[3, 3, 3, 9]  
> pref[4] = sum[**3, 3, 3**, 9, 2] 要把超過2的都改成2  
> pref[4] = sum[2, 2, 2, 2, 2]  
> pref[5] = sum[2, 2, 2, 2, 2, 7]  

雖然邏輯正確，但是在[5,4,3,2,1]這種遞減的情況下，越前面的數字會被修改越多次，最後複雜度高達O(N^2)。  
但是可以發現，所有被刪掉的數都會改成跟maxHeights[i]相同，那直接用一個數對[base, freq]表示數字base連續出現freq次，這樣就可以保證每個索引i的數只進出堆疊各一次。  

後綴suff也按照相同步驟處理，最後合併pref[i]和suff[i]更新答案。  
注意：前後綴都包含maxHeights[i]，所以要扣掉maxHeights[i]。  

時間複雜度O(N)。  
空間複雜度O(N)。  

```python
class Solution:
    def maximumSumOfHeights(self, maxHeights: List[int]) -> int:
        N=len(maxHeights)
        
        pref=[0]*N
        sm=0
        st=[] # [base,freq]
        for i,x in enumerate(maxHeights):
            cnt=1
            while st and st[-1][0]>x:
                base,freq=st.pop()
                sm-=base*freq
                cnt+=freq
            sm+=x*cnt
            st.append([x,cnt])
            pref[i]=sm
        
        suff=[0]*N
        sm=0
        st=[] # [base,freq]
        for i in reversed(range(N)):
            x=maxHeights[i]
            cnt=1
            while st and st[-1][0]>x:
                base,freq=st.pop()
                sm-=base*freq
                cnt+=freq
            sm+=x*cnt
            st.append([x,cnt])
            suff[i]=sm
        
        ans=0
        for i,x in enumerate(maxHeights):
            tot=pref[i]+suff[i]-x
            ans=max(ans,tot)
            
        return ans
```
