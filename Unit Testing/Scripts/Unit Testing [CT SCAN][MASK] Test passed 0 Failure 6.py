import unittest
import os


class TestCase(unittest.TestCase):  # Testare daca exista masti Masks pentru CT Scan images
    def test_LEFTfrontBack(self):
        TRAIN_DIR = 'D:\\Git\\TrainCTRs'
        subfolders = [f.path for f in os.scandir(TRAIN_DIR) if f.is_dir()]
        for sub in subfolders:
            # print(sub[-3:])
            path = os.path.join(TRAIN_DIR, sub[-3:] + '\\Masks\\Mask1\\OnlyLeftLung\\FrontBack')
            # D:\Git\TrainCTRs\001\Masks\Mask1\FrontBack
            pathMask = os.path.join(TRAIN_DIR, sub[-3:] + '\\CT Scan\\FrontBack')
            for root, dirs, files in os.walk(path):
                for name in files:
                    nume_poza_mask = name
                    found = 0
                    for root1, dirs1, files1 in os.walk(pathMask):
                        for name1 in files1:
                            if nume_poza_mask == name1:
                                found = 1
                        self.assertEqual(found, 1, '[OnlyLeftLung\FrontBack']Nu gaseste: ' + nume_poza_mask + '. ')


    def test_LEFTtopBottom(self):
        TRAIN_DIR = 'D:\\Git\\TrainCTRs'
        subfolders = [f.path for f in os.scandir(TRAIN_DIR) if f.is_dir()]
        for sub in subfolders:
            # print(sub[-3:])
            path = os.path.join(TRAIN_DIR, sub[-3:] + '\\Masks\\Mask1\\OnlyLeftLung\\TopBottom')
            # D:\Git\TrainCTRs\001\Masks\Mask1\FrontBack
            pathMask = os.path.join(TRAIN_DIR, sub[-3:] + '\\CT Scan\\TopBottom')
            for root, dirs, files in os.walk(path):
                for name in files:
                    nume_poza_mask = name
                    found = 0
                    for root1, dirs1, files1 in os.walk(pathMask):
                        for name in files1:
                            if nume_poza_mask == name:
                                found = 1
                        self.assertEqual(found, 1, "[OnlyLeftLung\TopBottom']Nu am gasit imaginea: " + nume_poza_mask + " .")


    def test_LEFTLeftRight(self):
        TRAIN_DIR = 'D:\\Git\\TrainCTRs'
        subfolders = [f.path for f in os.scandir(TRAIN_DIR) if f.is_dir()]
        for sub in subfolders:
            # print(sub[-3:])
            path = os.path.join(TRAIN_DIR, sub[-3:] + '\\Masks\\Mask1\\OnlyLeftLung\\LeftRight')
            # D:\Git\TrainCTRs\001\Masks\Mask1\FrontBack
            pathMask = os.path.join(TRAIN_DIR, sub[-3:] + '\\CT Scan\\LeftRight')
            for root, dirs, files in os.walk(path):
                for name in files:
                    nume_poza_mask = name
                    found = 0
                    for root1, dirs1, files1 in os.walk(pathMask):
                        for name in files1:
                            if nume_poza_mask == name:
                                found = 1
                        self.assertEqual(found, 1, "[OnlyLeftLung\LeftRight']Nu am gasit imaginea: " + nume_poza_mask + " .")


    def test_RIGHTfrontBack(self):
        TRAIN_DIR = 'D:\\Git\\TrainCTRs'
        subfolders = [f.path for f in os.scandir(TRAIN_DIR) if f.is_dir()]
        for sub in subfolders:
            # print(sub[-3:])
            path = os.path.join(TRAIN_DIR, sub[-3:] + '\\Masks\\Mask1\\OnlyRightLung\\FrontBack')
            # D:\Git\TrainCTRs\001\Masks\Mask1\FrontBack
            pathMask = os.path.join(TRAIN_DIR, sub[-3:] + '\\CT Scan\\FrontBack')
            for root, dirs, files in os.walk(path):
                for name in files:
                    nume_poza_mask = name
                    found = 0
                    for root1, dirs1, files1 in os.walk(pathMask):
                        for name in files1:
                            if nume_poza_mask == name:
                                found = 1
                        self.assertEqual(found, 1, "[OnlyRightLung\FrontBack]Nu am gasit imaginea: " + nume_poza_mask + " .")



    def test_RIGHTtopBottom(self):
        TRAIN_DIR = 'D:\\Git\\TrainCTRs'
        subfolders = [f.path for f in os.scandir(TRAIN_DIR) if f.is_dir()]
        for sub in subfolders:
            # print(sub[-3:])
            path = os.path.join(TRAIN_DIR, sub[-3:] + '\\Masks\\Mask1\\OnlyRightLung\\TopBottom')
            # D:\Git\TrainCTRs\001\Masks\Mask1\FrontBack
            pathMask = os.path.join(TRAIN_DIR, sub[-3:] + '\\CT Scan\\TopBottom')
            for root, dirs, files in os.walk(path):
                for name in files:
                    nume_poza_mask = name
                    found = 0
                    for root1, dirs1, files1 in os.walk(pathMask):
                        for name in files1:
                            if nume_poza_mask == name:
                                found = 1
                        self.assertEqual(found, 1, "[OnlyRightLung\TopBottom]Nu am gasit imaginea: " + nume_poza_mask + " .")


    def test_RIGHTLeftRight(self):
        TRAIN_DIR = 'D:\\Git\\TrainCTRs'
        subfolders = [f.path for f in os.scandir(TRAIN_DIR) if f.is_dir()]
        for sub in subfolders:
            # print(sub[-3:])
            path = os.path.join(TRAIN_DIR, sub[-3:] + '\\Masks\\Mask1\\OnlyRightLung\\LeftRight')
            # D:\Git\TrainCTRs\001\Masks\Mask1\FrontBack
            pathMask = os.path.join(TRAIN_DIR, sub[-3:] + '\\CT Scan\\LeftRight')
            for root, dirs, files in os.walk(path)
                for name in files:
                    nume_poza_mask = name
                    found = 0
                    for root1, dirs1, files1 in os.walk(pathMask):
                        for name in files1:
                            if nume_poza_mask == name:
                                found = 1
                        self.assertEqual(found, 1, "[OnlyRightLung\LeftRight]Nu am gasit imaginea: " + nume_poza_mask + " .")



if __name__ == '__main__':
    unittest.main()

# CT SCAN IMAGES DON'T HAVE MASK

# def LEFTfrontBack():
#     TRAIN_DIR = 'D:\\Git\\TrainCTRs'
#     subfolders = [f.path for f in os.scandir(TRAIN_DIR) if f.is_dir()]
#     for sub in subfolders:
#         # print(sub[-3:])
#         path = os.path.join(TRAIN_DIR, sub[-3:] + '\\Masks\\Mask1\\OnlyLeftLung\\FrontBack')
#         # D:\Git\TrainCTRs\001\Masks\Mask1\FrontBack
#         pathMask = os.path.join(TRAIN_DIR, sub[-3:] + '\\CT Scan\\FrontBack')
#         for root, dirs, files in os.walk(pathMask):
#             for name in files:
#                 nume_poza_mask = name
#                 found = 0
#                 for root1, dirs1, files1 in os.walk(path):
#                     for name1 in files1:
#                         if nume_poza_mask == name1:
#                             found = 1
#                     if(found==0):
#                         print(name)
#
#
# def LEFTtopBottom():
#     TRAIN_DIR = 'D:\\Git\\TrainCTRs'
#     subfolders = [f.path for f in os.scandir(TRAIN_DIR) if f.is_dir()]
#     for sub in subfolders:
#         # print(sub[-3:])
#         path = os.path.join(TRAIN_DIR, sub[-3:] + '\\Masks\\Mask1\\OnlyLeftLung\\TopBottom')
#         # D:\Git\TrainCTRs\001\Masks\Mask1\FrontBack
#         pathMask = os.path.join(TRAIN_DIR, sub[-3:] + '\\CT Scan\\TopBottom')
#         for root, dirs, files in os.walk(pathMask):
#             for name in files:
#                 nume_poza_mask = name
#                 found = 0
#                 for root1, dirs1, files1 in os.walk(path):
#                     for name in files1:
#                         if nume_poza_mask == name:
#                             found = 1
#                     if(found==0):
#                         print(name)
#
#
# def LEFTLeftRight():
#     TRAIN_DIR = 'D:\\Git\\TrainCTRs'
#     subfolders = [f.path for f in os.scandir(TRAIN_DIR) if f.is_dir()]
#     for sub in subfolders:
#         # print(sub[-3:])
#         path = os.path.join(TRAIN_DIR, sub[-3:] + '\\Masks\\Mask1\\OnlyLeftLung\\LeftRight')
#         # D:\Git\TrainCTRs\001\Masks\Mask1\FrontBack
#         pathMask = os.path.join(TRAIN_DIR, sub[-3:] + '\\CT Scan\\LeftRight')
#         for root, dirs, files in os.walk(pathMask):
#             for name in files:
#                 nume_poza_mask = name
#                 found = 0
#                 for root1, dirs1, files1 in os.walk(path):
#                     for name in files1:
#                         if nume_poza_mask == name:
#                             found = 1
#                     if(found==0):
#                         print(name)
#
#
# def RIGHTfrontBack():
#     TRAIN_DIR = 'D:\\Git\\TrainCTRs'
#     subfolders = [f.path for f in os.scandir(TRAIN_DIR) if f.is_dir()]
#     for sub in subfolders:
#         # print(sub[-3:])
#         path = os.path.join(TRAIN_DIR, sub[-3:] + '\\Masks\\Mask1\\OnlyRightLung\\FrontBack')
#         # D:\Git\TrainCTRs\001\Masks\Mask1\FrontBack
#         pathMask = os.path.join(TRAIN_DIR, sub[-3:] + '\\CT Scan\\FrontBack')
#         for root, dirs, files in os.walk(pathMask):
#             for name in files:
#                 nume_poza_mask = name
#                 found = 0
#                 for root1, dirs1, files1 in os.walk(path):
#                     for name in files1:
#                         if nume_poza_mask == name:
#                             found = 1
#                     if(found==0):
#                         print(name)
#
#
#
# def RIGHTtopBottom():
#     TRAIN_DIR = 'D:\\Git\\TrainCTRs'
#     subfolders = [f.path for f in os.scandir(TRAIN_DIR) if f.is_dir()]
#     for sub in subfolders:
#         # print(sub[-3:])
#         path = os.path.join(TRAIN_DIR, sub[-3:] + '\\Masks\\Mask1\\OnlyRightLung\\TopBottom')
#         # D:\Git\TrainCTRs\001\Masks\Mask1\FrontBack
#         pathMask = os.path.join(TRAIN_DIR, sub[-3:] + '\\CT Scan\\TopBottom')
#         for root, dirs, files in os.walk(pathMask):
#             for name in files:
#                 nume_poza_mask = name
#                 found = 0
#                 for root1, dirs1, files1 in os.walk(path):
#                     for name in files1:
#                         if nume_poza_mask == name:
#                             found = 1
#                     if(found==0):
#                         print(name)
#
#
# def RIGHTLeftRight():
#     TRAIN_DIR = 'D:\\Git\\TrainCTRs'
#     subfolders = [f.path for f in os.scandir(TRAIN_DIR) if f.is_dir()]
#     for sub in subfolders:
#         # print(sub[-3:])
#         path = os.path.join(TRAIN_DIR, sub[-3:] + '\\Masks\\Mask1\\OnlyRightLung\\LeftRight')
#         # D:\Git\TrainCTRs\001\Masks\Mask1\FrontBack
#         pathMask = os.path.join(TRAIN_DIR, sub[-3:] + '\\CT Scan\\LeftRight')
#         for root, dirs, files in os.walk(pathMask):
#             for name in files:
#                 nume_poza_mask = name
#                 found = 0
#                 for root1, dirs1, files1 in os.walk(path):
#                     for name in files1:
#                         if nume_poza_mask == name:
#                             found = 1
#                     if(found==0):
#                         print(name)
#
# LEFTfrontBack()
# LEFTLeftRight()
# LEFTtopBottom()
# RIGHTfrontBack()
# RIGHTLeftRight()
# RIGHTtopBottom()