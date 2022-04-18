---
layout      : single
title       : LeetCode 2245. Maximum Trailing Zeros in a Cornered Path
tags 		: LeetCode Medium Matrix PrefixSum
---
周賽289。本來寫得挺流暢，直到碰到這垃圾題，搞將近一小時才想到核心概念，但是來不及寫出來。  
後來自己找時間寫，也差不多敲了20分鐘才把BUG處理完，敲完50行手差點沒斷掉，要說這題是hard應該很多人都同意。  
更誇張的是[史帝芬大神](https://leetcode.com/problems/maximum-trailing-zeros-in-a-cornered-path/discuss/1959385/7-lines-Python)用numpy寫出7行版本，有夠誇張。

# 題目
輸入M*N的矩陣。  
cornered path(有轉彎的路徑？)指的是一連串的相鄰格子，最多只轉彎一次。反正就是走直線到某個點之後轉彎繼續直走。以下簡稱路徑。  
乘積指的是路徑上所有格子數值相乘的結果。  
求所有路徑的乘積中最多能有幾個**尾隨0**。

# 解法
這題幾個核心概念：  
1. 前綴和，避免路徑值的重複計算  
2. 尾隨0只受2和5影響，乘上其他數字不會改變結果  
3. 轉彎的路徑就是一條直+一條橫，多走也沒關係  

剛開始沒意識到第二點，就做成了**前綴乘積**，雖然可以在O(1)時間內得到範圍乘積，但是沒辦法確定有幾個0，所以在更新答案時還是很浪費時間，最後TLE。  
先寫兩個函數，分別用來算某數n可以拆出幾個2和5，之後拿去建立前綴和。  
對每個row和col建立計算2和5數量的前綴和，然後枚舉所有有效的路徑。  

根據先前提到第三點，多走了幾格頂多就是乘上不必要的數，並不會讓尾隨0的數量減少，所以拐彎後走到底就對了。  
遍歷每個點mid，以此為轉角處生成的有效路徑共有四種：  
1. 由上走到mid再左轉到底  
2. 由上走到mid再右轉到底  
3. 由下走到mid再左轉到底  
4. 由下走到mid再右轉到底  

一個2搭配一個5可以升成一個尾隨0，路徑上的的2和5分別加總，取最小值就是該路徑尾隨0的數量。

```python
class Solution:
    def maxTrailingZeros(self, grid: List[List[int]]) -> int:
        
        def get2(n):
            cnt=0
            while n%2==0:
                cnt+=1
                n//=2
            return cnt
        
        def get5(n):
            cnt=0
            while n%5==0:
                cnt+=1
                n//=5
            return cnt
        
        M,N=len(grid),len(grid[0])
        #build row psum
        R2=[[0]*(N+1) for _ in range(M)]
        R5=[[0]*(N+1) for _ in range(M)]
        for r in range(M):
            for i in range(N):
                R2[r][i+1]=R2[r][i]+get2(grid[r][i])
                R5[r][i+1]=R5[r][i]+get5(grid[r][i])
                
        #build col psum
        C2=[[0]*(M+1) for _ in range(N)]
        C5=[[0]*(M+1) for _ in range(N)]
        for c in range(N):
            for i in range(M):
                C2[c][i+1]=C2[c][i]+get2(grid[i][c])
                C5[c][i+1]=C5[c][i]+get5(grid[i][c])
        
        #get all paths
        ans=0
        for r in range(M):
            for c in range(N):
                mid2=get2(grid[r][c])
                mid5=get5(grid[r][c])
                left2=R2[r][c+1]-R2[r][0]
                left5=R5[r][c+1]-R5[r][0]
                right2=R2[r][N]-R2[r][c]
                right5=R5[r][N]-R5[r][c]
                up2=C2[c][r+1]-C2[c][0]
                up5=C5[c][r+1]-C5[c][0]
                down2=C2[c][M]-C2[c][r]
                down5=C5[c][M]-C5[c][r]
                #update ans with 4 combinations
                ans=max(ans,
                        min(left2+up2-mid2,left5+up5-mid5),
                        min(right2+up2-mid2,right5+up5-mid5),
                        min(left2+down2-mid2,left5+down5-mid5),
                        min(right2+down2-mid2,right5+down5-mid5),
                       )

        return ans
```

