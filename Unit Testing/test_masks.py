import unittest
import os
from os import path

# 1) imagini random puse intr-un folder, pathul catre folderul ala. outputul va fi un test
# 2) path catre un folder care nu are nimic si sa obtinem o eroare
# 3) test daca se creeaza directoarele si daca se scrie imaginea

class MyTestCase(unittest.TestCase) :
    # checks the path for a given directory (containing random images we add to directory) is correct
    def test_path(self) :
        # add picture to directory. if directory does not exist, create it
        directory = 'D:\\Facultate\\Anul_II\\Sem_II\\IP\\Processed-Images-Left\\001\\FrontBack'
        picture = 'D:\\Facultate\\Anul_II\\Sem_II\\IP\\Processed-Images-Left\\001\\FrontBack\\CTR_TRN_001_z193.png'
        file_path = os.path.join(directory, picture)
        if not os.path.isdir(directory) :
            os.mkdir(directory)
        file = open(file_path, "w")
        file.write(directory)
        file.close()
        # # picture in folder is file or subdirectory?
        # print(picture + " is file: " + str(os.path.isfile(picture)))
        # # making sure the path is a directory
        # print(directory + " is directory: " + str(os.path.isdir(directory)))
        print("File exists:" + str(path.exists(picture)))
        print("File exists:" + str(path.exists('random-picture-name-for-test')))
        # if the path to the given directory exists
        print("Directory exists:" + str(path.exists(directory)))

    # checks whether a path leads to an empty directory --> error
    def test_empty_folder(self) :
        # take directory at random
        directory = 'D:\\Facultate\\Anul_II\\Sem_II\\IP\\Processed-Images-Left\\001\\FrontBack'
        # checking whether the path to the given directory exists
        if os.path.exists(directory) and os.path.isdir(directory) :
            print("Directory exists: True")
            if not os.listdir(directory) :
                print("Directory is empty: " + str(path.exists(directory)))
        else :
            print("Directory exists: False")

    # are the directories created? is the image added to the directory?
    def test_created_directories(self) :
        # path of the directory
        directory = 'D:\\Facultate\\Anul_II\\Sem_II\\IP\\Processed-Images-Left\\001\\FrontBack'
        picture = 'D:\\Facultate\\Anul_II\\Sem_II\\IP\\Processed-Images-Left\\001\\FrontBack\\CTR_TRN_001_z209.png'
        # does the directory exist? is the picture copied in the directory?
        if os.path.exists(directory) and os.path.isdir(directory) :
            print("Directory exists: True")
            if not os.listdir(directory) :  # comparing the returned list to empty list
                print("Directory is empty: True")
            else :
                print("Directory is empty: False")
                # we now look for our picture with the given path
                found = False
                for fname in os.listdir('.') :
                    if fname == picture :
                        # we found our picture. yay
                        found = True
                        print("Directory contains the right picture: True")
                if not found :
                    print("Directory contains right picture: False")
        else :
            print("Directory exists: False")


if __name__ == '__main__' :
    unittest.main()
