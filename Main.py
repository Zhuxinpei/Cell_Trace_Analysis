'''
=======================================================================
THIS PROGRAM IS PRIVATE, DO NOT USE OR COPY WITHOUT PERMISSION

Project Name:     Cell_Trace_Analysis
File Name:        Main.py
Date:             2023.06.24

Copyright (c) 2023 Qingdao University, All Rights Reserved.
=======================================================================
'''

from DataProcess import RandomWalk, zero_score, pca_exe, data_seg
from Reader import csv_read
from Draw import draw_plot, draw_plot_3D


########################################################################################################################

def main():
    # 原始数据路径
    path = "C:\\Users\\hisense\\Desktop\\张斌\\M2_ENK_ov_6m_Mating4_Sync_20230615-DFmin-CellTrace.csv"

    # 读取原始数据，
    origin_data, time_stamp = csv_read(path, down_sample_rate = 1)

    # 原始数据做标准化并进行PCA降维
    zero_data = zero_score(origin_data)
    pca_data = pca_exe(zero_data, 3)

    # 将数据跟根据任务和对照进行分割
    task_data_list, control_data_list = data_seg(pca_data, time_stamp, [[0.0, 303.4], [676.8, 757.7], [757.8, 1131.0], [1212.2, 1654.9],[1750.9, 1820.9]], [])

    # 将数据生成为漫步数据
    task_data_list_walk = []
    for i in task_data_list:
        rw = RandomWalk(i, 3)
        rw.fill_walks()
        rw_data = rw.get_array()
        task_data_list_walk.append(rw_data)

    # 画图
    draw_plot_3D(task_data_list_walk)

########################################################################################################################

if __name__ == "__main__":
    main()