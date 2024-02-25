---
layout      : single
title       : LeetCode 3047. Find the Largest Area of Square Inside Two Rectangles
tags        : LeetCode Medium Array Matrix
---
周賽386。我真的是被這題搞死了，寫半天還錯好多次，剩下時間還不夠做 Q3。應該會破最低名次紀錄，最近幾場周賽打的分全沒了。  
上次 [3027. find the number of ways to place people ii]({% post_url 2024-02-04-leetcode-3027-find-the-number-of-ways-to-place-people-ii %}) 也是，看來我的腦子碰到座標系相關的題都會大爆炸。  

## 題目

2D 平面上有 n 個矩形。  
輸入長度為 n\*2 的二維整數陣列 bottomLeft 和 topRight，其中 bottomLeft[i] 代表矩形的**左下**座標，而 topRight[i] 代表**右上**座標。  

你可以在任意兩個矩形的**交集區域**中選擇一個**正方形區域**。  

求可以選擇的**最大**正方形面積，若不存在任何交集則回傳 0。  

## 解法

本題麻煩的點在於變數太多，要同時枚舉兩個整正方形，每個正方形有兩個座標，每個座標又有兩個維度，同時存在高達 8 個變數。  
直接取用輸入測資很容易眼瞎，建議在枚舉的同時**重新命名變數**，或是**封裝**成物件/結構體，對於可讀性有很大的幫助。  

再來是，兩個矩形的相對關係有非常多種，不只是單純的上下左右，還有完全包含，以及十字型交集等。  
原本想排序，但只能保證 x軸有序，要另外判斷 y軸。  
又自己透過交換保證 y軸大小後，又沒辦法處理完全包含的情況，非常麻煩。  

然後輸入變數的名稱也很臭長，建議自己改短成 bl 和 rt 之類的。  

---

**交集區域**是由兩個維度組成，相當於 **x軸交集**和 **y軸交集**的乘積。分開求兩項東西就簡單很多：  

- get_width(A, B)：求兩矩形的 x軸交集  
- get_height(A, B)：求兩矩形的 y軸交集  

到目前為止，分類討論已經簡單了很多。  
設矩形座標分別為 (x1, y1), (x2, y2)，並限制 A.x1 <= B.x1。  
試著求 x軸交集：  

- 因 A.x1 <= B.x1，交集左邊界最小只能到 B.x1  
- 但是 A.x2 和 B.x2 不保證大小關係，則兩者都可能是右邊界，取**較小值** min(A.x2, B.x2)  
- 若 A.x1 < A.x2 < B.x1 < B.x2，兩者**無交集**，交集長度為 0  

求 y軸交集同理。  

---

最後只要枚舉所有數對，以交集面積更新答案即可。  
注意：答案要求的是**正方形面積**，因此求出來的交集只能取等長部分，也就是 min(width, height)。  

時間複雜度 O(N^2)。  
空間複雜度 O(N)，原地計算可達 O(1)。  

```python
class Solution:
    def largestSquareArea(self, bottomLeft: List[List[int]], topRight: List[List[int]]) -> int:
        N = len(bottomLeft)
        rect = [Rect(p1[0],p1[1],p2[0],p2[1]) for p1, p2 in zip(bottomLeft, topRight)]
        
        ans = 0
        for i, A in enumerate(rect):
            for B in rect[:i]:
                w = get_width(A, B)
                h = get_height(A, B)
                ans = max(ans, min(w, h))
    
        return ans ** 2
    
class Rect:
    def __init__(self, x1, y1, x2, y2):
        self.x1=x1
        self.x2=x2
        self.y1=y1
        self.y2=y2
        
def get_width(A, B):
    if A.x1 > B.x1:
        return get_width(B, A)
    if A.x2 < B.x1:
        return 0
    return min(A.x2, B.x2) - B.x1
    
def get_height(A, B): 
    if A.y1 > B.y1:
        return get_height(B, A)
    if A.y2 < B.y1:
        return 0
    return min(A.y2, B.y2) - B.y1
```

其實我在比賽中，求交集的方法更簡潔，不必判斷兩點的相對關係。  

同樣以求 x軸交集為例。  
總共有四個點 A.x1, A.x2, B.x1, B.x2，若有交集，則必定符合以下條件：  

- 交集左邊界最小為 max(A1.x1, B.x1)  
- 交集右邊界最大為 min(A1.x2, B.x2)  

所以交集長度是 min(A1.x2, B.x2) - max(A1.x1, B.x1)。  

那沒交集的話呢？  
> A.x1 < A.x2 < B.x1 < B.x2  
> 假設值為 1 < 2 < 3 < 4
> = min(2, 4) - max(1, 3)  
> = 2 - 3 = -1

會得到負值，因此再和 0 取個最大值即可。  

---

雖然說 python 很多語法都很方便，這時候就碰到小缺點。  
就是因為太過方便，所以內建函數其實做了很多事情，會比想像中還要慢，**慢到在比賽中吃了 TLE**。  

以 min/max 為例，他會先判斷傳入的 args tuple 大小，若只有 1 個參數且是可疊代的，則將其解包。之後才開始用指定的 key 去比較元素。  

雖然行數不是判斷演算法效率的，但還是想說他在 cpython 原碼裡面超過 100 行，光看都怕。  
如果需要大量使用到 min/max，不妨自己複寫函數，或是自己用 if 判斷，會跑得快很多。  

```python
def get_width(A, B):
    return max(0, min(A.x2, B.x2) - max(A.x1, B.x1))
    
def get_height(A, B): 
    return max(0, min(A.y2, B.y2) - max(A.y1, B.y1))

# override min/max
min = lambda x, y:  x if x < y else y 
max = lambda x, y:  x if x > y else y
```

寫成 O(1) 空間濃縮版本就是這樣，反正我是覺得可讀性很差。  
~~至少我沒辦法一次性寫成這樣~~。  

```python
class Solution:
    def largestSquareArea(self, bl: List[List[int]], tr: List[List[int]]) -> int:
        N = len(bl)
        ans = 0
        for i in range(N):
            for j in range(i):
                w = min(tr[i][0], tr[j][0]) - max(bl[i][0], bl[j][0])
                h = min(tr[i][1], tr[j][1]) - max(bl[i][1], bl[j][1])
                ans = max(ans, min(w, h))
    
        return ans ** 2
```
