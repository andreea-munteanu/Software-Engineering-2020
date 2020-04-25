import getopt
import sys
import nibabel
import numpy
import os
import scipy
import shutil
import scipy.misc
import imageio
import gc
import time
from concurrent.futures import ThreadPoolExecutor, wait
import math
from skimage.transform import resize


def allZeros(list): #folosit pentru a vedea daca o imagine este total neagra
    for elem in list:
        for number in elem:
            if number != 0:
                return False
    return True


def slice_lr(image_array, inputfile, outputlr, from_slice, to_slice):
    if to_slice > image_array.shape[0]:
        to_slice = image_array.shape[0]
    for current_slice in range(from_slice, to_slice):
        data = numpy.rot90(image_array[current_slice, :, :])
        image_name = inputfile[:-7] + "_z" + "{:0>3}".format(str(current_slice + 1)) + ".png"
        data = resize(data, (512, 512))
        imageio.imwrite(image_name, data)
        src = image_name
        shutil.move(src, outputlr)
    gc.collect()


def slice_fb(image_array, inputfile, outputfb, from_slice, to_slice):
    if to_slice > image_array.shape[1]:
        to_slice = image_array.shape[1]
    for current_slice in range(from_slice, to_slice):
        data = numpy.rot90(image_array[:, current_slice, :])
        image_name = inputfile[:-7] + "_z" + "{:0>3}".format(str(current_slice + 1)) + ".png"
        data = resize(data, (512, 512))
        imageio.imwrite(image_name, data)
        # move images to folder
        src = image_name
        shutil.move(src, outputfb)
    gc.collect()


def slice_tb(image_array, inputfile, outputtb, from_slice, to_slice):
    if to_slice > image_array.shape[2]:
        to_slice = image_array.shape[2]
    for current_slice in range(from_slice, to_slice):
        data = image_array[:, :, current_slice]
        image_name = inputfile[:-7] + "_z" + "{:0>3}".format(str(current_slice + 1)) + ".png"
        data = data.astype(numpy.float32)
        imageio.imwrite(image_name, data)
        # move images to folder
        src = image_name
        shutil.move(src, outputtb)
    gc.collect()


def main(argv):
    #number_of_threads = 4  # Number of threads used

    #in toScan se vor adauga toate CTR-urile care trebuie scanate

    #A fost modificat astfel incat sa fie nevoie doar de o singura rulare per pacient

    #Daca in toScan adaugi 201, el va scana si transforma si CT-ul, si mastile1, si mastile2

    #Trebuie precizat folder-ul de input pentru fiecare dintre ele

    toScan = [98,105]
    for i in toScan:
        inputfileM1 = "C:\\Users\\denis\\Desktop\\Masks1\\"  # Scans location
        inputfileM2 = "C:\\Users\\denis\\Desktop\\Masks2\\"
        inputfileCT = "C:\\Users\\denis\\Desktop\\CTs\\"
        if i < 10:
            j = "00" + str(i)
        elif i < 100:
            j = "0" + str(i)
        elif i < 1000:
            j = str(i)
        outputfolder = "C:\\Users\\denis\\Desktop\\Software-Engineering-2020\\LeftLung\\LeftLungUnaffected\\" + j  # Output location

        file_name = "CTR_TRN_" + str(j) + ".nii.gz"
        inputfileM1 = inputfileM1 + file_name
        inputfileM2 = inputfileM2 + file_name
        inputfileCT = inputfileCT + file_name

        outputlrM1 = outputfolder + "\\Masks\\Mask1\\LeftRight"
        outputfbM1 = outputfolder + "\\Masks\\Mask1\\FrontBack"
        outputtbM1 = outputfolder + "\\Masks\\Mask1\\TopBottom"

        outputlrM2 = outputfolder + "\\Masks\\Mask2\\LeftRight"
        outputfbM2 = outputfolder + "\\Masks\\Mask2\\FrontBack"
        outputtbM2 = outputfolder + "\\Masks\\Mask2\\TopBottom"

        outputlrCT = outputfolder + "\\CT Scan\\LeftRight"
        outputfbCT = outputfolder + "\\CT Scan\\FrontBack"
        outputtbCT = outputfolder + "\\CT Scan\\TopBottom"

        image_arrayM1 = nibabel.load(inputfileM1).get_fdata()
        image_arrayM1 = image_arrayM1.astype(numpy.int16)

        image_arrayM2 = nibabel.load(inputfileM2).get_fdata()
        image_arrayM2 = image_arrayM2.astype(numpy.int16)

        image_arrayCT = nibabel.load(inputfileCT).get_fdata()
        image_arrayCT = image_arrayCT.astype(numpy.int16)

        if len(image_arrayM1.shape) == 3:
            # set destination folder
            if not os.path.exists(outputfolder):
                os.makedirs(outputfolder)
                print("Created output directory: " + outputfolder)
            else:
                shutil.rmtree(outputfolder)
                os.makedirs(outputfolder)

            os.makedirs(outputlrM1)
            os.makedirs(outputfbM1)
            os.makedirs(outputtbM1)

            os.makedirs(outputlrM2)
            os.makedirs(outputfbM2)
            os.makedirs(outputtbM2)

            os.makedirs(outputlrCT)
            os.makedirs(outputfbCT)
            os.makedirs(outputtbCT)

            print("Processing " + file_name + "...")

            total_slicesLR = image_arrayM1.shape[0]
            total_slicesFB = image_arrayM1.shape[1]
            total_slicesTB = image_arrayM1.shape[2]

            futures = []
            for j in range(0, total_slicesLR):
                if j % 4 == 0 and not(allZeros(image_arrayM1[j, :, :])):
                    slice_lr(image_arrayM1, inputfileM1, outputlrM1, j, (j + 1))
                    slice_lr(image_arrayM2, inputfileM2, outputlrM2, j, (j + 1))
                    slice_lr(image_arrayCT, inputfileCT, outputlrCT, j, (j + 1))
            gc.collect()

            for j in range(0, total_slicesFB):
                if j % 4 == 0 and not(allZeros(image_arrayM1[:, j, :])):
                    slice_fb(image_arrayM1, inputfileM1, outputfbM1, j, (j + 1))
                    slice_fb(image_arrayM2, inputfileM2, outputfbM2, j, (j + 1))
                    slice_fb(image_arrayCT, inputfileCT, outputfbCT, j, (j + 1))
            gc.collect()
            for j in range(0, total_slicesTB):
                if j % 4 == 0 and not(allZeros(image_arrayM1[:, :, j])):
                    slice_tb(image_arrayM1, inputfileM1, outputtbM1, j, (j + 1))
                    slice_tb(image_arrayM2, inputfileM2, outputtbM2, j, (j + 1))
                    slice_tb(image_arrayCT, inputfileCT, outputtbCT, j, (j + 1))
            gc.collect()
            wait(futures)


# call the function to start the program
if __name__ == "__main__":
    main(sys.argv[1:])
