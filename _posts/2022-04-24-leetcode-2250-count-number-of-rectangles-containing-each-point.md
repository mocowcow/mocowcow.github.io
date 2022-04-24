---
layout      : single
title       : LeetCode 2250. Count Number of Rectangles Containing Each Point
tags 		: LeetCode Medium Array Math Geometry Sorting BinarySearch
---
周賽290。這題難度大概也接近hard了，難點在於測資大小的分析，實作起來並不會太複雜。

# 題目
輸入二維陣列rectangles代表各長方形的寬和高，二維陣列points代表好幾個座標點。  
每個長方形i的左下角座標都在(0,0)，而右上角座標為rectangles[i]。  
求每個點points[i]被多少長方形覆蓋住。若點在某長方形的邊上，也算是被覆蓋住。
> Input: rectangles = [[1,2],[2,3],[2,5]], points = [[2,1],[1,4]]  
> 點(2,1)被長方形(2,3),(2,5)覆蓋  
> 點(1,4)被長方形(2,5)覆蓋  
> 答案為[2,1]

# 解法
乍看之下沒什麼可以偷工減料的地方，因為某個點要被正方形覆蓋的話，一定要長寬都足夠大，只靠排序沒辦法簡單做到。  
測資寫到x<=10^9，但是y<=100，就覺得是很明顯的提示，要我們以高度將長方形分組，之後以二分搜檢查每個高度，這樣最多只要100*(log 5*10^4)而已，還算可以接受。  

遍歷所有長方形(l,h)，先以高度h分組，將寬度l加入雜湊表中。將所有有效的高度排序存為ks，也將所有高度的組別排序。  
處理完後，雜湊表d應會是照著高低出現，然後每個高度h的長方形寬度依序列出，例：  
> rectangles = [[1,1],[2,2],[3,3],[3,5],[1,2]]  
> 排序好的高度ks = [1,2,3,5]   
> 高度為1的長方形寬度 = [1]  
> 高度為2的長方形寬度 = [1,2]  
> 高度為3的長方形寬度 = [3]  
> 高度為5的長方形寬度 = [3]  

之後對於每個點(x,y)，只要在雜湊表中對大於等於y的高度k做二分搜，找到每個k有多少寬度大於等於x的長方形。  
延續上面的例子，若要找點(1,2)被多少長方形覆蓋：  
> 只要找高度大於等於2的長方形  
> 高度為2，且寬度大於等於1的有[1,2]  
> 高度為3，且寬度大於等於1的有[3]  
> 高度為5，且寬度大於等於1的有[3]  
> 答案應為4  

最後解釋一下，對每個d[k]找第一個大於等於x的索引位置i，d[k]大小為N，則i~N-1都是大於x的長方形，故數量為N-i。

```python
class Solution:
    def countRectangles(self, rectangles: List[List[int]], points: List[List[int]]) -> List[int]:
        N=len(rectangles)
        d=defaultdict(list) # group by height
        for l,h in rectangles:
            d[h].append(l)
            
        for k in d:
            d[k]=sorted(d[k])

        ks=sorted(d.keys())
        ans=[]
        for x,y in points:
            cnt=0
            for k in ks:
                if k<y:
                    continue
                cnt+=len(d[k])-(bisect_left(d[k],x))
            ans.append(cnt)
            
        return ans
```

