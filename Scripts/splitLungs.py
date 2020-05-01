import os
import shutil
import sys
from threading import Thread
from PIL import Image


def isFinalDir(inputDir):
    for fname in os.listdir(inputDir):
        if os.path.isdir(os.path.join(inputDir, fname)):
            return False
    return True


def separateLungs(dir):
    if "FrontBack" in dir:
        os.makedirs(os.path.dirname(dir) + "\\OnlyLeftLung\\FrontBack")
        os.makedirs(os.path.dirname(dir) + "\\OnlyRightLung\\FrontBack")
    if "TopBottom" in dir:
        os.makedirs(os.path.dirname(dir) + "\\OnlyLeftLung\\TopBottom")
        os.makedirs(os.path.dirname(dir) + "\\OnlyRightLung\\TopBottom")
    if "LeftRight" in dir:
        os.makedirs(os.path.dirname(dir) + "\\OnlyLeftLung\\LeftRight")
        os.makedirs(os.path.dirname(dir) + "\\OnlyRightLung\\LeftRight")
        for file in os.listdir(dir):
            f = file[-7:]
            f = f[:-4]
            if int(f) <= 256:
                f = Image.open(dir + "\\" + file)
                f.save(os.path.dirname(dir) + "\\OnlyLeftLung\\LeftRight\\" + file)
            else:
                f = Image.open(dir + "\\" + file)
                f.save(os.path.dirname(dir) + "\\OnlyRightLung\\LeftRight\\" + file)
        return 0
    for file in os.listdir(dir):
        leftLung = Image.open(dir + "\\" + file)
        rightLung = Image.open(dir + "\\" + file)
        left = leftLung.load()
        right = rightLung.load()

        for i in range(512):
            for j in range(512):
                if left[i, j] != 0 and left[i, j] != 127:
                    left[i, j] = 0
                if left[i, j] == 127:
                    left[i, j] = 255
                if right[i, j] != 0 and right[i, j] != 255:
                    right[i, j] = 0
        if "FrontBack" in dir:
            leftLung.save(os.path.dirname(dir) + "\\OnlyLeftLung\\FrontBack\\" + file)
            rightLung.save(os.path.dirname(dir) + "\\OnlyRightLung\\FrontBack\\" + file)
        if "TopBottom" in dir:
            leftLung.save(os.path.dirname(dir) + "\\OnlyLeftLung\\TopBottom\\" + file)
            rightLung.save(os.path.dirname(dir) + "\\OnlyRightLung\\TopBottom\\" + file)


def main(argv):
    threads = []
    for root, dirs, file in os.walk("C:\\Users\\Elax\\Desktop\\Facultate\\Anul 2\\Sem 2\\Software Engineering\\111-123"): #To change acording to location on your computer
        if "Mask1" in root and isFinalDir(root):
            t = Thread(target=separateLungs, args=(root,))
            t.start()
            threads.append(t)
    for t in threads:
        t.join()


if __name__ == "__main__":
    main(sys.argv[1:])
