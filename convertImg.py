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
            #print i, j
            row += toBinary(pixel[j,i])
        res.append(row)
    return res

def toBinary(value):
    print (value+1)%32
    res = '1'
    if value <= 127:
        res = '0'
    return res


class Img2ascii:
    __chars=[' ', ',', '+', '1', 'n','D','&','M']
    def getchar(self,pi):
        for i in range(0,8):
            if pi< (i+1)*32:
                return self.__chars[7-i]
    def __init__(self,src,resize=1.0):
        img = Image.open(src)
        if img.mode=='P' or img.mode =='RGBA':
             im=Image.new('RGB',img.size,'white')
             im.paste(img.convert('RGBA'),img.convert('RGBA'))
             img= im
        img= img.convert('L')
        w,h =img.size
        h/=2
        w=int(w*resize)
        h=int(h*resize)
        img=img.resize((w,h),Image.ANTIALIAS)
        #img.save('tmp.jpg')
        pixs = img.load()
        self.data=[]
        for i in range(0,h):
            line =''
            for j in range(0,w):
                line+=self.getchar(pixs[j,i])
            self.data.append(line)

a = convertImg("img.jpg")
#output = file('aaa.txt','w')
#for line in a.data:
#    print >>output, line
#output.close()

