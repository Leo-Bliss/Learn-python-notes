#!/usr/bin/env python
# coding: utf-8

# ![](https://raw.githubusercontent.com/Qinbf/tf-model-zoo/master/README_IMG/01.jpg)
# AI MOOC： **www.ai-xlab.com**  
# 如果你也是AI爱好者，可以添加我的微信一起交流：**sdxxqbf**

# In[ ]:


import numpy as np
import matplotlib.pyplot as plt


# In[3]:


# 载入数据
data = np.genfromtxt("data.csv", delimiter=",")
x_data = data[:,0]
y_data = data[:,1]
plt.scatter(x_data,y_data)
plt.show()


# In[6]:


# 学习率learning rate
lr = 0.0001
# 截距
b = 0 
# 斜率
k = 0 
# 最大迭代次数
epochs = 50

# 最小二乘法
def compute_error(b, k, x_data, y_data):
    totalError = 0
    for i in range(0, len(x_data)):
        totalError += (y_data[i] - (k * x_data[i] + b)) ** 2
    return totalError / float(len(x_data)) / 2.0

def gradient_descent_runner(x_data, y_data, b, k, lr, epochs):
    # 计算总数据量
    m = float(len(x_data))
    # 循环epochs次
    for i in range(epochs):
        b_grad = 0
        k_grad = 0
        # 计算梯度的总和再求平均
        for j in range(0, len(x_data)):
            b_grad += (1/m) * (((k * x_data[j]) + b) - y_data[j])
            k_grad += (1/m) * x_data[j] * (((k * x_data[j]) + b) - y_data[j])
        # 更新b和k
        b = b - (lr * b_grad)
        k = k - (lr * k_grad)
        # 每迭代5次，输出一次图像
        if i % 5==0:
            print("epochs:",i)
            plt.plot(x_data, y_data, 'b.')
            plt.plot(x_data, k*x_data + b, 'r')
            plt.show()
    return b, k


# In[7]:


print("Starting b = {0}, k = {1}, error = {2}".format(b, k, compute_error(b, k, x_data, y_data)))
print("Running...")
b, k = gradient_descent_runner(x_data, y_data, b, k, lr, epochs)
print("After {0} iterations b = {1}, k = {2}, error = {3}".format(epochs, b, k, compute_error(b, k, x_data, y_data)))

# 画图
# plt.plot(x_data, y_data, 'b.')
# plt.plot(x_data, k*x_data + b, 'r')
# plt.show()


# In[ ]:





# # In[2]:
#
#
# import numpy as np
# x0, x1 = np.meshgrid([1,2,3], [4,5,6])
#
#
# # In[3]:
#
#
# x0
#
#
# # In[4]:
#
#
# x1
#
#
# # In[ ]:
#
#
# (1,4) (2,4) (3,4)
# (1,5) (2,5) (3,5)
# (1,6) (2,6) (3,6)

