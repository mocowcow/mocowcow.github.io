---
layout      : single
title       : LeetCode 2211. Count Collisions on a Road
tags 		: LeetCode Medium Array Greedy
---
周賽285。本來想說終於有stack了，結果測試的時候發現不太對，果斷換方法。

# 題目代表
字串directions中只會出現"LRS"三種字母，分別代表車子向左開、向右開，以及靜止狀態。  
每台移動中的車速度都相同。依照以下規則計算碰撞數：  
- 當兩台方向相反的車相撞，則碰撞數+2  
- 若某台移動中的車撞到靜止的車，則碰撞數+1  
- 每次碰撞後，相撞的車**都會變成靜止**  

# 解法
移動中的車一定要碰到靜止車，或是逆向來車才會碰撞。  
遍歷directions，分別對三種情形處理：  
- 碰到R時，變數r+1，表示向右開著車數，留著等遇到障礙再併入答案  
- 碰到S時，不管，因為不會增加碰撞數
- 碰到L時，若左方有東西可以撞，則碰撞數增加r+1，再把r歸零  

重點在於如何知道左向來車有沒有東西會讓他撞到？  
我們需要多一個布林變數lbound來表示左邊障礙物。  
lbound初始為false，只要有遇到S或是R，就代表之後出現的左向來車有得撞了，lbound設為true。  
如此一來，像是"LLLLRL"這種就可以正確計算。

```python
class Solution:
    def countCollisions(self, directions: str) -> int:
        ans=0
        r=0
        lbound=False
    
        for d in directions:
            if d=='R':
                r+=1
                lbound=True
            elif d=='S':
                ans+=r
                r=0
                lbound=True
            elif lbound:
                ans+=r+1
                r=0
                    
        return ans
```

