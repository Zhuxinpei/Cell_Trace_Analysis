'''
=======================================================================
THIS PROGRAM IS PRIVATE, DO NOT USE OR COPY WITHOUT PERMISSION

Project Name:     Cell_Trace_Analysis
File Name:        DataProcess.py
Date:             2023.06.24

Copyright (c) 2023 Qingdao University, All Rights Reserved.
=======================================================================
'''

from sklearn.decomposition import PCA
import numpy as np


########################################################################################################################

def zero_score(rsc_data, debug=False):
    """
    数据标准化
    :param rsc_data: 原始数据
    :return: 经过标准化的数据
    """
    # 错误检查
    if rsc_data is None:
        raise Exception("输入数据为空")
    if not isinstance(rsc_data, np.ndarray):
        raise Exception("不支持的输入数据类型 %r" % type(rsc_data))
    # 求均值
    mean_value = np.nanmean(rsc_data)
    if debug:
        print("原始数据的平均值是: ", mean_value)
    # 求标准差
    std_value = np.nanstd(rsc_data)
    if debug:
        print("原始数据的方差是：", std_value)
    # 计算标准化的数据
    dst_data = (rsc_data - mean_value) / (std_value * 10)
    if debug:
        print("标准化后的数据是：", dst_data)
        print("标准化后数据的最大值是：", np.nanmax(dst_data))
        print("标准化后数据的最小值是：", np.nanmin(dst_data))
    return dst_data


def pca_exe(rsc_data, n_components, debug=False):
    """
    PCA降维
    :param rsc_data: 原始数据
    :param n_components: 需要降低至的维度
    :param debug: 检错开关
    :return: 降维后的numpy矩阵
    """
    # 错误检查
    if rsc_data is None:
        raise Exception("输入数据为空")
    if not isinstance(rsc_data, np.ndarray):
        raise Exception("不支持的输入数据类型 %r" % type(rsc_data))
    if len(rsc_data.shape) != 2:
        raise Exception("不支持的输入数据维度 %r" % str(rsc_data.shape))
    # PCA的实例
    pca_instance = PCA(n_components)
    # 求解降维后的输出矩阵
    dst_data = pca_instance.fit_transform(rsc_data)
    # 查看PCA的输出矩阵
    if debug:
        print("PCA输出的矩阵是：", dst_data)
        print("PCA后数据的最大值是：", np.nanmax(dst_data))
        print("PCA后数据的最小值是：", np.nanmin(dst_data))
        print("PCA后数据的平均值是：", np.nanmean(dst_data))
        print("PCA后数据的方差是：", np.nanstd(dst_data))
    return dst_data


def data_seg(rsc_data, time_stamp, task_time_node, control_time_node, debug=False):
    """
    :param rsc_data:
    :param time_stamp:
    :param task_time_node:
    :param control_time_node:
    :param debug:
    :return:
    """
    # 错误检查
    if rsc_data.shape[0] != time_stamp.shape[0]:
        raise Exception("输入数据与时间戳维度不对应")
    # 初始化存储任务数据的列表
    task_data_list = []
    # 初始化存储对照数据的列表
    control_data_list = []
    # 将时间戳数据都保留一位小数
    time_stamp = time_stamp * 10
    time_stamp = time_stamp.astype(np.int)
    time_stamp = time_stamp / 10
    # 迭代任务组列表时间戳
    for task_i, task in enumerate(task_time_node):
        start_time = task[0]
        end_time = task[1]
        start_time_index = np.where(time_stamp == start_time)[0][0]
        end_time_index = np.where(time_stamp == end_time)[0][0]
        task_data_list.append(rsc_data[start_time_index: end_time_index, :])
    # 迭代对照组列表时间戳
    return task_data_list, control_data_list


class RandomWalk():
    """
    漫步图，根据数据的坐标以原点为起始点做数据漫步
    """

    def __init__(self, rsc_data, n_component=2, debug=False):
        self.rsc_data = rsc_data
        self.num_points = rsc_data.shape[0]
        self.n_component = n_component
        self.x_value = [0]
        self.y_value = [0]
        self.z_value = [0]
        self.debug = debug
        if n_component != 2 and n_component != 3:
            raise Exception("参数n_component的维度只能是2或者3")

    def fill_walks(self):
        # 遍历每个数据
        for i in range(self.num_points):
            # 实际移动的距离就是数据的x和y的数值
            x_step = self.rsc_data[i, 0]
            y_step = self.rsc_data[i, 1]

            # 数据在原始基础上做加减
            x = self.x_value[-1] + x_step
            y = self.y_value[-1] + y_step

            # 将新数据补充在列表中
            self.x_value.append(x)
            self.y_value.append(y)

            # 如果是三维数据则补充第三维
            if self.n_component == 3:
                z_step = self.rsc_data[i, 2]
                z = self.z_value[-1] + z_step
                self.z_value.append(z)

    def get_array(self):
        # 将漫步数据的x和y或z数据组合成矩阵
        if self.n_component == 3:
            return np.squeeze(np.dstack((self.x_value, self.y_value, self.z_value)))
        else:
            return np.squeeze(np.dstack((self.x_value, self.y_value)))
