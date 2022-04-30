--- 
layout      : single
title       : LeetCode 2182. Construct String With Repeat Limit
tags        : LeetCode Medium String Greedy Counting Heap
---
這題難度不高，但是沒有一次把整個流程考慮好的話很容易變醜，剛開始寫了好幾個垃圾迴圈又跳不出去，搞快一小時。

# 題目
輸入字串s和整數repeatLimit。請重組一個新的字串，並符合以下規定：  
- 新字串中，所有字元出現次數不得大於s  
- 同樣的字元最多只能連續出現repeatLimit次  
- 以字典順序最大的方式排序  
  
# 解法
每個字元次數限制，很明顯要先遍歷s，計算各字元有幾個。  
先講講一開始的超醜巢狀解法。用雜湊表紀錄各字元後，以ks保存有出現過的字元並遞減排序，減少檢查次數。  
維護變數last，以計算可用子次串長度，並重複以下步驟直到字元用完為止：  
1. 找到最大的可用字元k  
2. 計算最大連續長度mx，如果k與上一次使用的字元相同，則為repeatLimit-1；否則repeatLimit  
3. 計算當前子字串長度use，不可超過mx，並更新last為k  
4. 若use==mx，則尋找次大的字元kk來做間隔  
   成功找到則更新last為kk，否則直接回傳ans  

```python
class Solution:
    def repeatLimitedString(self, s: str, repeatLimit: int) -> str:
        ctr = Counter(s)
        N = len(s)
        ks = sorted(ctr, reverse=1)
        ans = ''
        last = None
        while len(ans) < N:
            for k in ks:
                if ctr[k] > 0:
                    mx = repeatLimit-(last == k)
                    use = min(ctr[k], mx)
                    ans += k*use
                    # print('+++', k*use)
                    ctr[k] -= use
                    last = k
                    if use == mx:
                        ok = False
                        for kk in ks:
                            if kk < k and ctr[kk] > 0:
                                ok = True
                                ans += kk
                                last = kk
                                # print('+++', kk)
                                ctr[kk] -= 1
                                break
                        if not ok:
                            return ans
                        break

        return ans
```

真的覺得上面那版太醜，只好再多寫幾次。  
改使用陣列計數，雖然慢了些，但是可讀性更佳。  
處理邏輯稍微有點不同，改成若使用的字元c數量超過repeatLimit時，才去找次大的字元來做間隔。  
且多一個remain變數，記錄剩下的字元數，若在c超過repeatLimit且剛好等於remain，可以確定找不到間隔，直接跳出迴圈。

```python
class Solution:
    def repeatLimitedString(self, s: str, repeatLimit: int) -> str:
        remain=len(s)
        ans=[]
        cnt=[0]*123
        for c in s:
            cnt[ord(c)]+=1
            
        while remain>0:
            i=122
            while i>=97 and cnt[i]==0:
                i-=1
            if cnt[i]<=repeatLimit:
                ans+=[chr(i)]*cnt[i]
                remain-=cnt[i]
                cnt[i]=0
            else:
                ans+=[chr(i)]*repeatLimit
                if cnt[i]==remain: # cant find padding
                    remain=0
                else:
                    cnt[i]-=repeatLimit
                    j=i-1
                    while j>=97 and cnt[j]==0:
                        j-=1
                    ans+=[chr(j)]
                    cnt[j]-=1
                    remain-=repeatLimit+1
                        
        return ''.join(ans)
```

使用heap的版本，可讀性高和效率比上面兩個更好。  
直接以字典順序去做min heap，在使用字元c等於repeatLimit時，才查看heap中是否還有剩下元素，若heap為空則無法做間隔，跳出迴圈。

```python
class Solution:
    def repeatLimitedString(self, s: str, repeatLimit: int) -> str:
        h=[]
        ans=[]
        for k,v in Counter(s).items():
            heappush(h,[-ord(k),k,v])
            
        while h:
            weight,char,cnt=heappop(h)
            if cnt<=repeatLimit:
                ans+=[char]*cnt
            else:
                ans+=[char]*repeatLimit
                if not h:
                    break
                ans+=[h[0][1]]
                if h[0][2]==1:
                    heappop(h)
                else:
                    h[0][2]-=1
                heappush(h,[weight,char,cnt-repeatLimit])
        
        return ''.join(ans)
```