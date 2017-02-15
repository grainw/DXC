#--coding: utf-8--#
import pandas as pd
import math

def error_function(a,b):
    inputfile = '../data/DXCerror_ana.xlsx'
    data = pd.read_excel(inputfile)  # 导入数据
    x = data.iloc[:, a].as_matrix()
    y = data.iloc[:, b].as_matrix()
    sum = 0
    for i in range(len(x)):
        sum = sum + (x[i] - y[i]) ** 2
    error = math.sqrt(sum / len(x))
    return error

print error_function(0,3)
print error_function(1,3)
print error_function(2,3)
