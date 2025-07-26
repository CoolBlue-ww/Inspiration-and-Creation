from PIL import Image
import time
# 打开图片
image = Image.open("cat.jpg")  # PIL对象
# image.show()  # 显示图片
img_size = image.size  # 获取图片的宽高，以元组返回
img_width = image.width  # 单独获取图片的宽
img_height = image.height  # 单独获取图片的高
image_R, image_G, image_B = image.split()  # 返回一个元组，共有三个元素，分别表示RGB三个通道的图片
for index, RGB_object in enumerate([image_R, image_G, image_B]):  # 保存图片，一共有五个参数，依次为保存的文件名和保存路径、保存的格式、保存的质量、是否进行优化、是否开启渐进式
    if index == 0:
        RGB_object.save("cat-R.jpg", "jpeg", quality=100, optimize=True,  progressive=True)
    elif index == 1:
        RGB_object.save("cat-G.jpg", "png", quality=100, optimize=True, progressive=True)
    else:
        RGB_object.save('cat-B.jpg', "gif", quality=100, optimize=True, progressive=True)
image_load = image.load()  # 将图片转换成三维数组，可通过坐标[x,y]对图片上的每一个像素进行访问（R,G,B）
image_convert = image.convert(mode="L", matrix=None, dither=None, palette=None, colors=256)  #
image_copy = image.copy()  # 创建图片的副本（复制）
image_R.alpha_composite(image_G, (0, 0), (0, 0))  # 将两张格式为RGBA的图片进行混合叠加
