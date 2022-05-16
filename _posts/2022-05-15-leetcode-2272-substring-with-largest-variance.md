--- 
layout      : single
title       : LeetCode 2272. Substring With Largest Variance
tags        : LeetCode Hard Array DP
---
雙周賽78。有點像是kadane的變形版，難度算高，比賽當時還真沒想到是dp。  

# 題目
字串的**變異值**指的是字串中出現的任意2字元出現次數的最大差值。兩個字元可能相同也可能不同。  
輸入小寫字串s，回傳s所有子字串中的最大**變異值**。

# 解法
又是霸凌python的一天，同樣的演算法，python會超時，java卻勝過100%提交。難怪都說至少要學兩種語言。  

題目說在某子字串中，找兩個字元出現次數的最大差值，而且兩個字元可以相同。  
但是相同的話差值一定是0，所以只要找枚舉25*26種字元組合就可以。  

枚舉不同的字元a和b，各遍歷一次字串s，如果碰到a則+1，碰到b則-1，問題就簡化成**最大子陣列**了。  
維護變數score代表**最大子陣列的和**，初始為0。  
變數v代表實際的**變異值**，但因為至少要有一個字元b，所以**變異值**要先初始化為-inf，在第一個b出現之後才以score去更新。  

遍歷s中的字元c，當a出現時，子陣列和+1，變異值也+1。  
當b出現時，有兩種可能：  
- 使用新的子陣列，加上當前的b，變異值=子陣列和-1  
- 沿用原本的變異值，變異值-1

因為子陣列已經合併到最大的變異值裡面去了，所以要將子陣列和歸0。  

```java
class Solution {
    public int largestVariance(String s) {
        char[] cs=s.toCharArray();
        int ans=0;
        for(int i=97;i<123;i++){
            for(int j=97;j<123;j++){
                if(i==j)continue;
                char a=(char)i;
                char b=(char)j;
                int score=0;
                int v=-1000000000;
                for(char c:cs){
                    if(c==a){
                        score++;
                        v++;
                    }else if(c==b){
                        v=Math.max(score-1,v-1);
                        score=0;
                    }
                    if(v>ans)ans=v;
                }
            }
        }
        return ans;
    }
}
```
