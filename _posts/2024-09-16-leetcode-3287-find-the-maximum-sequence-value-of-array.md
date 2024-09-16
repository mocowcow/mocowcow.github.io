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

---

到目前為止都很順利，但難點來了：前綴怎麼算？  
每個元素選或不選，都可能得到相同的 OR 值，有**重疊的子問題**，因此考慮 dp。  

定義 dp[i][j][v] = true/false：在 nums[0..i] 中選 j 個數做 OR，能否湊出 v。  
轉移 dp[i][j][v] = 選或不選 nums[i]：  

- 選： dp[i-1][j-1][old_v] 為 true，且滿足 old_v XOR nums[i] = v  
- 不選： dp[i-1][j][v]

base：當 i < 0 時，只有 j = 0 一種狀態是 true，即**選擇零個**；其餘都是 false。  

光是狀態數就有 N \* k \* MX = 1e7 個。每次轉移來源的 old_v 又有 MX 個，一看就會超時。  
得想想優化的方法。  

---

在求 dp[i][j][v] 的時候，因為 OR 運算只增不少的性質，滿足 old_v XOR nums[i] = v 的 old_v 可能會有好幾個。  
我們是在先前已經求的子問題 dp[i-1] 中，選擇其結果來算出 dp[i]，就像是填答案一樣，叫做**填表法**。  

那對於 dp[i][j][old_v] 來說，他實際上會影響到幾個 dp[i+1] 的結果？  

- 不選 nums[i]：使得 dp[i+1][j][v] 繼續沿用 v = old_v，即 dp[i+1][j][old_v] 為 true  
- 選 nums[i]：使得 dp[i+1][j+1][v XOR nums[i]] 為 true

咦只有兩個喔？那剛才轉移 128 個來源是根本在轉辛酸的。  
這種以當前答案去**更新產生的新狀態**，叫做**刷表法**。  
