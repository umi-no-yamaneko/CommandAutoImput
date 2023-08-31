# coding:utf-8

"""
コマンド自動実行プログラム(Linux用)

対応Pythonバージョン: Python3

必要ライブラリ: なし(標準ライブラリ)

読み込ませるファイル: コマンド一覧(テキストファイル)
コマンドを一行ずつ記載したもの
例: 
cd
ls
cat aaa

使い方
$ python3 CommandAutoInput3.py コマンド一覧ファイル名

"""

from math import log
from operator import truediv
import subprocess, sys, datetime

#main関数
def main():
    dt_now = datetime.datetime.now()                    #現在時刻を取得(logファイル用)
    DateTimeNow = dt_now.strftime('%Y-%m-%d_%H-%M-%S')
    CommandListFileName = sys.argv                      #コマンドリストのファイル名取得(コマンドライン第1引数)
    CommandList = open(CommandListFileName[1], 'r')     
    logfile = open('CheckLog'+DateTimeNow+'.txt', 'a')  #ログファイル生成

    output = '!!! Start Logging !!!\n'
    logfile.write("Date: "+DateTimeNow+"\n")            #ログファイルへ開始時刻の書き込み
    print(output)
    logfile.write(output)

    cmd = CommandList.readlines()                       #コマンドリスト読み込み
    CommandList.close()                                 

    CommandListLength = len(cmd)                        #コマンドリストの行数取得
    LineNumber = 0
    while( LineNumber <= CommandListLength-1):          #コマンドを上から順番に実行
        if exe(cmd[LineNumber].rstrip('\n'), logfile) != 1:
            LineNumber +=1
        else:
            break
    output = '!!! End Logging !!!'                      #ログ停止
    print(output)
    logfile.write(output)
    
    logfile.close()

#関数定義
#コマンド実行関数
def exe(char,_logfile):
    cmd = str(char)                         #コマンドを文字列に変換'''
    print("> "+cmd+"\n")                    #コマンドの表示
    OperatorAnswer = input("Execute this command? (y/n):")  #作業者へコマンド実行の確認
    if OperatorAnswer == "y":               # 返答がyなら
        _logfile.write("> "+cmd+"\n")                 #ログファイルへコマンドの書き込み
        try:
            d = subprocess.check_output(cmd.split())  #コマンドの実行
            #if d == 0:                          #コマンド実行後エラーが返されなかったら
            print(d.decode())
            message = "\nStatus: OK\n"                #OKを表示
            print(message)
            _logfile.write(str(d.decode()))
            _logfile.write(message)
        except subprocess.CalledProcessError as d:                               #コマンドでエラーが発生したら
            message = "Error Occured.\n"    #エラー発生を表示
            print(d.decode().split('\n'))                            #エラー内容表示
            _logfile.write(str(d.decode()))                   #エラー内容をログファイルに書き込み
            print(message) 
            _logfile.write(d.stdout+"\n")                     
            _logfile.write(message)             #エラー発生をログファイルに書き込み
        except OSError as d:
            message = "Error Occured.\n"    #エラー発生を表示
            print(d)                            #エラー内容表示
            _logfile.write(str(d)+"\n")                   #エラー内容をログファイルに書き込み
            print(message)
            _logfile.write(message)             #エラー発生をログファイルに書き込み

    elif OperatorAnswer == "n":             #返答がnなら
        print("quit\n")                       #終了
        _logfile.write("quit")
        return 1
    else:                                   #不正な返答の場合
        print("Please answer y or n\n")     #再度返答を要求
        exe(char,_logfile)


if __name__ == "__main__":
    main()
