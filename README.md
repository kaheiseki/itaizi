# itaizi
異体字と常用字の間の変換をすることができるPythonライブラリです

<!-- ## demo -->


## 使い方
### インストール
```
pip install git+https://github.com/kaheiseki/itaizi
```
によってインストールすることができます  
いずれ
```
pip install itaizi
```
の形でも対応予定です。

### 関数の機能
#### to_itaizi
```
to_itaizi("hogehoge")
```
によって文章中の正字を全て異体字に変更することができます。  
変換後の文字列が返り値として出力されます。

#### to_seizi
```
to_seizi("hogehoge")
```
によって文章中の異体字を全て正字に変更することができます。  
変換後の文字列が返り値として出力されます。

#### is_itaizi
```
is_itaizi("hogehoge")
```
によって文章中に異体字が含まれているかどうかを判定することができます。  
TrueまたはFalseが返り値として出力されます。

#### count_itaizi
```
count_itaizi("hogehoge")
```
によって文章中に含まれる異体字の個数を数えることができます。  
個数が返り値として出力されます。


## 参考文献
東京大学史料編纂所データベース異体字同定一覧  
https://wwwap.hi.u-tokyo.ac.jp/ships/itaiji_list.jsp  
3/22現在このリストの40番目まで対応しています。