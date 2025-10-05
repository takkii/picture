### このプロジェクトは顔写真を撮影します。

英語版は、[こちら](https://github.com/takkii/Picture/tree/main/wiki)。

> 使い方は単純です。

```markdown
pip3 install bakachon

git clone git@github.com:takkii/picture.git

cd picture

mkdir images

pip3 install -r requirements.txt

# 停止、端末上でCtrl+Cですが通常opencvのウインドウ内qでよいです。
python take.py

# jpg → gif 拡張子変換、Image/face.gifを生成します。
python convert.py

# hold/face.gif(比較元) | Images/face.gif(比較先)
python run.py

# ログ
cd picture/tools

# フォルダー 削除 yes/no(保留)
ruby cleaner.rb
```

_※ クリア、写真をばかちょんで取ることと、jpegからgif変換する機能。_