---
layout      : single
title       : LeetCode 2207. Maximize Number of Subsequences in a String
tags 		: LeetCode Medium Array Greedy Math
---
雙周賽74。吃了四次WA，上次周賽的累加公式a*(a+1)/2意外派上用場，用心檢討是有回報的。  

# 題目
輸入字串text及pattern，且pattern長度固定為2，在text裡面找等於pattern的子序列。  
你可以text的任意位置插入pattern的其中一個字母，試將子序列出現次數最大化，並回傳最大出現次數。  

# 解法
pattern固定由兩個字元組成，以下稱為c1, c2。  
第一個想法是：對每個c1，查看右邊還有多少c2可以和他組成子序列。  
因此先計算c2的出現次數cnt2，再從左邊往右掃，每次碰到c1就加上cnt2；碰到c2就將cnt2扣掉1。  

但是題目說可以在某個地方插入c1或c2，這要怎麼搞？  
想要增加子序列的方式有兩種：  
1. 插入c1，與現存的c2們組成子序列  
2. 插入c2，與現存的c1們組成子序列  

想要最大化次數，方法1則要將c1插入在所有c2左方，而方法2要將c2插入在所有c1右方。  
那麼就可以推導出：  
1. 在左方插入c1後，子序列增加(c2出現次數)個
2. 在右方插入c2後，子序列增加(c1出現次數)個  

由c1和c2出現次數高者

然而問題還沒解決，撞上奇怪的edge case，當c1=c2時這算法就不合用了。  
> text = "fw**y**mvreuftzgrcrxczjacqovduqaiig", pattern = "yy"  

裡面只有一個y，要求子序列"yy"次數，照理說把y加在哪都一樣，正確答案為1，可是上面方法會算成2。  
只好手動推算，"y"時答案為1，"yy"時答案為1+2，"yyy"時答案為1+2+3，這不就是累加數列嗎！  
當c1=c2時，直接公式解結束。  

竟然贏過100%提交，真是歡樂。  
![執行時間](/assets/img/lc2207.jpg)

```python
class Solution:
    def maximumSubsequenceCount(self, text: str, pattern: str) -> int:
        c1,c2=pattern
        if c1==c2:
            a=text.count(c1)
            return a*(a+1)//2
        
        c1_freq=0
        c2_freq=c2_remain=text.count(c2)
        sub=0
        
        for c in text:
            if c==c1:
                c1_freq+=1
                sub+=c2_remain
            elif c==c2:
                c2_remain-=1
                
        return max(c1_freq,c2_freq)+sub
```

