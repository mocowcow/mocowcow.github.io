--- 
layout      : single
title       : LeetCode 2379. Minimum Recolors to Get K Consecutive Black Blocks
tags        : LeetCode Easy Array SlidingWindow
---
雙周賽85。老實說看到這題有嚇到，一時想不到怎麼暴力解，難道Q1就要求滑動窗口？感覺這次比賽有點可怕。  
雖然後來確定能用暴力解，但是討論區有人說做出Q4確做不出這題，有點誇張。  

# 題目
輸入長度為n字串blocks，其中blocks[i]可能是"W"或"B"，分別表示白色和黑色磁磚。  
還有一個整數k，代表要需要k個連續黑色區塊。  

每次動作中，可以將任意白色區塊變成黑色。  
求最少需要幾次動作才能使得k個連續黑色區塊出現。    

# 解法
找固定大小的連續範圍，很明顯可以使用滑動窗口，只要統計出非目標的元素個數即可。  

例如：  
> blocks = "WBBWWBBWBW", k = 7  
> 建立一個大小為7個窗口，向右滑動  
> "**WBBWWBB** WBW" 有3個W  
> "W **BBWWBBW** BW" 有3個W  
> "WB **BWWBBWB** W"  有3個W  
> "WBB **WWBBWBW**"  有4個W  
> 至少需要4次動作  

```python
class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        cnt=0
        ans=inf
        window=deque()
        
        for c in blocks:
            window.append(c)
            if c=='W':
                cnt+=1
            if len(window)==k:
                ans=min(ans,cnt)
                cnt-=window.popleft()=='W'
        
        return ans
```

最後還是來補個暴力法。列舉每個出發點i，開始數k個格子，計算當中出現幾個白色塊，以白色塊的數量更新最小值。  
總共會有N-k+1個出發點，每次k個格子，時間複雜度為O(N*k)。  

```python
class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        N=len(blocks)
        ans=inf
        
        for i in range(N-k+1):
            cnt=0
            for j in range(k):
                if blocks[i+j]=='W':cnt+=1    
            ans=min(ans,cnt)
            
        return ans
```