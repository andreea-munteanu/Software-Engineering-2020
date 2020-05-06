# TODO: rewrite run and create array to support both sides at the same time -> array[]
# TODO: write test ->
# TODO: add unhealthy to right/left
# TODO: add healthy to caverns/pleurisy
# TODO: create directories for .npy files
import csv
import datetime
import os

import numpy as np
from joblib import dump
from keras.preprocessing import image
from sklearn import svm

from constants import _train_set_unequal, _train_set

path_left = \
    'D:\\JetBrains\\FII\\Software-Engineering-2020-Pre-Processing\\Software-Engineering-2020-Pre-Processing\\Left'
path_right = \
    'D:\\JetBrains\\FII\\Software-Engineering-2020-Pre-Processing\\Software-Engineering-2020-Pre-Processing\\Right'
path_test = \
    'D:\\JetBrains\\FII\\Software-Engineering-2020-Pre-Processing\\Software-Engineering-2020-Pre-Processing\\Test'


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
        print(result)


def separate():
    with open('CT_Report.csv', newline='') as patients:
        counts = [[53, 135], [36, 152], [153, 35], [138, 50], [183, 5], [178, 10]]
        reader = csv.reader(patients, delimiter=',')
        reader = list(reader)
        for i in range(len(counts)):
            counter = min(counts[i])
            unaffected = []
            affected = []
            for row in reader:
                if row[i + 1] == '1' and len(affected) < counter + 10:
                    affected.append(row[0])
                if row[i + 1] == '0' and len(unaffected) < counter:
                    unaffected.append(row[0])
            print([unaffected, affected])


def run():
    right_image_data = np.load('equal_processed-right.npy')
    right_caverns_image_data = np.load('equal_processed-right-caverns.npy')
    right_pleurisy_image_data = np.load('equal_processed-right-pleurisy.npy')
    labels_right = np.load('equal_right-lung-labels.npy')
    labels_caverns_right = np.load('equal_right-caverns-labels.npy')
    labels_pleurisy_right = np.load('equal_right-pleurisy-labels.npy')
    svm_classifier = svm.SVC(kernel='rbf', C=1.0)
    svm_classifier2 = svm.SVC(kernel='rbf', C=1.0)
    svm_classifier3 = svm.SVC(kernel='rbf', C=1.0)
    svm_classifier.fit(right_image_data, labels_right)
    print('Fitted')
    svm_classifier2.fit(right_caverns_image_data, labels_caverns_right)
    print('Fitted')
    svm_classifier3.fit(right_pleurisy_image_data, labels_pleurisy_right)
    print('Fitted')
    dump(svm_classifier, 'equal_right-learn.joblib')
    dump(svm_classifier2, 'equal_right-caverns-learn.joblib')
    dump(svm_classifier3, 'equal_right-pleurisy-learn.joblib')
    print('Saved')
    for file in os.listdir(path_test):
        test_image_data = []
        root, ext = os.path.splitext(file)
        _path = os.path.join(path_right, root)
        for _file in os.listdir(_path):
            __path = os.path.join(_path, _file)
            for __file in os.listdir(__path):
                img = image.load_img(os.path.join(__path, __file), target_size=(32, 32))
                img = image.img_to_array(img)
                test_image_data.append(img)
        test_image_data = np.array(test_image_data, dtype='float32') / 255.0
        m = test_image_data.shape[0]
        test_image_data = test_image_data.reshape(m, -1)
        ypred = svm_classifier.predict(test_image_data)
        ypred2 = svm_classifier2.predict(test_image_data)
        ypred3 = svm_classifier3.predict(test_image_data)
        print(file, end=" ")
        print(round(np.count_nonzero(ypred == '1') / (
                np.count_nonzero(ypred == '1') + np.count_nonzero(ypred == '0')), 2), end=" ")
        print(round(np.count_nonzero(ypred2 == '1') / (
                np.count_nonzero(ypred2 == '1') + np.count_nonzero(ypred2 == '0')), 2), end=" ")
        print(round(np.count_nonzero(ypred3 == '1') / (
                np.count_nonzero(ypred3 == '1') + np.count_nonzero(ypred3 == '0')), 2))


def create_arrays():
    with open('CT_Report.csv', newline='') as patients:
        image_data_right = []
        image_data_right_pleurisy = []
        image_data_right_caverns = []
        labels_right = []
        labels_caverns_right = []
        labels_pleurisy_right = []
        reader = csv.reader(patients, delimiter=',')
        reader = list(reader)
        for file in os.listdir(path_right):
            root, ext = os.path.splitext(file)
            if file in _train_set[1][0] or file in _train_set[1][1]:
                _path = os.path.join(path_right, root)
                for _file in os.listdir(_path):
                    __path = os.path.join(_path, _file)
                    for __file in os.listdir(__path):
                        img = image.load_img(os.path.join(__path, __file), target_size=(32, 32))
                        img = image.img_to_array(img)
                        image_data_right.append(img)
                        labels_right.append(reader[int(file)][2])
            if file in _train_set[3][0] or file in _train_set[3][1]:
                _path = os.path.join(path_right, root)
                for _file in os.listdir(_path):
                    __path = os.path.join(_path, _file)
                    for __file in os.listdir(__path):
                        img = image.load_img(os.path.join(__path, __file), target_size=(32, 32))
                        img = image.img_to_array(img)
                        image_data_right_caverns.append(img)
                        labels_caverns_right.append(reader[int(file)][4])
            if file in _train_set[5][0] or file in _train_set[5][1]:
                _path = os.path.join(path_right, root)
                for _file in os.listdir(_path):
                    __path = os.path.join(_path, _file)
                    for __file in os.listdir(__path):
                        img = image.load_img(os.path.join(__path, __file), target_size=(32, 32))
                        img = image.img_to_array(img)
                        image_data_right_pleurisy.append(img)
                        labels_pleurisy_right.append(reader[int(file)][6])
        image_data_right = np.array(image_data_right, dtype='float32') / 255.0
        image_data_right_caverns = np.array(image_data_right_caverns, dtype='float32') / 255.0
        image_data_right_pleurisy = np.array(image_data_right_pleurisy, dtype='float32') / 255.0
        labels_right = np.array(labels_right)
        labels_caverns_right = np.array(labels_caverns_right)
        labels_pleurisy_right = np.array(labels_pleurisy_right)
        m = image_data_right.shape[0]
        image_data_right = image_data_right.reshape(m, -1)
        m = image_data_right_caverns.shape[0]
        image_data_right_caverns = image_data_right_caverns.reshape(m, -1)
        m = image_data_right_pleurisy.shape[0]
        image_data_right_pleurisy = image_data_right_pleurisy.reshape(m, -1)
        np.save('equal_processed-right.npy', image_data_right)
        np.save('equal_processed-right-caverns.npy', image_data_right_caverns)
        np.save('equal_processed-right-pleurisy.npy', image_data_right_pleurisy)
        np.save('equal_right-lung-labels.npy', labels_right)
        np.save('equal_right-caverns-labels.npy', labels_caverns_right)
        np.save('equal_right-pleurisy-labels.npy', labels_pleurisy_right)


print(datetime.datetime.now())
#create_arrays()
#run()
# separate()
count()
print(datetime.datetime.now())
