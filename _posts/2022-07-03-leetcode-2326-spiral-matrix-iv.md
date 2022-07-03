--- 
layout      : single
title       : LeetCode 2326. Spiral Matrix IV
tags        : LeetCode Medium Array Matrix LinkedList Simulation
---
周賽300。看到Spiral Matrix就想說完蛋，這系列都很麻煩，結果還真的卡了我十分鐘debug。

# 題目
輸入整數m和n，代表m*n的矩陣，還有linked list的首節點head。  
你必須從矩陣的左上角出發，依順時針的方向螺旋遍歷矩陣，並將linked list中的整數依序填入。  
若有剩餘的空格，則以-1填充。  

# 解法
一開始先將矩陣以-1初始化，這樣head中的元素處理完後才不用慢慢填充，省下一堆判斷。  
DIRS裝的分別是右下左上，四個方向，並以變數i指向當前的移動方向。  
第一點恆為(0,0)，且由左向右，故出發點初始為(0,-1)。  

重複以下動作直到head遍歷完為止：  
1. 依照當前移動方向DIRS[i]求出移動後的位置(rr,cc)  
2. 若(rr,cc)超出邊界，或是已經填充過，則改變移動方向，回到步驟1  
3. 將(rr,cc)填入head.val，並將head指向下一個節點  
4. 更新當前位置(r,c)為(rr,cc)  

```python
class Solution:
    def spiralMatrix(self, m: int, n: int, head: Optional[ListNode]) -> List[List[int]]:
        mat=[[-1]*n for _ in range(m)]
        DIRS=[[0,1],[1,0],[0,-1],[-1,0]]
        i=0
        r=0
        c=-1
        
        while head:
            dx,dy=DIRS[i]
            rr,cc=r+dx,c+dy
            if not(0<=rr<m and 0<=cc<n) or mat[rr][cc]!=-1:
                i=(i+1)%4
                continue
            mat[rr][cc]=head.val
            head=head.next
            r=rr
            c=cc

        return mat
```
