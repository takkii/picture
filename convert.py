import os

from PIL import Image
from os.path import join, dirname

# 写真を保存先
img_jpg = './Images/face.jpg'

# 作成したgifファイル
img_gif = './Images/face.gif'

# 顔写真のpath
is_file_jpg = os.path.isfile(img_jpg)
is_file_gif = os.path.isfile(img_gif)

# jpeg画像があるとき処理を行う
if is_file_jpg and not is_file_gif:
  img_jpg = './Images/face.jpg'
  img = Image.open(str(img_jpg))
  img.save('./Images/face.gif', 'gif')
  print('create image file ./Images/face.gif')
# jpeg画像がないときraise発生
else:
  raise ValueError("None, Please Check the jpeg image file.")


# 画像フォーマット
# print(img.format)
# 画像サイズ
# print(img.size)
# 画像モードを取得・表示
# 画像モードはトゥルーカラーの場合はRGB、グレースケールの場合はLなどが入ります。
# print(img.mode)

# copy.jpg – 元ファイルlogo.jpgを別名保存（コピー）
# img.save('./copy.jpg')
# logo.bmp – 元ファイルlogo.jpgからBMPへ変換して保存
# img.save('./logo.bmp', 'bmp')
# logo.gif – 元ファイルlogo.jpgからGIFへ変換して保存
# img.save('./logo.gif', 'gif')

# logo_left_right.jpg – 元ファイルlogo.jpgを左右反転保存
# left_right_image = img.transpose(Image.FLIP_LEFT_RIGHT)
# left_right_image.save('./logo_left_right.jpg')

# logo_top_bottom.jpg – 元ファイルlogo.jpgを上下反転保存
# top_buttom_image = img.transpose(Image.FLIP_TOP_BOTTOM)
# top_buttom_image.save('./logo_top_bottom.jpg')

# logo_thum.jpg – 元ファイルlogo.jpgからサムネイル画像を生成
# img.thumbnail((125, 25))
# img.save('./logo_thum.jpg')