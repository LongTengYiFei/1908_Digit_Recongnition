"""as you know,this script is used to show images.
   mnist是一个字典，相当于键值对，访问里面的数组要用键

   这个脚本可以直接运行
"""
import numpy as np
from PIL import Image

mnist_data_path = "D:\\111_PythonProjects\\mnist\\mnist.npz"
mnist_data_loaded = np.load(mnist_data_path)

x_train = mnist_data_loaded["x_train"]
teacher_train = mnist_data_loaded["y_train"]

print("图片是一张一张展示的，你需要关闭一张图片，下一张才会显示。")
print("现在展示训练集里的数据，从第一张图片开始浏览。")
image_count = input("请输入你想浏览的图片数量：")
for i in range(int(image_count)):
    print(teacher_train[i])
    image = Image.fromarray(x_train[i])
    image.show()
print("展示完毕!!!")