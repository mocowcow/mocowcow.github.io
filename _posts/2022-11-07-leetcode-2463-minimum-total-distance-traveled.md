--- 
layout      : single
title       : LeetCode 2463. Minimum Total Distance Traveled
tags        : LeetCode Hard Array Greedy DP Sorting
---
周賽318。比賽時只想到是貪心，一直想著鄰項交換法，沒發現更重要的dp要素。  

# 題目
X軸上有一些機器人和工廠。輸入一個整數陣列robot，其中robot[i]是第i個機器人的位置。還有一個二維整數陣列factory，其中factory[j] = [position<sub>j</sub>, limit<sub>j</sub>]，表示第j個工廠的位於position<sub>j</sub>，且最多可修復limit<sub>j</sub>個機器人。  

每個機器人的位置都是獨一無二的；每個工廠的位置也各不相同。注意，機器人和工廠的初始位置可以相同。  

所有的機器人一開始都是壞的，只會朝著同個X軸的正向或反向前進。當機器人抵達未滿的工廠時，工廠會修理該機器人，使其停止移動。  

你可以**隨時**改變任意機器人的行進方向，使得所有機器人的總移動距離最小化。  

求所有機器人**移動的最小總距離**。測試資料保證所有機器人都可以被修復。  

注意：  
- 所有機器人移動速度相同  
- 如果兩個機器人朝同方向移動，則兩者永遠不會發生碰撞  
- 如果兩個機器人朝反方向移動且在某個點相遇，也不會發生碰撞，可以順利穿越  
- 如果一個機器人經過一個抵達已滿的工廠，則不會進行修理，會直接路過  
- 如果機器人從位置x移動到位置y，其移動的距離為|y - x|  

# 解法
最下面那串注意事項幾乎都是廢話，感覺沒什麼重點。反正就是一直走到有空位才會停。  

鄰項交換法的重點大概是：  
> 有依序的座標 x1 x2 y1 y2 
> 要將兩個x和兩個y配對 
> |x1-y1|+|x2-y2| = |x1-y2|+|x2-y1| . 
> 兩者距離一樣，所以照著相對次序配對為最佳解  

因此**每個工廠修理的機器人都會是連續的**。將robot和factory排序後，問題簡化為第i個工廠要接著修理多少機器人。  

定義dp(i,j,k)：在第j個工廠，修理第i個機器人，且在這之前此工廠已經修理過k個。  
轉移方程式：如果還有修理次數，則第i個機器人可以在工廠j修；否則只能到下一個工廠修。dp(i,j,k)=min(dp(下一個工廠),dp(此工廠修理+1)+機器人到工廠距離)
base cases：如果i等於機器人總數，代表全部修理完成，不會再有任何移動，回傳0；如果j等於工廠總數，代表沒工廠可以修了，但機器人還沒修完，回傳inf令此結果不被使用。  

時空間複雜度皆為O(NMK)，其中N為機器人總數，M為工廠總數，K為工廠修理次數上限。  

```python
class Solution:
    def minimumTotalDistance(self, robot: List[int], factory: List[List[int]]) -> int:
        robot.sort()
        factory.sort()
        N=len(robot)
        M=len(factory)
        
        @cache
        def dp(i,j,k):
            if i==N:return 0
            if j==M:return inf
            best=dp(i,j+1,0)
            if factory[j][1]>k:
                best=min(best,abs(robot[i]-factory[j][0])+dp(i+1,j,k+1))
            return best
    
        return dp(0,0,0)
        
        
```

三維DP看起來很可怕，轉移起來也很麻煩。可以把位於x且有y次修理機會的工廠變成y個位於x的工廠，將factory陣列攤平。  
每個工廠修理次數都剩下1次，轉移方程式就只要考慮修或不修就好。  

理論上時空間複雜度都一樣，就不知道為什麼會噴MLE：
> 40 / 40 test cases passed, but took too much memory.  

但是回傳答案之前把cache清空就沒事了，真是神奇。  

```python
class Solution:
    def minimumTotalDistance(self, robot: List[int], factory: List[List[int]]) -> int:
        robot.sort()
        factory.sort()
        f=[]
        for a,b in factory:
            f+=[a]*b
            
        N=len(robot)
        M=len(f)
        
        @cache
        def dp(i,j):
            if i==N:return 0
            if j==M:return inf
            return min(dp(i,j+1),abs(robot[i]-f[j])+dp(i+1,j+1))
        
        ans=dp(0,0)
        dp.cache_clear() # important
        
        return ans
```
        
自己手動做記憶化也可以通過，真的搞不懂這個cache有什麼魔法。  

```python
class Solution:
    def minimumTotalDistance(self, robot: List[int], factory: List[List[int]]) -> int:
        robot.sort()
        factory.sort()
        f=[]
        for a,b in factory:
            f+=[a]*b
            
        N=len(robot)
        M=len(f)
        memo=[[None]*M for _ in range(N)]
        
        def dp(i,j):
            if i==N:return 0
            if j==M:return inf
            if memo[i][j]==None:
                memo[i][j]=min(dp(i,j+1),abs(robot[i]-f[j])+dp(i+1,j+1))
            return memo[i][j]
        
        return dp(0,0)
```