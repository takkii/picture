import cv2
import debugpy
import face_recognition
import japanize_matplotlib
import golden_eagle as ga
import gc
import matplotlib.pyplot as plt
import numpy as np
import numpy.typing as npt
import os
import threading

from typing import Optional
from os.path import join, dirname
from dotenv import load_dotenv

load_dotenv(verbose=True)

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

BFP = os.environ.get("before_param")
AFP = os.environ.get("after_param")
GAN = os.environ.get("ga_num_run") or ""


# Use SublimeDebugger, debugpy lib.
def debug_wait_for_attach(listen_to):
    scoop: Optional[str] = os.path.expanduser(
        '~/scoop/apps/python/current/python.exe')
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


# face class
class Face(threading.Thread):

    # use thread
    def __init__(self):
        threading.Thread.__init__(self)

    # run method
    def run(self):
        # Specify the path of the face photo to be compared.
        my_before = face_recognition.load_image_file(
            os.path.expanduser(str(BFP)))
        my_after = face_recognition.load_image_file(
            os.path.expanduser(str(AFP)))

        # The default is “hog”.
        lo_before = face_recognition.face_locations(my_before, model='cnn')
        lo_after = face_recognition.face_locations(my_after, model='cnn')

        # A list of dicts of face feature locations (eyes, nose, etc)
        # model – Optional - which model to use.
        # “large” (default) or “small”.
        around_the_face_b = face_recognition.face_landmarks(
            my_before, lo_before)
        around_the_face_a = face_recognition.face_landmarks(my_after, lo_after)

        # facecompare version.
        print("golden-eagle_version: " + ga.__version__)

        # golden-eagle accuary number.
        ga_lose: Optional[str] = GAN

        # value is 0.6 and lower numbers make face comparisons more strict:
        ga.compare_before_after(my_before, my_after, float(ga_lose))

        # The data is processed as a feature quantity.
        en_b = face_recognition.face_encodings(my_before)[0]
        en_a = face_recognition.face_encodings(my_after)[0]
        face_d: npt.NDArray = face_recognition.face_distance([en_b], en_a)
        hyoka: npt.DTypeLike = (np.floor(face_d * 1000).astype(int) / 1000)

        # Accuracy evaluation, no face photo editing.
        accuracy = "accuracy:" + str(hyoka)
        print(accuracy)

        # Face coordinate.
        print("Before Image, Get face coordinates  :" + str(lo_before))
        print("After Image, Get face coordinates :" + str(lo_after))

        # Get around the face.
        print("Before Image, Get around the face :" + str(around_the_face_b))
        # print("After Image, Get around the face :" + str(around_the_face_a))

        # Use dlib, face recognition.
        cv2.startWindowThread()
        # Use face recognition my_after/my_before.
        cv2.imshow('Yourself before picture image.', my_before)
        cv2.imshow('Yourself after picture image.', my_after)
        # Window closes in 8 seconds
        cv2.waitKey(15000)
        cv2.waitKey(1)
        cv2.destroyAllWindows()
        cv2.waitKey(1)

        # 日本語訳
        jp_names = {
            'nose_bridge': '鼻筋',
            'nose_tip': '鼻先',
            'top_lip': '上唇',
            'bottom_lip': '下唇',
            'left_eye': '左目',
            'right_eye': '左目',
            'left_eyebrow': '左眉毛',
            'right_eyebrow': '右眉毛',
            'chin': '下顎'
        }

        # my_before load image, Plotting face recognition with matplotlib.
        fig = plt.figure('Yourself before picture image.',
                         figsize=(7, 7),
                         facecolor='lightskyblue',
                         layout='constrained')
        bx = fig.add_subplot()
        bx.imshow(my_before)
        bx.set_axis_off()
        for face in around_the_face_b:
            for name, points in face.items():
                points = np.array(points)

                bx.plot(points[:, 0],
                        points[:, 1],
                        'o-',
                        ms=3,
                        label=jp_names[name])
                bx.legend(fontsize=14)
                bx.set_title('Face Recognition Range')

        plt.show()

        # my_after load images, Plotting face recognition with matplotlib.
        fig = plt.figure('Yourself after picture image.',
                         figsize=(7, 7),
                         facecolor='deeppink',
                         layout='constrained')
        ax = fig.add_subplot()
        ax.imshow(my_after)
        ax.set_axis_off()
        for face in around_the_face_a:
            for name, points in face.items():
                points = np.array(points)
                ax.plot(points[:, 0],
                        points[:, 1],
                        'o-',
                        ms=3,
                        label=jp_names[name])
                ax.legend(fontsize=14)
                ax.set_title('Face Recognition Range')

        plt.show()


# try ~ except ~ finally.
try:
    thread = Face()
    thread.run()
# Custom Exception, raise throw.
except ValueError as ext:
    print(ext)
    raise RuntimeError from None

# Once Exec.
finally:
    # GC collection.
    gc.collect()
