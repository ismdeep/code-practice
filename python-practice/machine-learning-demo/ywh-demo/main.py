# coding: utf-8
# author: ismdeep
# dateime: 2019-06-11 10:27:29
# filename: main.py
# blog: https://ismdeep.com
import numpy as np
from matplotlib import colors
from sklearn import svm
from sklearn.svm import SVC
from sklearn import model_selection
import matplotlib.pyplot as plt
import matplotlib as mpl


# *************将字符串转为整型***************************
def iris_type(s):
    it = {b'Iris-setosa': 0, b'Iris-versicolor': 1, b'Iris-virginica': 2}
    return it[s]


# *****************并判断a b是否相等，计算acc的均值*************
def show_accuracy(a, b, tip):
    acc = a.ravel() == b.ravel()
    print('%s Accuracy:%.3f' % (tip, np.mean(acc)))


def print_accuracy(clf, x_train, y_train, x_test, y_test):
    # 分别打印训练集和测试集的准确率  score(x_train,y_train):表示输出x_train,y_train在模型上的准确率
    print('trianing prediction:%.3f' % (clf.score(x_train, y_train)))
    print('test data prediction:%.3f' % (clf.score(x_test, y_test)))
    # 原始结果与预测结果进行对比   predict()表示对x_train样本进行预测，返回样本类别
    show_accuracy(clf.predict(x_train), y_train, 'traing data')
    show_accuracy(clf.predict(x_test), y_test, 'testing data')
    # 计算决策函数的值，表示x到各分割平面的距离
    # print('decision_function:\n', clf.decision_function(x_train))


def draw(clf, x):
    iris_feature = 'sepal length', 'sepal width', 'petal lenght', 'petal width'
    # 开始画图
    x1_min, x1_max = x[:, 0].min(), x[:, 0].max()  # 第0列的范围
    x2_min, x2_max = x[:, 1].min(), x[:, 1].max()  # 第1列的范围
    x1, x2 = np.mgrid[x1_min:x1_max:200j, x2_min:x2_max:200j]  # 生成网格采样点
    grid_test = np.stack((x1.flat, x2.flat), axis=1)  # 测试点
    print('grid_test:\n', grid_test)
    # 输出样本到决策面的距离
    z = clf.decision_function(grid_test)
    print('the distance to decision plane:\n', z)

    grid_hat = clf.predict(grid_test)  # 预测分类值 得到【0,0.。。。2,2,2】
    print('grid_hat:\n', grid_hat)
    grid_hat = grid_hat.reshape(x1.shape)  # reshape grid_hat和x1形状一致
    # 若3*3矩阵e，则e.shape()为3*3,表示3行3列

    cm_light = mpl.colors.ListedColormap(['#A0FFA0', '#FFA0A0', '#A0A0FF'])
    cm_dark = mpl.colors.ListedColormap(['g', 'b', 'r'])

    plt.pcolormesh(x1, x2, grid_hat, cmap=cm_light)  # pcolormesh(x,y,z,cmap)这里参数代入
    # x1，x2，grid_hat，cmap=cm_light绘制的是背景。
    plt.scatter(x[:, 0], x[:, 1], c=np.squeeze(y), edgecolor='k', s=50, cmap=cm_dark)  # 样本点
    plt.scatter(x_test[:, 0], x_test[:, 1], s=120, facecolor='none', zorder=10)  # 测试点
    plt.xlabel(iris_feature[0], fontsize=20)
    plt.ylabel(iris_feature[1], fontsize=20)
    plt.xlim(x1_min, x1_max)
    plt.ylim(x2_min, x2_max)
    plt.title('svm in iris data classification', fontsize=30)
    plt.grid()
    plt.show()


# **********SVM分类器构建*************************************
def classifier():
    # clf = svm.SVC(C=0.8, kernel='rbf', gamma=50, decision_function_shape='ovr')# 高斯核
    clf = svm.SVC(C=0.5,  # 误差项惩罚系数
                  kernel='linear',  # 线性核 kenrel="rbf":高斯核
                  decision_function_shape='ovr')  # 决策函数
    return clf


# ****************训练模型************************************
def train(clf, x_train, y_train):
    clf.fit(x_train,  # 训练集特征向量
            y_train.ravel())  # 训练集目标值


# 1.数据准备
# 1.1加载数据
data = np.loadtxt('iris.data',  # 数据文件路径
                  dtype=float,  # 数据类型
                  delimiter=',',  # 数据分隔符
                  converters={4: iris_type})  # 将第5列使用函数iris_type进行转换
# 1.2数据分割
x, y = np.split(data,  # 数组数据
                (4,),  # 第5列开始往后为y
                axis=1)  # 代表纵向分割，按列分割
x = x[:, :2]
x_train, x_test, y_train, y_test = model_selection.train_test_split(x,  # 被划分的样本特征集
                                                                    y,  # 被划分的样本标签
                                                                    random_state=1,  # 随机数种子
                                                                    test_size=0.3)  # 测试样本占比
print(x_train)
print(y_train)
# 2.定义模型：SVM模型定义
clf = classifier()
# 3.训练模型
train(clf, x_train, y_train)
# 4.模型评估
print('-' * 80)
print_accuracy(clf, x_train, y_train, x_test, y_test)
print('-' * 80)
# 5.模型使用
# draw(clf, x)
