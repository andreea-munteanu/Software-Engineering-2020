import sys
import nibabel
import numpy
import os
import shutil
import imageio
import gc
from skimage.transform import resize

def slice_fb(image_array, inputfile, outputfb, from_slice, to_slice):
    if to_slice > image_array.shape[1]:
        to_slice = image_array.shape[1]
    for current_slice in range(from_slice, to_slice):
        data = numpy.rot90(image_array[:, current_slice, :])
        image_name = inputfile[:-7] + "_z" + "{:0>3}".format(str(current_slice + 1)) + ".png"
        data = data.astype(numpy.float32)
        data = resize(data, (512, 512))
        imageio.imwrite(image_name, data)
        src = image_name
        shutil.move(src, outputfb)
    gc.collect()

def deleteLastN(folder, n):
    listOfFiles = os.listdir(folder)
    listOfFiles.sort(reverse=True)
    for i in range(0,n):
        os.remove(folder + "\\" + listOfFiles[i])

def deleteFirstN(folder, n):
    listOfFiles = os.listdir(folder)
    listOfFiles.sort()
    for i in range(0,n):
        os.remove(folder + "\\" + listOfFiles[i])


def main(argv):
    toScan = [87,92,98,105,109,116,118,126,127,129,130,131,139,141,142,143,149,150,156,158,159,160,162,164,165,166,168]
    for i in toScan:
        inputfileM1 = "C:\\Users\\denis\\Desktop\\Masks1\\"  # Scans location
        inputfileM2 = "C:\\Users\\denis\\Desktop\\Masks2\\"
        inputfileCT = "C:\\Users\\denis\\Desktop\\CTs\\"
        # Scan number
        if i < 10:
            j = "00" + str(i)
        elif i < 100:
            j = "0" + str(i)
        elif i < 1000:
            j = str(i)
        outputfolder = "C:\\Users\\denis\\Desktop\\Software-Engineering2020\\TrainCTRs\\" + j  # Output location

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

        deleteFirstN(outputlrM1, 5)
        deleteFirstN(outputlrM2, 5)
        deleteFirstN(outputlrCT, 5)

        for file in os.listdir(outputlrM1):
            if int(file[-7:-4]) >225 and int(file[-7:-4]) < 270:
                os.remove(outputlrM1 + "\\" + file)
        for file in os.listdir(outputlrM2):
            if int(file[-7:-4]) >225 and int(file[-7:-4]) < 270:
                os.remove(outputlrM2 + "\\" + file)

        for file in os.listdir(outputlrCT):
            if int(file[-7:-4]) >225 and int(file[-7:-4]) < 270:
                os.remove(outputlrCT + "\\" + file)

        deleteLastN(outputlrCT,5)
        deleteLastN(outputlrM1,5)
        deleteLastN(outputlrM2,5)

        deleteFirstN(outputfbM1,10)
        deleteFirstN(outputfbM2,10)
        deleteFirstN(outputfbCT,10)

        for j in range(241, 272):
            if not (os.path.exists(outputfbM1 + "\\" + file)):
                try:
                    slice_fb(image_arrayM1, inputfileM1, outputfbM1, j, (j + 1))
                    slice_fb(image_arrayM2, inputfileM2, outputfbM2, j, (j + 1))
                    slice_fb(image_arrayCT, inputfileCT, outputfbCT, j, (j + 1))
                except Exception as e:
                    print(e)

        deleteLastN(outputfbM1, 10)
        deleteLastN(outputfbM2, 10)
        deleteLastN(outputfbCT, 10)

        deleteLastN(outputtbCT, 4)
        deleteLastN(outputtbM1, 4)
        deleteLastN(outputtbM2, 4)

        deleteFirstN(outputtbM1, 4)
        deleteFirstN(outputtbM2, 4)
        deleteFirstN(outputtbCT, 4)


if __name__== "__main__":
    main(sys.argv[1:])