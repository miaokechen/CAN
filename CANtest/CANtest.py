
from ctypes import *
import sys
from PyQt5.QtWidgets import (QCheckBox,QWidget, QToolTip, 
    QPushButton, QApplication,QLabel,QLineEdit,QInputDialog,QAction,QMenu,QMainWindow,QSizePolicy)
from PyQt5.QtGui import QFont  
from PyQt5.QtCore import QCoreApplication
from PyQt5.QtCore import QBasicTimer
from PyQt5.QtCore import QTimer
from PyQt5.QtCore import Qt
from matplotlib import pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import random
import numpy as np
from scipy import interpolate
import pandas as pd
import time

lib= CDLL('ControlCAN.dll')

def opeancanbus(nDeviceInd):#打开CAN设备 设备选择
	return lib.VCI_OpenDevice(4, c_int(nDeviceInd), 0)
def closecanbus(nDeviceInd):#关闭CAN设备 设备选择
	return lib.VCI_CloseDevice(4, c_int(nDeviceInd))
print (opeancanbus(0))
#print (closecanbus(0))
class py_struct_(Structure):
    _fields_ = [("AccCode", c_ulong), ("AccMask", c_ulong),("Reserved",c_ulong),("Filter",c_byte),("Timing0",c_byte),("Timing1",c_byte),("Mode",c_byte)]
def initcan(nDeviceInd,nCANInd,nTiming0,nTiming1):#设备选择，通道选择，波特率选择1，波特率选择2
	vic = py_struct_()
	vic.AccCode=0x80000008
	vic.AccMask=0xFFFFFFFF
	vic.Reserved = 0
	vic.Filter=1
	vic.Timing0=nTiming0
	vic.Timing1=nTiming1
	vic.Mode=0
	py_vic =  byref(vic)
	lib.VCI_InitCAN(4,c_int(nDeviceInd),c_int(nCANInd),py_vic)
	lib.VCI_StartCAN(4, c_int(nDeviceInd), c_int(nCANInd)) 