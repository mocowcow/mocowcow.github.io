---
layout      : single
title       : LeetCode 3283. Maximum Number of Moves to Kill All Pawns
tags        : LeetCode Hard
---
weekly contest 414。  

## 題目

有個 50 x 50 的棋盤，上方有一個**馬**和一些**兵**。  
輸入兩個整數 kx, ky，其中 (kx, ky) 代表馬的位置。  
還有二維整數陣列 positions，其中 positions[i] = [x<sub>i</sub>, y<sub>i</sub>] 代表兵的位置。  

Alice 和 Bob 在玩一種回合制遊戲，由 Alice 先。每回合：  

- 玩家控制馬，並吃掉還存在棋盤上的任意一個兵，且**不能繞遠路**。  
    注意：可以選擇**任何**兵，不一定要選距離馬最近的兵。  
- 馬在移動的過程，**可能**會碰到其他兵，但他們**不會被吃掉**。在本回合內只有被選中的兵會被吃。  

Alice 希望使得兩人的**總移動次數最大化**，而 Bob 則希望**最小化**。  

求兩者都選擇**最佳策略**的情況下，Alice 可以達到的**最大總移動次數**。  

注意：馬有 8 種移動方向，都是朝某個方向前進 1 格，然後再朝垂直的方向前進 1 格。  

## 解法
