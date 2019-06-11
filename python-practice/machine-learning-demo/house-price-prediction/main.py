# coding: utf-8
# author: ismdeep
# dateime: 2019-06-11 11:34:04
# filename: main.py
# blog: https://ismdeep.com

# 导入必要的库
import paddle.fluid as fluid
import paddle
import numpy as np
import os

#  从paddle接口中获取房价数据训练集
train_reader = paddle.batch(
    paddle.reader.shuffle(paddle.dataset.uci_housing.train(),  # 获取uci_housing训练数据
                          buf_size=500),  # 在buf_size的空间内进行乱序
    batch_size=20)  # batch_size:每个批次读入的训练数据量
#  从paddle接口中获取房价数据测试集
test_reader = paddle.batch(paddle.reader.shuffle(paddle.dataset.uci_housing.test(), buf_size=500),  # 获取uci_housing的测试数据
                           batch_size=20)  # batch_size:每个批次读入的测试数据量

# 定义一个简单的线性网络，网络有1层。输入层为x，输出大小为1，激活函数是relu的全连接层
# 定义张量变量x，表示13维的特征值
x = fluid.layers.data(name='x', shape=[13], dtype='float32')
# 定义一个简单的线性网络
net = fluid.layers.fc(input=x, size=1, act=None)

# 定义损失函数
y = fluid.layers.data(name='y', shape=[1], dtype='float32')  # 定义张量y,表示目标值
cost = fluid.layers.square_error_cost(input=net, label=y)  # 求一个batch的损失值
avg_cost = fluid.layers.mean(cost)  # 对损失值求平均值

# 定义优化方法
optimizer = fluid.optimizer.SGDOptimizer(learning_rate=0.001)
opts = optimizer.minimize(avg_cost)

# 创建一个使用CPU的解释器
place = fluid.CPUPlace()
exe = fluid.Executor(place)
# 进行参数初始化
exe.run(fluid.default_startup_program())

# 定义输入数据维度
feeder = fluid.DataFeeder(place=place, feed_list=[x, y])

# 开始训练和测试
for pass_id in range(100):  # 训练10次
    # 开始训练并输出最后一个batch的损失值
    train_cost = 0
    for batch_id, data in enumerate(train_reader()):  # 遍历train_reader迭代器
        train_cost = exe.run(program=fluid.default_main_program(),  # 运行主程序
                             feed=feeder.feed(data),  # 喂入一个batch的训练数据
                             fetch_list=[avg_cost])
    print("Pass:%d, Cost:%0.5f" % (pass_id, train_cost[0][0]))  # 打印最后一个batch的损失值

    # 开始测试并输出最后一个batch的损失值
    test_cost = 0
    for batch_id, data in enumerate(test_reader()):  # 遍历test_reader迭代器
        test_cost = exe.run(program=fluid.default_main_program(),  # 运行测试cheng
                            feed=feeder.feed(data),  # 喂入一个batch的测试数据
                            fetch_list=[avg_cost])  # fetch均方误差
    print('Test:%d, Cost:%0.5f' % (pass_id, test_cost[0][0]))  # 打印最后一个batch的损失值
    # 保存模型
    model_save_dir = "/Users/ismdeep/Downloads/房价预测fluid/easy_fit_a_line.inference.model"
    # 如果保存路径不存在就创建
    if not os.path.exists(model_save_dir):
        os.makedirs(model_save_dir)
    #     print ('save models to %s' % (model_save_dir))
    fluid.io.save_inference_model(model_save_dir,  # 保存推理model的路径
                                  ['x'],  # 推理（inference）需要 feed 的数据
                                  [net],  # 保存推理（inference）结果的 Variables
                                  exe)  # exe 保存 inference model

infer_exe = fluid.Executor(place)  # 创建推测用的executor
inference_scope = fluid.core.Scope()  # Scope指定作用域

# load_inference_model()的返回: 这个函数的返回有三个元素的元组(Program，feed_target_names, fetch_targets)。Program 是一个 Program ，它是推理 Program。 feed_target_names 是一个str列表，它包含需要在推理 Program 中提供数据的变量的名称。fetch_targets 是一个 Variable 列表，从中我们可以得到推断结果。

with fluid.scope_guard(inference_scope):  # 修改全局/默认作用域（scope）, 运行时中的所有变量都将分配给新的scope。
    # 从指定目录中加载 推理model(inference model)
    [inference_program,  # 推理的program
     feed_target_names,  # str列表，包含需要在推理program中提供数据的变量名称
     fetch_targets] = fluid.io.load_inference_model(model_save_dir,  # fetch_targets: 推断结果，model_save_dir:模型训练路径
                                                    infer_exe)  # infer_exe: 运行 inference model的 executor
    # 获取推测数据
    infer_reader = paddle.batch(paddle.dataset.uci_housing.test(),  # 获取uci_housing的测试数据
                                batch_size=10)  # 从测试数据中读取一个大小为10的batch数据
    # 从test_reader中分割x
    test_data = next(infer_reader())
    test_x = np.array([data[0] for data in test_data]).astype("float32")
    test_y = np.array([data[1] for data in test_data]).astype("float32")
    results = infer_exe.run(inference_program,  # 模型
                            feed={feed_target_names[0]: np.array(test_x)},  # 喂入要预测的x值
                            fetch_list=fetch_targets)  # 得到推测结果
    print("infer results: (House Price)")
    for idx, val in enumerate(results[0]):
        print("%d: %.2f" % (idx, val))
    print("ground truth:")
    for idx, val in enumerate(test_y):
        print("%d: %.2f" % (idx, val))
