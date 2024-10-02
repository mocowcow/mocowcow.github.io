---
layout      : single
title       : LeetCode 3303. Find the Occurrence of First Almost Equal Substring
tags        : LeetCode Hard
---
biweekly contest 140。  
我搞了半天的 rolling hash 竟然被卡常數，真搞不懂時間限制的標準。  

## 題目

輸入兩個字串 s 和 pattern。  

若一個字串 x 在修改**至多一個**字元後等同於字串 y，則稱 x 和 y **幾乎相等**。  

回傳**最小**的 s 的子字串起始索引，其子字串與 pattern **幾乎相等**。  
若不存在則回傳 -1。  

## 解法

修改 pattern **至多一個**字元，可能的結果有 pattern 本身，或是任意 pattern[i] 修改成任意字母。  
總共 26 \* N = 2e6 種可能。  

透過 rolling hash 將所有可能的子字串加入集合中，最後再枚舉 s 中的子字串，第一個找到的就是答案。  
可惜會超時，只能想想別的辦法。  

---

Q3 的時候是求**子序列**，我們利用了**前後綴分解**的技巧找到分割點，使得左右兩邊的匹配長度至少等於 N-1。  
雖然本題 Q4 是求**子字串**，但同樣也適用**前後綴分解**的思維。  

設一個子字串 sub = s[i..j] 幾乎相等於 pattern。  
那麼兩者肯定具有**公用前綴** pref = sub[i..] 還有**公共後綴** suff = sub[..j]，並有 len(pref) + len(suff) >= N-1。  

---

問題轉換成：找 sub 和 pattern 的**公共前綴**與**公共後綴**。  
以前周賽中也碰過不少次，正是 z-function。  

但是原始的 z-function 是在字串 s 本身找子字串 s[i..] 的**最長公共前綴**。  
此處是要在 s 裡找 pattern，所以需要將兩者串接為 pattern + "#" +s。  
其中 "#" 號是只是分隔習慣，不加也可以。  
