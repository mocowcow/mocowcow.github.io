---
layout      : single
title       : LeetCode 2249. Count Lattice Points Inside a Circle
tags 		: LeetCode Medium Math Geometry
---
周賽290。看到題目差點嚇尿，想起某次Q2挖骨董的噩夢，結果還真和那次差不多慘烈，用了錯誤方法吃兩個WA。  
不過這題給python的時間限制好像很短，看到好幾個python大老拿到TLE，很生氣的上去罵官方，剛好我的解法沒有超時而已。

# 題目
輸入二維陣列circles代表好幾個圓，circles[i]代表[x座標, y座標, 圓半徑]，求有多少座標點至少被一個圓形覆蓋住。  
**座標點**是整數座標，且若剛好在圓形邊線上也算被覆蓋住。

# 解法
原本看到半徑1的圓覆蓋了1+3+1個點，而半徑2覆蓋了1+3+5+3+1個點，本來想用這樣去推算那些點會被圓蓋住，有夠難寫還寫錯，後來才想回去用暴力法試試。  

至少這題在邊界處理上很良心，圓形一定完整出現，不會有某部分跑到邊界外。  
題目有說x,y座標最多到100，而半徑最多也是100，推定地圖範圍最大200*200，先開個陣列latt表示該點有沒有被覆蓋住。  
遍歷每個圓，若圓心在(r,c)且半徑為h，至少可以確定圓的最高、最低點為r+h和r-h，而最左、最右點為c-h和c+h，在此範圍內的點只要與圓心距離小於等於h都可以算是被圓覆蓋住，若有覆蓋住則標記為true。  
最後在遍歷整個地圖，計算有多少標為true的點，加總就是答案。

```python
class Solution:
    def countLatticePoints(self, circles: List[List[int]]) -> int:
        
        def dis(r1,c1,r2,c2):
            return math.sqrt((r1-r2)**2+(c1-c2)**2)
        
        latt=[[False]*201 for _ in range(201)]
        for r,c,h in circles:
            for R in range(r-h,r+h+1):
                for C in range(c-h,c+h+1):
                    if dis(r,c,R,C)<=h:
                            latt[R][C]=True
                        
        ans=0
        for r in range(201):
            for c in range(201):
                if latt[r][c]:
                    ans+=1

        return ans
```

