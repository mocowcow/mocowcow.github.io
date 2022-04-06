---
layout      : single
title       : LeetCode 923. 3Sum With Multiplicity
tags 		: LeetCode Medium HashTable Array TwoPointers Sorting
---
每日題。其實可以用原版3sum的解法稍微改一下。

# 題目
數列arr只會出現0~100的數字。在arr裡隨便挑三個不同位置的數使arr[i]+arr[j]+arr[k]=target，求有幾種組合。  
答案可能很大，模10^9+7後再回傳。

# 解法
先把arr排序，每次取左邊第i個數為arr[i]，j為i+1，k為N-1，藉由調整雙指標j和k的位置使arr[j]+arr[k]=target-arr[i]。  
j和k位置確定後，若arr[j]!=arr[k]，計算和arr[j]和arr[k]的出現次數，兩者出現次數相乘就是arr[i]可以生成的合法數對數量。  
或arr[j]=arr[k]，代表位置j到k都是同樣的數，共出現k-j+1次。n個數挑選2個，公式為n*(n-1)/2。此時所有數都計算完成，可以直接跳出迴圈。  
跑了3998ms，提交的時候還以為會超時。

```python
class Solution:
    def threeSumMulti(self, arr: List[int], target: int) -> int:
        ans=0
        arr.sort()
        N=len(arr)
        
        for i in range(N):
            need=target-arr[i]
            j=i+1
            k=N-1
            while j<k:
                x=arr[j]+arr[k]
                if x<need:
                    j+=1
                elif x>need:
                    k-=1
                elif arr[j]!=arr[k]:
                    jcnt=kcnt=1
                    while j+1<k and arr[j+1]==arr[j]:
                        j+=1
                        jcnt+=1
                    while k-1>j and arr[k-1]==arr[k]:
                        k-=1
                        kcnt+=1
                    ans+=jcnt*kcnt
                    j+=1
                    k-=1
                else:
                    cnt=k-j+1
                    ans+=cnt*(cnt-1)//2
                    break
        
        return ans % (10**9+7)
```

上面方法太慢了，參考別人的解法改良一下。變成92ms。  
和target相等的數對有三種可能的情況：  
1. (i,i,i) 三個同樣數字  
2. (i,i,j) 前兩個相同，第三個不同的  
3. (i,j,k) 三個都不同
   
先計算各數字的出現次數，然後把所有出現過的數字keys排序。  
遍歷keys中的每個數i，先看三個i能不能組成target。  
再對keys中比i大的每個數j，看看2i+j或是i+2j能不能組成target。  
最後，k是target扣掉i和j後所不足的部分，如果k比j大的話，可以再用k組成(i,j,k)。  

```python
class Solution:
    def threeSumMulti(self, arr: List[int], target: int) -> int:
        ans = 0
        c = Counter(arr)
        keys = sorted(c.keys())
        N = len(keys)

        for i in range(N):
            if keys[i]*3 == target:  # (i,i,i)
                ans += c[keys[i]]*(c[keys[i]]-1)*(c[keys[i]]-2)//6
            for j in range(i+1, N):
                if keys[i]*2+keys[j] == target:  # (i,i,j)
                    ans += c[keys[i]]*(c[keys[i]]-1)*c[keys[j]]//2
                if keys[i]+keys[j]*2 == target:  # (i,j,j)
                    ans += c[keys[i]]*c[keys[j]]*(c[keys[j]]-1)//2
                k = target-keys[i]-keys[j]
                if k > keys[j]:  # (i,j,k)
                    ans += c[keys[i]]*c[keys[j]]*c[k]

        return ans % (10**9+7)
```

同上，犧牲一點速度換可讀性，121ms。  

```python
class Solution:
    def threeSumMulti(self, arr: List[int], target: int) -> int:
        ans = 0
        c = Counter(arr)
        keys = sorted(c.keys())

        for i in keys:
            if i*3 == target:  # (i,i,i)
                ans += c[i]*(c[i]-1)*(c[i]-2)//6
            for j in keys:
                if j <= i:
                    continue
                if i*2+j == target:  # (i,i,j)
                    ans += c[i]*(c[i]-1)*c[j]//2
                if i+j*2 == target:  # (i,j,j)
                    ans += c[i]*c[j]*(c[j]-1)//2
                k = target-i-j
                if k > j:  # (i,j,k)
                    ans += c[i]*c[j]*c[k]

        return ans % (10**9+7)

```