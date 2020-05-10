# Version 1.1
# TODO: write test ->
import csv
import datetime
import os

import numpy as np
from joblib import dump, load
from keras.preprocessing import image
from sklearn import svm

from constants import image_files, label_files

paths = ['D:\\JetBrains\\FII\\Git\\Software-Engineering-2020\\Train',
         'D:\\JetBrains\\FII\\Git\\Software-Engineering-2020\\Test\\Left']

target = 'D:\\JetBrains\\FII\\IP-2\\target'


def count():
    with open('CT_Report.csv', newline='') as patients:
        reader = csv.reader(patients, delimiter=',')
        reader = list(reader)
        result = []
        for j in range(1, 7):
            count0 = 0
            count1 = 0
            for i in reader:
                if i[j] == '0':
                    count0 += 1
                if i[j] == '1':
                    count1 += 1
            result.append([count0, count1])
        return result


def separate(counts):
    with open('CT_Report.csv', newline='') as patients:
        reader = csv.reader(patients, delimiter=',')
        reader = list(reader)
        result = []
        for i in range(len(counts)):
            counter = min(counts[i])
            unaffected = []
            affected = []
            for row in reader:
                if 0 <= i < 2:
                    if row[i + 1] == '1' and len(affected) < counter + 15:
                        affected.append(row[0])
                    if row[i + 1] == '0' and len(unaffected) < counter:
                        unaffected.append(row[0])
                if 2 <= i < 4:
                    if row[i + 1] == '1' and len(affected) < counter:
                        affected.append(row[0])
                    if row[i + 1] == '0' and len(unaffected) < counter + 15:
                        unaffected.append(row[0])
                if 4 <= i < 6:
                    if row[i + 1] == '1' and len(affected) < counter:
                        affected.append(row[0])
                    if row[i + 1] == '0' and len(unaffected) < counter + 10:
                        unaffected.append(row[0])
            result.append([affected, unaffected])
        return result


def get_column(side, region):
    regions = [[1, 3, 5], [2, 4, 6]]
    return regions[side][region]


def create_arrays(path, counts):
    with open('CT_Report.csv', newline='') as patients:
        reader = csv.reader(patients, delimiter=',')
        reader = list(reader)
        file_name = ['left', 'right']
        region_type = ['lung', 'caverns', 'pleurisy']
        file_ext = ['fb', 'lr', 'tb']
        final_files = ['%s-%s.npy' % (x, y) for x in file_name for y in file_ext]
        final_label_files = ['%s-%s-%s.npy' % (x, y, z) for x in file_name for y in file_ext for z in region_type]
        image_data = [[[], [], []], [[], [], []]]
        labels = [[[[], [], []], [[], [], []], [[], [], []]], [[[], [], []], [[], [], []], [[], [], []]]]
        for file in os.listdir(path[0]):
            file_path = os.path.join(path[0], file)
            side = 0 if file == 'Left' else 1
            for _file in os.listdir(file_path):
                _path = os.path.join(file_path, _file)
                for dirs in os.listdir(_path):
                    region = 0 if dirs == 'FrontBack' else 1 if dirs == 'LeftRight' else 2
                    if _file in counts[3 * side + region][0] or _file in counts[3 * side + region][1]:
                        __path = os.path.join(_path, dirs)
                        for __file in os.listdir(__path):
                            img = image.img_to_array(image.load_img(os.path.join(__path, __file), target_size=(32, 32)))
                            image_data[side][region].append(img)
                            for i in range(3):
                                labels[side][region][i].append(reader[int(_file) - 1][get_column(side, i)])
        for side in range(len(image_data)):
            for region in range(len(image_data[side])):
                data = np.array(image_data[side][region], dtype='float32') / 255.0
                m = data.shape[0]
                data = data.reshape(m, -1)
                np.save(os.path.join(target, final_files[3 * side + region]), data)
                for i in range(3):
                    label = np.array(labels[side][region][i])
                    np.save(os.path.join(target, 'labels', final_label_files[9 * side + 3 * region + i]), label)


def run(saved=False):
    print('Fitting...')
    svm_array = [[[[], [], []], [[], [], []], [[], [], []]], [[[], [], []], [[], [], []], [[], [], []]]]
    if saved:
        for i in range(2):
            for j in range(3):
                for k in range(3):
                    svm_array[i][j][k] = svm.SVC(kernel='rbf', C=1.0)
        for i in range(2):
            for j in range(3):
                for k in range(3):
                    svm_array[i][j][k] = load(str(i) + str(j) + str(k) + '.joblib')
    else:
        image_data = [[[], [], []], [[], [], []]]
        labels = [[[[], [], []], [[], [], []], [[], [], []]], [[[], [], []], [[], [], []], [[], [], []]]]
        for i in range(2):
            for j in range(3):
                image_data[i][j] = np.load(os.path.join(target, image_files[3 * i + j]))
                for z in range(3):
                    labels[i][j][z] = np.load(os.path.join(target, "labels", label_files[9 * i + 3 * j + z]))
        for i in range(2):
            for j in range(3):
                for k in range(3):
                    svm_array[i][j][k] = svm.SVC(kernel='rbf', C=1.0)
        for i in range(2):
            for j in range(3):
                for k in range(3):
                    svm_array[i][j][k].fit(image_data[i][j], labels[i][j][k])
                    dump(svm_array[i][j][k], str(i) + str(j) + str(k) + '.joblib')
    print('Fitted')
    out = open('results.csv', 'w', newline='')
    fields = ['Filename', 'LeftLungAffected', 'RightLungAffected', 'CavernsLeft', 'CavernsRight', 'PleurisyLeft',
              'PleurisyRight']
    writer = csv.DictWriter(out, fieldnames=fields)
    writer.writeheader()
    for file in os.listdir(paths[1]):
        location = [paths[1], paths[1].replace("Left", "Right")]
        test_data = [[[], [], []], [[], [], []]]
        for i in range(len(location)):
            for dirs in os.listdir(os.path.join(location[i], file)):
                region = 0 if dirs == 'FrontBack' else 1 if dirs == 'LeftRight' else 2
                _path = os.path.join(location[i], file, dirs)
                for _file in os.listdir(_path):
                    img = image.img_to_array(image.load_img(os.path.join(_path, _file), target_size=(32, 32)))
                    test_data[i][region].append(img)
        for i in range(2):
            for j in range(3):
                test_data[i][j] = np.array(test_data[i][j], dtype='float32') / 255.0
                m = test_data[i][j].shape[0]
                test_data[i][j] = test_data[i][j].reshape(m, -1)
        results = [[[[], [], []], [[], [], []], [[], [], []]], [[[], [], []], [[], [], []], [[], [], []]]]
        for i in range(2):
            for j in range(3):
                for k in range(3):
                    results[i][j][k] = svm_array[i][j][k].predict(test_data[i][j])
        final_result = [[[], [], []], [[], [], []]]
        for i in range(2):
            for j in range(3):
                final_result[i][j] = np.round(np.average([np.count_nonzero(arr == '1') / (
                        np.count_nonzero(arr == '1') + np.count_nonzero(arr == '0')) for arr in results[i][j]]), 2)
        writer.writerow(
            {'Filename': file, 'LeftLungAffected': final_result[0][0], 'RightLungAffected': final_result[1][0],
             'CavernsLeft': final_result[0][1], 'CavernsRight': final_result[1][1],
             'PleurisyLeft': final_result[0][2], 'PleurisyRight': final_result[1][2]})


def driver():
    print(datetime.datetime.now())
    create_arrays(paths, separate(count()))
    run(saved=True)
    print(datetime.datetime.now())


driver()
