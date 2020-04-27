import unittest
import os


class TestCase10(unittest.TestCase):
    def test(self):  # testam daca exista o anume imagine atat in CT Scan cat si in Mask1 si Mask2
        file_name = "CTR_TRN_017_z033.png"
        path1 = "D:\\Facultate\\An 2\\Sem 2\\I.P\\Proiect\\Imagini\\2D\\017\\CT Scan\\TopBottom\\"
        found = 0
        # r=root, d=directories, f = files
        for r, d, f in os.walk(path1):
            for file in f:
                if file_name in file:
                    found = 1

        self.assertEqual(found, 1, "Nu am gasit imaginea")

        path2 = "D:\\Facultate\\An 2\\Sem 2\\I.P\\Proiect\\Imagini\\2D\\017\\Masks\\Mask1\\TopBottom\\"
        found = 0
        # r=root, d=directories, f = files
        for r, d, f in os.walk(path2):
            for file in f:
                if file_name in file:
                    found = 1

        self.assertEqual(found, 1, "Nu am gasit imaginea")

        path3 = "D:\\Facultate\\An 2\\Sem 2\\I.P\\Proiect\\Imagini\\2D\\017\\Masks\\Mask2\\TopBottom\\"
        found = 0
        # r=root, d=directories, f = files
        for r, d, f in os.walk(path3):
            for file in f:
                if file_name in file:
                    found = 1

        self.assertEqual(found, 1, "Nu am gasit imaginea")


if __name__ == '__main__':
    unittest.main()
