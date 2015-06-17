# -*- coding=utf-8 -*-
from PIL import Image
def convertImg(src):
    res = []
    img = Image.open(src)
    img = img.convert("L")
    img.save("tem.jpg")
    pixel = img.load()
    #print list(img.getdata())
    h = img.size[0]
    w = img.size[1]
    if h != w:
        raise Exception("error")
    print "hight: %s, width: %s" %(h,w)
    for i in range(h):
        row = ""
        for j in range(w):
            print i, j
            row += toBinary(pixel[j,i])
        res.append(row)
    return res

def toBinary(value):
    res = '1'
    if value <= 127:
        res = '0'
    return res

a = convertImg("hehe.jpg")
output = file('aaa.txt','w')
for line in a:
    print >>output, line
output.close()

