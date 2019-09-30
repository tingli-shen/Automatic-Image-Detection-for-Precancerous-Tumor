#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar  2 19:40:57 2019

@author: tshen
"""
import Augmentor
p = Augmentor.Pipeline("C:/Users/Dennis/Desktop/CV_Project/data_augmentation/original_data/original")
# Point to a directory containing ground truth data.
# Images with the same file names will be added as ground truth data
# and augmented in parallel to the original data.
p.ground_truth("C:/Users/Dennis/Desktop/CV_Project/data_augmentation/original_data/ground_truth")
# Add operations to the pipeline as normal:
p.rotate90(probability=1)
p.rotate180(probability=0.5)
p.flip_left_right(probability=0.5)
p.flip_top_bottom(probability=0.5)
p.random_distortion(probability=1, grid_width=4, grid_height=4, magnitude=8)

p.sample(10000)