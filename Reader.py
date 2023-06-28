"""
=======================================================================
THIS PROGRAM IS PRIVATE, DO NOT USE OR COPY WITHOUT PERMISSION

Project Name:     Cell_Trace_Analysis
File Name:        Reader.py
Date:             2023.06.24

Copyright (c) 2023 Qingdao University, All Rights Reserved.
=======================================================================
"""

import numpy as np
import csv


########################################################################################################################

def csv_read(path, down_sample_rate=1, debug=False):
    """
    读取本地的csv文件返回原始数据的矩阵
    :param path: csv文件路径
    :param down_sample_rate: 降采样频率
    :param debug: 检错开关
    :return: 数据的numpy矩阵 每条数据的时间戳
    """
    # 创建初始列表用于存储csv文件的数据
    res_list = []
    # 读取csv原始数据
    reader = csv.reader(open(path))
    # 迭代每一行数据
    for index, row_string in enumerate(reader):
        # 因为前两行没有有效数据所以过滤前两行
        if index > 1:
            # 将字符串格式转为浮点型
            row_float = list(map(float, row_string))
            res_list.append(row_float)
    # 将列表转为矩阵
    origin_array = np.array(res_list)
    # 找到存在nan数据的横纵坐标位置
    nan_place = np.where(np.isnan(origin_array))
    # 只留下nan数据的横坐标并删除重复的
    nan_row = np.unique(nan_place[0])
    # 删除nan数据
    nan_array = np.delete(origin_array, nan_row, axis=0)
    # 查看矩阵
    if debug:
        print("原始数据是：", nan_array)
        print("原始数据的数据量是：", nan_array.shape)
    # 降低采样频率
    z = []
    for i in range(nan_array.shape[0]):
        if i % down_sample_rate == 0:
            z.append(i)
    down_array = np.take(nan_array, z, axis=0)
    if debug:
        print("降采样数据是：", down_array)
        print("降采样数据的数据量是：", down_array.shape)
    # 将数据切分为时间戳数据和荧光数据
    time_stamp = down_array[:, 0]
    res_array = down_array[:, 1:]
    if debug:
        print("时间戳的数据是：", time_stamp)
    return res_array, time_stamp
