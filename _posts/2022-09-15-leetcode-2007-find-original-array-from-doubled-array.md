--- 
layout      : single
title       : LeetCode 2007. Find Original Array From Doubled Array
tags        : LeetCode Medium Array HashTable Greedy Sorting
---
每日題。跟我電波不太合，如果比賽碰到這題八成會氣死。  

# 題目
某個整數陣列original可以將所有元素變成兩倍，然後隨機排序，成為一個**雙倍陣列**。  
輸入一個陣列changed，如果改變是一個**雙倍陣列**，則回傳其original陣列；若非，則回傳空陣列。  
original陣列可以依任何順序回傳。  

# 解法
既然是雙倍陣列，那麼長度一定是偶數，碰到奇數長度直接不處理。  
為了方便處理，先將changed排序，統計各元素的出現次數，稍後來進行配對。  

遍歷排序好的陣列中每個元素n，如果所有n都配對完成，則不處理；若找不到可用n\*2進行配對，則代表無法回推成original，直接回傳空陣列；否則將配對成功的n和n\*2計數各減1，並加入答案中。  

最後回傳答案。時間複雜度主要為排序O(N log N)，空間複雜度(N)。  

如果沒有排序的話，碰上[2,4,8,1]這種測資會使得[2,4]先配對，誤以為無法還原。  
又如果沒有過濾奇數陣列的話，碰到[0]這種又要特別處理，因為n和n\*2都會指到0，共用產生錯誤判斷。  

```python
class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        changed.sort()
        d=Counter(changed)
        ans=[]
        
        if len(changed)&1:
            return []
        
        for n in changed:
            if d[n]==0:
                continue
            if d[n*2]==0:
                return []
            ans.append(n)
            d[n]-=1
            d[n*2]-=1     
            
        return ans
```

看到別人的方法比較好，雖然同樣需要排序，但不必特別處理奇數長度。  

這次雜湊表改成紀錄某個元素的所需數量，若每個數n沒有被前方的n/2預訂，則使n和n\*2配對，並紀錄預訂一個n\*2。  
若最後所有元素的收支平衡，則代表成功還原成original。  

```python
class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        changed.sort()
        d=Counter()
        ans=[]
        
        for n in changed:
            if d[n]>0:
                d[n]-=1
            else:
                d[n*2]+=1
                ans.append(n)
            
        for v in d.values():
            if v!=0:
                return []
            
        return ans
```        
        