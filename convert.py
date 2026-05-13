import debugpy
import gc
import os
import threading

from typing import Optional
from PIL import Image
from os.path import join, dirname

__all__ = ['join', 'dirname']


# Use SublimeDebugger, debugpy lib.
def debug_wait_for_attach(listen_to):
    scoop: Optional[str] = os.path.expanduser(
        '~/scoop/apps/python313/current/python.exe')
    pyenv: Optional[str] = os.path.expanduser('~/.pyenv/shims/python')
    anyenv: Optional[str] = os.path.expanduser(
        '~/.anyenv/envs/pyenv/shims/python')

    # Use Scoop.
    if os.path.exists(os.path.expanduser(scoop)):
        debugpy.configure(python=str(scoop))
        debugpy.listen(listen_to)
        debugpy.wait_for_client()
    # Use Pyenv.
    elif os.path.exists(pyenv):
        debugpy.configure(python=str(pyenv))
        debugpy.listen(listen_to)
        debugpy.wait_for_client()
    # Use Anyenv.
    elif os.path.exists(anyenv):
        debugpy.configure(python=str(anyenv))
        debugpy.listen(listen_to)
        debugpy.wait_for_client()


# Convert class
class Convert(threading.Thread):

    # use thread
    def __init__(self):
        threading.Thread.__init__(self)

    # run method
    def run(self):
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


# try ~ except ~ finally.
try:
    thread = Convert()
    thread.run()
# Custom Exception, raise throw.
except ValueError as ext:
    print(ext)
    raise RuntimeError from None

# Once Exec.
finally:
    # GC collection.
    gc.collect()
