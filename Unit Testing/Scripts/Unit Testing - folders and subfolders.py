import unittest
import os


class TestCase(unittest.TestCase):  # Testare daca exista masti Masks pentru CT Scan images
    def test_LEFTfrontBack(self):
        TRAIN_DIR = 'D:\\Git\\TrainCTRs'
        countNumePozaMask = 0
        countNumePozaCTScan = 0
        subfoldersCTScan = 0
        subfodersMask = 0
        subfolders = [f.path for f in os.scandir(TRAIN_DIR) if f.is_dir()]
        for sub in subfolders:
            # print(sub[-3:])
            subfodersMask = sub[-3:]
            path = os.path.join(TRAIN_DIR, sub[-3:] + '\\Masks\\Mask1\\OnlyLeftLung\\FrontBack')
            # D:\Git\TrainCTRs\001\Masks\Mask1\FrontBack
            for root, dirs, files in os.walk(path):
                for name in files:
                    nume_poza_mask = name
                    countNumePozaMask = countNumePozaMask + 1
        for sub in subfolders:
            # print(sub[-3:])
            subfoldersCTScan = sub[-3:]
            # D:\Git\TrainCTRs\001\Masks\Mask1\FrontBack
            pathMask = os.path.join(TRAIN_DIR, sub[-3:] + '\\CT Scan\\FrontBack')
            for root1, dirs1, files1 in os.walk(pathMask):
                for name1 in files:
                    nume_poza_CTScan = name1
                    countNumePozaCTScan = countNumePozaCTScan + 1
        self.assertEqual(subfodersMask, subfoldersCTScan, "[OnlyLeftLung\FrontBack']Numarul de foldere din CT Scan nu corespunde cu numarul de foldere din Mask1 (numar subfoldere de forma XYZ din CT Scan " + str(subfoldersCTScan) +  ", numar subfoldere de forma XYZ din Mask1" + str(subfodersMask) + ".)")

    def test_LEFTtopBottom(self):
        TRAIN_DIR = 'D:\\Git\\TrainCTRs'
        countNumePozaMask = 0
        countNumePozaCTScan = 0
        subfoldersCTScan = 0
        subfodersMask = 0
        subfolders = [f.path for f in os.scandir(TRAIN_DIR) if f.is_dir()]
        for sub in subfolders:
            # print(sub[-3:])
            subfodersMask = sub[-3:]
            path = os.path.join(TRAIN_DIR, sub[-3:] + '\\Masks\\Mask1\\OnlyLeftLung\\TopBottom')
            # D:\Git\TrainCTRs\001\Masks\Mask1\FrontBack
            for root, dirs, files in os.walk(path):
                for name in files:
                    nume_poza_mask = name
                    countNumePozaMask = countNumePozaMask + 1
        for sub in subfolders:
            # print(sub[-3:])
            subfoldersCTScan = sub[-3:]
            # D:\Git\TrainCTRs\001\Masks\Mask1\FrontBack
            pathMask = os.path.join(TRAIN_DIR, sub[-3:] + '\\CT Scan\\TopBottom')
            for root1, dirs1, files1 in os.walk(pathMask):
                for name1 in files:
                    nume_poza_CTScan = name1
                    countNumePozaCTScan = countNumePozaCTScan + 1
        self.assertEqual(subfodersMask, subfoldersCTScan,"[OnlyLeftLung\TopBottom']Numarul de foldere din CT Scan nu corespunde cu numarul de foldere din Mask1 (numar subfoldere de forma XYZ din CT Scan " + str(subfoldersCTScan) + ", numar subfoldere de forma XYZ din Mask1" + str(subfodersMask) + ".)")


    def test_LEFTLeftRight(self):
        TRAIN_DIR = 'D:\\Git\\TrainCTRs'
        countNumePozaMask = 0
        countNumePozaCTScan = 0
        subfoldersCTScan = 0
        subfodersMask = 0
        subfolders = [f.path for f in os.scandir(TRAIN_DIR) if f.is_dir()]
        for sub in subfolders:
            # print(sub[-3:])
            subfodersMask = sub[-3:]
            path = os.path.join(TRAIN_DIR, sub[-3:] + '\\Masks\\Mask1\\OnlyLeftLung\\LeftRight')
            # D:\Git\TrainCTRs\001\Masks\Mask1\FrontBack
            for root, dirs, files in os.walk(path):
                for name in files:
                    nume_poza_mask = name
                    countNumePozaMask = countNumePozaMask + 1
        for sub in subfolders:
            # print(sub[-3:])
            subfoldersCTScan = sub[-3:]
            # D:\Git\TrainCTRs\001\Masks\Mask1\FrontBack
            pathMask = os.path.join(TRAIN_DIR, sub[-3:] + '\\CT Scan\\LeftRight')
            for root1, dirs1, files1 in os.walk(pathMask):
                for name1 in files:
                    nume_poza_CTScan = name1
                    countNumePozaCTScan = countNumePozaCTScan + 1
        self.assertEqual(subfodersMask, subfoldersCTScan,"[OnlyLeftLung\LeftRight']Numarul de foldere din CT Scan nu corespunde cu numarul de foldere din Mask1 (numar subfoldere de forma XYZ din CT Scan " + str(subfoldersCTScan) + ", numar subfoldere de forma XYZ din Mask1" + str(subfodersMask) + ".)")


    def test_RIGHTfrontBack(self):
        TRAIN_DIR = 'D:\\Git\\TrainCTRs'
        countNumePozaMask = 0
        countNumePozaCTScan = 0
        subfoldersCTScan = 0
        subfodersMask = 0
        subfolders = [f.path for f in os.scandir(TRAIN_DIR) if f.is_dir()]
        for sub in subfolders:
            # print(sub[-3:])
            subfodersMask = sub[-3:]
            path = os.path.join(TRAIN_DIR, sub[-3:] + '\\Masks\\Mask1\\OnlyRightLung\\FrontBack')
            # D:\Git\TrainCTRs\001\Masks\Mask1\FrontBack
            for root, dirs, files in os.walk(path):
                for name in files:
                    nume_poza_mask = name
                    countNumePozaMask = countNumePozaMask + 1
        for sub in subfolders:
            # print(sub[-3:])
            subfoldersCTScan = sub[-3:]
            # D:\Git\TrainCTRs\001\Masks\Mask1\FrontBack
            pathMask = os.path.join(TRAIN_DIR, sub[-3:] + '\\CT Scan\\FrontBack')
            for root1, dirs1, files1 in os.walk(pathMask):
                for name1 in files:
                    nume_poza_CTScan = name1
                    countNumePozaCTScan = countNumePozaCTScan + 1
        self.assertEqual(subfodersMask, subfoldersCTScan, "[OnlyRightLung\FrontBack']Numarul de foldere din CT Scan nu corespunde cu numarul de foldere din Mask1 (numar subfoldere de forma XYZ din CT Scan " + str(subfoldersCTScan) +  ", numar subfoldere de forma XYZ din Mask1" + str(subfodersMask) + ".)")

    def test_RIGHTtopBottom(self):
        TRAIN_DIR = 'D:\\Git\\TrainCTRs'
        countNumePozaMask = 0
        countNumePozaCTScan = 0
        subfoldersCTScan = 0
        subfodersMask = 0
        subfolders = [f.path for f in os.scandir(TRAIN_DIR) if f.is_dir()]
        for sub in subfolders:
            # print(sub[-3:])
            subfodersMask = sub[-3:]
            path = os.path.join(TRAIN_DIR, sub[-3:] + '\\Masks\\Mask1\\OnlyLeftLung\\TopBottom')
            # D:\Git\TrainCTRs\001\Masks\Mask1\FrontBack
            for root, dirs, files in os.walk(path):
                for name in files:
                    nume_poza_mask = name
                    countNumePozaMask = countNumePozaMask + 1
        for sub in subfolders:
            # print(sub[-3:])
            subfoldersCTScan = sub[-3:]
            # D:\Git\TrainCTRs\001\Masks\Mask1\FrontBack
            pathMask = os.path.join(TRAIN_DIR, sub[-3:] + '\\CT Scan\\TopBottom')
            for root1, dirs1, files1 in os.walk(pathMask):
                for name1 in files:
                    nume_poza_CTScan = name1
                    countNumePozaCTScan = countNumePozaCTScan + 1
        self.assertEqual(subfodersMask, subfoldersCTScan,"[OnlyRightLung\TopBottom']Numarul de foldere din CT Scan nu corespunde cu numarul de foldere din Mask1 (numar subfoldere de forma XYZ din CT Scan " + str(subfoldersCTScan) + ", numar subfoldere de forma XYZ din Mask1" + str(subfodersMask) + ".)")


    def test_RIGHTLeftRight(self):
        TRAIN_DIR = 'D:\\Git\\TrainCTRs'
        countNumePozaMask = 0
        countNumePozaCTScan = 0
        subfoldersCTScan = 0
        subfodersMask = 0
        subfolders = [f.path for f in os.scandir(TRAIN_DIR) if f.is_dir()]
        for sub in subfolders:
            # print(sub[-3:])
            subfodersMask = sub[-3:]
            path = os.path.join(TRAIN_DIR, sub[-3:] + '\\Masks\\Mask1\\OnlyRightLung\\LeftRight')
            # D:\Git\TrainCTRs\001\Masks\Mask1\FrontBack
            for root, dirs, files in os.walk(path):
                for name in files:
                    nume_poza_mask = name
                    countNumePozaMask = countNumePozaMask + 1
        for sub in subfolders:
            # print(sub[-3:])
            subfoldersCTScan = sub[-3:]
            # D:\Git\TrainCTRs\001\Masks\Mask1\FrontBack
            pathMask = os.path.join(TRAIN_DIR, sub[-3:] + '\\CT Scan\\LeftRight')
            for root1, dirs1, files1 in os.walk(pathMask):
                for name1 in files:
                    nume_poza_CTScan = name1
                    countNumePozaCTScan = countNumePozaCTScan + 1
        self.assertEqual(subfodersMask, subfoldersCTScan,"[OnlyRightLung\LeftRight']Numarul de foldere din CT Scan nu corespunde cu numarul de foldere din Mask1 (numar subfoldere de forma XYZ din CT Scan " + str(subfoldersCTScan) + ", numar subfoldere de forma XYZ din Mask1" + str(subfodersMask) + ".)")


if __name__ == '__main__':
    unittest.main()
