"""这个脚本目前 有两个函数。
   这个脚本不能直接运行，因为它只有一些函数
"""



def visual_array(the_array):
    """由于灰度是从0到255的，图片是一个二维数组，如果我打印每一个图片，那种3位数两位数，就对不齐
     我是想直观的感受这个数字的形状，就把正整数变成1，忽略灰度，这样能对齐了。

    #参数
       the_array：一个二维数组。（数组中的值代表这个图像每个像素的灰度值）
    #返回值
       没有返回值，这个函数就是把二维数打印出来，正数打印成“1”，零打印成“0”
    #例子
       每一个mnist图片都是28*28的二维数组，传入这个函数即可看到结果。
    """
    if the_array.ndim != 2:
        print("对不起，您传入的参数不是二维数组，请重新传参。")
        return 0

    for i in range(the_array.shape[0]):
      for j in range(the_array.shape[1]):
        if the_array[i][j] != 0:
          print(1, end='')
        else:
          print(0, end='')
        if j == 27:
          print("")
