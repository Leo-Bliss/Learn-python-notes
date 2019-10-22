import numpy as np
import matplotlib.pyplot as plt
#
# #普通文件读取方式
# data = open('data.csv','r',encoding='utf-8')
# data_list = []
# for line in data:
#     x,y = line.split(',')
#     data_list.append([float(x),float(y)])
#     #print(x,y)
# print(data_list)

#加载数据
data = np.genfromtxt('data.csv',delimiter=',')
# print(data)
x_data = data[:,0]
y_data = data[:,1]

#画散点图
plt.scatter(x_data,y_data)
plt.show()

#y = kx+b
#斜率
k = 0
#截距
b = 0
#学习率,不能太小也不能太大，（0.1,0.03,0.01,0.003,0.001,0.0003,0.0001...）
lr = 0.0001
#最大迭代次数
max_times = 50

#最小二乘法：代价函数（cost Function）
def compute_cost(k,b,x_data,y_data):
    m = len(x_data)
    total_cost = 0
    for j in range(m):
        total_cost += (y_data[j] - (k * x_data[j] + b)) ** 2
    return total_cost / float(m) / 2.0
#梯度下降法
def gradient_descent(x_data,y_data,k,b,lr,max_times):
    m = len(x_data)
    for i in range(max_times):
        #临时存截距与斜率
        b_grad = 0
        k_grad = 0
        for j in range(m):
            b_grad += 1/float(m) * ((k * x_data[j] + b) - y_data[j])
            k_grad += 1/float(m) * x_data[j] * ((k * x_data[j] + b) - y_data[j])
        b -= lr *  b_grad
        k -= lr * k_grad

    return b,k
print('初始数据,b = {0},k = {1},cost = {2}'.format(b,k,compute_cost(k,b,x_data,y_data)))

b,k = gradient_descent(x_data,y_data,k,b,lr,max_times)
print('梯度下降法迭代{0}次后,b = {1},k = {2},cost = {3}'.format(max_times,b,k,compute_cost(k,b,x_data,y_data)))
#拟合图
plt.plot(x_data,y_data,'b.')
plt.plot(x_data,(k*x_data+b),'r')
plt.show()






