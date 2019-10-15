""" mnist 里面是4个numpy数组"""
""" 运行这个脚本------就可以训练了。"""

import numpy as np

mnist_data_path = ".\\mnist.npz"
mnist_data_loaded = np.load(mnist_data_path)

x_train = mnist_data_loaded["x_train"]
teacher_train = mnist_data_loaded["y_train"]

from keras import models
from keras import layers

theNet = models.Sequential()
theNet.add(layers.Dense(28*28, activation='relu', input_shape=(28*28,)))
theNet.add(layers.Dense(16, activation='relu'))
theNet.add(layers.Dense(16, activation='relu'))
theNet.add(layers.Dense(10, activation='softmax'))


from some_functions import  optimizer_name_select
optimizer_name = optimizer_name_select()
from some_functions import  loss_name_select
loss_name = loss_name_select()

theNet.compile(optimizer=optimizer_name,
               loss=loss_name,
               metrics=['acc']
               )

x_train = x_train.reshape(len(x_train), 28*28)
x_train = x_train.astype(np.float)/255
from keras.utils import to_categorical
teacher_train = to_categorical(teacher_train)

theEpochs = input("* * *你想训练几个Epoch？输入数字按回车结束:")
theEpochs = int(theEpochs)
theNet.fit(x_train, teacher_train, epochs=theEpochs, batch_size=100)

theNet.save('.\\Digit_Recongnition.h5')



