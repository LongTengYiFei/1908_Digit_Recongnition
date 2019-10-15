"""运行这个脚本------就可以测试模型在测试集上的精度了。"""

from keras import models
theNet = models.load_model('Digit_Recongnition.h5')

import numpy as np
mnist_data_path = "D:\\111_PythonProjects\\mnist\\mnist.npz"
mnist_data_loaded = np.load(mnist_data_path)

x_test = mnist_data_loaded["x_test"]
x_test = x_test.reshape(len(x_test), 28*28)
x_test = x_test.astype('float32')/255
print("测试集的形状：", x_test.shape)

count = input("你想看前几个图片？键入数字按回车结束：")
teacher_test = mnist_data_loaded["y_test"]
print("目录化前教师标签集的形状：", teacher_test.shape)
print("目录化前教师标签集的前", count, "个：")
for i in range(int(count)):
    print(teacher_test[i])

from keras.utils import to_categorical
teacher_test = to_categorical(teacher_test)
print("目录化后教师标签集的形状：", teacher_test.shape)
print("这是前", count, "个教师标签：")
print("[0. 1. 2. 3. 4. 5. 6. 7. 8. 9.]")
print("-------------------------------")
for i in range(int(count)):
    print(teacher_test[i])

test_loss, test_acc = theNet.evaluate(x_test, teacher_test)

print("测试损失：", test_loss)
print("测试精度：", test_acc)

print("这是前", count, "个图片:")
from visual_array import visual_array
for i in range(int(count)):
    print(visual_array(x_test[i].reshape(28, 28)))
