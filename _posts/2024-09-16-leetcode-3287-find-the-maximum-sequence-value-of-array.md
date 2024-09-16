---
layout      : single
title       : LeetCode 3287. Find the Maximum Sequence Value of Array
tags        : LeetCode Hard
---
biweekly contest 139。  

## 題目  

輸入整數陣列 nums 還有正整數 k。  

一個長度為 2 \* x 的子序列 seq 的**值**為：  

- (seq[0] OR seq[1] OR ... OR seq[x - 1]) XOR (seq[x] OR seq[x + 1] OR ... OR seq[2 \* x - 1])。  

求 nums 中所有長度為 2 \* k 的子序列的**最大值**。  

## 解法

簡單說就是選 2k 個數，切成兩半，兩半各 k 個元素相互做 OR 後，再把兩個 OR 結果做 XOR。  
XOR 運算具有**倆倆相消**的特性，若貪心地讓兩半的 OR 結果盡可能大，反而可能會使得 XOR 變小，因此貪心不可行。  

---

觀察測資範圍，發現 nums[i] 上限不超過 MX = 2^7。也就是說 OR 結果只有 128 種。  
測資範圍小一定有他的道理，暗示著我們可以枚舉**左右的 OR 結果**，共 128 \* 128 = 16384 種，看起來還好。  

說要將 seq 切成兩半，那中間必定有**分割點**。最多 N = 400 個元素，先枚舉中心點再枚舉左右 OR 值。  
複雜度 O(N \* MX^2)，大約 6e6 計算量，答案的雛型已經完成了。  

我們可以先枚舉所有索引 i 做為分割點，維護前綴 pref[i][j] 代表 nums[0..i] 任選 j 個元素可以得到的 OR 值；  
還有後綴 suff[i][j] 代表 nums[i..N-1] 任選 j 個元素可以得到的 OR 值。  
之後再枚舉中心點 i，再枚舉左右的 OR 值 v1, v2。若存在合法的 pref[i][k][v1] 和 suff[i+1][k][v2]，則以 v1 XOR v2 更新答案。  

這個技巧叫做**前後綴分解**。  
