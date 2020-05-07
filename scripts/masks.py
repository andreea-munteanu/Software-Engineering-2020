# Version 1.1
import os

import cv2


def count_files_dirs_walk(path, target):
    for file in os.listdir(path):
        root, ext = os.path.splitext(file)
        _end = [x + '\\' + file for x in target]
        [os.mkdir(x) for x in _end]
        _path = os.path.join(path, root)
        _path_ct = _path + '\\CT Scan'
        for _file in os.listdir(_path_ct):
            _current_path = os.path.join(_path_ct, _file)
            _path_masks = [_current_path.replace("CT Scan", "Masks\Mask1\OnlyRightLung"),
                           _current_path.replace("CT Scan", "Masks\Mask1\OnlyLeftLung")]
            for i in range(len(_path_masks)):
                __end = _end[i] + '\\' + _file
                os.mkdir(__end)
                for root, dirs, files in os.walk(_path_masks[i]):
                    for name in files:
                        mask = cv2.imread(os.path.join(root, name))
                        image = cv2.imread(os.path.join(_current_path, name))
                        mask = cv2.resize(mask, image.shape[1::-1])
                        dst1 = cv2.bitwise_and(image, mask)
                        cv2.imwrite(__end + '\\' + name, dst1)


def apply_masks():
    paths_train_source = 'D:\\JetBrains\\FII\\Git\\Software-Engineering-2020\\TrainCTRs'
    paths_train_target = ['D:\\JetBrains\\FII\\Git\\Software-Engineering-2020\\Right',
                          'D:\\JetBrains\\FII\\Git\\Software-Engineering-2020\\Left']
    paths_test_source = 'D:\\JetBrains\\FII\\Git\\Software-Engineering-2020\\TestCTRs'
    paths_test_target = ['D:\\JetBrains\\FII\\Git\\Software-Engineering-2020\\Test\\Right',
                         'D:\\JetBrains\\FII\\Git\\Software-Engineering-2020\\Test\\Left']
    paths = [[paths_train_source, paths_train_target], [paths_test_source, paths_test_target]]
    print('Applying masks...')
    for path in paths:
        count_files_dirs_walk(path[0], path[1])
    print('Masks applied')
