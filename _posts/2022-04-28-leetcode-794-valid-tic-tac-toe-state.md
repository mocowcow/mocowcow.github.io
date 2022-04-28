--- 
layout      : single
title       : LeetCode 794. Valid Tic-Tac-Toe State
tags        : LeetCode Medium Array String
---
好久好久以前碰過，然後沒想出來的鳥題目，結果這題竟是某次周賽的Q1，非常合理的解釋為什麼這麼多人按爛。  
當次周賽的第二名在這題吃3個WA，猜他八成氣到不行。

# 題目
圈圈叉叉遊戲，X一定先手，之後才輪到O。  
輸入固定長度3的陣列board，board[i]代表第i行，且一定有長度三的字串，由'O','X'和' '所組成。  
判斷board的局勢有沒有可能出現。

# 解法
總之先計算O和X的出現次數，至少我們兩種明顯是不合法的：  
- O不可以比X多  
- X不可能比O多超過一次  

本以為這樣就可以了，送出拿到WA才發現，漏掉一種形況：  
- X連成一直線後，X和O次數一樣多  

好了，修改完後送出，又爆炸一次。這次漏掉：  
- O連成一直線後，X比O還多  

這題我很滿意連線的判斷，透過把三個字串組合成一個，以0~8的索引輕鬆存取位置，並預先建立好8種連線的方式，直接用迴圈同時判斷O或X是否有連線。  
半年前的我肯定是想不到這種寫法，今天算是順利解決掉過去的小麻煩。

```python
class Solution:
    def validTicTacToe(self, board: List[str]) -> bool:
        X=O=0
        board=''.join(board)
        for c in board:
            if c=='X':
                X+=1
            elif c=='O':
                O+=1
        
        if O>X:
            return False
        if X-O>1:
            return False
        
        comb=[(0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6)]
        for a,b,c in comb:
            if board[a]==board[b]==board[c]=='X':
                if X==O:
                    return False
            elif board[a]==board[b]==board[c]=='O':
                if X>O:
                    return False
        
        return True
```
