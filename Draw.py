'''
=======================================================================
THIS PROGRAM IS PRIVATE, DO NOT USE OR COPY WITHOUT PERMISSION

Project Name:     Cell_Trace_Analysis
File Name:        Draw.py
Date:             2023.06.24

Copyright (c) 2023 Qingdao University, All Rights Reserved.
=======================================================================
'''

import matplotlib.pyplot as plt
import numpy as np

########################################################################################################################

def draw_plot(rsc_data):
    # 初始化
    fig = plt.figure()
    ax = plt.gca()

    # 去掉边框
    ax.spines['right'].set_color('none')
    ax.spines['top'].set_color('none')
    # 设置x与y轴的位置，以(0,0)作中心
    ax.spines['bottom'].set_position(('data', 0))
    ax.spines['left'].set_position(('data', 0))
    # 去掉ticks
    # ax.xaxis.set_ticks_position('none')
    # ax.yaxis.set_ticks_position('none')
    # 去掉坐标轴数字
    # ax.axes.xaxis.set_visible(False)
    # ax.axes.yaxis.set_visible(False)
    # 坐标轴范围
    # plt.xlim((-50,50))
    # plt.ylim((-50,50))

    # 绘画
    plt.plot(rsc_data[0][:, 0], rsc_data[0][:, 1], linewidth=3.0, color='red')
    plt.plot(rsc_data[1][:, 0], rsc_data[1][:, 1], linewidth=3.0, color='green')
    plt.plot(rsc_data[2][:, 0], rsc_data[2][:, 1], linewidth=3.0, color='blue')
    plt.plot(rsc_data[3][:, 0], rsc_data[3][:, 1], linewidth=3.0, color='cyan')
    plt.plot(rsc_data[4][:, 0], rsc_data[4][:, 1], linewidth=3.0, color='yellow')

    plt.show()

def draw_plot_3D(rsc_data):
    # 初始化
    fig = plt.figure()
    ax = plt.gca(projection='3d')

    # 画坐标轴面
    # a = np.linspace(-2000, 2000, 500)
    # b = np.linspace(-2000, 2000, 500)
    # A, B = np.meshgrid(a, b)
    # ax.plot_surface(A, B, A * 0, color='gray', alpha=0.2)
    # ax.plot_surface(A, B * 0, B, color='gray', alpha=0.2)
    # ax.plot_surface(A * 0, A, B, color='gray', alpha=0.2)

    # 绘画
    ax.plot(rsc_data[0][:, 0], rsc_data[0][:, 1], rsc_data[0][:, 2], linewidth=3.0, color='red')
    ax.plot(rsc_data[1][:, 0], rsc_data[1][:, 1], rsc_data[1][:, 2], linewidth=3.0, color='green')
    ax.plot(rsc_data[2][:, 0], rsc_data[2][:, 1], rsc_data[2][:, 2], linewidth=3.0, color='blue')
    ax.plot(rsc_data[3][:, 0], rsc_data[3][:, 1], rsc_data[3][:, 2], linewidth=3.0, color='cyan')
    ax.plot(rsc_data[4][:, 0], rsc_data[4][:, 1], rsc_data[4][:, 2], linewidth=3.0, color='yellow')

    plt.show()



