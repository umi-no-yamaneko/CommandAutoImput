# スクリプトの機能
- 実行するコマンドが記載されたファイルから，コマンドを1行ずつ対話形式で実行していきます。
- 簡単なログも出力します。

# 対応環境
## 対応OS
- Linux
## 対応Pythonバージョン
- Python 3系

# 使用方法
$ python3 CommandAutoInput3.py コマンド一覧ファイル名

## コマンド一覧ファイルの書き方
実行したいコマンドを1行ずつ記載します
例(CommandList_test.txt):
```
echo abc
ls
touch hoge.txt
ls
huga
```
### 実行例
```
$ python3 CommandAutoInput3.py ./CommandList_test.txt
!!! Start Logging !!!

> echo abc

Execute this command? (y/n):y
abc


Status: OK

> ls

Execute this command? (y/n):y
CheckLog2023-08-31_22-13-24.txt
CommandAutoInput3.py
CommandList_test.txt


Status: OK

> touch hoge.txt

Execute this command? (y/n):y


Status: OK

> ls

Execute this command? (y/n):y
CheckLog2023-08-31_22-13-24.txt
CommandAutoInput3.py
CommandList_test.txt
hoge.txt


Status: OK

> huga

Execute this command? (y/n):y
[Errno 2] No such file or directory: 'huga'
Error Occured.

!!! End Logging !!!
$
```


## ログ(CheckLog)
以下の内容が出力されます
- スクリプト実行開始日時
- 実行したコマンド
- コマンドの標準出力，エラー内容
- エラー判定("OK"または"Error Occured.")

### ログの例
```
Date: 2023-08-31_22-13-24
!!! Start Logging !!!
> echo abc
abc

Status: OK
> ls
CheckLog2023-08-31_22-13-24.txt
CommandAutoInput3.py
CommandList_test.txt

Status: OK
> touch hoge.txt

Status: OK
> ls
CheckLog2023-08-31_22-13-24.txt
CommandAutoInput3.py
CommandList_test.txt
hoge.txt

Status: OK
> huga
[Errno 2] No such file or directory: 'huga'
Error Occured.
!!! End Logging !!!
```


