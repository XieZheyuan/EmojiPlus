def to(image_name):
    '''
    https://www.cnblogs.com/bigpig369/articles/8749109.html

    '''
    # 1.导入Image类
    from PIL import Image
    # 2.使用Image的对象读取图片

    img = Image.open(image_name)
    # print(img.size,img.mode)
    # 3.将图片转为灰度图片
    img = img.convert('L')  # L是转换灰度图片
    # img.show() img.save('fff.jpg')
    # 4.获取原图大小，并根据实际需要缩小图片
    w, h = img.size
    # 如果图片太大，将高和宽做一个等比例的缩放
    if w > 100:
        h = int((100 / w) * h / 1.8)
        w = 100
    # 等比例缩放用到resize方法,第二个参数是加入滤镜，保证缩放质量
    img = img.resize((w, h), Image.ANTIALIAS)
    # img.save('fff.jpg')
    # 添加多行注释的快捷键： ctrl+/
    # 5.将缩小的图片像素点的颜色值转为字符并存放到列表
    data = []
    chars = [' ', '.', 'c', 'h', 'e', 'n', 'y', 'i', 'm', 'e', 'n', 'g',
             '!',
             "~",
             "@",
             "`",
             "#",
             "$",
             "%",
             "^",
             "&",
             "*",
             "(",
             ")",
             "-",
             "_",
             "+",
             "=",
             "1","2","3","4","5","6","7","8","9","0",
             "{","}","[","]",":",";","\"","'","|","\\",
             "<",">",",",".","?","/"]
    # 根据图片宽度和高度遍历像素点并取出每个像素点的颜色值
    for i in range(0, h):
        line = ''
        for j in range(0, w):
            # 取出每个像素点的值
            pi = img.getpixel((j, i))
            # 用字符去替换像素点的颜色值
            for k in range(0, 12):
                if pi < (k + 1) * 22:
                    line += chars[11 - k]
                    break
        data.append(line)
    return "\n".join(data)
# print(to("images/tupian1.jpg"))