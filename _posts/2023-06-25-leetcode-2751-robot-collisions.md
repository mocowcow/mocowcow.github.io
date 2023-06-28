--- 
layout      : single
title       : LeetCode 2751. Robot Collisions
tags        : LeetCode Hard Array Stack Sorting Simulation
---
周賽351。有點像是[2731. movement of robots]({% post_url 2023-06-11-leetcode-2731-movement-of-robots %})，當初浪費一堆時間做的模擬解竟然在今天得到回報。  
然後我還想到[735. Asteroid Collision]這題，基本上是一樣的東西。  

# 題目
有n個機器人，每個都站在直線上的不同位置，且分別擁有血量和移動方向。  

輸入整數陣列positions和healths，還有由"L"和"R"組成的字串derections。positions中的每個數字都是獨特的。  

所有機器人會**同時**且依照**相同速度**朝著設定的方向移動。如果兩個機器人移動到相同位置則會發生**碰撞**。  

若兩個機器人**碰撞**，**血量較低者**會消失；**血量較高者**會損失1點血量，並維持同方向繼續移動；若兩者血量**相同**，則兩者都會消失。  

你必須找到所有存活的機器人的剩餘血量，並依照原本輸入的編號順序排列。若無存活的機器人則回傳空陣列。  

等所有碰撞結束後，回傳代表所有存活機器人血量的陣列(按編號順序)。  

注意：positions可能是無序的。  

# 解法
這題還算有良心，沒有搞什麼同方向穿越的設計，只要有兩個面對面的機器人就**一定有碰撞**。  

先將機器人將起始位置排序，先分類討論幾種情況：  
1. 如果有L，左邊為空，或全都是L，那不會發生碰撞  
2. 如果有L，左邊一位正好為R，兩者會撞，撞贏的活下來繼續走  
3. 如果有R，右邊為空，或全都是R，那不會發生碰撞  
4. 如果有R，右邊一位正好為L，兩者會撞，撞贏的活下來繼續走  

從左到右依序處理機器人，碰到R的時候，先把它保存起來；碰到L的時候，再來找找左方有沒有活著的R可以撞。  
假設在位置i有L，要往i-1, i-2,..找R，剛好是後進先出的模式，所以可以使用stack保存R機器人。  
而遍歷到L機器人時，有可能跟R撞贏了，還可以繼續走，所以使用雙向隊列deque保存排序過的機器人。  

在上述第1點，這些L都不可能有碰撞，直接輸出到safe陣列裡面，待之後計算答案。  
同理，在處理完所有機器人之後，st中可能還有一些活著的R，也通通合併到safe裡面去。  
最後將活著的機器人safe按照id排序，把所有血量拿出來就是答案。  

每次碰撞一定會少一個機器人，處理碰撞複雜度為O(N)。  
瓶頸在於排序，時間複雜度O(N log N)。  
空間複雜度O(N)。  

```python
class Solution:
    def survivedRobotsHealths(self, positions: List[int], healths: List[int], directions: str) -> List[int]:
        bots=[[p,h,d,id] for p,h,d,id in zip(positions,healths,directions,range(1,len(positions)+1))]
        bots.sort()
        q=deque(bots) # pending bots
        st=[] # "R" bots waiting for collide
        live=[] # bots that will not collide anymore
        
        while q:
            p,h,d,id=q.popleft()
            if d=="L":
                if not st: # no "R" at left side
                    live.append([p,h,d,id])
                else:
                    left_h=st[-1][1]
                    if left_h==h: # both die
                        st.pop()
                    elif left_h>h: # R die
                        st[-1][1]-=1
                    else: # L die
                        st.pop()
                        h-=1
                        q.appendleft([p,h,d,id])
                
            else: # "R"
                st.append([p,h,d,id])
                
        live+=st
        live.sort(key=itemgetter(3))        
        
        return [x[1] for x in live]
```

改成只排序機器人編號，直接在原本的輸入做修改，順便修改一下排版，邏輯應該更加清楚。  

```python
class Solution:
    def survivedRobotsHealths(self, positions: List[int], healths: List[int], directions: str) -> List[int]:
        N=len(positions)
        bots=sorted(range(N),key=lambda x:positions[x])
        
        st=[] # keep "R"
        live=[] # keep "L"
        for i in bots: # iterative over sorted bots
            if directions[i]=="R":
                st.append(i)
                continue
                
            # "L"
            while st and healths[i]>0:
                if healths[st[-1]]>healths[i]:
                    healths[st[-1]]-=1
                    healths[i]=0
                elif healths[st[-1]]<healths[i]:
                    st.pop()
                    healths[i]-=1
                else:
                    st.pop()
                    healths[i]=0
                    
            # if "L" alive
            if healths[i]>0:
                live.append(i)
                    
        live+=st
        live.sort()
        
        return [healths[x] for x in live]
```