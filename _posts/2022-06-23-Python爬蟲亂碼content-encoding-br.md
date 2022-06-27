--- 
layout      : single
title       : Python爬蟲亂碼"content-encoding:br"
tags        : Python
---
# 懶人包
使用python 3.7版本請更新到3.10，安裝brotli套件後就沒事了。  
無法更新的朋友請繼續往下看。  

# 前言
幫朋友寫遊戲戰績爬蟲，順便練習API串接。  

# 出現亂碼
本來先在瀏覽器console測試發請求，得到的回應都很正常。  

![示意圖](/assets/img/brotli-1.jpg)

但是在python上卻變成亂碼，而且還不像是往常的ascii或是utf8編碼錯誤。  
嘗試對回應設置不同encoding，都沒有成功。  

![示意圖](/assets/img/brotli-2.jpg)

本來想說是不是設置的request檔頭有問題，仔細看看原本的請求封包標頭：  
> Accept-Encoding : zip, deflate, br  

接收到的回應封包標頭：  
> content-encoding : br  
> content-type : text/html  

br編碼？這什麼怪東西？  

# Brotli
br全名**Brotli**，是由Google推出的字串壓縮演算法，比常見的gzip高出約20%的壓縮率，且壓縮/解壓縮時間差不多。  
這次使用的API是架設在Google Cloud Platform上，使用自家規格也是合情合理的事。  

# 安裝函數庫
現在各大瀏覽器幾乎都有支援br編碼，不需要特別做什麼處理，但如果使用python，則需要額外安裝brotli函數庫。  
> pip install brotli

brotli安裝需要Microsoft Visual C++ 14.0以上版本，若不符合則會出現錯誤：  
> Microsoft Visual C++ 14.0 is required. Get it with "Microsoft Visual C++ Build Tools"  

從[這裡](https://visualstudio.microsoft.com/zh-hant/visual-cpp-build-tools/)下載vs_BuildTools，並安裝VC++ 14和Windows 10 SDK即可。

# 使用方法
根據[文件](http://python-hyper.org/projects/brotlipy/en/latest/api.html#brotli.Decompressor.decompress)的說明，brotli使用的型別是**bytestring**，而不是string。所以在取得response後，應該要選擇content，而非text。   
先將收到的回應解壓縮，再以相應的編碼解碼，即可得到正確的內容。

```python
import brotli
url = # some url
res = requests.get(url)
bytestring = brotli.decompress(res.content) # 不是res.text
print(type(bytestring)) # <class 'bytes'>
text = bytestring.decode('utf-8') # 將bytestring解碼
print(type(text)) # <class 'str'>
```

![示意圖](/assets/img/brotli-3.jpg)

2022-6-27補充：  
昨天更新系統到windows 10，連帶把python版本也更上3.10，才發現新版只需要安裝brotli套件，而request會自動選擇解碼器。  

```python
url = # some url
res = requests.get(url)
res.encoding=('utf-8')
print(res.text) # data
```
