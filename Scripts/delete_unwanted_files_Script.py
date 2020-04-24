import sys
import os
import gc
from PIL import Image

def isFinalDir(inputDir):
    for fname in os.listdir(inputDir):
        if os.path.isdir(os.path.join(inputDir, fname)):
            return False
    return True


def deleteAllBlack(inputDir):
    for filename in os.listdir(inputDir):
        f = Image.open(inputDir + "\\" + filename, 'r')
        data = list(f.getdata())
        allZeros = all(elem == 0 for elem in data)
        if allZeros:
            os.remove(inputDir + "\\"+ filename)
            try:
                if "FrontBack" in inputDir:
                    os.remove(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(inputDir + "\\" +filename)))) +
                              "\\CT Scan\\FrontBack\\" + filename)
                    os.remove(os.path.dirname(os.path.dirname(os.path.dirname(inputDir + "\\" + filename))) +
                              "\\Mask2\\FrontBack\\" + filename)
                if "LeftRight" in inputDir:
                    os.remove(os.path.dirname(
                        os.path.dirname(os.path.dirname(os.path.dirname(inputDir + "\\" + filename)))) + "\\CT Scan\\LeftRight\\"
                              + filename)
                    os.remove(os.path.dirname(os.path.dirname(os.path.dirname(inputDir + "\\" + filename))) +
                              "\\Mask2\\LeftRight\\" + filename)

                if "TopBottom" in inputDir:
                    os.remove(os.path.dirname(
                        os.path.dirname(os.path.dirname(os.path.dirname(inputDir + "\\" + filename)))) + "\\CT Scan\\TopBottom\\" +
                              filename)
                    os.remove(os.path.dirname(os.path.dirname(os.path.dirname(inputDir + "\\" + filename))) +
                              "\\Mask2\\TopBottom\\" + filename)

            except FileNotFoundError as e:
                print(e)
    gc.collect()

def deleteThreeOutOfFour(inputDir):
    counter = 0
    for filename in os.listdir(inputDir):
        if counter % 4 != 0:
            os.remove(inputDir + "\\" + filename)
        counter += 1
    gc.collect()


def delete_unwanted(inputDir):
    if "Mask1" in inputDir:
        deleteAllBlack(inputDir)
    deleteThreeOutOfFour(inputDir)


def main(argv):
    rootdir = "C:\\Users\\denis\\Desktop\\Software-Engineering-2020\\LeftLung\\LeftLungAffected"
    listOfCTScansAndMask2 = []
    for subdir, dirs, files in os.walk(rootdir):
        if isFinalDir(subdir):
            if "Mask1" in subdir:
                delete_unwanted(subdir)
            else:
                listOfCTScansAndMask2.append(subdir)
    for dir in listOfCTScansAndMask2:
        delete_unwanted(dir)


if __name__ == '__main__':
    main(sys.argv[1:])
