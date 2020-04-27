import unittest
import nii_to_png_script
import os
import time
from datetime import datetime

class TestStringMethods(unittest.TestCase):

    def test_suprascriere(self):
        outputfolder = "C:\\Scans\\Processed\\049"
        if os.path.exists(outputfolder):
            old_time=time.ctime(os.path.getmtime(outputfolder))
            nii_to_png_script.main('')
            new_time=time.ctime(os.path.getmtime(outputfolder))
            self.assertTrue(old_time != new_time)
        else:
            nii_to_png_script.main('')
            new_time = time.ctime(os.path.getmtime(outputfolder))
            self.assertTrue(new_time != 0)
    def test_existentaFelii(self):
        outputfolder = "C:\\Scans\\Processed\\049"
        nii_to_png_script.main('')
        masksfolder = outputfolder + "\\Masks"
        for subdir, dirs, files in os.walk(masksfolder):
            for file in files:
                filepath = subdir + os.sep + file
                ct_file = filepath.replace("Masks\\Mask1", "CT Scan")
                ct_file = ct_file.replace("Masks\\Mask2", "CT Scan")
                self.assertTrue(os.path.exists(ct_file))



if __name__ == '__main__':
    unittest.main()
