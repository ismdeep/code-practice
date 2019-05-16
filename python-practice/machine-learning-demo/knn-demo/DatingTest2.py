# coding: utf-8
# author: ismdeep
# dateime: 2019-05-14 10:00:59
# filename: app.py
# blog: https://ismdeep.com
from numpy import *
from sklearn.neighbors import KNeighborsClassifier


# get dataset from file
def file2matrix(filename):
    fr = open(filename)
    numberOfLines = len(fr.readlines())  # get the number of lines in the file
    returnMat = np.zeros([numberOfLines, 3])  # prepare matrix to return
    classLabelVector = []  # prepare labels return
    fr = open(filename)
    index = 0
    tmp = []
    for line in fr.readlines():
        line = line.strip()
        listFromLine = line.split('\t')
        tmp.append(listFromLine)
        # returnMat[index, :] = listFromLine[0:3]
        # classLabelVector.append(int(listFromLine[-1]))
    random.shuffle(tmp)
    for item in tmp:
        returnMat[index, :] = item[0:3]
        classLabelVector.append(int(item[-1]))
        index += 1
    return returnMat, classLabelVector


# 数据归一化

def autoNorm(dataSet):
    minVals = dataSet.min(0)
    maxVals = dataSet.max(0)
    ranges = maxVals - minVals
    normDataSet = np.zeros(shape(dataSet))
    print(np.shape(dataSet))
    m = dataSet.shape[0]
    normDataSet = dataSet - tile(minVals, (m, 1))
    normDataSet = normDataSet / tile(ranges, (m, 1))  # element wise divide
    return normDataSet, ranges, minVals


# 测试
def datingClassTest():
    hoRatio = 0.10  # hold out 10%
    # get data from
    X, y = file2matrix('datingTestSet2.txt')
    normMat, ranges, minVals = autoNorm(X)
    m = normMat.shape[0]
    print('m: {%d}' % m)
    numTestVecs = int(m * hoRatio)
    print('Test Vecs Count: %d' % (numTestVecs))
    errorCount = 0.0
    clf = KNeighborsClassifier(n_neighbors=10, algorithm='kd_tree', p=2)
    clf.fit(normMat[numTestVecs:m, :], y[numTestVecs:m])
    for i in range(numTestVecs):
        # print(X[i, :])
        # print("the classifier came back with: %d, the real answer is: %d" % (clf.predict([X[i, :]]), y[i]))
        print(X[i, :], y[i])
        if clf.predict([normMat[i, :]]) != y[i]:
            errorCount += 1.0
    print('errorCount: {%d} / numTestVecs: {%d}' % (errorCount, numTestVecs))
    print('Test Vecs Count: %d' % numTestVecs)
    print("the total error rate is: %f" % (errorCount / float(numTestVecs)))
    print(errorCount)


datingClassTest()
