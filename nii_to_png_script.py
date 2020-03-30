import getopt
import sys
import nibabel
import numpy
import os
import shutil
import imageio
import gc
from skimage.transform import resize

def main(argv):
    for i in range(35, 36):
        inputfile = "C:\\Users\\denis\\Desktop\\CTs\\CTR_TRN_0"+str(i)+".nii.gz"
        outputfolder="C:\\Scans2d"
        outputfile = outputfolder+"\\2d-"+str(i)
        outputlr=outputfile+"\\LeftRight"
        outputfb=outputfile+"\\FrontBack"
        outputtb=outputfile+"\\TopBottom"
        try:
            opts, args = getopt.getopt(argv, "hi:o:", ["ifile=", "ofile="])
        except getopt.GetoptError:
            print('nii2png.py -i <inputfile> -o <outputfile>')
            sys.exit(2)
        for opt, arg in opts:
            if opt == '-h':
                print('nii2png.py -i <inputfile> -o <outputfile>')
                sys.exit()
            elif opt in ("-i", "--input"):
                inputfile = arg
            elif opt in ("-o", "--output"):
                outputfile = arg

        print('Input file is ', inputfile)
        print('Output folder is ', outputfile)

        # set fn as your 4d nifti file
        image_array = nibabel.load(inputfile).get_fdata()
        print(len(image_array.shape))

        if len(image_array.shape) == 3:
            # set 4d array dimension values
            nx, ny, nz = image_array.shape
            # set destination folder
            if not os.path.exists(outputfile):
                os.makedirs(outputfile)
                print("Created ouput directory: " + outputfile)
                
            os.mkdir(outputlr) 
            total_slices = image_array.shape[0]
            slice_counter = 0
            # iterate through slices
            for current_slice in range(0, total_slices):
                # alternate slices
                if (slice_counter % 1) == 0:
                    data = numpy.rot90(image_array[current_slice,:, :])
                    
                    print(data.shape)
                    # alternate slices and save as png
                    if (slice_counter % 1) == 0:
                        image_name = inputfile[:-7] + "_z" + "{:0>3}".format(str(current_slice + 1)) + ".png"
                        data = data.astype(numpy.float32)
                        data = resize(data,(512,512))
                        imageio.imwrite(image_name, data)
                        # move images to folder
                        src = image_name
                        shutil.move(src, outputlr)
                        slice_counter += 1 
            gc.collect()
                            
            os.mkdir(outputfb) 
            total_slices = image_array.shape[1]
            slice_counter = 0
            # iterate through slices
            for current_slice in range(0, total_slices):
                # alternate slices
                if (slice_counter % 1) == 0:
                    data = numpy.rot90(image_array[:,current_slice, :])
                    print(data.shape)
                    # alternate slices and save as png
                    if (slice_counter % 1) == 0:
                        image_name = inputfile[:-7] + "_z" + "{:0>3}".format(str(current_slice + 1)) + ".png"
                        data = data.astype(numpy.float32)
                        data = resize(data,(512,512))
                        imageio.imwrite(image_name, data)
                        # move images to folder
                        src = image_name
                        shutil.move(src, outputfb)
                        slice_counter += 1 
            gc.collect()
                        
            os.mkdir(outputtb)  
            total_slices = image_array.shape[2]
            slice_counter = 0
            # iterate through slices
            for current_slice in range(0, total_slices):
                # alternate slices
                if (slice_counter % 1) == 0:
                    data = image_array[:,:,current_slice]
                    print(data.shape)
                    # alternate slices and save as png
                    if (slice_counter % 1) == 0:
                        image_name = inputfile[:-7] + "_z" + "{:0>3}".format(str(current_slice + 1)) + ".png"
                        data = data.astype(numpy.float32)
                        imageio.imwrite(image_name, data)
                        # move images to folder
                        src = image_name
                        shutil.move(src, outputtb)
                        slice_counter += 1 
            gc.collect()
    

# call the function to start the program
if __name__ == "__main__":
    main(sys.argv[1:])
