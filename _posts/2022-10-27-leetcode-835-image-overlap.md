--- 
layout      : single
title       : LeetCode 835. Image Overlap
tags        : LeetCode Medium Array Matrix
---
每日題。看描述就感覺這題不妙，去查查rating竟然1900+，還真不簡單。  

# 題目
輸入兩個圖片img1和img2，為大小為n\*n矩陣，值只有0和1。  
你可以將其中一張圖片中所有1元素向四個方向移動任意單位距離，然後放在另一個圖片的上面。  
**重疊量**指的是兩張圖片中同時都為1的座標數量。  

求**最大重疊量**為多少。  

注意：圖片不可進行旋轉，且移動超出矩陣邊界外的1都會消失。  

# 解法
一下子真沒想到什麼好方法，看看測資範圍不大，發現暴力法4迴圈剛好能過。  

我們要移動其中一個矩陣，且移動後兩者還有交集，那麼移動量不得超過矩陣邊長。  
矩陣的最大邊長為N=30，所以水平/垂直移動範圍為[-29:29]。簡單來算有60\*60種移動方式，要移動的矩陣最大為30\*30，大約3240000次計算量，看起來還能接受。  

窮舉所有水平/垂直移動量dx和dy，帶入其中一個圖片後和另外一個對比，統計此移動方式的重疊值後更新答案。  

總共四個迴圈，時間複雜度為O(N^4)。空間只有使用到答案和移動方法重疊值，空間複雜度O(1)。  

```python
class Solution:
    def largestOverlap(self, img1: List[List[int]], img2: List[List[int]]) -> int:
        N=len(img1)
        
        def f(dx,dy):
            cnt=0
            for i in range(N):
                for j in range(N):
                    x=dx+i
                    y=dy+j
                    if 0<=x<N and 0<=y<N and 1==img1[i][j]==img2[x][y]:
                        cnt+=1
            return cnt
        
        ans=0
        for dx in range(-N,N):
            for dy in range(-N,N):
                ans=max(ans,f(dx,dy))

        return ans
```

後來參考別人更合理的做法：先篩選出兩者圖片中為1的座標，分別保存在陣列a和b中。接下來窮舉a和b的組合，計算出兩者間的偏移量(dx,dy)，以雜湊表計數+1。  
最後找到所有偏移量中重疊數最大者即為答案。  

在最差的情況下，兩個圖片中全部都是1，各有N^2個元素，相乘後時間複雜度還是O(N^4)。但因為測資裡面1的數量不多，所以執行時間加速不少。因為使用雜湊表來保存篩選出的1元素座標以及偏移量，故空間複雜度為O(N^2)。  

```python
class Solution:
    def largestOverlap(self, img1: List[List[int]], img2: List[List[int]]) -> int:
        N=len(img1)
        d=defaultdict(int)
        ans=0
        a=[]
        b=[]
        for r in range(N):
            for c in range(N):
                if img1[r][c]:a.append([r,c])
                if img2[r][c]:b.append([r,c])
        
        for x1 in a:
            for x2 in b:
                dx=x1[0]-x2[0]
                dy=x1[1]-x2[1]
                d[(dx,dy)]+=1
                    
        for k,v in d.items():
            ans=max(ans,v)
                    
        return ans
```

附上golang版本，原來struct是可以放進map中的，算是意外小收穫。  

```go
func largestOverlap(img1 [][]int, img2 [][]int) int {
     
    type cood struct{
        x int
        y int
    }
    
    N:=len(img1)
    mp:=make(map[cood]int)
    a:=make([]cood,0)
    b:=make([]cood,0)
    ans:=0
    
    for r:=0;r<N;r++{
        for c:=0;c<N;c++{
            if img1[r][c]==1{a=append(a,cood{r,c})}
            if img2[r][c]==1{b=append(b,cood{r,c})}
        }
    }
    
    for _,co1:=range a{
        for _,co2:=range b{
            dx:=co1.x-co2.x
            dy:=co1.y-co2.y
            mp[cood{dx,dy}]++
        }
    }
    
    for _,v:=range mp{
        ans=max(ans,v)
    }
    
    return ans
}

func max(a,b int)int{
    if a>b{
        return a
    }
    return b
}
```
