# FileSender
LAN内でファイルを送るサーバーを立てる

# 使い方
1. flaskをインストール
   ```
   pip install flask
   ```
1. filesender.py内のfilepathを送りたいファイルのパスに変える
   ```python
   filepath = "./file1.zip"
   ```
1. filesender.pyを実行
1. 同じLAN内にある別のパソコンから実行したパソコンのIPアドレスにアクセス
   1. パソコンのIPアドレスを調べる
      - windowsの場合
         ターミナルで以下のコマンドを実行
         ```
         ipconfig
         ```
         実行結果のIPv4アドレスを使用する
      - mac,linuxの場合
         ターミナルで以下のコマンドを実行
         ```
         ifconfig
         ```
         実行結果のIPv4アドレスを使用する
   1. webブラウザのurlバーに以下のようにしてアクセスする(実行したパソコンのIPが192.168.0.11の場合)
      ```
      http//192.168.0.11
      ```
