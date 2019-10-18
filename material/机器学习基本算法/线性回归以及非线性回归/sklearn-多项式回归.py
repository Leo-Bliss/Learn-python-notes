#!/usr/bin/env python
# coding: utf-8

# ![](https://raw.githubusercontent.com/Qinbf/tf-model-zoo/master/README_IMG/01.jpg)
# AI MOOC： **www.ai-xlab.com**  
# 如果你也是AI爱好者，可以添加我的微信一起交流：**sdxxqbf**

# In[ ]:


import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression


# In[2]:


# 载入数据
data = np.genfromtxt("job.csv", delimiter=",")
x_data = data[1:,1]
y_data = data[1:,2]
plt.scatter(x_data,y_data)
plt.show()


# In[3]:


x_data


# In[4]:


x_data = x_data[:,np.newaxis]
y_data = y_data[:,np.newaxis]


# In[5]:


x_data


# In[6]:


# 创建并拟合模型
model = LinearRegression()
model.fit(x_data, y_data)


# In[7]:


# 画图
plt.plot(x_data, y_data, 'b.')
plt.plot(x_data, model.predict(x_data), 'r')
plt.show()


# In[15]:


# 定义多项式回归,degree的值可以调节多项式的特征
poly_reg  = PolynomialFeatures(degree=5) 
# 特征处理
x_poly = poly_reg.fit_transform(x_data)
# 定义回归模型
lin_reg = LinearRegression()
# 训练模型
lin_reg.fit(x_poly, y_data)


# In[16]:


x_poly


# In[17]:


# 画图
plt.plot(x_data, y_data, 'b.')
plt.plot(x_data, lin_reg.predict(poly_reg.fit_transform(x_data)), c='r')
plt.title('Truth or Bluff (Polynomial Regression)')
plt.xlabel('Position level')
plt.ylabel('Salary')
plt.show()


# In[23]:


# 画图
plt.plot(x_data, y_data, 'b.')
x_test = np.linspace(1,10,100)
x_test = x_test[:,np.newaxis]
plt.plot(x_test, lin_reg.predict(poly_reg.fit_transform(x_test)), c='r')
plt.title('Truth or Bluff (Polynomial Regression)')
plt.xlabel('Position level')
plt.ylabel('Salary')
plt.show()


# In[18]:


np.linspace(1,10,100)


# In[ ]:




