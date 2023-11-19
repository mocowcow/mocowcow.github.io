---
layout      : single
title       : LeetCode 2937. Make Three Strings Equal
tags        : LeetCode Easy String Greedy
---
周賽372。很可惡的Q1，我直接在這邊領了三個WA，心態崩潰。  

## 題目

輸入三個字串s1, s2和s3。你可以對字串執行任意次操作。  

每次操作，可以選擇任意一個長度至少2的字串，並刪除最右方的字元。  

求**最少**需要幾次操作，才能使得三個字串相等。若不可能相等，則回傳-1。  

## 解法

這三個字串長度不一定相同，本來還想著先把他們弄到齊頭，然後再來判斷，寫起來超級麻煩。  

後來仔細想想，其實題目要求的只是三者的共通前綴，只要從頭開始比對即可。  
三字串長度加總扣掉共通前綴長度\*3就是答案。  
若前綴長度只有1，則不合法，回傳-1。  

時間複雜度O(N)。  
空間複雜度O(1)。  

```python
class Solution:
    def findMinimumOperations(self, s1: str, s2: str, s3: str) -> int:
        N=min(len(x) for x in [s1,s2,s3])
        tot=sum(len(x) for x in [s1,s2,s3])
        i=-1
        while i+1<N and s1[i+1]==s2[i+1]==s3[i+1]:
            i+=1
        
        if i==-1:
            return -1
            
        return tot-(i+1)*3
```

zip函數的輸出長度是取決於最短的輸入，無法成對的部分會被丟棄，剛好適用本題。  
看來是我python不夠流暢。  

```python
class Solution:
    def findMinimumOperations(self, s1: str, s2: str, s3: str) -> int:
        tot=sum(len(x) for x in [s1,s2,s3])
        i=-1
        for a,b,c in zip(s1,s2,s3):
            if a!=b or b!=c:
                break
            i+=1
        
        if i==-1:
            return -1
            
        return tot-(i+1)*3
```
