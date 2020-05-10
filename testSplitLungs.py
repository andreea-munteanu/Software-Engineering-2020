from splitLungss import isFinalDir
import os
import unittest

class MyTestCase(unittest.TestCase):
    def test_isFinalDir(self):
        directory = os.path.abspath('.')
        self.assertFalse(isFinalDir(directory))

    def test_equalNumberOfFiles(self):
        onlyleftlung = len(os.listdir( "C:\\Users\\User\\Desktop\\Software-Engineering-2020\\1-10\\001\\Masks\\Mask1\\OnlyLeftLung"))
        onlyrightlung = len(os.listdir( "C:\\Users\\User\\Desktop\\Software-Engineering-2020\\1-10\\001\\Masks\\Mask1\\OnlyRightLung"))
        self.assertEqual(onlyleftlung,onlyrightlung)

    def test_allInputFilesArePng(self):
        first = 0
        second = 0
        third = 0
        for root, dirs, files in os.walk("C:\\Users\\User\\Desktop\\Software-Engineering-2020\\1-10\\001\\Masks\\Mask1\\FrontBack"):
            for file in files:
                if file.endswith(".png"):
                    first = first + 1
        for root, dirs, files in os.walk("C:\\Users\\User\\Desktop\\Software-Engineering-2020\\1-10\\001\\Masks\\Mask1\\LeftRight"):
            for file in files:
                if file.endswith(".png"):
                    second = second + 1
        for root, dirs, files in os.walk("C:\\Users\\User\\Desktop\\Software-Engineering-2020\\1-10\\001\\Masks\\Mask1\\TopBottom"):
            for file in files:
                if file.endswith(".png"):
                    third = third + 1
        nr = len(os.listdir("C:\\Users\\User\\Desktop\\Software-Engineering-2020\\1-10\\001\\Masks\\Mask1\\FrontBack"))
        nr2 = len(os.listdir("C:\\Users\\User\\Desktop\\Software-Engineering-2020\\1-10\\001\\Masks\\Mask1\\LeftRight"))
        nr3 = len(os.listdir("C:\\Users\\User\\Desktop\\Software-Engineering-2020\\1-10\\001\\Masks\\Mask1\\TopBottom"))
        self.assertTrue(first,nr)
        self.assertTrue(second, nr2)
        self.assertTrue(third, nr3)

    def test_allOutputFilesArePng(self):
        first = 0
        second = 0
        third = 0
        for root, dirs, files in os.walk(
                "C:\\Users\\User\\Desktop\\Software-Engineering-2020\\1-10\\001\\Masks\\Mask1\\OnlyLeftLung\\FrontBack"):
            for file in files:
                if file.endswith(".png"):
                    first = first + 1
        for root, dirs, files in os.walk(
                "C:\\Users\\User\\Desktop\\Software-Engineering-2020\\1-10\\001\\Masks\\Mask1\\OnlyLeftLung\\LeftRight"):
            for file in files:
                if file.endswith(".png"):
                    second = second + 1
        for root, dirs, files in os.walk(
                "C:\\Users\\User\\Desktop\\Software-Engineering-2020\\1-10\\001\\Masks\\Mask1\\OnlyLeftLung\\TopBottom"):
            for file in files:
                if file.endswith(".png"):
                    third = third + 1
        first1 = 0
        second1 = 0
        third1 = 0
        for root, dirs, files in os.walk(
                "C:\\Users\\User\\Desktop\\Software-Engineering-2020\\1-10\\001\\Masks\\Mask1\\OnlyRightLung\\FrontBack"):
            for file in files:
                if file.endswith(".png"):
                    first1 = first1 + 1
        for root, dirs, files in os.walk(
                "C:\\Users\\User\\Desktop\\Software-Engineering-2020\\1-10\\001\\Masks\\Mask1\\OnlyRightLung\\LeftRight"):
            for file in files:
                if file.endswith(".png"):
                    second1 = second1 + 1
        for root, dirs, files in os.walk(
                "C:\\Users\\User\\Desktop\\Software-Engineering-2020\\1-10\\001\\Masks\\Mask1\\OnlyRightLung\\TopBottom"):
            for file in files:
                if file.endswith(".png"):
                    third1 = third1 + 1
        nr1 = len(os.listdir("C:\\Users\\User\\Desktop\\Software-Engineering-2020\\1-10\\001\\Masks\\Mask1\\OnlyLeftLung\\FrontBack"))
        nr2 = len(os.listdir("C:\\Users\\User\\Desktop\\Software-Engineering-2020\\1-10\\001\\Masks\\Mask1\\OnlyLeftLung\\LeftRight"))
        nr3 = len(os.listdir("C:\\Users\\User\\Desktop\\Software-Engineering-2020\\1-10\\001\\Masks\\Mask1\\OnlyLeftLung\\TopBottom"))
        nr11 = len(os.listdir("C:\\Users\\User\\Desktop\\Software-Engineering-2020\\1-10\\001\\Masks\\Mask1\\OnlyRightLung\\FrontBack"))
        nr12 = len(os.listdir("C:\\Users\\User\\Desktop\\Software-Engineering-2020\\1-10\\001\\Masks\\Mask1\\OnlyRightLung\\LeftRight"))
        nr13 = len(os.listdir("C:\\Users\\User\\Desktop\\Software-Engineering-2020\\1-10\\001\\Masks\\Mask1\\OnlyRightLung\\TopBottom"))
        self.assertTrue(first, nr1)
        self.assertTrue(second, nr2)
        self.assertTrue(third, nr3)
        self.assertTrue(first1, nr11)
        self.assertTrue(second1, nr12)
        self.assertTrue(third1, nr13)

    def test_inputDirectoriesExist(self):
        self.assertTrue(os.path.isdir("C:\\Users\\User\\Desktop\\Software-Engineering-2020\\1-10\\001\\Masks\\Mask1\\TopBottom"))
        self.assertTrue(os.path.isdir("C:\\Users\\User\\Desktop\\Software-Engineering-2020\\1-10\\001\\Masks\\Mask1\\LeftRight"))
        self.assertTrue(os.path.isdir("C:\\Users\\User\\Desktop\\Software-Engineering-2020\\1-10\\001\\Masks\\Mask1\\FrontBack"))

    def test_outputDirectoriesExist(self):
        self.assertTrue(os.path.isdir("C:\\Users\\User\\Desktop\\Software-Engineering-2020\\1-10\\001\\Masks\\Mask1\\OnlyLeftLung"))
        self.assertTrue(os.path.isdir("C:\\Users\\User\\Desktop\\Software-Engineering-2020\\1-10\\001\\Masks\\Mask1\\OnlyRightLung"))

    def test_outputDirectoriesNotEmpty(self):
        self.assertNotEqual(len(os.listdir("C:\\Users\\User\\Desktop\\Software-Engineering-2020\\1-10\\001\\Masks\\Mask1\\OnlyLeftLung\\TopBottom")),0)
        self.assertNotEqual(len(os.listdir("C:\\Users\\User\\Desktop\\Software-Engineering-2020\\1-10\\001\\Masks\\Mask1\\OnlyLeftLung\\FrontBack")),0)
        self.assertNotEqual(len(os.listdir("C:\\Users\\User\\Desktop\\Software-Engineering-2020\\1-10\\001\\Masks\\Mask1\\OnlyLeftLung\\LeftRight")),0)
        self.assertNotEqual(len(os.listdir("C:\\Users\\User\\Desktop\\Software-Engineering-2020\\1-10\\001\\Masks\\Mask1\\OnlyLeftLung")),0)
        self.assertNotEqual(len(os.listdir("C:\\Users\\User\\Desktop\\Software-Engineering-2020\\1-10\\001\\Masks\\Mask1\\OnlyRightLung\\TopBottom")),0)
        self.assertNotEqual(len(os.listdir("C:\\Users\\User\\Desktop\\Software-Engineering-2020\\1-10\\001\\Masks\\Mask1\\OnlyRightLung\\FrontBack")),0)
        self.assertNotEqual(len(os.listdir("C:\\Users\\User\\Desktop\\Software-Engineering-2020\\1-10\\001\\Masks\\Mask1\\OnlyRightLung\\LeftRight")),0)
        self.assertNotEqual(len(os.listdir("C:\\Users\\User\\Desktop\\Software-Engineering-2020\\1-10\\001\\Masks\\Mask1\\OnlyRightLung")),0)

    def test_inputDirectoriesNotEmpty(self):
        self.assertNotEqual(len(os.listdir("C:\\Users\\User\\Desktop\\Software-Engineering-2020\\1-10\\001\\Masks\\Mask1\\TopBottom")),0)
        self.assertNotEqual(len(os.listdir("C:\\Users\\User\\Desktop\\Software-Engineering-2020\\1-10\\001\\Masks\\Mask1\\FrontBack")),0)
        self.assertNotEqual(len(os.listdir("C:\\Users\\User\\Desktop\\Software-Engineering-2020\\1-10\\001\\Masks\\Mask1\\LeftRight")),0)

    def test_allLungsHaveBeenSplit(self):
        frontback = len(os.listdir("C:\\Users\\User\\Desktop\\Software-Engineering-2020\\1-10\\001\\Masks\\Mask1\\FrontBack"))
        leftlung_frontback = len(os.listdir("C:\\Users\\User\\Desktop\\Software-Engineering-2020\\1-10\\001\\Masks\\Mask1\\OnlyLeftLung\\FrontBack"))
        rightlung_frontback = len(os.listdir("C:\\Users\\User\\Desktop\\Software-Engineering-2020\\1-10\\001\\Masks\\Mask1\\OnlyRightLung\\FrontBack"))
        self.assertEqual(frontback,leftlung_frontback)
        self.assertEqual(frontback,rightlung_frontback)

if __name__ == '__main__':
    unittest.main()
