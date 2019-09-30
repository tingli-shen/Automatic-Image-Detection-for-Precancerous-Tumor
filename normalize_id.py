# -*- coding: utf-8 -*-
"""
Created on Fri Apr 26 16:47:39 2019

@author: Dennis
"""

from pathlib import Path, PureWindowsPath
import os
half=1
name=0
#print(os.listdir("practice/."))
breakpoint=len(os.listdir("practice/."))
for filename in os.listdir("practice/."):
        
    find_ground_truth=filename.split(".")[1]
    for gt in os.listdir("practice/."):
        if gt[0]=='_' and find_ground_truth in gt:
            print(filename,gt)
            os.rename(filename, 'original_'+str(half)+'.jpg')
            os.rename(gt, 'ground_truth_'+str(half)+'.jpg')
            break
    if half==breakpoint/2:
        break
    half+=1
