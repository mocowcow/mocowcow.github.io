--- 
layout      : single
title       : LeetCode 2353. Design a Food Rating System
tags        : LeetCode Medium Array Design SortedList HashTable
---
周賽303。這題和雙周賽83的[2349. design a number container system]({% post_url 2022-07-24-leetcode-2349-design-a-number-container-system %})幾乎是一樣的東西，我願稱本周為**week of sorted list**。  

# 題目
設計一個可以執行以下操作的食物評分系統：  
- 修改系統中的食物評分  
- 回傳系統中某類菜系的分數最高的食物  

實作類別FoodRatings：  
- FoodRatings(String[] foods, String[] Cuisines, int[] rating)：三個鎮列長度都是n，分別代表第i種食物的名稱、菜系和分數  
- void changeRating(String food, int newRating)：將food的分數改為newRating  
- String highestRated(String cuisine)：回傳cuisine菜系中分數最高的食物名稱。若有多者分數相同，則回傳字典順序最小者  

# 解法
或許是因為食物要先以**分數遞減**，再以**名稱遞增**做排序，把不少人的腦子搞糊塗。其實只要對key值加上負號，就可以簡單的改變為遞增/遞減。  

食物的菜系不會改變，直接以一個雜湊表type以食物名稱映射到正確的菜系分類。另外雜湊表mp映射食物的評分。最後雜湊表d以sorted list維護各項菜系的最佳食物。  

就如先前提到的，原本的sorted list預設是遞增排序，我們想要改成對**分數遞增**，所以將評分設為負數，組成(-分數, 食物名)的格式，再放入對應的菜系list中。如此一來，list中個第一個元素會是該菜系中**分數最高**且**字典順序最小**的食物。  

既然各菜系已經排序好，highestRated函數就只要回傳指定菜系中第一個食物就好，複雜度O(1)。  
changeRating比較麻煩一些，必須先至mp找到食物原本的評分，於對應list中刪除，之後再插入新的評分，複雜度O(log N)。  

```python
from sortedcontainers import SortedList

class FoodRatings:

    def __init__(self, foods: List[str], cuisines: List[str], ratings: List[int]):
        self.type={}
        self.mp={}
        self.d=defaultdict(SortedList)
        for f,c,r in zip(foods,cuisines,ratings):
            self.type[f]=c
            self.mp[f]=-r
            self.d[c].add([-r,f])

    def changeRating(self, food: str, newRating: int) -> None:
        c=self.type[food]
        # remove old rating
        oldRating=self.mp[food]
        rmv=[oldRating,food]
        self.d[c].remove(rmv)
        # insert new rating
        self.mp[food]=-newRating
        self.d[c].add([-newRating,food])

    def highestRated(self, cuisine: str) -> str:
        return self.d[cuisine][0][1]
```
