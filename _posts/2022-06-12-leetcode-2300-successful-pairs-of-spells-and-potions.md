--- 
layout      : single
title       : LeetCode 2300. Successful Pairs of Spells and Potions
tags        : LeetCode Medium Array BinarySearch Sorting
---
雙周賽80。當時有點傻眼，以前似乎沒有在Q2看過二分搜，總感覺不太對勁。結果陣亡率超高，確實是比往常都難了些。  

# 題目
輸入兩個正整數陣列spell和potion，長度分別為n和m，其中spells[i]代表第i個法術的強度，potions[j]代表第j個藥水的強度。  
另外還有整數success，如果某法術和某藥水的乘積滿足success，則認為這種配對是成功的。  

回傳長度n的整數陣列pairs，其中pairs[i]代表第i個法術成功配對的藥水數量。  

# 解法
假設某個法術需要最少需要搭配強度x的藥水才能達到success，那麼搭配強度大於x的藥水一定也可以成功。  
我們不在乎藥水的使用順序，所以先將potions排序，以便進行二分搜。  

遍歷每個法術，先計算出至少需要強度為x的藥水才能成功，再到potions中找到第一個大於等於x的索引位置idx。  
這代表著有idx個藥水是不符合需求，所以以藥水總數M扣掉idx，即為成功配對的藥水數量，將其加入ans中。  

```python
class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        potions.sort()
        ans=[]
        M=len(potions)
        
        for n in spells:
            x=(success+n-1)//n
            idx=bisect_left(potions,x)
            ans.append(M-idx)
            
        return ans
```

試著用c++來寫，看人家寫多了自己好像也學會一半，或許是時候補上c++了？  

```c++
class Solution {
public:
    vector<int> successfulPairs(vector<int>& sp, vector<int>& po, long long success) {
        vector<int> ans;
        sort(po.begin(),po.end());

        for(int i=0;i<sp.size();i++){
            long long x=(sp[i]+success-1)/sp[i];
            auto it=lower_bound(po.begin(),po.end(),x);
            ans.push_back(po.size()-(it-po.begin()));
        }
        
        return ans;
    }
};
```