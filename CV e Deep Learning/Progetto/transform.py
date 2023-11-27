#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 1: car, 2:trucks, 4: tractors, 5: camping cars, 7: motorcycles, 8:buses, 9: vans, 10: others, 11: pickup, 23: boats , 201: Small Land Vehicles, 31: Large land Vehicles

import os
import pandas as pd
PATH = './dataset/' #chanhe the path firstly (PATH TO dataset)dddd

def changepath():
    for i in ['01','02','03','04','05','06','07','08','09','10']:
        path = PATH + 'DETECTION/fold{}.txt'.format(i)
        img_path = PATH + 'DETECTION_1280/images/'
        write_path=(PATH + 'DETECTION/fold{}_write.txt').format(i)
        with open(path, "r") as file:
            img_files = file.readlines()
            for j in range(len(img_files)):
                img_files[j] =  img_path + img_files[j].rstrip()
        file.close()
        with open(write_path, "w") as file:
            for j in range(len(img_files)):
                file.write(img_files[j]+'\n')
        file.close()

        path = PATH + 'DETECTION/fold{}test.txt'.format(i)
        img_path = PATH + 'DETECTION/images/'
        write_path=PATH + 'DETECTION/fold{}test_write.txt'.format(i)
        with open(path, "r") as file:
            img_files = file.readlines()
            for j in range(len(img_files)):
                img_files[j] =  img_path + img_files[j].rstrip()
        file.close()
        with open(write_path, "w") as file:
            for j in range(len(img_files)):
                file.write(img_files[j]+'\n')
        file.close()

if __name__ == '__main__':
    changepath()

