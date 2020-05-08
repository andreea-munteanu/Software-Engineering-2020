#initial, simple, raw, mask application algorithm

import numpy as np
from PIL import Image
import os


def left_masks_right_lung():
    os.mkdir('D:\\Software Engineering\\Processed-Images-Right')

    for root, dirs, files in os.walk("D:\\Software Engineering\\TrainCTRs"):
        for root1, dirs1, files1 in os.walk(root):

            if root1.endswith('Masks'):
                path = 'D:\\Software Engineering\\Processed-Images-Right\\' + root1[-9:-6]
                os.mkdir(path)
                pathFB = path + '\\FrontBack'
                os.mkdir(pathFB)
                pathLR = path + '\\LeftRight'
                os.mkdir(pathLR)
                pathTB = path + '\\TopBottom'
                os.mkdir(pathTB)
                for root4, dirs4, files4 in os.walk(root1):
                    if root4.endswith('Mask1'):
                        for root2, dirs2, files2 in os.walk(root4):
                            if (root2.endswith('OnlyLeftLung')):
                                for root3, dirs3, files3 in os.walk(root4):

                                    if (root3.endswith('OnlyLeftLung\\FrontBack')):
                                        for name in files3:
                                            mask = root3
                                            aux_mask = mask.replace('Masks\\Mask1\\OnlyLeftLung', 'CT Scan')
                                            src = np.array(Image.open(aux_mask + '\\' + name))
                                            mask1 = np.array(
                                                Image.open(root3 + '\\' + name).resize(
                                                    src.shape[1::-1], Image.BILINEAR))
                                            mask1 = mask1 / 255
                                            dst = src * mask1
                                            Image.fromarray(dst.astype(np.uint8)).save(pathFB + '\\' + name)
                                            print(name)

                                    if (root3.endswith('OnlyLeftLung\\LeftRight')):
                                        for name in files3:
                                            mask = root3
                                            aux_mask = mask.replace('Masks\\Mask1\\OnlyLeftLung', 'CT Scan')
                                            src = np.array(Image.open(aux_mask + '\\' + name))
                                            mask1 = np.array(
                                                Image.open(root3 + '\\' + name).resize(
                                                    src.shape[1::-1], Image.BILINEAR))
                                            mask1 = mask1 / 255
                                            dst = src * mask1
                                            Image.fromarray(dst.astype(np.uint8)).save(pathLR + '\\' + name)
                                            print(name)

                                    if (root3.endswith('OnlyLeftLung\\TopBottom')):
                                        for name in files3:
                                            mask = root3
                                            aux_mask = mask.replace('Masks\\Mask1\\OnlyLeftLung', 'CT Scan')
                                            src = np.array(Image.open(aux_mask + '\\' + name))
                                            mask1 = np.array(
                                                Image.open(root3 + '\\' + name).resize(
                                                    src.shape[1::-1], Image.BILINEAR))
                                            mask1 = mask1 / 255
                                            dst = src * mask1
                                            Image.fromarray(dst.astype(np.uint8)).save(pathTB + '\\' + name)
                                            print(name)
                                break

        break


def right_masks_left_lung():
    os.mkdir('D:\\Software Engineering\\Processed-Images-Left')

    for root, dirs, files in os.walk("D:\\Software Engineering\\TrainCTRs"):
        for root1, dirs1, files1 in os.walk(root):

            if root1.endswith('Masks'):
                path = 'D:\\Software Engineering\\Processed-Images-Left\\' + root1[-9:-6]
                os.mkdir(path)
                pathFB = path + '\\FrontBack'
                os.mkdir(pathFB)
                pathLR = path + '\\LeftRight'
                os.mkdir(pathLR)
                pathTB = path + '\\TopBottom'
                os.mkdir(pathTB)
                for root4, dirs4, files4 in os.walk(root1):
                    if root4.endswith('Mask1'):
                        for root2, dirs2, files2 in os.walk(root4):
                            if (root2.endswith('OnlyRightLung')):
                                for root3, dirs3, files3 in os.walk(root4):

                                    if (root3.endswith('OnlyRightLung\\FrontBack')):
                                        for name in files3:
                                            mask = root3
                                            aux_mask = mask.replace('Masks\\Mask1\\OnlyRightLung', 'CT Scan')
                                            src = np.array(Image.open(aux_mask + '\\' + name))
                                            mask1 = np.array(
                                                Image.open(root3 + '\\' + name).resize(
                                                    src.shape[1::-1], Image.BILINEAR))
                                            mask1 = mask1 / 255
                                            dst = src * mask1
                                            Image.fromarray(dst.astype(np.uint8)).save(pathFB + '\\' + name)
                                            print(name)

                                    if (root3.endswith('OnlyRightLung\\LeftRight')):
                                        for name in files3:
                                            mask = root3
                                            aux_mask = mask.replace('Masks\\Mask1\\OnlyRightLung', 'CT Scan')
                                            src = np.array(Image.open(aux_mask + '\\' + name))
                                            mask1 = np.array(
                                                Image.open(root3 + '\\' + name).resize(
                                                    src.shape[1::-1], Image.BILINEAR))
                                            mask1 = mask1 / 255
                                            dst = src * mask1
                                            Image.fromarray(dst.astype(np.uint8)).save(pathLR + '\\' + name)
                                            print(name)

                                    if (root3.endswith('OnlyRightLung\\TopBottom')):
                                        for name in files3:
                                            mask = root3
                                            aux_mask = mask.replace('Masks\\Mask1\\OnlyRightLung', 'CT Scan')
                                            src = np.array(Image.open(aux_mask + '\\' + name))
                                            mask1 = np.array(
                                                Image.open(root3 + '\\' + name).resize(
                                                    src.shape[1::-1], Image.BILINEAR))
                                            mask1 = mask1 / 255
                                            dst = src * mask1
                                            Image.fromarray(dst.astype(np.uint8)).save(pathTB + '\\' + name)
                                            print(name)
                                break

        break


right_masks_left_lung()
left_masks_right_lung()