#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 20 21:59:09 2020

@author: nathaniel
"""


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False
'''
一、子图

1. 使用 plt.subplots 绘制均匀状态下的子图

返回元素分别是画布和子图构成的列表，第一个数字为行，第二个为列

figsize 参数可以指定整个画布的大小

sharex 和 sharey 分别表示是否共享横轴和纵轴刻度

tight_layout 函数可以调整子图的相对大小使字符不会重叠
'''
fig, axs = plt.subplots(2, 5, figsize=(10, 4), sharex=True, sharey=True)
fig.suptitle('样例1', size=20)
for i in range(2):
    for j in range(5):
        axs[i][j].scatter(np.random.randn(10), np.random.randn(10))
        axs[i][j].set_title('第%d行，第%d列'%(i+1,j+1))
        axs[i][j].set_xlim(-5,5)
        axs[i][j].set_ylim(-5,5)
        if i==1: axs[i][j].set_xlabel('横坐标')
        if j==0: axs[i][j].set_ylabel('纵坐标')
fig.tight_layout()
'''
output_3_0
output_3_0
712×285 11.8 KB

​
2. 使用 GridSpec 绘制非均匀子图

所谓非均匀包含两层含义，第一是指图的比例大小不同但没有跨行或跨列，第二是指图为跨列或跨行状态

利用 add_gridspec 可以指定相对宽度比例 width_ratios 和相对高度比例参数 height_ratios
'''
fig = plt.figure(figsize=(10, 4))
spec = fig.add_gridspec(nrows=2, ncols=5, width_ratios=[1,2,3,4,5], height_ratios=[1,3])
fig.suptitle('样例2', size=20)
for i in range(2):
    for j in range(5):
        ax = fig.add_subplot(spec[i, j])
        ax.scatter(np.random.randn(10), np.random.randn(10))
        ax.set_title('第%d行，第%d列'%(i+1,j+1))
        if i==1: ax.set_xlabel('横坐标')
        if j==0: ax.set_ylabel('纵坐标')
fig.tight_layout()
​'''

output_5_0
output_5_0
702×285 12.8 KB

​
在上面的例子中出现了 spec[i, j] 的用法，事实上通过切片就可以实现子图的合并而达到跨图的共能
'''
fig = plt.figure(figsize=(10, 4))
spec = fig.add_gridspec(nrows=2, ncols=6, width_ratios=[2,2.5,3,1,1.5,2], height_ratios=[1,2])
fig.suptitle('样例3', size=20)
# sub1
ax = fig.add_subplot(spec[0, :3])
ax.scatter(np.random.randn(10), np.random.randn(10))
# sub2
ax = fig.add_subplot(spec[0, 3:5])
ax.scatter(np.random.randn(10), np.random.randn(10))
# sub3
ax = fig.add_subplot(spec[:, 5])
ax.scatter(np.random.randn(10), np.random.randn(10))
# sub4
ax = fig.add_subplot(spec[1, 0])
ax.scatter(np.random.randn(10), np.random.randn(10))
# sub5
ax = fig.add_subplot(spec[1, 1:5])
ax.scatter(np.random.randn(10), np.random.randn(10))
fig.tight_layout()
​
'''
output_7_0
output_7_0
712×285 5.54 KB

​
二、子图上的方法

在 ax 对象上定义了和 plt 类似的图形绘制函数，常用的有： plot, hist, scatter, bar, barh, pie

fig, ax = plt.subplots(figsize=(4,3))
ax.plot([1,2],[2,1])
[<matplotlib.lines.Line2D at 0x120c03070c8>]
​
output_9_1
​'''

fig, ax = plt.subplots(figsize=(4,3))
ax.hist(np.random.randn(1000))
'''
(array([  4.,  21.,  53., 157., 210., 255., 178.,  83.,  32.,   7.]),
 array([-3.21675023, -2.5967257 , -1.97670118, -1.35667665, -0.73665212,
        -0.1166276 ,  0.50339693,  1.12342145,  1.74344598,  2.3634705 ,
         2.98349503]),
 
 <BarContainer object of 10 artists>)
​
output_10_1
​

常用直线的画法为： axhline, axvline, axline （水平、垂直、任意方向）
'''
fig, ax = plt.subplots(figsize=(4,3))
ax.axhline(0.5,0.2,0.8)
ax.axvline(0.5,0.2,0.8)
ax.axline([0.3,0.3],[0.7,0.7])
'''
<matplotlib.lines._AxLine at 0x120c042b6c8>
​
output_12_1
​

使用 grid 可以加灰'''色网格

fig, ax = plt.subplots(figsize=(4,3))
ax.grid(True)
​'''
output_14_0
​

使用 set_xscale, set_title, set_xlabel 分别可以设置坐标轴的规度（指对数坐标等）、标题、轴名
'''
fig, axs = plt.subplots(1, 2, figsize=(10, 4))
fig.suptitle('大标题', size=20)
for j in range(2):
    axs[j].plot(list('abcd'), [10**i for i in range(4)])
    if j==0:
        axs[j].set_yscale('log')
        axs[j].set_title('子标题1')
        axs[j].set_ylabel('对数坐标')
    else:
        axs[j].set_title('子标题1')
        axs[j].set_ylabel('普通坐标')
fig.tight_layout()
​'''

output_16_0
output_16_0
712×285 14.2 KB

​
与一般的 plt 方法类似， legend, annotate, arrow, text 对象也可以进行相应的绘制
'''
fig, ax = plt.subplots()
ax.arrow(0, 0, 1, 1, head_width=0.03, head_length=0.05, facecolor='red', edgecolor='blue')
ax.text(x=0, y=0,s='这是一段文字', fontsize=16, rotation=70, rotation_mode='anchor', color='green')
ax.annotate('这是中点', xy=(0.5, 0.5), xytext=(0.8, 0.2), arrowprops=dict(facecolor='yellow', edgecolor='black'), fontsize=16)
Text(0.8, 0.2, '这是中点')
​'''
output_18_1
​'''

fig, ax = plt.subplots()
ax.plot([1,2],[2,1],label="line1")
ax.plot([1,1],[1,2],label="line1")
ax.legend(loc=1)